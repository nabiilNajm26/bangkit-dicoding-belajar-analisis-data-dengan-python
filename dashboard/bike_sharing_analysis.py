import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Load dataset
day_df = pd.read_csv('data/day.csv')
hour_df = pd.read_csv('data/hour.csv')

# Mengubah tipe data int menjadi category pada kolom 'season', 'mnth', 'holiday', 'weekday', 'weathersit'
columns = ['season', 'mnth', 'holiday', 'weekday', 'weathersit']
for column in columns:
    day_df[column] = day_df[column].astype("category")
    hour_df[column] = hour_df[column].astype("category")

# Mengubah tipe data dteday menjadi datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Mengganti nama kolom agar lebih mudah dibaca
day_df.rename(columns={'yr':'year', 'mnth':'month', 'weekday':'one_of_week', 'weathersit':'weather_situation', 'windspeed':'wind_speed', 'cnt':'count_cr', 'hum':'humidity'}, inplace=True)
hour_df.rename(columns={'yr':'year', 'hr':'hours', 'mnth':'month', 'weekday':'one_of_week', 'weathersit':'weather_situation', 'windspeed':'wind_speed', 'cnt':'count_cr', 'hum':'humidity'}, inplace=True)

# Mengkonversi isi kolom agar mudah dipahami
day_df['season'].replace({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}, inplace=True)
hour_df['season'].replace({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}, inplace=True)
day_df['month'].replace({1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}, inplace=True)
hour_df['month'].replace({1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}, inplace=True)
day_df['weather_situation'].replace({1: 'Clear', 2: 'Misty', 3: 'Light_rainsnow', 4: 'Heavy_rainsnow'}, inplace=True)
hour_df['weather_situation'].replace({1: 'Clear', 2: 'Misty', 3: 'Light_rainsnow', 4: 'Heavy_rainsnow'}, inplace=True)
day_df['one_of_week'].replace({0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}, inplace=True)
hour_df['one_of_week'].replace({0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}, inplace=True)
day_df['year'].replace({0: '2011', 1: '2012'}, inplace=True)
hour_df['year'].replace({0: '2011', 1: '2012'}, inplace=True)

# Menghitung Humidity
day_df['humidity'] = day_df['humidity'] * 100
hour_df['humidity'] = hour_df['humidity'] * 100

# Normalisasi suhu (mengembalikan ke Celsius)
hour_df['temp_celsius'] = hour_df['temp'] * 41
hour_df['atemp_celsius'] = hour_df['atemp'] * 50

day_df['temp_celsius'] = hour_df['temp'] * 41
day_df['atemp_celsius'] = hour_df['atemp'] * 50

# Membuat kolom baru bernama category_days yang menunjukan isi kolom tersebut weekend atau weekdays
def get_category_days(one_of_week):
    if one_of_week in ["Saturday", "Sunday"]:
        return "weekend"
    else:
        return "weekdays"

hour_df["category_days"] = hour_df["one_of_week"].apply(get_category_days)
day_df["category_days"] = day_df["one_of_week"].apply(get_category_days)

def classify_humidity(humidity):
    if humidity < 45:
        return "Terlalu kering"
    elif humidity >= 45 and humidity < 65:
        return "Ideal"
    else:
        return "Terlalu Lembab"

hour_df["humidity_category"] = hour_df["humidity"].apply(classify_humidity)
day_df["humidity_category"] = day_df["humidity"].apply(classify_humidity)

# Streamlit App
st.title('Bike Sharing Analysis')

# Selectbox for switching between plots
selected_tab = st.selectbox("Pilih Analisis", options=["Weather Impact", "Monthly Usage", "Peak and Off-Peak Hours", "RFM Analysis"])

if selected_tab == "Weather Impact":
    with st.sidebar:
        weather_options = st.multiselect(
            'Select Weather Situations',
            options=day_df['weather_situation'].cat.categories.tolist(),
            default=day_df['weather_situation'].cat.categories.tolist()
        )
    # Filter the data based on selections
    filtered_df_weather = day_df[day_df['weather_situation'].isin(weather_options)]
    st.subheader(f'Pengaruh Kondisi Cuaca terhadap Jumlah Peminjaman Sepeda')
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='weather_situation', y='count_cr', data=filtered_df_weather)
    plt.title(f'Pengaruh Kondisi Cuaca terhadap Jumlah Peminjaman Sepeda')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Jumlah Peminjaman Sepeda')
    st.pyplot(plt)

elif selected_tab == "Monthly Usage":
    with st.sidebar:
        month_options = st.multiselect(
            'Select Months',
            options=day_df['month'].cat.categories.tolist(),
            default=day_df['month'].cat.categories.tolist()
        )
    # Filter the data based on selections
    filtered_df_month = day_df[day_df['month'].isin(month_options)]
    st.subheader('Penggunaan Sepeda Berdasarkan Bulan')
    month_avg = filtered_df_month.groupby('month')['count_cr'].mean().reindex(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.figure(figsize=(12, 6))
    bar_plot = sns.barplot(x=month_avg.index, y=month_avg.values, palette='viridis')
    for p in bar_plot.patches:
        bar_plot.annotate(format(p.get_height(), '.0f'),
                          (p.get_x() + p.get_width() / 2., p.get_height()),
                          ha = 'center', va = 'center',
                          xytext = (0, 9),
                          textcoords = 'offset points')
    plt.title('Penggunaan Sepeda Berdasarkan Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Peminjaman Sepeda')
    plt.xticks(rotation=45)
    st.pyplot(plt)

elif selected_tab == "Peak and Off-Peak Hours":
    st.subheader('Jam Berapa Saja Penggunaan Sepeda Ramai dan Sepi?')
    hour_avg = hour_df.groupby('hours')['count_cr'].mean().reset_index().rename(columns={'hours': 'hour', 'count_cr': 'avg_rentals'})
    threshold = hour_avg['avg_rentals'].mean()
    hour_avg['cluster'] = ['High' if x >= threshold else 'Low' for x in hour_avg['avg_rentals']]
    plt.figure(figsize=(12, 6))
    sns.barplot(x='hour', y='avg_rentals', hue='cluster', data=hour_avg, palette='viridis')
    plt.title('Clustering Analysis of Bike Rentals by Hour')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Average Rentals')
    plt.legend(title='Cluster')
    st.pyplot(plt)

elif selected_tab == "RFM Analysis":
    st.subheader('Analisis Retensi dan Loyalitas Pengguna')
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
    current_date = hour_df['dteday'].max()
    rfm_df = hour_df.groupby('registered').agg({
        'dteday': lambda x: (current_date - x.max()).days,
        'instant': 'count',
        'count_cr': 'sum'
    }).reset_index()
    rfm_df.columns = ['registered', 'Recency', 'Frequency', 'Monetary']

    fig, axs = plt.subplots(3, 1, figsize=(10, 18))
    
    sns.histplot(rfm_df['Recency'], bins=20, kde=True, ax=axs[0])
    axs[0].set_title('Distribusi Recency Pengguna')
    axs[0].set_xlabel('Recency (days)')
    axs[0].set_ylabel('Jumlah Pengguna')
    
    sns.histplot(rfm_df['Frequency'], bins=20, kde=True, ax=axs[1])
    axs[1].set_title('Distribusi Frequency Pengguna')
    axs[1].set_xlabel('Frequency (jumlah transaksi)')
    axs[1].set_ylabel('Jumlah Pengguna')
    
    sns.histplot(rfm_df['Monetary'], bins=20, kde=True, ax=axs[2])
    axs[2].set_title('Distribusi Monetary Pengguna')
    axs[2].set_xlabel('Monetary (total peminjaman)')
    axs[2].set_ylabel('Jumlah Pengguna')

    st.pyplot(fig)

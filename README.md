
# Bike Sharing Analysis Project

## Project Overview

This project aims to analyze a bike-sharing dataset to derive insights that can inform business decisions for a bike rental service. The analysis addresses four main business questions:

1. **How does weather impact the number of bike rentals?**
2. **What are the trends in bike usage across different months?**
3. **What are the peak and off-peak hours for bike usage?**
4. **How is user retention and loyalty?**

The project includes data wrangling, exploratory data analysis (EDA), and advanced analyses such as clustering and RFM (Recency, Frequency, Monetary) analysis.

## Project Structure

- **Bike_Sharing_Analysis_notebook.ipynb**: Jupyter notebook containing the full analysis of the bike-sharing dataset.
- **data/day.csv**: Daily bike rental data.
- **data/hour.csv**: Hourly bike rental data.

## Requirements

To run the analyses, you need the following Python packages:

```bash
numpy==1.26.0
pandas==2.2.2
matplotlib==3.7.1
seaborn==0.12.2
streamlit==1.25.0
```

Install the required packages using:
```bash
pip install -r requirements.txt
```

## Data Wrangling

The data wrangling process includes:

1. **Loading the datasets**:
   - `day.csv` for daily data.
   - `hour.csv` for hourly data.

2. **Cleaning Data**:
   - Dropping irrelevant columns (`instant`, `workingday`).
   - Converting data types for specific columns.
   - Renaming columns for better readability.
   - Normalizing values (e.g., humidity, temperature).
   - Creating new categorical columns for days (`weekend` or `weekdays`) and humidity categories.

## Exploratory Data Analysis (EDA)

### Question 1: How does weather impact the number of bike rentals?

**Method**:
- Group data by weather conditions and calculate descriptive statistics for the number of rentals.

**Results**:
- **Clear Weather**: Highest median number of rentals.
- **Misty Weather**: Slightly lower median rentals but still significant.
- **Light Rain/Snow**: Lowest median rentals, indicating adverse weather impacts bike rentals.

### Question 2: What are the trends in bike usage across different months?

**Method**:
- Calculate the average number of rentals per month.

**Results**:
- **Peak Usage**: June and September have the highest average rentals.
- **Low Usage**: January and February have the lowest average rentals.
- **Seasonal Trends**: Rentals increase from March to September and decrease from October to February.

### Question 3: What are the peak and off-peak hours for bike usage?

**Method**:
- Calculate the average number of rentals per hour and classify hours as 'High' or 'Low' based on the average rentals.

**Results**:
- **Peak Hours**: 7-9 AM and 4-8 PM.
- **Off-Peak Hours**: 12-6 AM and 10-11 PM.

### Question 4: How is user retention and loyalty?

**Method**:
- Perform RFM analysis to understand user retention and loyalty.

**Results**:
- **Recency**: Majority of users have rented bikes recently (0-100 days).
- **Frequency**: Most users have low transaction counts (less than 50 transactions).
- **Monetary**: Majority of users spend less than 2000 in total rentals.

## Business Recommendations

1. **Weather-Based Strategies**:
   - Promote rentals during clear weather.
   - Offer incentives during bad weather to maintain rental volumes.

2. **Seasonal Promotions**:
   - Increase marketing efforts during low usage months (January, February, December).
   - Plan events or promotions during peak months (June, July, August, September).

3. **Operational Efficiency**:
   - Allocate more bikes during peak hours (7-9 AM, 4-8 PM).
   - Reduce bike availability during off-peak hours (12-6 AM, 10-11 PM).

4. **User Retention and Loyalty**:
   - Offer promotions or incentives to users who have rented bikes recently to keep them engaged.
   - Implement loyalty programs or discounts to increase the frequency and value of rentals.

## Running the Streamlit App

To run the Streamlit app locally, use the following command:
```bash
streamlit run dashboard/bike_sharing_analysis.py
```

Alternatively, you can access the Streamlit app online [here](https://nabiil-najm266-bike-sharing.streamlit.app).

## Contact Information

- **Name**: Nabil Najmudin
- **Email**: nabiil.najm266@gmail.com
- **Dicoding ID**: nabiil_najm266

Feel free to reach out if you have any questions or feedback regarding this project.

from dotenv import load_dotenv
from os import getenv
import requests

try:
    load_dotenv() # Environment loaded
except FileNotFoundError:
    print(".env file not found.\nGo to Alpha Vantage and make your own API Key, copy the URl for Stocks and include in .env file of your repository.")
else:
    STOCK_API_KEY = getenv("STOCK_API_KEY") # From Alpha Vantage
    STOCK_API_ENDPT = getenv("STOCK_API_ENDPT") # From Alpha Vantage
    
# Function to check the fluctuation percentage
def calc_Fluctuation(Value1, Value2):
    # Converting to floats
    f_Value1 = float(Value1)
    f_Value2 = float(Value2)
    # Implementing the percentage formula
    return abs(round((f_Value1 - f_Value2) / f_Value2 * 100, 2))
    
# Function to check the fluctuation in stock
def fluctuated(STOCK_Name, Time_Interval):
    # Making API request
    paramaters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": str(STOCK_Name),
        "interval": str(f"{Time_Interval}min"),
        "apikey": STOCK_API_KEY,
    }

    response = requests.get(url=STOCK_API_ENDPT, params=paramaters)
    response.raise_for_status() # Raise exception if any
    # Stocks data in json format
    Stocks_Data = response.json()["Time Series (Daily)"]
    # Converting the dict data days into list using list comphrension
    Stock_Data_2_day_list = [value for (key, value) in Stocks_Data.items()]
    # Getting the open and close prices of previous two days
    # New Day Price
    new_Day_Open = Stock_Data_2_day_list[0]['1. open']
    new_Day_High = Stock_Data_2_day_list[0]['2. high']
    new_Day_Low = Stock_Data_2_day_list[0]['3. low']
    new_Day_Close = Stock_Data_2_day_list[0]['4. close']
    # Previous Day Price
    previous_Day_Open = Stock_Data_2_day_list[1]['1. open']
    previous_Day_High = Stock_Data_2_day_list[1]['2. high']
    previous_Day_Low = Stock_Data_2_day_list[1]['3. low']
    previous_Day_Close = Stock_Data_2_day_list[1]['4. close']
    # Calculating the percentages
    open_Percntage = calc_Fluctuation(new_Day_Open, previous_Day_Open)
    high_Percentage = calc_Fluctuation(new_Day_High, previous_Day_High)
    low_Percentage = calc_Fluctuation(new_Day_Low, previous_Day_Low)
    close_Percentage = calc_Fluctuation(new_Day_Close, previous_Day_Close)
    
    # Checking and returning precentages
    if open_Percntage >= 5 or high_Percentage >= 5 or low_Percentage >= 5 or close_Percentage >= 5:
        return True
    else:
        return False
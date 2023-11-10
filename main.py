from API_Data import API_request, new_Alert
import time

STOCK_NAME = "TSLA"
TIME_INTERVAL = 30
COMPANY_NAME = "Tesla Inc"

# Making API request and checking the percentages
if API_request.fluctuated(STOCK_NAME, TIME_INTERVAL):
    time.sleep(1) # 1 sec delay
    print("Price fluctuation found. Getting the news...")
    # Calling get_News() function 
    new_Alert.get_News(COMPANY_NAME)
else:
    print("Fluctuation not found.")
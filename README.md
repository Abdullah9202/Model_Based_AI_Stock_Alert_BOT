# Stock Alert BOT Description

This repository contains Python scripts for monitoring stock fluctuations and fetching relevant news articles.

## Description

The Stock Fluctuation Alert System is a Python application that monitors the fluctuations in the stock prices of a specified company and alerts users if significant fluctuations are detected. It utilizes APIs from Alpha Vantage for stock data and News API for fetching relevant news articles related to the specified company.

## Files

1. **main.py**: Python script containing the main logic for monitoring stock fluctuations and fetching news alerts.

2. **api_request.py**: Python script containing functions for making API requests to Alpha Vantage and calculating stock price fluctuations.

3. **new_alert.py**: Python script containing functions for fetching relevant news articles using the News API.

## Usage

To use the Stock Fluctuation Alert System, run the `main.py` script. Make sure to specify the desired stock name, time interval, and company name within the script. The program will then monitor the specified stock for fluctuations and fetch relevant news articles if significant fluctuations are detected.

## Dependencies

Make sure to install the following Python packages before running the scripts:
- `requests`: For making HTTP requests to APIs.
- `dotenv`: For loading environment variables from a .env file.

## Configuration

Before running the scripts, create a `.env` file in the root directory of the project and add the following environment variables:
- `STOCK_API_KEY`: Your API key from Alpha Vantage.
- `STOCK_API_ENDPT`: The API endpoint URL for stock data from Alpha Vantage.
- `NEWS_API_KEY`: Your API key from News API.
- `NEWS_API_ENDPT`: The API endpoint URL for news articles from News API.

## Credits

Developed By Abdullah Khurram <https://www.github.com/Abdullah9202>.



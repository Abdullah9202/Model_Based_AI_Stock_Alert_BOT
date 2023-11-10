from dotenv import load_dotenv
from os import getenv
import requests

# Function to get relevant news
def get_News(Company_Name):
    try:
        load_dotenv() # Environment Loaded
    except FileNotFoundError:
        print(".env file not found.\nGoto newsapi.org, create your own API key, copy and API URL and make an .env file.")
    else:
        NEWS_API_KEY = getenv("NEWS_API_KEY") # From news api
        NEWS_API_ENDPT = getenv("NEWS_API_ENDPT") # From news api
        
    # Making request
    paramaters = {
        "qInTitle": str(Company_Name),
        "apikey": NEWS_API_KEY,
    }

    response = requests.get(url=NEWS_API_ENDPT, params=paramaters)
    response.raise_for_status() # Raise exception if any
    News_Data = response.json()['articles']
    # Printing the data of first five articles
    for article in News_Data[:5]:
        print(
            f"Author: {article['author']}\n",
            f"Title: {article['title']}\n",
            f"Description: {article['description']}\n",
            f"Url: {article['url']}\n",
            f"Published at: {article['publishedAt'].split("T")[0]}, Time: {article['publishedAt'].split("T")[1]}\n"
        )
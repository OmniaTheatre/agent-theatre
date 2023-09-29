'''
This file contains the StockDataScraper class for scraping historical stock data using Alpha Vantage.
'''
import requests
class StockDataScraper:
    def __init__(self):
        self.base_url = "https://www.alphavantage.co/query"
        self.api_key = "NT0GL8WWMNPOJVZ1"  # Replace with your Alpha Vantage API key
    def scrape(self, ticker):
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": ticker,
            "interval": "1min",
            "outputsize": "full",
            "apikey": self.api_key
        }
        response = requests.get(self.base_url, params=params)
        data = response.json()
        if "Time Series (1min)" in data:
            return data["Time Series (1min)"]
        else:
            return None
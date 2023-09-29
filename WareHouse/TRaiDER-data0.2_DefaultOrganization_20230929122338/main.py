'''
This is the main file of the Python app for scraping historical stock data using Alpha Vantage.
'''
import tkinter as tk
from tkinter import filedialog
from scraper import StockDataScraper
from spreadsheet import StockDataSpreadsheet
def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            tickers = file.read().splitlines()
        scrape_data(tickers)
def scrape_data(tickers):
    scraper = StockDataScraper()
    spreadsheet = StockDataSpreadsheet()
    for ticker in tickers:
        data = scraper.scrape(ticker)
        spreadsheet.save_data(ticker, data)
def main():
    select_file()
if __name__ == "__main__":
    main()
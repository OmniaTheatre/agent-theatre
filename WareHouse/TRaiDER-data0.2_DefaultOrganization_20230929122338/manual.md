# Omnia Theatre Stock Data Scraper

The Omnia Theatre Stock Data Scraper is a Python application designed to scrape historical stock data using the Alpha Vantage API. It allows you to retrieve and store 1-minute interval data for a list of ticker names in a spreadsheet format that is easy to evaluate and train a machine learning model on.

## Installation

To install the Omnia Theatre Stock Data Scraper, follow these steps:

1. Make sure you have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/

2. Clone the repository or download the source code from the GitHub repository: [Omnia Theatre Stock Data Scraper](https://github.com/omniatheatre/stock-data-scraper)

3. Open a terminal or command prompt and navigate to the project directory.

4. Create a virtual environment (optional but recommended) by running the following command:

   ```
   python -m venv venv
   ```

5. Activate the virtual environment:

   - For Windows:

     ```
     venv\Scripts\activate
     ```

   - For macOS/Linux:

     ```
     source venv/bin/activate
     ```

6. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

7. Obtain an API key from Alpha Vantage by signing up for a free account on their website: https://www.alphavantage.co/

8. Open the `scraper.py` file in a text editor and replace the placeholder `YOUR_API_KEY` with your actual API key.

9. Save the changes and close the file.

## Usage

To use the Omnia Theatre Stock Data Scraper, follow these steps:

1. Prepare a text file containing a list of ticker names, with each ticker name on a separate line. For example:

   ```
   META
   TSLA
   MSFT
   PLTR
   ```

2. Run the `main.py` file by executing the following command in the terminal or command prompt:

   ```
   python main.py
   ```

3. A file selection dialog will appear. Choose the text file containing the ticker names.

4. The scraper will retrieve the historical stock data for each ticker from the Alpha Vantage API and store it in separate sheets or workbooks in an Excel spreadsheet.

5. The spreadsheet will be saved in the current directory with the ticker name as the filename (e.g., `META.xlsx`, `TSLA.xlsx`, etc.).

## Spreadsheet Format

The generated Excel spreadsheet will have the following columns for each ticker:

- Timestamp: The date and time of the data point.
- Open: The opening price of the stock.
- High: The highest price of the stock during the interval.
- Low: The lowest price of the stock during the interval.
- Close: The closing price of the stock.
- Volume: The trading volume of the stock.

Additionally, the spreadsheet will include the following columns for each ticker:

- RSI: The Relative Strength Index indicator.
- MACD: The Moving Average Convergence Divergence indicator.
- 9EMA: The 9-day Exponential Moving Average.
- 20EMA: The 20-day Exponential Moving Average.
- 50EMA: The 50-day Exponential Moving Average.
- 200EMA: The 200-day Exponential Moving Average.
- VWAP: The Volume Weighted Average Price.
- ADX: The Average Directional Index indicator.
- Stochastic: The Stochastic indicator.

## Data Range

The algorithm is designed to cycle from the current date and time, running backwards to fill in data for the past 20 years. However, please note that the availability of historical data may vary depending on the stock and the Alpha Vantage API.

## Conclusion

The Omnia Theatre Stock Data Scraper is a powerful tool for scraping and storing historical stock data for multiple tickers. It provides a convenient way to retrieve and organize the data in a format that is suitable for further analysis and machine learning model training.
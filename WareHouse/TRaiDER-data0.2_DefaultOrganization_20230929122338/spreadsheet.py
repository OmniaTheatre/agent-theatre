'''
This file contains the StockDataSpreadsheet class for storing historical stock data in a spreadsheet.
'''
import openpyxl
class StockDataSpreadsheet:
    def __init__(self):
        self.workbook = openpyxl.Workbook()
    def save_data(self, ticker, data):
        sheet = self.workbook.create_sheet(title=ticker)
        sheet.append(["Timestamp", "Open", "High", "Low", "Close", "Volume"])
        for timestamp, values in data.items():
            sheet.append([timestamp, values["1. open"], values["2. high"], values["3. low"], values["4. close"], values["5. volume"]])
        self.workbook.save(f"{ticker}.xlsx")
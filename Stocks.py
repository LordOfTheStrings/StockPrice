import sys
#for exit
from time import sleep
import time
import yfinance as yf

flag = True
while flag:
    stock = input("Enter the ticker you would like to see data for: ")
    selectData = input("What data would you like to see? Enter 1 for Market Price or 2 for Full report: ")
    stock_info = yf.Ticker(stock).info

    if selectData == '1':
        market_price = stock_info['regularMarketPrice']
        print('market price ', market_price)

        previous_close_price = stock_info['regularMarketPreviousClose']
        print('previous close price ', previous_close_price)

    elif selectData == '2':
        # show balance sheet
        balance_sheet = stock_info['balanceSheetHistory']
        print('Balance sheet', balance_sheet)
        cashflow = stock_info['cashflowStatementHistory']
        print('Cashflow', cashflow)
        earnings = stock_info['earnings']
        print('Earnings', earnings)

        #quarterly data
        quarterly_balance_sheet = stock_info['balanceSheetHistoryQuarterly']
        print('Quarterly balance sheet', quarterly_balance_sheet)
        quarterly_cashflow = stock_info['cashflowStatementHistoryQuarterly']
        print('Quarterly cashflow', quarterly_cashflow)
        quarterly_earnings = stock_info['earningsQuarterlyGrowth']
        print('Quarterly earnings', quarterly_earnings)

    else:
        print('Invalid input!')
        flag = False

print('Have a nice day! :)')

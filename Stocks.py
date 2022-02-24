import sys        #for exit
from time import sleep
import time
import yfinance as yf

stock = input("Enter the ticker you would like to see data for: ")

stock_info = yf.Ticker(stock).info
market_price = stock_info['regularMarketPrice']

print('market price ', market_price)

previous_close_price = stock_info['regularMarketPreviousClose']

print('previous close price ', previous_close_price)

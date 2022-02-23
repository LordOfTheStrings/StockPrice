from selenium import webdriver
import sys	    #for exit
from time import sleep
import time
from bs4 import BeautifulSoup


stock = input("Enter the ticker you would like to see data for: ")

url = 'https://finance.yahoo.com/quote/' + stock
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(url)






#code based on https://www.thepythoncode.com/article/extract-weather-data-python
def check_price():
	price = BeautifulSoup(driver.page_source, 'html.parser')#parse the html code
	temp = price.find('div', {'class':'condition-data'})#finds condition-data class to find temperature
	current = temp.find('span',{'class':'wu-value wu-value-to'}).text #gets current temp 
print(check_price.current)


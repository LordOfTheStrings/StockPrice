from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

stock = input("Enter the ticker you would like to see data for: ")

url = 'https://finance.yahoo.com/quote/' + stock
s = Service(r"C:\Users\mraar\AppData\Local\EdgeDriver\edgedriver_win64\msedgedriver.exe")

#Using Edge because Windows :)
#driver = webdriver.Chrome(PATH)
#driver.get(url)

driver = webdriver.Edge(service = s)
driver.get(url)

#code based on https://www.thepythoncode.com/article/extract-weather-data-python
def check_price():
	price = BeautifulSoup(driver.page_source, 'html.parser')#parse the html code
	temp = price.find('div', {'class':'condition-data'})#finds condition-data class to find price
	current = temp.find('span',{'class':'wu-value wu-value-to'}).text #gets current price
print(check_price.current)


from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import re

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit("https://iextrading.com/trading/eligible-symbols/")

results = browser.html
soup = BeautifulSoup(results, 'html.parser')

results_raw = soup.find_all("tr", class_="bg-silver-on-hover")

filteredonce = re.findall(r'bg-silver-on-hover\"(.*?)\</td\>', str(results_raw))
filteredtwice = re.findall(r'\>\<td(.*?)\,', str(filteredonce))
filteredthrice = re.findall(r'\>(.*?)\,', str(filteredtwice))
TickerList = re.findall(r'">(.*?)\\', str(filteredtwice))

Tickerdf = pd.DataFrame({'Ticker':TickerList}).set_index('Ticker')
Tickerdf.to_csv(r'TickerList.csv')
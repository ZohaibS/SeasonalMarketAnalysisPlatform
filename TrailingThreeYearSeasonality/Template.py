from pandas_datareader import data as wb
import pandas as pd
from itertools import chain
import time
import logging

MARKET_OPEN_DAYS = 200

logging.basicConfig(level=logging.INFO)

IEXTickerList = pd.read_csv('TickerList.csv').values.tolist()
IEXTickers = list(chain.from_iterable(IEXTickerList))

TickersWithAvailableData = list()

Tickers = IEXTickers
CurrentYear = int(time.strftime("%Y"))
Years = [CurrentYear-3, CurrentYear-2, CurrentYear-1]

for Ticker in Tickers:
	logging.info("Processing the ticker symbol {}.".format(Ticker))

	tickerLengthFlag = 'false' #Reset Flag for each ticker


	for Year in Years:
		RawData = pd.DataFrame()
		try:
			RawData[Ticker] = wb.DataReader(Ticker, data_source = 'iex', start=str(Year) + '-1-1', end=str(Year)+'-12-31')['close']
		
			if len(RawData[Ticker].index) < MARKET_OPEN_DAYS:
				tickerLengthFlag = 'true'		#if any of the 3 years are empty for a Ticker, set flag to true

		except KeyError:
			tickerLengthFlag = 'true'
			break

		
		
	if tickerLengthFlag == 'false':
		TickersWithAvailableData.append(Ticker)

Tickerdf = pd.DataFrame({'Ticker':TickersWithAvailableData}).set_index('Ticker')
Tickerdf.to_csv(r'TickersWithAvailableData.csv')
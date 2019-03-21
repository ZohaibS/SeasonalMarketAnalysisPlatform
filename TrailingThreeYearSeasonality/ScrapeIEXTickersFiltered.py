import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import json
import datetime
from datetime import date
import os
import time
import logging
from sqlalchemy import create_engine
import sqlalchemy
from itertools import chain

engine = create_engine('postgresql://postgres:@localhost/Stocks')
connection = engine.raw_connection()
cursor = connection.cursor()

IEXTickerList = pd.read_csv('TickersWithAvailableData.csv').values.tolist()

# print(list(chain(*IEXTickerList)))
# or better: (available since Python 2.6)
IEXTickers = list(chain.from_iterable(IEXTickerList))
Tickers = IEXTickers
CurrentYear = int(time.strftime("%Y"))

Years = [CurrentYear-3, CurrentYear-2, CurrentYear-1]


kStds = []
dfPrepTicker = []
dfPrepMean = []
dfPrepStandardDeviation = []
OctaveCollection = []
T3YList = []
kTickers = []
T3YAllTickers = pd.DataFrame(columns=('Ticker', 'Mean Octave', 'Mean Deviation'))

logging.basicConfig(level=logging.INFO)

#IEX : wb.DataReader(Ticker, data_source='iex', start=str(Year)+'-12-31', end = Today)['close']
#Yahoo : wb.DataReader(Ticker, data_source='yahoo', start=str(Year)+'-12-31')['Adj Close']

#T3Y refers to Total 3 Year (Seasonal)
for Ticker in Tickers:
        for Year in Years:
            
            logging.info("Processing the year {} for ticker symbol {}.".format(Year, Ticker))

            RawData = pd.DataFrame()

            RawData[Ticker] = wb.DataReader(Ticker, data_source = 'iex', start=str(Year) + '-1-1', end=str(Year)+'-12-31')['close']
            
            RawData.to_sql(Ticker+str(Year)+"RawEODs", engine, if_exists="replace")            
            
            RawData['Delta'] = np.append(np.array([0]), np.diff(RawData[Ticker].values))
            
            RawData.to_sql(Ticker+str(Year)+"RawSignal", engine, if_exists="replace")
            
            RawData = RawData.iloc[1:]

            SortedData = RawData['Delta'].sort_values()

            OctaveN5 = SortedData[0:len(RawData)//11]
            OctaveN4 = SortedData[len(RawData)//11:2*len(RawData)//11]
            OctaveN3 = SortedData[2*len(RawData)//11:3*len(RawData)//11]
            OctaveN2 = SortedData[3*len(RawData)//11:4*len(RawData)//11]
            OctaveN1 = SortedData[4*len(RawData)//11:5*len(RawData)//11]
            OctaveZeroList = SortedData[5*len(RawData)//11:6*len(RawData)//11]
            OctaveP1 = SortedData[6*len(RawData)//11:7*len(RawData)//11]
            OctaveP2 = SortedData[7*len(RawData)//11:8*len(RawData)//11]
            OctaveP3 = SortedData[8*len(RawData)//11:9*len(RawData)//11]
            OctaveP4 = SortedData[9*len(RawData)//11:10*len(RawData)//11]
            OctaveP5 = SortedData[10*len(RawData)//11:len(RawData)]

            OctaveN5 = OctaveN5.to_frame(name=None)
            OctaveN4 = OctaveN4.to_frame(name=None)
            OctaveN3 = OctaveN3.to_frame(name=None)
            OctaveN2 = OctaveN2.to_frame(name=None)
            OctaveN1 = OctaveN1.to_frame(name=None)
            OctaveZero = OctaveZeroList.to_frame(name=None)
            OctaveP1 = OctaveP1.to_frame(name=None)
            OctaveP2 = OctaveP2.to_frame(name=None)
            OctaveP3 = OctaveP3.to_frame(name=None)
            OctaveP4= OctaveP4.to_frame(name=None)
            OctaveP5 = OctaveP5.to_frame(name=None)

            OctaveN5['Octave'] = -5
            OctaveN4['Octave'] = -4
            OctaveN3['Octave'] = -3
            OctaveN2['Octave'] = -2
            OctaveN1['Octave'] = -1
            OctaveZero['Octave'] = 0
            OctaveP1['Octave'] = 1
            OctaveP2['Octave'] = 2
            OctaveP3['Octave'] = 3
            OctaveP4['Octave'] = 4
            OctaveP5['Octave'] = 5

            maxN5 = round(OctaveN5['Delta'][len(OctaveN5)-1], 2)
            maxN4 = round(OctaveN4['Delta'][len(OctaveN4)-1], 2)
            maxN3 = round(OctaveN3['Delta'][len(OctaveN3)-1], 2)
            maxN2 = round(OctaveN2['Delta'][len(OctaveN2)-1], 2)
            maxN1 = round(OctaveN1['Delta'][len(OctaveN1)-1], 2)
            minZero = round(OctaveZero['Delta'][0], 2)
            maxZero = round(OctaveZero['Delta'][len(OctaveZeroList)-1], 2)
            minP1 = round(OctaveP1['Delta'][0], 2)
            minP2 = round(OctaveP2['Delta'][0], 2)
            minP3 = round(OctaveP3['Delta'][0], 2)
            minP4 = round(OctaveP4['Delta'][0], 2)
            minP5 = round(OctaveP5['Delta'][0], 2)
            
            OctaveRangeN5 = [str(maxN5), str(maxN4)]
            OctaveRangeN4 = [str(maxN4), str(maxN3)]
            OctaveRangeN3 = [str(maxN3), str(maxN2)]
            OctaveRangeN2 = [str(maxN2), str(maxN1)]
            OctaveRangeN1 = [str(maxN1), str(minZero)]
            OctaveRangeZero = [str(minZero), str(maxZero)]
            OctaveRangeP1 = [str(maxZero), str(minP1)]
            OctaveRangeP2 = [str(minP1), str(minP2)]
            OctaveRangeP3 = [str(minP2), str(minP3)]
            OctaveRangeP4 = [str(minP3), str(minP4)]
            OctaveRangeP5 = [str(minP4), str(minP5)]

            OctaveRanges = {
                "OctaveRangeP1": OctaveRangeP1,
                "OctaveRangeP2": OctaveRangeP2,
                "OctaveRangeP3": OctaveRangeP3,
                "OctaveRangeP4": OctaveRangeP4,
                "OctaveRangeP5": OctaveRangeP5,
                "OctaveRangeZero" : OctaveRangeZero,
                "OctaveRangeN1": OctaveRangeN1,
                "OctaveRangeN2": OctaveRangeN2,
                "OctaveRangeN3": OctaveRangeN3,
                "OctaveRangeN4": OctaveRangeN4,   
                "OctaveRangeN5": OctaveRangeN5}
            
            OctavesRanges = pd.DataFrame.from_dict(OctaveRanges)
            
            OctavesRanges.to_sql(str(Ticker)+str(Year)+"OctaveRanges", engine, if_exists="replace")
            
            Octaves = pd.concat([OctaveN5, OctaveN4, OctaveN3, OctaveN2, OctaveN1, OctaveZero, OctaveP1, OctaveP2, OctaveP3, OctaveP4, OctaveP5], sort=True).sort_index()

            Octaves['Week'] = pd.to_datetime(Octaves.index).week

            OctavesSum = pd.DataFrame(Octaves.groupby(['Week']).sum())

            OctaveCollection.append(OctavesSum)
            
for n in range(0, len(OctaveCollection)):
    if n%3 == 0:
        OctaveCollection[n].to_sql(Tickers[n//3]+str(Years[0])+"OctaveCollection", engine, if_exists="replace")
    if n%3 == 1:
        OctaveCollection[n].to_sql(Tickers[n//3]+str(Years[1])+"OctaveCollection", engine, if_exists="replace")
    if n%3 == 2:
        OctaveCollection[n].to_sql(Tickers[n//3]+str(Years[2])+"OctaveCollection", engine, if_exists="replace")

for j in range(0, len(Tickers)):   
    WeeklyMeansT3Y=[]
    WeeklyDeviationsT3Y = []
    for i in range(1,53):
        WeeklyMeansT3Y.append(np.mean([OctaveCollection[j*3].loc[i].iloc[1], OctaveCollection[j*3+1].loc[i].iloc[1], OctaveCollection[j*3+2].loc[i].iloc[1]]))            
        WeeklyDeviationsT3Y.append(np.std([OctaveCollection[j*3].loc[i].iloc[1], OctaveCollection[j*3+1].loc[i].iloc[1], OctaveCollection[j*3+2].loc[i].iloc[1]]))

    WeeklyT3YDict = {
        'Week': range(1,53),
        'Total Three Year (Weekly) Standard Deviation': WeeklyDeviationsT3Y}

    WeeklyT3YDf = pd.DataFrame.from_dict(WeeklyT3YDict).set_index('Week')
    T3YList.append(WeeklyT3YDf)

for k in range(0, len(T3YList)):

    kStd = round(np.mean(T3YList[k]['Total Three Year (Weekly) Standard Deviation']), 2)
    kStds.append(kStd)


SeasonalVolatilityList = pd.DataFrame(list(zip(Tickers, kStds)), columns=['Ticker','Volatility'])

AnnualConsistencyRankings = SeasonalVolatilityList.sort_values(by=['Volatility'])

AnnualConsistencyRankings.to_sql("AllSeasonalVolatility", engine, if_exists="replace")
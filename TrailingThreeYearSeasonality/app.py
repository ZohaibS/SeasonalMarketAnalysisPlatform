from flask import Flask, render_template, jsonify, redirect
import json
import pandas as pd
import os
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy import Table, Column, String, MetaData
import sqlalchemy as db




app = Flask(__name__)

####################################
##Timescale Connection #############
####################################

# engine = create_engine('postgresql://postgres:@localhost/Stocks')
# connection = engine.raw_connection()
# cursor = connection.cursor()

engine = db.create_engine('postgresql://postgres:@localhost/Stocks')
connection = engine.connect()
metadata = db.MetaData()

####################################

@app.route('/')
def index():
    """Return the homepage."""

    tickers = db.Table('AllSeasonalVolatility', metadata, autoload=True, autoload_with=engine)
    query = db.select([tickers])
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()

    x01 = []
    y01 = []
    for n in range(0,len(ResultSet)):
        x01.append(ResultSet[n][1])
        y01.append(ResultSet[n][2])

    data = {'x': x01, 'y': y01}

    return render_template("index.html", data=data)

@app.route('/HistoricT3Y/<Ticker>')
def GenerateData(Ticker):

    #Raw EOD Fetch Year One
    tickers = db.Table('{}2016RawEODs'.format(Ticker), metadata, autoload=True, autoload_with=engine)
    query = db.select([tickers])
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()
    Results = list(map(list, zip(*ResultSet)))
    x11 = list(Results[0])
    y11 = list(Results[1])

    tickers = db.Table('{}2017RawEODs'.format(Ticker), metadata, autoload=True, autoload_with=engine)
    query = db.select([tickers])
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()
    Results = list(map(list, zip(*ResultSet)))
    x12 = list(Results[0])
    y12 = list(Results[1])

    tickers = db.Table('{}2018RawEODs'.format(Ticker), metadata, autoload=True, autoload_with=engine)
    query = db.select([tickers])
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()
    Results = list(map(list, zip(*ResultSet)))
    x13 = list(Results[0])
    y13 = list(Results[1])

    tickers = db.Table('{}2016RawSignal'.format(Ticker), metadata, autoload=True, autoload_with=engine)
    query = db.select([tickers])
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()
    Results = list(map(list, zip(*ResultSet)))
    x21 = list(Results[0])
    y21 = list(Results[2])

    tickers = db.Table('{}2017RawSignal'.format(Ticker), metadata, autoload=True, autoload_with=engine)
    query = db.select([tickers])
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()
    Results = list(map(list, zip(*ResultSet)))
    x22 = list(Results[0])
    y22 = list(Results[2])

    tickers = db.Table('{}2018RawSignal'.format(Ticker), metadata, autoload=True, autoload_with=engine)
    query = db.select([tickers])
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()
    Results = list(map(list, zip(*ResultSet)))
    x23 = list(Results[0])
    y23 = list(Results[2])

    # tickers = db.Table('{}2016OctaveCollection'.format(Ticker), metadata, autoload=True, autoload_with=engine)
    # query = db.select([tickers])
    # ResultProxy = connection.execute(query)
    # ResultSet = ResultProxy.fetchall()
    # Results = list(map(list, zip(*ResultSet)))
    # x31 = list(Results[0])
    # y31 = list(Results[2])

    # tickers = db.Table('{}2017OctaveCollection'.format(Ticker), metadata, autoload=True, autoload_with=engine)
    # query = db.select([tickers])
    # ResultProxy = connection.execute(query)
    # ResultSet = ResultProxy.fetchall()
    # Results = list(map(list, zip(*ResultSet)))
    # x32 = list(Results[0])
    # y32 = list(Results[2])

    # tickers = db.Table('{}2018OctaveCollection'.format(Ticker), metadata, autoload=True, autoload_with=engine)
    # query = db.select([tickers])
    # ResultProxy = connection.execute(query)
    # ResultSet = ResultProxy.fetchall()
    # Results = list(map(list, zip(*ResultSet)))
    # x33 = list(Results[0])
    # y33 = list(Results[2])

    # return(str(list(Results[0])))
    return render_template("reportDashboard.html", x11=x11, y11=y11, x12=x12, y12=y12, x13=x13, y13=y13, x21=x21, y21=y21, x22=x22, y22=y22, x23=x23, y23=y23)

    #Don't forget to include when putting back in Octave Collection x31=x31, y31=y31, x32=x32, y32=y32, x33=x33, y33=y33

if __name__ == "__main__":
    app.run(debug=True)
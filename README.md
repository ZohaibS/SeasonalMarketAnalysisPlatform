# SeasonalMarketAnalysisPlatform

This is an app in progress. It uses IEX data.

General Overview:

                                        Data Extraction and Processing Setup (to be automated on deployal)

Step 1: Scraper is included to obtain the full list of working tickers for the IEX website (slightly under 6,000 tickers.)

Step 2: A python script filters the list of working IEX tickers for only tickers that have atleast 3 years of data.

Step 3: A python script collects data from all of the filtered IEX endpoints from Step 2. (Eventually will add a timer in the Flask file to automate this step.)

Step 4: The python script computes various metrics from the data from Step 3.

Step 5: The python script dumps the processed and some of the important raw data locally to PostgreSQL (with the TimescaleDB extension.)


                                                              Front End
                                                       
     Consists of an Interactive Table for Browsing, a Historical Dashboard, and a Predictions Dashboard.
     The Interactive Table will allow for searching/browsing based on various criteria. (currently being built on index.html)
     The Dashboards are unique to individual stock tickers and the data is served via Flask.



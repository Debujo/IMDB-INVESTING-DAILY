import investpy
import datetime
import pandas as pd
import time

today = datetime.date.today()
date = str(today.day) + "/" + str(today.month) + "/" + str(today.year)
from_date = str(today.day) + "/" + str(today.month) + "/" + str(today.year-2)
mean_date = str(today.day) + "/" + str(today.month-1) + "/" + str(today.year)
print("Today is: " +  date)

stock = []
stocks = investpy.get_stocks_list(country = 'United States')
#print(len(stocks)) #4582*25kb = 120Mb en csv

for x in stocks:
    try:
        stock = investpy.get_stock_historical_data(stock= x, country='United States', from_date=from_date, to_date=date)
        #print(str(x))
        #media = mean(stock.tail()[:,4])
        media = stock.mean(axis=0)
        print(media)
        name = str(x + "_data.csv")
        stock.to_csv('C:/Users/ignac/pyprojects/Investing_daily/Data/' + name)
        sleep(0.5)

    except:
        pass

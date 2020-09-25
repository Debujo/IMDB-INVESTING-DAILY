import investpy
import datetime
import pandas as pd
import time, config, os

today = datetime.date.today()
date = str(today.day) + "/" + str(today.month) + "/" + str(today.year)
mean_datetime = today - datetime.timedelta(days = config.mean_number)
mean_date = str(mean_datetime.day) + "/" + str(mean_datetime.month) + "/" + str(mean_datetime.year)

stocks = investpy.get_stocks_list(country = config.country_name)
#print(len(stocks)) #4582*25kb = 120Mb en csv

stock = []
for x in stocks:
    try:
        stock = investpy.get_stock_historical_data(stock= x, country=config.country_name, from_date=config.from_date, to_date=date)
        print(str(x))
        n_days = len(stock)
        mean_df = stock[n_days-config.mean_number:n_days] # Filters the Data Frame to get the last mean_number days
        simple_mean = mean_df.Close.mean()
        print(simple_mean)

        name = str(x + "_data.csv")
        if config.csv_save == True:
            stock.to_csv(config.data_location + name)
            sleep(0.5)
        else:
            try:
                os.remove(config.data_location + name)
            except OSError:
                pass


    except:
        pass

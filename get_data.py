import investpy, datetime, time, config, os, notification, math, rsi
import pandas as pd

t = time.time()
today = datetime.date.today()
print(today)
date = str(today.day) + "/" + str(today.month) + "/" + str(today.year)
mean_datetime = today - datetime.timedelta(days = config.moving_average)
mean_date = str(mean_datetime.day) + "/" + str(mean_datetime.month) + "/" + str(mean_datetime.year)

stocks = investpy.get_stocks_list(country = config.country_name)
#print(stocks[0:100]) # NASDAQ
stocks = stocks[0:620]
#print(stocks[300:600]) # NASDAQ + SP500
#print(len(stocks)) #4582*25kb = 120Mb en csv

def csv_save(x):
    name = str(x + "_data.csv")
    if config.csv_save == True:
        stock.to_csv(config.data_location + name)
        sleep(0.5)
    else:
        try:
            os.remove(config.data_location + name)
        except OSError:
            pass

def get_stocks_data():
    stock = []
    for x in stocks:
        try:
            stock = investpy.get_stock_historical_data(stock=x, country=config.country_name, from_date=config.from_date, to_date=date)
        except:
            print("Error al obtener los datos de " + x)
            continue
        print(str(x))
        n_days = len(stock)
        mean1_df = stock[n_days-config.moving_average:n_days] # Filters the Data Frame to get the last mean_number days
        mean2_df = stock[math.floor(n_days-(config.moving_average/3)):n_days] # Filters the Data Frame to get the last mean_number/2 days
        mean1_simple = mean1_df.Close.mean() # Long term mean
        mean2_simple = mean2_df.Close.mean() # Short term mean
        rsi_x = rsi.get_rsi(stock, 14)
        # Bearish trend with bearish candlestick (2)
        if (mean1_simple >= mean2_simple) & ((stock.Open[n_days-2]-stock.Close[n_days-2]) >= 0):
            # Big bullish turning clandlestick with rsi
            if ((stock.Close[n_days-1]/stock.Open[n_days-2]) >= config.turn_up_percentage) & ((stock.Open[n_days-1]/stock.Close[n_days-2]) <= 1.01):
                # Check RSI for prove
                if (rsi_x[-2] < 31):
                    print("TURNING STOCK: " + x +"!")
                    notification.send_email(x)  #Send Alert notification()
        csv_save(x)

get_stocks_data()
elapsed = time.time() - t
print("ELAPSED TIME: " + str(elapsed))

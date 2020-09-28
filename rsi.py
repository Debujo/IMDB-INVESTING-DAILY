import pandas, datetime, config, time
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Window length for moving average
window_length = 14
# Dates
today = datetime.date.today()
mean_datetime = today - datetime.timedelta(days = config.moving_average)

def get_rsi(stock, n):

    n_days = len(stock)
    diff = stock.Close.diff(1)      # diff in one field(one day)

    #this preservers dimensions off diff values
    up_chg = 0 * diff
    down_chg = 0 * diff

    # up change is equal to the positive difference, otherwise equal to zero
    up_chg[diff > 0] = diff[ diff>0 ]

    # down change is equal to negative deifference, otherwise equal to zero
    down_chg[diff < 0] = diff[ diff < 0 ]

    # check pandas documentation for ewm
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.ewm.html
    # values are related to exponential decay
    # we set com=time_window-1 so we get decay alpha=1/time_window
    up_chg_avg   = up_chg.ewm(com=n-1 , min_periods=n).mean()
    down_chg_avg = down_chg.ewm(com=n-1 , min_periods=n).mean()

    rs = abs(up_chg_avg/down_chg_avg)
    rsi = 100 - 100/(1+rs)
    return rsi

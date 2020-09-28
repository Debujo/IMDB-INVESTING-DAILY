"""
   ___                 __  _
  / __\  ___   _ __   / _|(_)  __ _
 / /    / _ \ | '_ \ | |_ | | / _` |
/ /___ | (_) || | | ||  _|| || (_| |
\____/  \___/ |_| |_||_|  |_| \__, |
                              |___/
"""
""" GET_DATA.PY """
# From which date you want to obtain the data
from_date = "01/01/2018"
# Number of days to calculate the mean
moving_average =  68
# Percentage required for the turning up candlestick
turn_up_percentage = 1.01
# Country where the stocks you want are located
country_name = 'United States'
# Default language
language = 'english'
# Saves all data in different csv (True / False)
csv_save = False
# Location of the saved csv_save
data_location = 'C:/Users/ignac/pyprojects/Investing_daily/Data/'


""" NOTIFICATION.PY """
# SMTP server host
smtp_host = 'smtp.gmail.com'
# SMTP server port
smtp_port = 587

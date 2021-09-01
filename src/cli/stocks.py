# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: September 1st, 2021

import time, datetime
import pandas as pd

ticker = input("Enter the stock ticker: ")
period1 = int(time.mktime(datetime.datetime(2021, 8, 1, 23, 59).timetuple()))  # Starting stock information date
period2 = int(time.mktime(datetime.datetime(2021, 8, 31, 23, 59).timetuple())) # Ending stock information date
interval = '1d'

query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

df = pd.read_csv(query_string)
print(df)

# Export To CSV
#df.to_csv()
#df.to_excel()

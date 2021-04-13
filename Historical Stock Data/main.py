'''
Developed by: Calinescu Mihai
Date: 8 Apr, 2021

Github: https://github.com/CMihai99
'''


import time, datetime
import pandas as pd

ticker = 'FB'   # Stock ticker symbol
period1 = int(time.mktime(datetime.datetime(2020, 12, 1, 23, 59).timetuple()))  # Starting stock information date
period2 = int(time.mktime(datetime.datetime(2020, 12, 31, 23, 59).timetuple())) # Ending stock information date
interval = '1d' # 1d, 1m

# Setup Link
query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

# Export To CSV
df = pd.read_csv(query_string)
print(df)
#df.to_csv()
#df.to_excel()

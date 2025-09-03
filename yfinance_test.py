# import yfinance as yf

# data = yf.download("AMZN AAPL GOOG", start="2017-01-01", end="2017-04-30")
# data

import pandas as pd

days = pd.read_csv("tempdata.csv")

days= days.dropna()
myvar = pd.DataFrame(days)
x=pd.Series

print(myvar.head(20))
print(myvar.tail(10))

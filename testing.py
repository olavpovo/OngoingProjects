import yfinance

print(dir(yfinance))

stock=yfinance.Ticker("NVDA")

# print(type(stock.news))
print(stock.analyst_price_targets,"\n")
for item in stock.news:
    print(item['title'])

        



 
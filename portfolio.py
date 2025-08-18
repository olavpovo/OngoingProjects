
##Get stocks, quantity, cost to provide costprice.
from datetime import datetime

### DEFS ###
#def to add shares into readable portfolio
#   - PRTF is a dictionary, easy entry/symbol is a new entry if not already added.
#   - entry is assgined a dateAdded, shares, cost, costprice entries.

def addShares(prtf):
    name= input("Enter symbol: ").upper() #"djjd".upper()
    if name not in prtf:
        prtf[name]={}
        shares= int(input("Enter shares: "))
        prtf[name]["shares"] =  shares
        prtf[name]["cost"] = float(input("Enter cost: "))
        prtf[name]["costprice"]=prtf[name]["cost"]*shares
        datePurchase= input("Date of Trade: YYYY.MM.DD ")
        prtf[name]["dateAdded"]=datetime.strptime(datePurchase, "%Y.%m.%d")
        print(f"{prtf[name]['dateAdded'].strftime('%Y.%m.%d')}: {shares} shares of {name} at {prtf[name]['cost']}, for a total value of {prtf[name]['costprice']}")
    else:
        print(f"{name} is already in portfolio {prtf[name]}.")

#There is room above to improve code into a def def to organize data.

#Get Share info for each ticker
#   - find duration of ownership

def shareInfo(prtf):
    for key,value in prtf.items():
        duration=datetime.now()-prtf[key]['dateAdded']
        purchaseDate=datetime.strftime(prtf[key]['dateAdded'], "%Y.%m.%d")
        print(key)
        print(f"Shares Owned: {prtf[key]['shares']}, Cost Price: {prtf[key]['cost']}, Avg Price: {prtf[key]['costprice']}, Purchase Date: {purchaseDate}, Duration: {duration.days} days")

#Navigation Menu
def start():
    print("")
    print("1. Add Stock")
    print("2. Share Info")
    print("0. EXIT")
    print("")




prtf={}

while True:
    start()
    entry=int(input("Please type of #: "))

    if entry == 1:
        addShares(prtf)
    elif entry == 2:
        shareInfo(prtf)
    if entry == 0:
        break







# print(f"Added {int(quantity)} shares of {ticker} for a total price of {price}")


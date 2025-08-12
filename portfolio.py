
##Get stocks, quantity, cost to provide costprice.
from datetime import datetime

def addShares(prtf):
    name= "nvda".upper() #input("Enter symbol: ").upper()
    if name not in prtf:
        prtf[name]={}
        shares= 8 #int(input("Enter shares: "))
        prtf[name]["shares"] =  shares
        prtf[name]["cost"] = 10 #float(input("Enter cost: "))
        prtf[name]["costprice"]=prtf[name]["cost"]*shares
        date=input("Date of Trade: YYYY.MM.DD ")
        prtf[name]["dateAdded"]=datetime.strptime(date, "%Y.%m.%d")
        print(f"{prtf[name]['dateAdded'].strftime('%Y.%m.%d')}: {shares} shares of {name} at {prtf[name]['cost']}, for a total value of {prtf[name]['costprice']}")
    else:
        print(f"{name} is already in portfolio {prtf[name]}.")
#There is room above to improve code into a def def to organize data.

#Navigation Menu
def start():
    print("")
    print("1. Add Stock")
    print("2. Share Info")
    print("0. EXIT")
    print("")

def shareInfo(prtf):
    today=datetime.today()
    for key,value in prtf.items():
        print(key,value, f"Duration: {prtf[key]['dateAdded']-today}")


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


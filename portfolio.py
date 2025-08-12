
##Get stocks, and quantity##

def addShares(prtf):
    name=input("Enter symbol: ").upper()
    if name not in prtf:
        prtf[name]={}
        shares= 8 #int(input("Enter shares: "))
        prtf[name]["shares"] = shares
        prtf[name]["cost"] = 10 #float(input("Enter cost: "))
        prtf[name]["costprice"]=prtf[name]["cost"]*shares
        print(f"Added {shares} shares of {name} at {prtf[name]['cost']}, for a total value of {prtf[name]['costprice']}")

prtf={}

def start():
    print("")
    print("1. Add Stock")
    print("0. EXIT")
    print("")


while True:
    start()
    entry=int(input("Please type of #: "))

    if entry == 1:
        addShares(prtf)
    if entry == 0:
        break







# print(f"Added {int(quantity)} shares of {ticker} for a total price of {price}")


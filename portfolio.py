
##Get stocks, and quantity##


def addPosition():
    ticker= "nvda".upper() #str(input("Please input ticker symbol: ")).upper()
    if ticker not in prtf:
        prtf["name"]= ticker
        for key,values in prtf.items():
            if values == ticker:
                prtf["name"]["shares"]=30
                print("done")



prtf={}
addPosition()


def addShares(stkQuan):
    quantity=float(input("How many shares?: "))
    stkQuan.append(quantity)
    price=float(input("At what price? "))




# print(f"Added {int(quantity)} shares of {ticker} for a total price of {price}")


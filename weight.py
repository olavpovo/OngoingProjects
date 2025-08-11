from datetime import datetime

def add_weight(weight):
    time=datetime.now()

    with open("weight.csv", "a") as file:
        line=time.strftime("%x,%X")
        
        file.write(f"{line},{weight}\n")

weight=float(input("Please enter todays weight:"))



add_weight(weight)

print("Added!")

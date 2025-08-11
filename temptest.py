def thtest():

    day=[]
    hum=100
    with open("tempdata.csv") as file:
        for line in file:
            newline=line.replace("\n","")
            newline=newline.split(",")
            # print(newline)
            if newline[3] == '24':
                continue
            else:
                if float(newline[3])<  float(hum):
                    hum=float(newline[3])

            day.append(float(newline[2]))

    print(f"The highest temp recorded is {max(day):.1f}C, min:{min(day)},average: {(sum(day)/len(day)):.1f}C and lowest humidity is {hum:.1f}%")

if __name__ == "__main__":
    thtest()


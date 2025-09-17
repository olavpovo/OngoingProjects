from astral import LocationInfo
from datetime import datetime,timedelta
from astral.sun import sun
from astral import moon

locC=LocationInfo("Canberra","Australia","Australia/ACT",-35.3135878,148.9649744)
locRH=LocationInfo("Richmond Hill","Canada","America/Toronto",43.8868872,-79.4222348)
locs=[]
locs.append(locC)
locs.append(locRH)
wen=datetime.strptime('2025,9,11','%Y,%m,%d')+timedelta(days=0)

for location in locs:
    sund=sun(location.observer, wen,tzinfo="America/Toronto")
    print(f"Location: {location.name}, Sunrise: {datetime.strftime(sund['sunrise'], '%d.%m.%Y, %H:%M:%S')}")
    print(f"Location: {location.name}, Sunset: {datetime.strftime(sund['sunset'], '%d.%m.%Y, %H:%M:%S')}")

moond=moon.phase(wen)

print(f"Moon Phase: {moond}")

import astral
import astral.sun
from datetime import datetime

loc=astral.LocationInfo("Richmond Hill","Canada","America/Toronto",43.8828,79.4403)
# z=astral.zoneinfo("America/Toronto")
s=astral.sun(loc,datetime.today(),loc.timezone)
print(s)
import Adafruit_DHT 
import sys
import requests
from datetime import datetime


# Set the sensor type
sensor = Adafruit_DHT.DHT22

# Set the GPIO pin where the DHT11 data pin is connected
pin = 26                # Change to your actual GPIO pin
# Try to grab a sensor reading. Use the read_retry method which will retry up to 15 times to get a sensor reading (waiting 2 seconds between each retry).
#humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
humidity, temperature = 24, 0 #Adafruit_DHT.read_retry(sensor, pin)


# Check if we got a valid reading if humidity is not None and temperature is not None: 
# print('Temp={0:0.1f}*C, Humidity={1:0.1f}%'.format(temperature, humidity))
#else: 
#    print("Failed to get reading. Try again!")

#Post to ntfy/raspi1
requests.post("http://192.168.1.146:9002/raspi1", data=f"Temp: {temperature:.1f}*C, Humidity: {humidity:.1f}%", headers={"Title": "438 Weather Update", "Tags":"computer"})

#Gather timie date and convert date/time.
dateData=datetime.now()
date=dateData.strftime("%d.%m.%y")
time=dateData.strftime("%H:%M")

#Write information to file, tempdata.csv- date, time, temp, humidity, count
line=f"{date},{time},{temperature},{humidity}"

with open("tempdata.csv", "a") as filename:
    filename.write(line+"\n")


sys.exit(1)

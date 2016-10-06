import Adafruit_DHT

#setup the sensor type
sensor = Adafruit_DHT.DHT11

# Setup the pins we are connect to
GPIOpin = 4

def getTempF():
  "This function returns the temperature in F from the sensor"
  humidity, temperature = Adafruit_DHT.read_retry(sensor, GPIOpin)
  temperature = ((temperature * 9) / 5) + 32
  return temperature

def getTempC():
    "This function returns the temperature in C from the sensor"
    humidity, temperature = Adafruit_DHT.read_retry(sensor, GPIOpin)
    return temperature

def getHumidity():
    "This function returns the humidity from the sensor"
    humidity, temperature = Adafruit_DHT.read_retry(sensor, GPIOpin)
    return humidity

print(getTemp())

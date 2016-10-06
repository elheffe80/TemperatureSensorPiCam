import Adafruit_DHT

sensor = Adafruit_DHT.DHT11

# Setup the pins we are connect to
DHTpin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, DHTpin)

#convert temperature to Fahrenheit
temperature = ((temperature * 9) / 5) + 32

if humidity is not None and temperature is not None:
	dht11info = ('Temp={0:0.1f}F  Humidity={1:0.1f}%'.format(temperature, humidity))
	print(dht11info)
else:
	print('Failed to get reading, you suck.')

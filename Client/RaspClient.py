import requests
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

# Set the DHT sensor type and GPIO pin
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # GPIO pin where DHT11 data pin is connected
# Set the GPIO pin for the raindrop sensor
RAIN_PIN = 17  # GPIO pin where the raindrop sensor is connected
# Server endpoint to post data
SERVER_URL = "https://weatherrpi.azurewebsites.net/upload"  

def Raining(israining):
            if (israining):
                return "Raining"
            return "Not Raining"
while True:
    try:
        # Read temperature and humidity data from the DHT11 sensor
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

        # Read raindrop sensor data
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(RAIN_PIN, GPIO.IN)
        rain_data = GPIO.input(RAIN_PIN)
        
        israining= rain_data == 0 
        # Prepare the data to be sent to the server
        data_to_send = {
            "Temperature": temperature,
            "Humidity": humidity ,
            "Rain":israining
            
        }
        
        print("Humidity:{0}% , Temperature:{1} , {2}".format(humidity,temperature,Raining(israining)))

        # Send the data to the server
        response = requests.post(SERVER_URL, json=data_to_send)

        if response.status_code == 200:
            print("Data sent successfully")
        else:
            print("Failed to send data. Status code:", response.status_code)

        # Cleanup GPIO resources
        GPIO.cleanup()

        time.sleep(3)  # Wait for 3 seconds before sending the next request
    except Exception as e:

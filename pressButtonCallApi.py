import RPi.GPIO as GPIO
import time
import requests

BUTTON_PIN = 17
API_URL = "http://192.168.1.24:8080/api/buttonTest"
API_DATA = {"message": "Button was pressed"}
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            try:
                response = requests.post(API_URL, json=API_DATA)
                print(f"API Response: {response.status_code} - {response.text}")
            except Exception as e:
                print(f"Error calling API: {e}")
                time.sleep(0.5)
            while GPIO.input(BUTTON_PIN) == GPIO.LOW:
                time.sleep(0.02)
            time.sleep(0.15)
        time.sleep(0.01)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
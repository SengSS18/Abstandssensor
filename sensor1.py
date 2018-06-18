import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
 
def distance():
    GPIO.output(18, True)
    time.sleep(0.000001)
    GPIO.output(18, False)
    start = time.time()
    stop = time.time()
    while GPIO.input(24) == 0:
        start = time.time()
    while GPIO.input(24) == 1:
        stop = time.time()
    distance = ((stop - start) * 17160)
    return distance

try:
    while True:
       	messung = distance()
	print (messung)
	time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
 

import RPi.GPIO as GPIO
import time
import os
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
       	print messung
	if messung > 150:
            pass
        else:
            if messung >= 150:
                os.system("aplay Desktop/links.wav")
                time.sleep(1.5)
            else:
                if messung >= 100:
                    os.system("aplay Desktop/links.wav")
                    time.sleep(1.0)
                else:
                    if messung >= 75:
                        os.system("aplay Desktop/links.wav")
                        time.sleep(0.6)
                    else:
                        if messung >= 50:
                            os.system("aplay Desktop/links.wav")
                            time.sleep(0.5)
                        else:
                            if messung >= 40:
                                os.system("aplay Desktop/links.wav")
                                time.sleep(0.3)
                            else:
                                if messung >= 30:
                                    os.system("aplay Desktop/links.wav")
                                    time.sleep(0.2)
                                else:
                                    if messung >= 20:
                                        os.system("aplay Desktop/links.wav")
                                        time.sleep(0.1)
                                    else:
                                        if messung >= 15:
                                            os.system("aplay Desktop/links.wav")
except KeyboardInterrupt:
    GPIO.cleanup()
 

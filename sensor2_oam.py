import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.IN)
GPIO.setup(17, GPIO.OUT)
 
def distance():
    GPIO.output(17, True)
    time.sleep(0.000001)
    GPIO.output(17, False)
    start = time.time()
    stop = time.time()
    while GPIO.input(23) == 0:
        start = time.time()
    while GPIO.input(23) == 1:
        stop = time.time()
    distance = ((stop - start) * 17160)
    return distance

try:
    while True:
       	messung = distance()
       	print messung
	if messung > 150:
            time.sleep(1.0)
        else:
            if messung >= 150:
                os.system("aplay Desktop/rechts.wav")
                time.sleep(1.5)
            else:
                if messung >= 100:
                    os.system("aplay Desktop/rechts.wav")
                    time.sleep(1.0)
                else:
                    if messung >= 75:
                        os.system("aplay Desktop/rechts.wav")
                        time.sleep(0.6)
                    else:
                        if messung >= 50:
                            os.system("aplay Desktop/rechts.wav")
                            time.sleep(0.5)
                        else:
                            if messung >= 40:
                                os.system("aplay Desktop/rechts.wav")
                                time.sleep(0.3)
                            else:
                                if messung >= 30:
                                    os.system("aplay Desktop/rechts.wav")
                                    time.sleep(0.2)
                                else:
                                    if messung >= 20:
                                        os.system("aplay Desktop/rechts.wav")
                                        time.sleep(0.1)
                                    else:
                                        if messung >= 15:
                                            os.system("aplay Desktop/rechts.wav")
                                            
                                            
except KeyboardInterrupt:
    GPIO.cleanup()
 

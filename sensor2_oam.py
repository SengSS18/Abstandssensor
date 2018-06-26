import RPi.GPIO as GPIO
import time
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
	if messung > 150:
            pass
        else:
            if messung >= 150:
                print "a"
                time.sleep(1.5)
            else:
                if messung >= 100:
                    print "b"
                    time.sleep(1.0)
                else:
                    if messung >= 75:
                        print "c"
                        time.sleep(0.6)
                    else:
                        if messung >= 50:
                            print "d"
                            time.sleep(0.5)
                        else:
                            if messung >= 40:
                                print "e"
                                time.sleep(0.4)
                            else:
                                if messung >= 30:
                                    print "f"
                                    time.sleep(0.3)
                                else:
                                    if messung >= 20:
                                        print "g"
                                        time.sleep(0.2)
                                    else:
                                        if messung >= 15:
                                            print "h"
                                            time.sleep(0.1)
                                            
except KeyboardInterrupt:
    GPIO.cleanup()
 

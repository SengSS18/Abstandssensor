import os
def playsound(frequency, duration):
    os.system('beep -f %s -l %s' % (frequency,duration))


while 1:
    frequency = 1000
    duration = 1000
    playsound(frequency, duration)





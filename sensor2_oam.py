# GPIO-Treiber importieren
import RPi.GPIO as GPIO

# Modul zur Zeitberechnung importieren
import time

# Modul zur Ausfuehrung von Bash-Befehlen importieren
import os

# GPIO-Bibliothek aktivieren
GPIO.setmode(GPIO.BCM)

# GPIO-Warnmeldungen deaktivieren
GPIO.setwarnings(False)

# GPIO 23 als Eingang definieren (Echo)
GPIO.setup(23, GPIO.IN)

# GPIO 17 als Ausgang definieren (Trigger)
GPIO.setup(17, GPIO.OUT)

#Funktion zur Entfernungsmessung
def distance():
    GPIO.output(17, True)			# High auf GPIO 17 (Trigger)
    time.sleep(0.000001)			# 1 Mikrosekunde warten
    GPIO.output(17, False)			# Low auf GPIO 17 (trigger)
    start = time.time()				# Aktuelle Zeit als Start-Variable
    stop = time.time()				# Aktuelle Zeit als Stop-Variable
    while GPIO.input(23) == 0:
        start = time.time()			# Solange GPIO 23 (Echo) Low ist, aktuelle Zeit als Start-Variable speichern
    while GPIO.input(23) == 1:
        stop = time.time()			# Sobald GPIO 23 (Echo) High ist, aktuelle Zeit als Stop-Variable speichern
    distance = ((stop - start) * 17160)		# Differenz zwischen Start-Variable und Stop-Variable (=Dauer der Messung) durch Schallgeschwindigkeit teilen
    return distance				# Ergebnis als Rueckgabewert ausgeben

try:
    while True:					# Endlosschleife generieren
       	messung = distance()    # Ergebnis der Funktion in Variable schreiben
	if messung > 150:           # Wenn Entfernung >1.50m, dann nichts tun und 2.5s warten
	    print ("Distanz: ueber 1.50m")
            time.sleep(2.5)
        else:
                if messung >= 100:      # Wenn Entfernung zwischen 1.50m und 1m, dann Entfernungsbereich anzeigen, piepen und 1.25s warten
                    print ("Distanz: 1.5m - 1m")
                    os.system("aplay Desktop/rechts.wav")
                    time.sleep(1.25)
                else:
                    if messung >= 75:   # Wenn Entfernung zwischen 1m und 0.75m, dann Entfernungsbereich anzeigen, piepen und 1s warten
                        print ("Distanz: 1m - 0.75m")
                        os.system("aplay Desktop/rechts.wav")
                        time.sleep(1)
                    else:
                        if messung >= 50:   # Wenn Entfernung zwischen 0.75m und0.5m, dann Entfernungsbereich anzeigen, piepen und 0.75s warten
                            print ("Distanz: 0.75m - 0.5m")
                            os.system("aplay Desktop/rechts.wav")
                            time.sleep(0.75)
                        else:
                                    if messung >= 25:   # Wenn Entfernung zwischen 0.50m und 0.25m, dann Entfernungsbereich anzeigen, piepen und 0.5s warten
                                        print ("Distanz: 0.5m - 0.25m")
                                        os.system("aplay Desktop/rechts.wav")
                                        time.sleep(0.5)
                                    else:
                                        if messung >= 15:   # Wenn Entfernung zwischen 0.25m und 0.15m, dann Entfernungsbereich anzeigen, piepen und 0.25s warten
                                            print ("Distanz: 0.25m - 0.15m")
                                            os.system("aplay Desktop/rechts.wav")
                                            time.sleep(0.25)
                                        else:
                                            if messung < 15:# Wenn Entfernung kleiner als 0.15m, dann Entfernungsbereich anzeigen, piepen und nicht warten
                                                print ("Distanz: unter 0.15m")
                                                os.system("aplay Desktop/rechts.wav")

except KeyboardInterrupt:   #Pruefen on Ctrl + C gedrueckt wurde
    GPIO.cleanup()
 

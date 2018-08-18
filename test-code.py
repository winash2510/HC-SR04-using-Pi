import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ECHO = 23
TRIG = 25


GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

while True:
    GPIO.output(TRIG,GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG,GPIO.LOW)

    while(GPIO.input(ECHO)) == False:
        pass
    start = time.time()

    while(GPIO.input(ECHO)) == True:
        pass
    stop = time.time()

    sig_time = stop-start

    distance = sig_time*17000

    print "Distance: %.2f cm"%distance
    time.sleep(0.05)
    


import RPi.GPIO as GPIO
import time
import sys


GPIO_POWER  =  8 # PIN 24
GPIO_STATUS =  7 # PIN 26

CMDS = {'power', 'power4s', 'status'}

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM) # pin scheme

    GPIO.setup(GPIO_STATUS, GPIO.IN) 
    GPIO.setup(GPIO_POWER, GPIO.OUT) 
    GPIO.output(GPIO_POWER, GPIO.LOW)

def power(sleeptime=0.5):
    GPIO.output(GPIO_POWER, GPIO.HIGH)
    time.sleep(sleeptime)
    GPIO.output(GPIO_POWER, GPIO.LOW)

def status():
    if GPIO.input(GPIO_STATUS) == 1:
        return 0
    else:
        return 1

def main():
    if len(sys.argv) != 2:
        print("You need to provide a command: {}".format(CMDS))
        exit(1)
    
    cmd = sys.argv[1]
    if cmd not in CMDS:
        print("Unknown command: {} not in {}".format(cmd, CMDS))
        exit(1)

    setup()

    if cmd == 'power':
        power()
    elif cmd == 'power4s':
        power(4.5)
    elif cmd == 'status':
        print("LED status: {}".format(status()))


if __name__ == '__main__':
    main()

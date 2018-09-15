import RPi.GPIO as GPIO
import time
import signal
import sys
import termios
import datetime

def signal_handler(sig, frame):
	GPIO.cleanup()
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)


def getch(inp = sys.stdin):
    old = termios.tcgetattr(inp)
    new = old[:]
    new[-1] = old[-1][:]
    new[3] &= ~(termios.ECHO | termios.ICANON)
    new[-1][termios.VMIN] = 1
    try:
        termios.tcsetattr(inp, termios.TCSANOW, new)
        return inp.read(1)
    finally:
        termios.tcsetattr(inp, termios.TCSANOW, old)

print('press t to start/end')
start = False
startTime = time.time()
endTime = time.time()

while 1:
    c = getch()
    if c == 't':
    	if start == False: 
    		start = True
    		GPIO.output(18, True)
    		startTime = time.time()
    		print('start')
    	else:
    		start = False
    		GPIO.output(18, False)
    		endTime = time.time() - startTime
    		st = datetime.datetime.fromtimestamp(endTime).strftime('%H:%M:%S:%f')
    		print('It took ' + st)

    
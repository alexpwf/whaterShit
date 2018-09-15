import RPi.GPIO as GPIO
import time
import signal
import sys

def signal_handler(sig, frame):
	GPIO.cleanup()
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()


size = 0.
if (len(sys.argv) >= 2):
    size = float(sys.argv[1])
else:
    print('I need to know the capacity')
    sys.exit(0)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

startTime = time.time()

GPIO.output(18, True)

timeWillTake = size*0.05
print('This will take ' + str(timeWillTake) + 's')

while time.time() - startTime < timeWillTake: 
	printProgressBar(time.time() - startTime, timeWillTake, prefix = 'Progress:', suffix = 'Complete', length = 50)
	time.sleep(.1)
	
printProgressBar(timeWillTake, timeWillTake, prefix = 'Progress:', suffix = 'Complete', length = 50)
print('Done')
GPIO.output(18, False)
GPIO.cleanup()

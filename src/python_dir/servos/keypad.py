# import required libraries
import RPi.GPIO as GPIO
import time
import subprocess

# these GPIO pins are connected to the keypad
# change these according to your connections!
L1 = 25
L2 = 8
L3 = 7
L4 = 1

C1 = 12
C2 = 16
C3 = 20
C4 = 21

# Initialize the GPIO pins

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

# Make sure to configure the input pins to use the internal pull-down resistors

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# The readLine function implements the procedure discussed in the article
# It sends out a single pulse to one of the rows of the keypad
# and then checks each column for changes
# If it detects a change, the user pressed the button that connects the given line
# to the detected column

PYTHON = "/home/oreo-pi/.local/share/virtualenvs/(venv)/bin/python"

def readLine(line):
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1 and line == L1):
        subprocess.Popen(["flock", "-n", "/tmp/script_running.lock", PYTHON, "/home/oreo-pi/python_dir/servos/testing/eyes_test.py"])
    if(GPIO.input(C2) == 1 and line == L1):
        subprocess.Popen(["flock", "-n", "/tmp/script_running.lock", PYTHON, "/home/oreo-pi/python_dir/servos/testing/jaw_test.py"])
    if(GPIO.input(C3) == 1 and line == L1):
        subprocess.Popen(["flock", "-n", "/tmp/script_running.lock", PYTHON, "/home/oreo-pi/python_dir/servos/testing/neck_test.py"])
    if(GPIO.input(C4) == 1 and line == L1):
        subprocess.Popen(["flock", "-n", "/tmp/script_running.lock", PYTHON, "/home/oreo-pi/python_dir/servos/testing/test_run.py"])
    if(GPIO.input(C1) == 1 and line == L4):
        subprocess.Popen(["flock", "-n", "/tmp/script_running.lock", PYTHON, "/home/oreo-pi/python_dir/servos/movements/casual.py"])
    if(GPIO.input(C2) == 1 and line == L4):
        subprocess.Popen(["flock", "-n", "/tmp/script_running.lock", PYTHON, "/home/oreo-pi/python_dir/servos/movements/laughing.py"])
    if(GPIO.input(C3) == 1 and line == L4):
        subprocess.Popen(["flock", "-n", "/tmp/script_running.lock", PYTHON, "/home/oreo-pi/python_dir/servos/movements/scared.py"])
    GPIO.output(line, GPIO.LOW)

try:
    while True:
        # call the readLine function for each row of the keypad
        readLine(L1)
        readLine(L2)
        readLine(L3)
        readLine(L4)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nApplication stopped!")
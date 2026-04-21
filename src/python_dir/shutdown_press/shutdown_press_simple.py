#!/usr/bin/env python3

from gpiozero import Button

import os

Button(11).wait_for_press()

os.system("sudo shutdown -h now")
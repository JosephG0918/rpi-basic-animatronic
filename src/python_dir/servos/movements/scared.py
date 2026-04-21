from servos_package import *
from time import *

open_lids()
look_straight()
h_center()
v_center()
close_jaw()

sleep(1)

wide_lids()

for _ in range(3):
    look_left()
    sleep(0.3)
    look_right()
    sleep(0.3)

open_jaw()

for _ in range(4):
    look_left()
    sleep(0.3)
    look_right()
    sleep(0.3)

close_jaw()
h_right()
look_right()
sleep(0.5)
h_left()
look_left()
sleep(0.5)
h_center()

for _ in range(4):
    look_left()
    sleep(0.3)
    look_right()
    sleep(0.3)

close_jaw()
h_right()
look_right()
sleep(0.5)
h_left()
look_left()
sleep(0.5)
h_center()

open_lids()
look_straight()
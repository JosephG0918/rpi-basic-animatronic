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
    open_jaw()
    sleep(0.3)
    close_jaw()
    sleep(0.3)

v_up()
h_right()

for _ in range(3):
    open_jaw()
    sleep(0.3)
    close_jaw()
    sleep(0.3)

h_left()

for _ in range(3):
    open_jaw()
    sleep(0.3)
    close_jaw()
    sleep(0.3)

v_center()
h_center()

for _ in range(3):
    open_jaw()
    sleep(0.3)
    close_jaw()
    sleep(0.3)

open_lids()
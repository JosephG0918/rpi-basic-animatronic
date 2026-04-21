from servos_package import *
from time import *

for _ in range(2):
    open_lids()
    look_straight()
    h_center()
    v_center()
    close_jaw()

    sleep(1)

    look_right()
    sleep(0.5)
    look_left()

    close_lids()
    sleep(0.5)
    open_lids()

    sleep(0.5)
    look_straight()

    sleep(1)

    h_right()
    look_right()
    sleep(1)
    look_left()
    h_left()

    sleep(0.5)

open_lids()
look_straight()
h_center()
v_center()
close_jaw()
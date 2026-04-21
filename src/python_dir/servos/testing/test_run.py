from servos_package import *
from time import *

for _ in range(2):
    open_lids()
    look_straight()
    h_center()
    v_center()
    close_jaw()

    sleep(1)

    look_left()
    sleep(0.5)
    look_right()

    h_right()
    v_down()

    close_lids()
    sleep(0.3)
    open_lids()

    h_left()
    v_up()

    open_jaw()
    sleep(0.5)
    close_jaw()

    sleep(1)

    h_center()
    v_center()

    look_straight()
    sleep(0.5)
    look_right()
    sleep(0.3)
    look_left()
    sleep(0.5)

    close_lids()
    sleep(0.3)
    wide_lids()
    look_straight()
    sleep(0.5)
    open_lids()

open_lids()
look_straight()
h_center()
v_center()
close_jaw()
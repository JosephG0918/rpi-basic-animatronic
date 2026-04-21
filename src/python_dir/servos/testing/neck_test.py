from servos_package import *
from time import *

for _ in range(3):
    h_left()
    sleep(0.5)
    h_right()
    sleep(0.5)
    h_center()

    sleep(1)

    v_up()
    sleep(0.5)
    v_down()
    sleep(0.5)
    v_center()

    sleep(1)

h_center()
v_center()
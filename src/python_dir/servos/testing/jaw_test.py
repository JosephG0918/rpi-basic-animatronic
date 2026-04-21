from servos_package import *
from time import *

for _ in range(5):
    open_jaw()
    sleep(0.3)
    close_jaw()
    sleep(0.3)
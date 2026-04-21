from adafruit_servokit import ServoKit

# Initialize the ServoKit with 16 channels
kit = ServoKit(channels=16)

# Servo channel assignments
L_EYE_BALL = 1
L_EYE_LIDS = 0
R_EYE_BALL = 4
R_EYE_LIDS = 5
HORIZONTAL = 10
VERTICAL = 11
JAW = 15

# Eye functions
def open_lids():
    kit.servo[L_EYE_LIDS].angle = 121
    kit.servo[R_EYE_LIDS].angle = 63

def close_lids():
    kit.servo[L_EYE_LIDS].angle = 155
    kit.servo[R_EYE_LIDS].angle = 34

def wide_lids():
    kit.servo[L_EYE_LIDS].angle = 95
    kit.servo[R_EYE_LIDS].angle = 85

def look_straight():
    kit.servo[L_EYE_BALL].angle = 100
    kit.servo[R_EYE_BALL].angle = 73

def look_left():
    kit.servo[L_EYE_BALL].angle = 120
    kit.servo[R_EYE_BALL].angle = 98

def look_right():
    kit.servo[L_EYE_BALL].angle = 80
    kit.servo[R_EYE_BALL].angle = 55

# Neck functions
def h_left():
    kit.servo[HORIZONTAL].angle = 40

def h_right():
    kit.servo[HORIZONTAL].angle = 146

def h_center():
    kit.servo[HORIZONTAL].angle = 95

def v_down():
    kit.servo[VERTICAL].angle = 10

def v_up():
    kit.servo[VERTICAL].angle = 165

def v_center():
    kit.servo[VERTICAL].angle = 88

# Jaw functions
def close_jaw():
    kit.servo[JAW].angle = 135

def open_jaw():
    kit.servo[JAW].angle = 25
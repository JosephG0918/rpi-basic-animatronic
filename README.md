# Animatronic Raspberry Pi Project

A basic animatronic powered by a **Raspberry Pi Zero 2 W** that moves its eyes, eyelids, jaw, and neck. Input is handled via a **4x4 matrix keypad**, and power is supplied by a **7.4V Li-ion battery** with soft and hard shutdown controls.

[docs folder](./docs/)

---

## Project Overview
- Animatronic project using a Raspberry Pi and Waveshare 16-Channel Servo Driver HAT.
- Uses **7 micro servos** to animate 3D-printed parts (eyes, eyelids, jaw, neck).
- Each button on the keypad controls a specific component; one button triggers all simultaneously.
- Includes soft shutdown via momentary push button and hard power switch via rocker switch.

---

## Quick Specs

**Electronics:**
- Raspberry Pi Zero 2 W
- Waveshare 16-Channel Servo Driver HAT
- 7x SG90 Micro Servos
- 4x4 Matrix Keypad
- 7.4V 900mAh Li-Po Battery
- Rocker Switch (hard power)
- Momentary Push Button (soft shutdown)

**Software:**
- Python 3.11
- Libraries: `RPi.GPIO`, `adafruit-circuitpython-servokit`, `gpiozero`, `smbus`, `time`, `subprocess`

**3D Printing:**
- Printer: Bambu Lab P1S
- Software: Bambu Studio
- Modified pre-existing model for Pi mount, battery compartment, keypad, switches, and base legs

---

## Power Notes
> ⚠️ Always use the soft shutdown button before turning off the hard power switch to avoid SD card corruption.

---

![alt text](./img/IMG_0547.png)
![alt text](./img/IMG_0548.png)
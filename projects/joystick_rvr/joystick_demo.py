from evdev import InputDevice, categorize, ecodes
from os import path
from signal import signal, SIGINT
import sys
from time import sleep

JOYSTICK_CENTER = 65535 / 2
#DEADBAND_RADIUS = JOYSTICK_CENTER / 10
DEADBAND_RADIUS = JOYSTICK_CENTER - 1000
DEADBAND_MIN = JOYSTICK_CENTER - DEADBAND_RADIUS
DEADBAND_MAX = JOYSTICK_CENTER + DEADBAND_RADIUS
devicePath = '/dev/input/event2'
gamepad: InputDevice = None

def sigIntHandler(sig, frame):
    print("Exiting")
    sys.stderr.close() # Ignore any lingering exceptions
    sys.exit(0)

def waitForGamepad():
    global gamepad

    if gamepad:
        return

    if not path.exists(devicePath):
        print("Waiting for controller...")

    while not path.exists(devicePath):
        sleep(0.1)

    while True:
        try:
            gamepad = InputDevice(devicePath)
            print(gamepad)
            break
        except PermissionError:
            sleep(0.1)

def main():
    global gamepad

    while True:
        try:
            waitForGamepad()
            for event in gamepad.read_loop():
                if event.type == ecodes.EV_ABS:
                    if event.code == ecodes.ABS_X and event.value < DEADBAND_MIN:
                        print("Go left")
                    elif event.code == ecodes.ABS_X and event.value > DEADBAND_MAX:
                        print("Go right")
                    elif event.code == ecodes.ABS_Y and event.value < DEADBAND_MIN:
                        print("Go up")
                    elif event.code == ecodes.ABS_Y and event.value > DEADBAND_MAX:
                        print("Go down")
        except OSError:
            gamepad = None

if __name__ == '__main__':
    signal(SIGINT, sigIntHandler)
    main()


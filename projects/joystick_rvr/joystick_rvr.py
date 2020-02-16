from evdev import InputDevice, categorize, ecodes
from os import path
from signal import signal, SIGINT
import sys
from time import sleep, time

sys.path.append(path.abspath(path.join(path.dirname(__file__), '../../')))
from sphero_sdk import SpheroRvrObserver, RawMotorModesEnum

from raw_drive import drive

JOYSTICK_MAX = 65535
JOYSTICK_CENTER = JOYSTICK_MAX / 2
DEADBAND_RADIUS = JOYSTICK_CENTER / 8
MAX_MAGNITUDE = JOYSTICK_CENTER

MAX_SPEED = 90
MIN_SPEED = 40

RVR_FRAME_PERIOD_SEC = 0.1

devicePath = '/dev/input/event0'
gamepad: InputDevice = None

rvr = SpheroRvrObserver()

x = 0 # -MAX_MAGNITUDE -> MAX_MAGNITUDE
y = 0

def sigIntHandler(sig, frame):
    print("Exiting")
    rvr.close()
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

def handleEvent(event):
    global x
    global y

    if event and event.type == ecodes.EV_ABS:
        #print("Got event")
        if event.code == ecodes.ABS_X:
            x = event.value - JOYSTICK_CENTER
        elif event.code == ecodes.ABS_Y:
            y = event.value - JOYSTICK_CENTER

def main():
    global gamepad

    rvr.wake()
    sleep(2)
    rvr.reset_yaw()

    while True:
        try:
            waitForGamepad()

            while True:
            #for event in gamepad.read_loop():
                try:
                    #print("Reading")
                    for event in gamepad.read():
                        handleEvent(event)
                except BlockingIOError:
                    pass # No events available

                drive(x, y, rvr, MIN_SPEED, MAX_SPEED, DEADBAND_RADIUS, MAX_MAGNITUDE)
                sleep(RVR_FRAME_PERIOD_SEC)

        except OSError as e:
            print(e)
            gamepad = None

if __name__ == '__main__':
    signal(SIGINT, sigIntHandler)
    try:
        main()
    finally:
        rvr.close()


from evdev import InputDevice, categorize, ecodes
from os import path
from signal import signal, SIGINT
import sys
from time import sleep

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
                    print(event)
        except OSError:
            gamepad = None

if __name__ == '__main__':
    signal(SIGINT, sigIntHandler)
    main()


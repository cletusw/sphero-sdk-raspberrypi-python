from evdev import InputDevice, categorize, ecodes
from os import path
from signal import signal, SIGINT
import sys
from time import sleep

sys.path.append(path.abspath(path.join(path.dirname(__file__), '../../')))
from sphero_sdk import SpheroRvrObserver, RawMotorModesEnum

JOYSTICK_CENTER = 65535 / 2
#DEADBAND_RADIUS = JOYSTICK_CENTER / 10
DEADBAND_RADIUS = JOYSTICK_CENTER - 1000
DEADBAND_MIN = JOYSTICK_CENTER - DEADBAND_RADIUS
DEADBAND_MAX = JOYSTICK_CENTER + DEADBAND_RADIUS
devicePath = '/dev/input/event0'
gamepad: InputDevice = None

rvr = SpheroRvrObserver()

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

def main():
    global gamepad

    rvr.wake()
    sleep(2)
    rvr.reset_yaw()

    while True:
        try:
            waitForGamepad()
            for event in gamepad.read_loop():
                if event.type == ecodes.EV_ABS:
                    if event.code == ecodes.ABS_X and event.value < DEADBAND_MIN:
                        print("Go left")
                        rvr.raw_motors(
                            left_mode = RawMotorModesEnum.reverse.value,
                            left_speed = 64, # 0-255
                            right_mode = RawMotorModesEnum.forward.value,
                            right_speed = 64,
                        )
                    elif event.code == ecodes.ABS_X and event.value > DEADBAND_MAX:
                        print("Go right")
                        rvr.raw_motors(
                            left_mode = RawMotorModesEnum.forward.value,
                            left_speed = 64,
                            right_mode = RawMotorModesEnum.reverse.value,
                            right_speed = 64,
                        )
                    elif event.code == ecodes.ABS_Y and event.value < DEADBAND_MIN:
                        print("Go up")
                        rvr.raw_motors(
                            left_mode = RawMotorModesEnum.forward.value,
                            left_speed = 64, # 0-255
                            right_mode = RawMotorModesEnum.forward.value,
                            right_speed = 64,
                        )
                    elif event.code == ecodes.ABS_Y and event.value > DEADBAND_MAX:
                        print("Go down")
                        rvr.raw_motors(
                            left_mode = RawMotorModesEnum.reverse.value,
                            left_speed = 64, # 0-255
                            right_mode = RawMotorModesEnum.reverse.value,
                            right_speed = 64,
                        )
                    #else:
                    #    print("Stopping")
                    #    rvr.raw_motors(
                    #        left_mode=RawMotorModesEnum.off.value,
                    #        left_speed=0,  # Valid speed values are 0-255
                    #        right_mode=RawMotorModesEnum.off.value,
                    #        right_speed=0  # Valid speed values are 0-255
                    #    )
        except OSError:
            gamepad = None

if __name__ == '__main__':
    signal(SIGINT, sigIntHandler)
    try:
        main()
    finally:
        rvr.close()


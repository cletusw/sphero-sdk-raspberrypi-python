from evdev import InputDevice, categorize, ecodes
from math import sqrt, atan2, pi
from numpy import interp
from os import path
from signal import signal, SIGINT
import sys
from time import sleep, time

sys.path.append(path.abspath(path.join(path.dirname(__file__), '../../')))
from sphero_sdk import SpheroRvrObserver, RawMotorModesEnum

JOYSTICK_MAX = 65535
JOYSTICK_CENTER = JOYSTICK_MAX / 2
MAX_MAGNITUDE = JOYSTICK_CENTER
DEADBAND_RADIUS = JOYSTICK_CENTER / 8
#DEADBAND_RADIUS = JOYSTICK_CENTER - 1000
DEADBAND_MIN = JOYSTICK_CENTER - DEADBAND_RADIUS
DEADBAND_MAX = JOYSTICK_CENTER + DEADBAND_RADIUS

MAX_SPEED = 180
MIN_SPEED = 0

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

def drive():
    global x
    global y

    r = min(sqrt(x ** 2 + y ** 2), MAX_MAGNITUDE)
    theta = atan2(y, x)
    rAfterDeadzone = max(DEADBAND_RADIUS, r)
    rMappedToMotorSpeed = interp(rAfterDeadzone, [DEADBAND_RADIUS, MAX_MAGNITUDE], [MIN_SPEED, MAX_SPEED])
    magnitude = 0
    #print("Drive", r, theta, rAfterDeadzone, rMappedToMotorSpeed)

    if r < DEADBAND_RADIUS:
        rvr.raw_motors(
            left_mode=RawMotorModesEnum.off.value,
            left_speed=0,
            right_mode=RawMotorModesEnum.off.value,
            right_speed=0,
        )
    elif theta <= -pi / 2:
        # UP & LEFT
        magnitude = interp(theta, [-pi, -pi/2], [-1, 1])
        rvr.raw_motors(
            left_mode=RawMotorModesEnum.forward.value if magnitude >= 0 else RawMotorModesEnum.reverse.value,
            left_speed=int(abs(magnitude * rMappedToMotorSpeed)),
            right_mode=RawMotorModesEnum.forward.value,
            right_speed=int(rMappedToMotorSpeed),
        )
    elif theta > -pi / 2 and theta <= 0:
        # UP & RIGHT
        magnitude = interp(theta, [-pi/2, 0], [1, -1])
        rvr.raw_motors(
            left_mode=RawMotorModesEnum.forward.value,
            left_speed=int(rMappedToMotorSpeed),
            right_mode=RawMotorModesEnum.forward.value if magnitude >= 0 else RawMotorModesEnum.reverse.value,
            right_speed=int(abs(magnitude * rMappedToMotorSpeed)),
        )

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

            #now = time()
            #nextFrame = now + RVR_FRAME_PERIOD_SEC

            while True:
            #for event in gamepad.read_loop():
                try:
                    #print("Reading")
                    for event in gamepad.read():
                        handleEvent(event)
                    #*_, event = gamepad.read() # Get latest joystick event (ignore rest)
                except BlockingIOError:
                    #print("No events")
                    pass # No events available

                drive()
                sleep(RVR_FRAME_PERIOD_SEC)
                #now = time()
                #if now >= nextFrame:
                #    nextFrame += RVR_FRAME_PERIOD_SEC
                #    drive(x, y)

        except OSError as e:
            print(e)
            gamepad = None

if __name__ == '__main__':
    signal(SIGINT, sigIntHandler)
    try:
        main()
    finally:
        rvr.close()


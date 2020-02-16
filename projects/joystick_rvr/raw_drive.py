from evdev import InputDevice, categorize, ecodes
from math import sqrt, atan2, pi
from numpy import interp
from os import path
from signal import signal, SIGINT
import sys
from time import sleep, time

sys.path.append(path.abspath(path.join(path.dirname(__file__), '../../')))
from sphero_sdk import RawMotorModesEnum

JOYSTICK_MAX = 65535
JOYSTICK_CENTER = JOYSTICK_MAX / 2
MAX_MAGNITUDE = JOYSTICK_CENTER
DEADBAND_RADIUS = JOYSTICK_CENTER / 8
#DEADBAND_RADIUS = JOYSTICK_CENTER - 1000
DEADBAND_MIN = JOYSTICK_CENTER - DEADBAND_RADIUS
DEADBAND_MAX = JOYSTICK_CENTER + DEADBAND_RADIUS

MAX_SPEED = 90
MIN_SPEED = 10

RVR_FRAME_PERIOD_SEC = 0.1

def drive(x, y, rvr, MIN_SPEED, MAX_SPEED, DEADBAND_RADIUS, MAX_MAGNITUDE):
    r = min(sqrt(x ** 2 + y ** 2), MAX_MAGNITUDE)
    theta = atan2(y, x)
    rAfterDeadzone = max(DEADBAND_RADIUS, r)
    rMappedToMotorSpeed = interp(rAfterDeadzone, [DEADBAND_RADIUS, MAX_MAGNITUDE], [MIN_SPEED, MAX_SPEED])
    magnitude = 0
    #print("Drive", r, theta, rAfterDeadzone, rMappedToMotorSpeed)

    if r < DEADBAND_RADIUS:
        #print("Stop")
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
    elif theta > 0 and theta <= pi / 2:
        # DOWN & RIGHT
        magnitude = interp(theta, [0, pi/2], [1, -1])
        rvr.raw_motors(
            left_mode=RawMotorModesEnum.forward.value if magnitude >= 0 else RawMotorModesEnum.reverse.value,
            left_speed=int(abs(magnitude * rMappedToMotorSpeed)),
            right_mode=RawMotorModesEnum.reverse.value,
            right_speed=int(rMappedToMotorSpeed),
        )
    elif theta > pi / 2:
        # DOWN & LEFT
        magnitude = interp(theta, [pi/2, pi], [-1, 1])
        rvr.raw_motors(
            left_mode=RawMotorModesEnum.reverse.value,
            left_speed=int(rMappedToMotorSpeed),
            right_mode=RawMotorModesEnum.forward.value if magnitude >= 0 else RawMotorModesEnum.reverse.value,
            right_speed=int(abs(magnitude * rMappedToMotorSpeed)),
        )


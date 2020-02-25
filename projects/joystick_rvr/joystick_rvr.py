import asyncio
from evdev import InputDevice, categorize, ecodes
from os import path
import sys
from mock import AsyncMock
from raw_drive import drive

sys.path.append(path.abspath(path.join(path.dirname(__file__), '../../')))
from sphero_sdk import SerialAsyncDal, SpheroRvrAsync, RawMotorModesEnum

JOYSTICK_MAX = 65535
JOYSTICK_CENTER = JOYSTICK_MAX / 2
DEADBAND_RADIUS = JOYSTICK_CENTER / 6
MAX_MAGNITUDE = JOYSTICK_CENTER

MAX_SPEED = 180
MIN_SPEED = 40

RVR_FRAME_PERIOD_SEC = 0.01

devicePath = '/dev/input/event0'
gamepad: InputDevice = None

loop = asyncio.get_event_loop()
try:
    rvr = SpheroRvrAsync(
        dal = SerialAsyncDal(
            loop
        )
    )
except asyncio.TimeoutError:
    print("Timed out waiting for SpheroRvrAsync. Using mock instead.")
    rvr = AsyncMock(SpheroRvrAsync)

x = 0 # -MAX_MAGNITUDE -> MAX_MAGNITUDE
y = 0

def resetJoystick():
    global x
    global y

    x = 0
    y = 0

def logJoystick():
    print(f'x: {x}, y: {y}')

async def waitForGamepad():
    global gamepad

    if gamepad:
        return

    if not path.exists(devicePath):
        print("Waiting for controller...")

    while not path.exists(devicePath):
        await asyncio.sleep(0.1)

    while True:
        try:
            gamepad = InputDevice(devicePath)
            print(gamepad)
            break
        except PermissionError:
            await asyncio.sleep(0.1)

def handleEvent(event):
    global x
    global y

    if event and event.type == ecodes.EV_ABS:
        #print("Got event")
        if event.code == ecodes.ABS_X:
            x = event.value - JOYSTICK_CENTER
        elif event.code == ecodes.ABS_Y:
            y = event.value - JOYSTICK_CENTER

async def handleRvr():
    await rvr.wake()
    await rvr.reset_yaw()

async def main():
    global gamepad

    while True:
        try:
            await waitForGamepad()

            while True:
            #for event in gamepad.read_loop():
                try:
                    for event in gamepad.read():
                        handleEvent(event)
                except BlockingIOError:
                    pass # No events available

                #logJoystick()
                await drive(x, y, rvr, MIN_SPEED, MAX_SPEED, DEADBAND_RADIUS, MAX_MAGNITUDE)
                await asyncio.sleep(RVR_FRAME_PERIOD_SEC)

        except OSError as e:
            resetJoystick()
            print(e)
            gamepad = None

if __name__ == '__main__':
    try:
        print("Starting main loop")
        loop.run_until_complete(
            main()
        )

    except KeyboardInterrupt:
        print("\nExiting")

        loop.run_until_complete(
            rvr.close()
        )

    finally:
        if loop.is_running():
            loop.close()


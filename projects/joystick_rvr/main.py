import asyncio
from os import path
import sys
from mock import AsyncMock
from raw_drive import drive
from gamepad import JOYSTICK_MAX, getJoystickValues

sys.path.append(path.abspath(path.join(path.dirname(__file__), '../../')))
from sphero_sdk import SerialAsyncDal, SpheroRvrAsync, RawMotorModesEnum

DEADBAND_RADIUS = JOYSTICK_MAX / 6

MAX_SPEED = 100
MIN_SPEED = 40

RVR_FRAME_PERIOD_SEC = 0.01

x = 0 # -JOYSTICK_MAX -> JOYSTICK_MAX
y = 0

loop = asyncio.get_event_loop()
try:
    rvr = SpheroRvrAsync(
        dal = SerialAsyncDal(
            loop
        )
    )
    print("Connected to RVR")
except asyncio.TimeoutError:
    print("Timed out waiting for SpheroRvrAsync. Using mock instead.")
    rvr = AsyncMock(SpheroRvrAsync)

def logJoystick():
    print(f'x: {x}, y: {y}')

async def handleJoystick():
    global x
    global y

    async for values in getJoystickValues():
        x, y = values
        #logJoystick()

async def handleRvr():
    global x
    global y

    await rvr.wake()
    await rvr.reset_yaw()

    while True:
        await drive(x, y, rvr, MIN_SPEED, MAX_SPEED, DEADBAND_RADIUS, JOYSTICK_MAX)
        await asyncio.sleep(RVR_FRAME_PERIOD_SEC)

async def main():
    await asyncio.gather(handleJoystick(), handleRvr())

if __name__ == '__main__':
    try:
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


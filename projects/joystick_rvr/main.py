import asyncio
from os import path
import sys
from mock import AsyncMock
from raw_drive import drive
from gamepad import JOYSTICK_MAX, Gamepad

sys.path.append(path.abspath(path.join(path.dirname(__file__), '../../')))
from sphero_sdk import SerialAsyncDal, SpheroRvrAsync, RawMotorModesEnum

DEADBAND_RADIUS = JOYSTICK_MAX / 6

MAX_SPEED = 100
MIN_SPEED = 40

RVR_FRAME_PERIOD_SEC = 0.01

gamepad = Gamepad('/dev/input/event0')

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

async def isRvrConnected():
    try:
        await rvr.wake()
        await rvr.get_board_revision(timeout = 0.1)
        return True
    except asyncio.TimeoutError:
        return False

async def waitForRvr(expectAlreadyConnected = False):
    waiting = not expectAlreadyConnected

    while True:
        if await isRvrConnected():
            if waiting:
                print("RVR connected")
            return
        else:
            if not waiting:
                waiting = True
                print("RVR disconnected")
            await asyncio.sleep(1)

async def handleRvr():
    await waitForRvr()
    await rvr.reset_yaw()

    while True:
        await drive(gamepad.x, gamepad.y, rvr, MIN_SPEED, MAX_SPEED, DEADBAND_RADIUS, JOYSTICK_MAX)
        await asyncio.sleep(RVR_FRAME_PERIOD_SEC)
        await waitForRvr(expectAlreadyConnected = True)

async def main():
    await asyncio.gather(gamepad.runLoop(), handleRvr())

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


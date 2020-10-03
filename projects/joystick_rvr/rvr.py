import asyncio
from gamepad import JOYSTICK_MAX, DEADBAND_RADIUS
from mock import AsyncMock
from os import path
from raw_drive import drive
# from fps_drive import fpsDrive
import sys

MAX_SPEED = 100
MIN_SPEED = 40

RVR_FRAME_PERIOD_SEC = 0.01

# PORT = '/dev/ttyS0'
PORT = '/dev/ttyGS0'

sys.path.append(path.abspath(path.join(path.dirname(__file__), '../../')))
from sphero_sdk import SerialAsyncDal, SpheroRvrAsync, RawMotorModesEnum

class Rvr:

    def __init__(self, loop):
        self.loop = loop

        try:
            self.rvr = SpheroRvrAsync(
                dal = SerialAsyncDal(
                    loop,
                    port_id = PORT,
                )
            )
        except asyncio.TimeoutError:
            print("Timed out waiting for SpheroRvrAsync. Using mock instead.")
            self.rvr = AsyncMock(SpheroRvrAsync)

    def close(self):
        self.loop.run_until_complete(
            self.rvr.close()
        )

    async def isRvrConnected(self):
        try:
            await self.rvr.wake()
            await self.rvr.get_board_revision(timeout = 0.1)
            return True
        except asyncio.TimeoutError:
            return False

    async def waitForRvr(self, expectAlreadyConnected = False):
        waiting = not expectAlreadyConnected

        while True:
            if await self.isRvrConnected():
                if waiting:
                    print("RVR connected")
                return
            else:
                if not waiting:
                    waiting = True
                    print("RVR disconnected")
                await asyncio.sleep(1)

    async def runLoop(self, gamepad):
        await self.waitForRvr()
        await self.rvr.reset_yaw()

        while True:
            await drive(gamepad.x, gamepad.y, self.rvr, MIN_SPEED, MAX_SPEED, DEADBAND_RADIUS, JOYSTICK_MAX)
            # await fpsDrive(gamepad.x, gamepad.y, gamepad.z, self.rvr, MIN_SPEED, MAX_SPEED, DEADBAND_RADIUS, JOYSTICK_MAX)
            await asyncio.sleep(RVR_FRAME_PERIOD_SEC)
            # TODO throttle next line and/or move to separate corountine since it causes troubles running at this high rate
            # await self.waitForRvr(expectAlreadyConnected = True)

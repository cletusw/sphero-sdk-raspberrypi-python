import asyncio
from mock import AsyncMock
from os import path
import sys

RVR_FRAME_PERIOD_SEC = 0.0025  # 400 Hz

sys.path.append(path.abspath(path.join(path.dirname(__file__), '../../')))
from sphero_sdk import SerialAsyncDal, SpheroRvrAsync, RawMotorModesEnum

class Rvr:

    def __init__(self, port, loop):
        try:
            self.rvr = SpheroRvrAsync(
                dal = SerialAsyncDal(
                    loop,
                    port_id = port,
                )
            )
        except asyncio.TimeoutError:
            print("Timed out waiting for SpheroRvrAsync. Using mock instead.")
            self.rvr = AsyncMock(SpheroRvrAsync)

    async def close(self):
        try:
            await asyncio.wait_for(self.rvr.close(), 1.0)
        except (asyncio.TimeoutError, OSError):
            pass

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

    async def runLoop(self, loopFn):
        await self.waitForRvr()
        await self.rvr.reset_yaw()

        while True:
            await loopFn()
            await asyncio.sleep(RVR_FRAME_PERIOD_SEC)
            # TODO throttle next line and/or move to separate corountine since it causes troubles running at this high rate
            # await self.waitForRvr(expectAlreadyConnected = True)

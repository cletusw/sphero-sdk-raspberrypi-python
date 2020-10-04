import asyncio
from gamepad import Gamepad, DEADBAND_RADIUS, JOYSTICK_MAX
from drive import drive
from rvr import Rvr

# RVR_PORT = '/dev/ttyS0'
RVR_PORT = '/dev/ttyGS0'
GAMEPAD_PATH = '/dev/input/event0'
MAX_SPEED = 100
MIN_SPEED = 10

loop = asyncio.get_event_loop()
rvr = Rvr(RVR_PORT, loop)
gamepad = Gamepad(GAMEPAD_PATH)

async def main():
    await asyncio.gather(
        gamepad.runLoop(),
        rvr.runLoop(loopFn),
    )

async def loopFn():
    await drive(gamepad.x, gamepad.y, gamepad.z, gamepad.rz, rvr.rvr, MIN_SPEED, MAX_SPEED, DEADBAND_RADIUS, JOYSTICK_MAX)

async def cleanup():
    print("\nCleaning up...")
    await rvr.close()
    print("\nDone")

if __name__ == '__main__':
    try:
        loop.run_until_complete(
            main()
        )

    except KeyboardInterrupt:
        asyncio.get_event_loop().run_until_complete(
            cleanup()
        )

    finally:
        if loop.is_running():
            loop.close()


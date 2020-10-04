import asyncio
# from fps_drive import fpsDrive
from gamepad import Gamepad, DEADBAND_RADIUS, JOYSTICK_MAX
from pan_tilt import PanTilt
from raw_drive import drive
from rvr import Rvr

# PORT = '/dev/ttyS0'
PORT = '/dev/ttyGS0'
MAX_SPEED = 100
MIN_SPEED = 40

loop = asyncio.get_event_loop()
rvr = Rvr(PORT, loop)
gamepad = Gamepad('/dev/input/event0')
panTilt = PanTilt()

async def main():
    await asyncio.gather(
        gamepad.runLoop(),
        rvr.runLoop(loopFn),
        panTilt.runLoop(gamepad)
    )

async def loopFn():
    await drive(gamepad.x, gamepad.y, rvr.rvr, MIN_SPEED, MAX_SPEED, DEADBAND_RADIUS, JOYSTICK_MAX)
    # await fpsDrive(gamepad.x, gamepad.y, gamepad.z, rvr.rvr, MIN_SPEED, MAX_SPEED, DEADBAND_RADIUS, JOYSTICK_MAX)

async def cleanup():
    print("\nCleaning up...")
    panTilt.cleanup()
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


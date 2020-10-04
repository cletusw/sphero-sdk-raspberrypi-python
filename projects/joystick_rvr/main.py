import asyncio
from gamepad import Gamepad
from pan_tilt import PanTilt
from rvr import Rvr

loop = asyncio.get_event_loop()
rvr = Rvr(loop)
gamepad = Gamepad('/dev/input/event0')
panTilt = PanTilt()

async def main():
    await asyncio.gather(
        gamepad.runLoop(),
        rvr.runLoop(gamepad),
        panTilt.runLoop(gamepad, fps = True)
    )

async def cleanup():
    print("\nCleaning up...")
    panTilt.cleanup()
    try:
        await asyncio.wait_for(rvr.close(), 1.0)
    except (asyncio.TimeoutError, OSError):
        pass
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


import asyncio
from gamepad import Gamepad
from pan_tilt import PanTilt
from rvr import Rvr

loop = asyncio.get_event_loop()
rvr = Rvr(loop)
gamepad = Gamepad('/dev/input/event0')
panTilt = PanTilt()

async def main():
    await asyncio.gather(gamepad.runLoop(),
        rvr.runLoop(gamepad),
        panTilt.runLoop(gamepad)
    )

if __name__ == '__main__':
    try:
        loop.run_until_complete(
            main()
        )

    except KeyboardInterrupt:
        print("\nExiting")
        rvr.close()

    finally:
        if loop.is_running():
            loop.close()


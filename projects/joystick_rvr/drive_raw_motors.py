import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

import asyncio
from sphero_sdk import SpheroRvrAsync
from sphero_sdk import SerialAsyncDal
from sphero_sdk import RawMotorModesEnum


loop = asyncio.get_event_loop()

rvr = SpheroRvrAsync(
    dal=SerialAsyncDal(
        loop
    )
)


async def main():
    """ This program has RVR drive around in different directions.
    """

    await rvr.wake()

    # Give RVR time to wake up
    await asyncio.sleep(2)

    await rvr.reset_yaw()

    await rvr.raw_motors(
        left_mode=RawMotorModesEnum.forward.value,
        left_speed=128,  # Valid speed values are 0-255
        right_mode=RawMotorModesEnum.forward.value,
        right_speed=128  # Valid speed values are 0-255
    )

    # Delay to allow RVR to drive
    await asyncio.sleep(1)

    await rvr.raw_motors(
        left_mode=RawMotorModesEnum.reverse.value,
        left_speed=64,  # Valid speed values are 0-255
        right_mode=RawMotorModesEnum.reverse.value,
        right_speed=64  # Valid speed values are 0-255
    )

    # Delay to allow RVR to drive
    await asyncio.sleep(1)

    await rvr.raw_motors(
        left_mode=RawMotorModesEnum.reverse.value,
        left_speed=128,  # Valid speed values are 0-255
        right_mode=RawMotorModesEnum.forward.value,
        right_speed=128  # Valid speed values are 0-255
    )

    # Delay to allow RVR to drive
    await asyncio.sleep(1)

    await rvr.raw_motors(
        left_mode=RawMotorModesEnum.forward.value,
        left_speed=128,  # Valid speed values are 0-255
        right_mode=RawMotorModesEnum.forward.value,
        right_speed=128  # Valid speed values are 0-255
    )

    # Delay to allow RVR to drive
    await asyncio.sleep(1)

    await rvr.raw_motors(
        left_mode=RawMotorModesEnum.off.value,
        left_speed=0,  # Valid speed values are 0-255
        right_mode=RawMotorModesEnum.off.value,
        right_speed=0  # Valid speed values are 0-255
    )

    # Delay to allow RVR to drive
    await asyncio.sleep(1)

    await rvr.close()


if __name__ == '__main__':
    try:
        loop.run_until_complete(
            main()
        )

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

        loop.run_until_complete(
            rvr.close()
        )

    finally:
        if loop.is_running():
            loop.close()

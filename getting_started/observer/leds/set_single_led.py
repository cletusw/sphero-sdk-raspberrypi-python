import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sphero_sdk import SpheroRvrObserver, SerialObserverDal
from sphero_sdk import Colors
from sphero_sdk import RvrLedGroups

port = '/dev/ttyGS0'

rvr = SpheroRvrObserver()

rvr._dal = SerialObserverDal(
    port_id = port
)

def main():
    """ This program demonstrates how to set a single LED.
    """

    try:
        rvr.wake()

        # Give RVR time to wake up
        time.sleep(2)

        rvr.set_all_leds(
            led_group=RvrLedGroups.all_lights.value,
            led_brightness_values=[color for _ in range(10) for color in Colors.off.value]
        )

        # Delay to show LEDs change
        time.sleep(1)

        rvr.set_all_leds(
            led_group=RvrLedGroups.headlight_right.value,   # 0xe00
            led_brightness_values=[255, 0, 0]
        )

        # Delay to show LEDs change
        time.sleep(1)

        rvr.set_all_leds(
            led_group=RvrLedGroups.headlight_left.value,      # 0x1c0
            led_brightness_values=[0, 255, 0]
        )

        # Delay to show LEDs change
        time.sleep(1)

        print('Done')

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

    finally:
        rvr.close()


if __name__ == '__main__':
    main()

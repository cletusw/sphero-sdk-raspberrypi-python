import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sphero_sdk import SpheroRvrObserver, SerialObserverDal
from sphero_sdk import Colors
from sphero_sdk import RvrLedGroups

port = '/dev/ttyS0'

rvr = SpheroRvrObserver()

rvr._dal = SerialObserverDal(
    port_id = port
)

def main():
    """ This program demonstrates how to sleep
    """

    try:
        rvr.wake()

        # Give RVR time to wake up
        time.sleep(2)

        print('Going to sleep...')

        rvr.sleep()

        time.sleep(1)

        print('Asleep')

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

    finally:
        rvr.close()


if __name__ == '__main__':
    main()

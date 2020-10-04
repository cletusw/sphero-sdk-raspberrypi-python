import asyncio
from gamepad import JOYSTICK_MAX, DEADBAND_RADIUS
from numpy import interp
import piconzero as pz

PERIOD_IN_SECONDS = 0.01

pz.init() # TODO: Ensure only happens once?

# Define which pin sets for each servo
PAN = 0
TILT = 1

PAN_CENTER = 90
PAN_HALF_WIDTH = 90
TILT_CENTER = 45
TILT_HALF_WIDTH = 45

class PanTilt:
    def __init__(self):
        # Set output mode to Servo
        pz.setOutputConfig(PAN, 2)
        pz.setOutputConfig(TILT, 2)

        # Center all servos
        pz.setOutput(PAN, PAN_CENTER)
        pz.setOutput(TILT, TILT_CENTER)

        print("Pan/Tilt ready")

    async def runLoop(self, gamepad, fps = False):
        while True:
            # TODO: exponential smoothing
            panValue = int(interp(
                gamepad.x,
                [-JOYSTICK_MAX, JOYSTICK_MAX],
                [PAN_CENTER - PAN_HALF_WIDTH, PAN_CENTER + PAN_HALF_WIDTH]))
            tiltValue = max(
                30,
                int(interp(
                    -gamepad.rz,
                    [-JOYSTICK_MAX, JOYSTICK_MAX],
                    [TILT_CENTER - TILT_HALF_WIDTH, TILT_CENTER + TILT_HALF_WIDTH])))
            pz.setOutput(PAN, panValue)
            pz.setOutput(TILT, tiltValue)
            await asyncio.sleep(PERIOD_IN_SECONDS)

    def cleanup(self):
        pz.cleanup()

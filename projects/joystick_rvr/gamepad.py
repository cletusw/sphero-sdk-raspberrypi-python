import asyncio
from evdev import InputDevice, categorize, ecodes
from os import path

EVDEV_MAX = 65535
EVDEV_CENTER = EVDEV_MAX / 2
JOYSTICK_MAX = EVDEV_CENTER

devicePath = '/dev/input/event0'
gamepad: InputDevice = None

x = 0 # -JOYSTICK_MAX -> JOYSTICK_MAX
y = 0

def resetGamepad():
    global gamepad
    global x
    global y

    gamepad = None
    x = 0
    y = 0

def logJoystick():
    print(f'x: {x}, y: {y}')

async def waitForGamepad():
    global gamepad

    if gamepad:
        return

    if not path.exists(devicePath):
        print("Waiting for controller...")

    while not path.exists(devicePath):
        await asyncio.sleep(0.1)

    while True:
        try:
            gamepad = InputDevice(devicePath)
            print(gamepad)
            break
        except PermissionError:
            await asyncio.sleep(0.1)

def handleEvent(event):
    global x
    global y

    if event and event.type == ecodes.EV_ABS:
        #print("Got event")
        if event.code == ecodes.ABS_X:
            x = event.value - EVDEV_CENTER
        elif event.code == ecodes.ABS_Y:
            y = event.value - EVDEV_CENTER

async def getJoystickValues():
    while True:
        try:
            await waitForGamepad()

            async for event in gamepad.async_read_loop():
                handleEvent(event)
                #logJoystick()
                yield (x, y)

        except OSError as e:
            print('Lost controller', e)
            resetGamepad()
            yield (x, y)



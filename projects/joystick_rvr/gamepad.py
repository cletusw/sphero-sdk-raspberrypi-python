import asyncio
from evdev import InputDevice, categorize, ecodes
from os import path

EVDEV_MAX = 65535
EVDEV_CENTER = EVDEV_MAX / 2
JOYSTICK_MAX = EVDEV_CENTER

class Gamepad:

    def __init__(self, devicePath):
        self.devicePath = devicePath
        self.reset()

    def reset(self):
        self.gamepad: InputDevice = None
        self.x = 0 # -JOYSTICK_MAX -> JOYSTICK_MAX
        self.y = 0

    def log(self):
        print(f'x: {self.x}, y: {self.y}')

    async def waitForGamepad(self):
        if self.gamepad:
            return

        if not path.exists(self.devicePath):
            print("Waiting for gamepad...")

        while not path.exists(self.devicePath):
            await asyncio.sleep(0.1)

        while True:
            try:
                self.gamepad = InputDevice(self.devicePath)
                print("Gamepad connected: ", self.gamepad)
                break
            except PermissionError:
                await asyncio.sleep(0.1)

    def handleEvent(self, event):
        if event and event.type == ecodes.EV_ABS:
            #print("Got event")
            if event.code == ecodes.ABS_X:
                self.x = event.value - EVDEV_CENTER
            elif event.code == ecodes.ABS_Y:
                self.y = event.value - EVDEV_CENTER

    async def runLoop(self):
        while True:
            try:
                await self.waitForGamepad()

                async for event in self.gamepad.async_read_loop():
                    self.handleEvent(event)
                    #self.log()

            except OSError as e:
                print('Gamepad disconnected:', e)
                self.reset()


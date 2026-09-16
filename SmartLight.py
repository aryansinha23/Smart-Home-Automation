class SmartLight:
    def __init__(self, roomLocation, isOn=False, brightness=0):
        self.roomLocation = roomLocation
        self.isOn = isOn
        self.brightness = brightness

    def togglePower(self):
        self.isOn = not self.isOn
        if not self.isOn:
            self.brightness = 0
        print(f"{self.roomLocation}: Power toggled {'ON' if self.isOn else 'OFF'}.")

    def setBrightness(self, level):
        if not self.isOn:
            print(f"{self.roomLocation}: Cannot set brightness - light is OFF.")
            return
        if 0 <= level <= 100:
            self.brightness = level
            print(f"{self.roomLocation}: Brightness set to {self.brightness}%.")
        else:
            print(f"{self.roomLocation}: Invalid brightness level. Use 0-100.")

    def getStatus(self):
        state = "ON" if self.isOn else "OFF"
        print(f"{self.roomLocation}: Power={state}, Brightness={self.brightness}%.")


def main():
    livingRoom = SmartLight("Living Room")
    kitchen = SmartLight("Kitchen")
    study = SmartLight("Study")

    livingRoom.togglePower()
    livingRoom.setBrightness(75)

    study.togglePower()
    study.setBrightness(30)

    kitchen.setBrightness(50)      # Fails because Kitchen is OFF
    livingRoom.setBrightness(150)  # Fails because 150 is outside 0-100

    study.togglePower()            # OFF; brightness becomes 0

    print("\nFinal Status:")
    livingRoom.getStatus()
    kitchen.getStatus()
    study.getStatus()


if __name__ == "__main__":
    main()

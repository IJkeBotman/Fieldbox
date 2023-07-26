import digitalio
import board
import busio
from adafruit_epd.ssd1680 import Adafruit_SSD1680
from adafruit_epd.ssd1675 import Adafruit_SSD1675

# Define the CS, DC, RST, and Busy pins
CS_PIN = board.CE0
DC_PIN = board.D25
RST_PIN = board.D24
BUSY_PIN = board.D23

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

ecs = digitalio.DigitalInOut(CS_PIN)
dc = digitalio.DigitalInOut(DC_PIN)
rst = digitalio.DigitalInOut(RST_PIN)
busy = digitalio.DigitalInOut(BUSY_PIN)

# Attempt to initialize the SSD1675 display
try:
    display = Adafruit_SSD1675(122, 250, spi, cs_pin=ecs, dc_pin=dc, sramcs_pin=None,
                               rst_pin=rst, busy_pin=busy)
    using_display = "SSD1675"
except:
    # If SSD1675 initialization fails, try SSD1680
    try:
        display = Adafruit_SSD1680(122, 250, spi, cs_pin=ecs, dc_pin=dc, sramcs_pin=None,
                                   rst_pin=rst, busy_pin=busy)
        using_display = "SSD1680"
    except:
        print("No supported eInk display found!")
        using_display = None

if using_display:
    # Clear the display and display "Hello World"
    display.fill(Adafruit_SSD1680.WHITE)
    display.text("Hello World", 10, 45, Adafruit_SSD1680.BLACK)
    display.display()
    print(f"Message displayed using {using_display} display!")

else:
    print("Unable to show the message. No supported eInk display detected!")

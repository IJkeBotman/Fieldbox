import digitalio
from board import SCK, MOSI, MISO, D10, D9
from PIL import Image, ImageDraw, ImageFont
import Adafruit_SSD1675

# Set up the eInk display
displayio.release_displays()

cs_pin = digitalio.DigitalInOut(D10)
dc_pin = digitalio.DigitalInOut(D9)
reset_pin = digitalio.DigitalInOut(D9)
busy_pin = digitalio.DigitalInOut(D9)
spi = busio.SPI(clock=SCK, MOSI=MOSI, MISO=MISO)

display = Adafruit_SSD1675.SSD1675(
    250, 122, spi, cs_pin, dc_pin, reset_pin, busy_pin,
    rotation=90
)

# Clear the display
display.fill(Adafruit_SSD1675.WHITE)
display.pixel(5, 5, Adafruit_SSD1675.BLACK)

# Create an image buffer
image = Image.new("1", (display.width, display.height))
draw = ImageDraw.Draw(image)

# Load a font
font = ImageFont.load_default()

# Draw text on the image buffer
draw.text((10, 45), "Hello World", font=font, fill=255)

# Display the image on the eInk screen
display.image(image)
display.display()


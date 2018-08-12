from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

t = 2

# Define some colours
g = (0, 255, 0) # Green
b = (0, 0, 255) #Blue
r = (255, 0, 0) #Red
bk = (0, 0, 0) # Black
y = (255, 255, 0) #Yellow
pu = (255, 0, 255) #purple
w = (255, 255, 255) #white
cy = (0, 255, 255) #cyan

sense.clear(pu)
sleep(t)
sense.clear




# Set up where each colour will display
creeper_pixels = [
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, b, b, g, g, b, b, g,
    g, b, b, g, g, b, b, g,
    g, g, g, b, b, g, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, g, g, b, g, g
]

happy_pixels = [
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, b, b, g, g, b, b, g,
    g, b, b, g, g, b, b, g,
    g, g, g, b, b, g, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, g, g, b, g, g
]

# Display these colours on the LED matrix
sense.set_pixels(creeper_pixels)
sleep(2)
sense.clear()
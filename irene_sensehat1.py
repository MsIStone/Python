from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
#acc = sense.get_accelerometer()

blue = (0, 0, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)

x = 0
t = 0.2

#sense.show_message("Hello Irene", text_colour = yellow, back_colour = blue)
#sense.clear()
#sense.set_pixel(0,2,blue)  #changing one pixel, 0th column, 2nd row, blue
#sense.set_pixel(0,3,red)   #changing one pixel, 0th column, 3rd row, red
#sleep(2)
#sense.clear()
#sleep(2)

while x < 10:
    print (x)
    sense.clear(255,255,255)   #white
    sleep(t)
    sense.clear(255,0,0)       #red
    sleep(t)
    sense.clear(0,255,0)       #green
    sleep(t)
    sense.clear(0,0,255)       #blue
    sleep(t)
    sense.clear(255,255,0)     #yellow
    sleep(t)
    sense.clear(0,255,255)     #
    sleep(t)
    sense.clear()
    x = x+1
    
    


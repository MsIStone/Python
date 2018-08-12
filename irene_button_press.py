from gpiozero import LED, Button
from time import sleep
from signal import pause

button = Button(18)
led = LED(17)

#button.wait_for_press()
#print('You pushed me')
#led.on()
#sleep(3)
#led.off()

#while True:
#    button.wait_for_press()
#    led.toggle()
#    sleep(0.5)

button_when_pressed = led.on()
button_when_released = led.off()

pause()

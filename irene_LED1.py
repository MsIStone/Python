from gpiozero import LED
from time import sleep

x = 0

led = LED(4)

led.on()
sleep(1)
led.off()

#while True:
#    led.on()
#    sleep(0.2)
#    led.off()
#    sleep(0.2)
    
while x < 10:
    led.on()
    sleep(0.2)
    led.off()
    sleep(0.2)
    x = x + 1
    




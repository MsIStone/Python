from gpiozero import LED, Button, TrafficLights, Buzzer
from time import sleep

button = Button(17)
#led = LED(6)
lights = TrafficLights(25, 5, 6)
buzzer = Buzzer(13)

while True:
#    led.blink(0.1,0.2)  #on 0.1s and off 0.2s
#    button.wait_for_press()
#    print("Pressed")
#    led.off()
#    button.wait_for_release()
#    print("Released")
#    led.off()

#    lights.on()
#    lights.blink()
#    buzzer.beep()
#    buzzer.off()
#    button.wait_for_press()
#    lights.blink()
#    buzzer.blink()
#    button.wait_for_release()
#    lights.off()
#    buzzer.off()

#    button.wait_for_press()
    lights.green.on()
    sleep(1)
    lights.green.off()
    lights.amber.on()
    sleep(1)
    lights.red.on()
    lights.amber.off()
    sleep(1)
    lights.off()
    buzzer.blink()
    sleep(3)
    buzzer.off()
    sleep(3)
    buzzer.on()
    sleep(2)
    buzzer.off()
#    sleep(1)

    button.wait_for_press()
    sleep(1)
    lights.off()
    lights.amber.on()
    sleep(2)
    lights.red.on()
#    buzzer.blink()
    lights.amber.off()
    sleep(3)
    lights.amber.on()
    buzzer.off()
    





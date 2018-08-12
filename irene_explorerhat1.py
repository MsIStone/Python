
from time import sleep
import explorerhat

explorerhat.light.red.on()
sleep(3)
explorerhat.light.blue.on()
sleep(3)
explorerhat.light.green.on()
sleep(3)
explorerhat.light.red.off()
explorerhat.light.blue.off()
explorerhat.light.green.off()

#explorerhat.light.green.blink(1,0.2)
#explorerhat.light.yellow.pulse(0.5,2,0.1,1)
sleep(10)
#explorerhat.lightoff()

explorerhat.output.one.on()
sleep(3)

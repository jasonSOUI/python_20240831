from machine import Pin
import time

# 使用 "LED" 標識符
led = Pin("LED", Pin.OUT)

# 閃爍 LED
i = 1
while True:
    led.on()   # 或 led.value(1)
    time.sleep(0.5)
    led.off()  # 或 led.value(0)
    time.sleep(0.5)
    i = i + 1
    print(i)
    if i > 10:
        break

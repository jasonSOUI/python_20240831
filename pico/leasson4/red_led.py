from machine import Pin
import time

# 使用 "LED" 標識符
led = Pin(15, Pin.OUT)

# 閃爍 LED
i = 0
while True:
    led.on()   # 或 led.value(1)
    time.sleep(1)
    led.off()  # 或 led.value(0)
    time.sleep(1)
    i = i + 1
    print(i)
    if i > 100:
        break


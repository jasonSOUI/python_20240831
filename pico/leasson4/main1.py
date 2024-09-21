from machine import Pin
import time

# 设置 GPIO 引脚为输入并启用上拉电阻
button = Pin(15, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 0:  # 当按钮被按下时，输入为低电平
        print("Button Pressed")
    else:
        print("Button Released")
    time.sleep(1)  # 稍作延迟，避免持续打印


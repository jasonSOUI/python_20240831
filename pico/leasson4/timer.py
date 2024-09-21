from machine import Timer
from machine import Pin

count = 0
led = Pin("LED", Pin.OUT)

# LED閃爍
def toggle_led(t:Timer):
    global count
    count = count + 1
    led.toggle()
    print(f"toggle_led目前被執行:{count}次")
    if count >= 10:
        t.deinit()
        print("結束執行")
    

# 定時器
led_timer = Timer(period=1000, mode=Timer.PERIODIC, callback=toggle_led)



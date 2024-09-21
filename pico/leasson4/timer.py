from machine import Timer, Pin


# LED閃爍
green_count = 0
green_led = Pin("LED", Pin.OUT)
def toggle_green_led(t:Timer):
    global green_count
    green_count = green_count + 1
    green_led.toggle()
    print(f"toggle_green_led目前被執行:{green_count}次")
    if green_count >= 10:
        t.deinit()
        print("toggle_green_led目前被執行結束執行")
        

# LED閃爍
red_count = 0
red_led = Pin(15, Pin.OUT)
def toggle_red_led(t:Timer):
    global red_count
    red_count = red_count + 1
    red_led.toggle()
    print(f"toggle_red_led目前被執行:{red_count}次")
    if red_count >= 10:
        t.deinit()
        print("toggle_red_led目前被執行結束執行")
    

# 定時器
led_green_timer = Timer(period=1000, mode=Timer.PERIODIC, callback=toggle_green_led)
led_red_timer = Timer(period=2000, mode=Timer.PERIODIC, callback=toggle_red_led)



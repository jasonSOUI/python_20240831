from machine import Pin
from machine import Timer
import time

led = Pin(15,Pin.OUT)
sr501 = Pin(14,Pin.IN)

sensors:list[int] = [] #收集5秒資訊
def check_people(t:Timer):
    global sensors
    sensor_state = sr501.value()
    print(sensor_state)
    length:int = len(sensors)
    if length >= 5: #大於=於5筆       
        if sum(sensors) > 0: #大於1,代表有人
            led.value(1)
            print(f"總合大於1 : {length}")
        else:
            led.value(0)
            print("None")
        
        sensors = [] #清空重新計算
    else:        
        sensors.append(sensor_state)
    

time1 = Timer() 
time1.init(period=1000, mode=Timer.PERIODIC, callback=check_people)
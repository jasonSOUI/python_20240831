from machine import Timer,ADC,Pin
import time

adc = ADC(4)
adc2 = ADC(Pin(26))
reference_voltage = 3.3   # ADC 參考電壓
temp_sensor_slope = 0.01  # 溫度感測器的斜率
temp_sensor_offset = 0.7  # 溫度感測器在 25°C 時的電壓

def print_temperature(t):
     # 讀取 ADC 值並轉換為電壓
    reading = adc.read_u16()
    voltage = reading * (reference_voltage / (2**16 - 1))

    # 根據溫度感測器特性計算溫度
    temperature = (voltage - temp_sensor_offset) / temp_sensor_slope + 25

    print(f"溫度: {temperature:.2f} °C")

def print_PWM(t):
    duty = adc2.read_u16()
    print(f"可變電阻: {round(duty/65535*10)}")


# 定時兩秒    
t1 = Timer(period=2000, mode=Timer.PERIODIC, callback=print_temperature)
t2 = Timer(period=500, mode=Timer.PERIODIC, callback=print_PWM)

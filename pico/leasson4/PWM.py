from machine import Pin, PWM, ADC, Timer
import time

pwm = PWM(Pin(15))
adc = ADC(Pin(26))
adc_light = ADC(Pin(28))
adc4 = ADC(4) # 內建溫度
conversion_factor = 3.3 / (65535)
pwm.freq(1000)

def change_pwd(t):
    duty = adc.read_u16()
    pwm.duty_u16(duty)
    print(f"可變電阻: {duty}, {round(duty/65535*10)}")
    reading = adc4.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print(f"溫度: {temperature}")
    adc_light_value = adc_light.read_u16()
    print(f"光線: {adc_light_value}")
    print("--------------------------------------")

t1 = Timer(period=2000, mode=Timer.PERIODIC, callback=change_pwd)
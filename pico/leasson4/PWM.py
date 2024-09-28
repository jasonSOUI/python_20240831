from machine import Pin, PWM, ADC, Timer
import time


pwm = PWM(Pin(15))
adc = ADC(Pin(26))

pwm.freq(1000)

def change_pwd(t):
	duty = adc.read_u16()
	pwm.duty_u16(duty)
	print(f"可變電阻: {duty}, {round(duty/65535*10)}")
	
t1 = Timer(period=500, mode=Timer.PERIODIC, callback=change_pwd)

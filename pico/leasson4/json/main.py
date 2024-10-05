import tools
from machine import Timer,ADC,Pin,PWM,RTC

light_value = 0
temperature = 0

def set_light_value(t):
    global light_value
    global temperature
    light_value = adc_light.read_u16() # 光敏感測
    conversion_factor = 3.3 / (65535)  # 電壓轉換率  
    temperature = 27 - (adc.read_u16() * conversion_factor - 0.706)/0.001721 # 溫度
    print(f'光敏感測:{light_value}, 溫度:{temperature}')


def send_json(t):
    sensor_data = tools.create_sensor_data(temperature, light_value)
    json_string = tools.create_json_payload(sensor_data)
    print(f'json_string : {json_string}')

def main():
    t1 = Timer(period=2000, mode=Timer.PERIODIC, callback=set_light_value)
    t1 = Timer(period=3000, mode=Timer.PERIODIC, callback=send_json)

if __name__ == '__main__':
    try:
        tools.connect()
    except RuntimeError as e:
        print(f"{e}")
    else:
        #sensor setup
        adc = ADC(4) #內建溫度感測器
        adc_light = ADC(Pin(28)) #光線感測器
        pwm = PWM(Pin(15),freq=50) #LED
        main()
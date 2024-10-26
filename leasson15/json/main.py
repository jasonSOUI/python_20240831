#! usr/bin/micropython

'''
led->gpio15
光敏電阻 -> gpio28
可變電阻 -> gpio26
內建溫度sensor -> adc最後1pin,共5pin
'''

from machine import Timer,ADC,Pin,PWM,RTC
import binascii
from umqtt.simple import MQTTClient
import tools, config
import ujson

def get_temperature():
    conversion_factor = 3.3 / (65535)
    reading = adc.read_u16() * conversion_factor
    temperature = round(27 - (reading - 0.706)/0.001721,2)
    return round(27 - (reading - 0.706)/0.001721,2)

def get_line_status():
    adc_value = adc_light.read_u16()
    return 0 if adc_value < 5000 else 1
    
def get_light_level():
    duty = adc1.read_u16()
    pwm.duty_u16(duty)
    return round(duty/65535*10)

def get_current_time():
    rtc = RTC()
    year, month, day, hour, minute, second, _, _ = rtc.datetime()
    return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"

def sendJson(t):
    global temperature
    global line_status
    global light_level
    global jsonData
    temperature = get_temperature()
    line_status = get_line_status()
    light_level = get_light_level()
    jsonData = pre_json_data(temperature, line_status, light_level)
    print(f'temperature:{temperature}, line_status:{line_status}, light_level:{light_level}')
    tools.send_json(jsonData, url)

def pre_json_data(temperature, line_status, light_level, device_id="pico01"):
    payload = {
        "device_id": device_id,
        "timestamp": get_current_time(),
        "temperature": f'{temperature}',
        "line_status": f'{line_status}',
        "light_level": f'{light_level}'
    }
    return ujson.dumps(payload)

def main():
    pass

if __name__ == '__main__':
    adc = ADC(4) #內建溫度
    adc1 = ADC(Pin(26)) #可變電阻
    adc_light = ADC(Pin(28)) #光敏電阻
    pwm = PWM(Pin(15),freq=50) #pwm led
    url = 'http://114.35.52.183:8080/prico/receiveJsonNode'
    temperature = None
    line_status = None
    light_level = None
    jsonData = None
    
    try:
        tools.connect()
    except RuntimeError as e:
        print(e)
    except Exception:
        print('不知明的錯誤')
    else:
        t3 = Timer(period=5000, mode=Timer.PERIODIC, callback=sendJson)
        
    main()

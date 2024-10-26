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


def do_thing(t):
    '''
    :param t:Timer的實體
    負責偵測溫度和光線
    每2秒執行1次
    '''
    conversion_factor = 3.3 / (65535)
    reading = adc.read_u16() * conversion_factor
    temperature = round(27 - (reading - 0.706)/0.001721,2) 
    print(f'溫度:{temperature}')
    #mqtt.publish('SA-01/TEMPERATURE', f'{temperature}')
    blynk_mqtt.publish('ds/temperature', f'{temperature}')
    adc_value = adc_light.read_u16()
    print(f'光線:{adc_value}')
    line_state = 0 if adc_value < 5000 else 1
    print(f'光線:{line_state}')
    blynk_mqtt.publish('ds/line_status', f'{line_state}')
    #mqtt.publish('SA-01/LINE_LEVEL', f'{line_state}')
    
def do_thing1(t):
    '''
    :param t:Timer的實體
    負責可變電阻和改變led的亮度
    '''    
    
    duty = adc1.read_u16()
    pwm.duty_u16(duty)
    light_level = round(duty/65535*10)
    print(f'可變電阻:{light_level}')
    #mqtt.publish('SA-01/LED_LEVEL', )
    blynk_mqtt.publish('ds/led_level', f'{light_level}')

def sendJson(t):
    duty = adc1.read_u16()
    pwm.duty_u16(duty)
    light_level = round(duty/65535*10)
    jsonData = tools.create_json_payload(f'{light_level}')
    print(f'sendJson:{jsonData}')
    tools.send_json(jsonData, 'http://114.35.52.183:8080/prico/receiveJson')
    

def main():
    global blynk_mqtt
    blynk_mqtt = MQTTClient(config.BLYNK_TEMPLATE_ID, config.BLYNK_MQTT_BROKER,user='device',password=config.BLYNK_AUTH_TOKEN)
    blynk_mqtt.connect()
    print(f'blynk_connect success!!!!!')

if __name__ == '__main__':
    adc = ADC(4) #內建溫度
    adc1 = ADC(Pin(26)) #可變電阻
    adc_light = ADC(Pin(28)) #光敏電阻
    pwm = PWM(Pin(15),freq=50) #pwm led
    #連線internet
    try:
        tools.connect()
    except RuntimeError as e:
        print(e)
    except Exception:
        print('不知明的錯誤')
    else:
        #MQTT
        SERVER = "192.168.0.252"
        CLIENT_ID = binascii.hexlify(machine.unique_id())
        mqtt = MQTTClient(CLIENT_ID, SERVER,user='pi',password='raspberry')
        mqtt.connect()
        #t1 = Timer(period=1000, mode=Timer.PERIODIC, callback=do_thing)
        #t2 = Timer(period=1000, mode=Timer.PERIODIC, callback=do_thing1)
        t3 = Timer(period=1000, mode=Timer.PERIODIC, callback=sendJson)
    
    blynk_mqtt = None # 這邊宣告的參數會變成全域變數
    main()
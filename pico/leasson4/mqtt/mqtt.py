import time
import binascii
from umqtt.simple import MQTTClient
import random
from machine import Timer,ADC,Pin,PWM,RTC
import tools

light_value = 0
last_light_value = 0
temperature = 0

def set_light_value():
    global light_value
    global last_light_value
    global temperature
    light_value = adc_light.read_u16() # 光敏感測
    conversion_factor = 3.3 / (65535)  # 電壓轉換率  
    temperature = 27 - (adc.read_u16() * conversion_factor - 0.706)/0.001721 # 溫度
    print(f'光敏感測:{light_value}, 溫度:{temperature}')


def main():
    try:
        tools.connect()
        mqtt = MQTTClient(CLIENT_ID, SERVER,user='pi',password='raspberry')
        mqtt.connect()  
        
        while True:
            
            # 設定溫度與光敏值
            set_light_value()
            
            # 與上一次的差異
            result = abs(light_value - last_light_value)
            
            if(result > 1000):
                mqtt.publish(TOPIC, f'{light_value}')
                print("發佈:", light_value)
            
            time.sleep_ms(2000)
    except Exception as e:
        print(e)
        mqtt.disconnect()
    
if __name__ == '__main__':
    
    # Default MQTT server to connect to
    SERVER = "192.168.0.252"
    CLIENT_ID = binascii.hexlify(machine.unique_id())
    TOPIC = b"SA-42/雞舍/光敏值"
    
    #sensor setup
    adc = ADC(4) #內建溫度感測器
    adc_light = ADC(Pin(28)) #光線感測器
    pwm = PWM(Pin(15),freq=50) #LED
        
    main()
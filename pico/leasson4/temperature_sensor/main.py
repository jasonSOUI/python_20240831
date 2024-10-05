#! usr/bin/micropython
'''
LED -> gpio15
光敏電阻 ->  gpio28
可變電阻 -> gpio26
內建溫度 -> adc最後一個ping，共五個
'''

from machine import Timer,ADC,Pin,PWM,RTC
import tools

light_value = 0
temperature = 0

def do_thing(t):
    '''
    :param t:Timer的實體
    處理溫度和光線
    '''
    global light_value
    global temperature
    conversion_factor = 3.3 / (65535) #電壓轉換率  
    reading = adc.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    #print(f'溫度:{temperature}')
    light_value = adc_light.read_u16()
    #print(f'光線:{light_value}')
    
def do_thing1(t):
    '''
    :param t:Timer的實體
    處理可變電阻
    '''
    
    adc1 = ADC(Pin(26))
    duty = adc1.read_u16()
    pwm.duty_u16(duty)    
    #print(f'可變電阻:{round(duty/65535*10)}')
    
def send_data(t):
    print(f'溫度:{temperature},光線:{light_value}')
    sensor_data = tools.create_sensor_data(temperature=temperature, light=light_value)
    json_string = tools.create_json_payload(sensor_data, device_id="pico01")
    print(f'json_string : {json_string}')
    optimize_json_string = tools.optimize_json_data(json_string)
    print(f'optimize_json_string : {optimize_json_string}')
    response = tools.send_json(optimize_json_string, "https://eod7ebsx9ueovkr.m.pipedream.net")
   
    
    
def main():
    t1 = Timer(period=2000, mode=Timer.PERIODIC, callback=do_thing)
    t2 = Timer(period=2000, mode=Timer.PERIODIC, callback=do_thing1)
    t3 = Timer(period=3000, mode=Timer.PERIODIC, callback=send_data)
    
if __name__ == "__main__":
    #pico_連結電腦時的寫法,要用connect
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
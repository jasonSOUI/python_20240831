import machine
import time

adc = machine.ADC(4)
reference_voltage = 3.3   # ADC 參考電壓
temp_sensor_slope = 0.01  # 溫度感測器的斜率
temp_sensor_offset = 0.7  # 溫度感測器在 25°C 時的電壓

while True:
    # 讀取 ADC 值並轉換為電壓
    reading = adc.read_u16()
    voltage = reading * (reference_voltage / (2**16 - 1))

    # 根據溫度感測器特性計算溫度
    temperature = (voltage - temp_sensor_offset) / temp_sensor_slope + 25

    print(f"溫度: {temperature:.2f} °C")
    time.sleep(2)
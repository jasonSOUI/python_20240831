import paho.mqtt.client as mqtt
from datetime import datetime
import os
import csv

org_values = {}

def is_record_value(name, value):
    """檢查名稱是否存在於字典中，如果不存在則寫入並賦值"""
    global org_values  # 明確聲明使用全局變量
    if name in org_values:
        # print(f"{name} 已經存在，對應的值是: {org_values[name]}")
        if org_values[name] != value:
            org_values[name] = value
            return True
        else:
            return False
    else:
        # 如果名稱不存在，寫入字典並賦予預設值
        org_values[name] = value
        # print(f"{name} 不存在，已寫入字典並賦予值: {org_values[name]}")
        return True

def is_float(value):
    try:
        # 嘗試將字串轉換為 float
        float(value)
        return True
    except ValueError:
        # 如果轉換失敗，說明不是浮點數
        return False

def decode_utf8_string(encoded_string):
    """
    解碼 UTF-8 編碼的字串。
    
    :param encoded_string: 編碼的字串，格式如 "\xe9\x96\x8b\xe7\x87\x88"
    :return: 解碼後的字串
    """
    # 移除可能存在的引號
    encoded_string = encoded_string.strip("'\"")
    
    # 將字串轉換為位元組序列
    byte_string = bytes(encoded_string, 'utf-8').decode('unicode_escape').encode('latin1')
    
    # 解碼為 UTF-8
    return byte_string.decode('utf-8')

def on_connect(client, userdata, flags, reason_code, properties):
    #連線bloker成功時,只會執行一次
    client.subscribe("SA-42/#")

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode("utf-8") 

    # 文字數字轉換判斷
    if is_float(payload):
        value = float(payload)    
    else:
        value = decode_utf8_string(f"{payload}")

    # 判斷資料是否有異動
    is_record = is_record_value(topic, value)

    # print(f"是否須更新資料:{value}, {is_record}")

    if is_record:
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = [[dt, topic, f'{value}']]
        print(f"資料有異動:{data[0]}")
        record(data)

def main():
    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    # 設定用戶名和密碼
    username = "pi"  # 替換為您的用戶名
    password = "raspberry"  # 替換為您的密碼
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_message = on_message 
    client.connect("192.168.0.252", 1883, 60)
    client.loop_forever()

def record(data:list):
    today = datetime.now()
    data_path = os.path.join(os.getcwd(), "data")
    data_dir = today.strftime("%Y%m%d")
    data_file_path = os.path.join(data_path, data_dir) + ".csv"
    create_csv_file(data_file_path, data)

def create_csv_file(file_path, data):
    # 獲取檔案的目錄路徑
    directory = os.path.dirname(file_path)
    
    # 如果目錄不存在,則建立它
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # 開啟檔案並寫入資料
    with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

if __name__ == "__main__":
    main()
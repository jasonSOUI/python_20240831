import paho.mqtt.client as mqtt
from datetime import datetime
import os
import csv

org_temperature = float(0)

def on_connect(client, userdata, flags, reason_code, properties):
    #連線bloker成功時,只會執行一次
    client.subscribe("SA-42/#")

def on_message(client, userdata, msg):
    global org_temperature
    topic = msg.topic
    value = float(msg.payload.decode())
    if topic == 'SA-42/LINE_LEVEL':
        if org_temperature != value:
            org_temperature = value
            dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data = [[dt, "光線", f'{org_temperature}']]
            record(data)
            print(f'{dt} - 光線:{org_temperature}')
    #print(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}'")

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

def record(data):
    today = datetime.now()
    data_path = os.getcwd()
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
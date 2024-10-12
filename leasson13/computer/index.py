import paho.mqtt.client as mqtt

org_temperature = float(0)

def on_connect(client, userdata, flags, reason_code, properties):
    #連線bloker成功時,只會執行一次
    client.subscribe("SA-42/#")

def on_message(client, userdata, msg):
    global org_temperature
    topic = msg.topic
    value = float(msg.payload.decode())
    if topic == 'SA-42/temperature':
        if org_temperature != value:
            org_temperature = value
            print(f'led_value:{org_temperature}')
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

def record():
    pass

if __name__ == "__main__":
    main()
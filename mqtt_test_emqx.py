import paho.mqtt.client as mqtt
import ssl
import time
import json
from random import randint

MQTT_TOPIC = "iot"
# Define the MQTT client
client = mqtt.Client( client_id="hien_server")

# Define the message callback
def on_message(client, userdata, message):
    print(f"Received message from topic ")
    # print("topic = ", message.topic)
    # print("data = ", message.payload.decode())
    message_topic = message.topic
    message_decode = message.payload.decode()
    print(f"data type: {type(message_decode)}")
    print(f"data deocde: {message_decode}")

    message_json = json.loads(message_decode)
    print(f"convert data type: {type(message_json)}")
    volt_value = (message_json["Volt"])
    ampe_value = (message_json["Ampe"])
    print(f"Volt value: {volt_value}, type: {type(volt_value)}")
    print(f"Ampe value: {ampe_value}, type: {type(ampe_value)}")

# Define the connect callback
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"Connect failed with code {rc}")

# Configure the client

# client.tls_insecure_set(False)
# client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.username_pw_set(username= 'duchien', password= 'duchien')
client.connect("34.97.119.55", 1883, 60)

# Function to publish temperature data
def publish_temperature(temperature):
    topic = "iot"
    data = {
    "temp": temperature,
    # "humi": data2
    }
    
    json_data = json.dumps(data)
    client.publish(topic, json_data)
    print(f"Published: {json_data} to topic: {topic}")

# Start the network loop in a separate thread
client.loop_start()

# Simulate sending temperature data
try:
    while True:
        temperature = randint(0,50)
        # publish_temperature(temperature)
        time.sleep(10)  # Publish temperature every 10 seconds

except KeyboardInterrupt:
    print("Stopping...")
    client.loop_stop()
    client.disconnect()
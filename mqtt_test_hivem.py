import paho.mqtt.client as mqtt
from time import sleep
from random import randint
import json

def on_connect(client, userdata, flags, rc):
	print("Connected with result code {}".format(rc))

def on_disconnect(client, userdata,rc):
	print("Disconnected From Broker")

client = mqtt.Client('D03')
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.on_connect = on_connect
client.on_disconnect = on_disconnect

client.username_pw_set(username= 'Device123', password= 'Device123')
client.connect("a13bc93369ea4867a98bb0e453764b2a.s1.eu.hivemq.cloud", 8883, 60)

def mqtp_publish(data1, data2):
	data = {
		"temp": data1,
		# "humi": data2
	}
	
	json_data = json.dumps(data)
	print(json_data)
	client.publish("iot", json_data)
	return "OK"

while True:
	data_random1 = randint(0,50)
	data_random2 = randint(0,50)
	mqtp_publish(data_random1, data_random2)
	
	sleep(5)
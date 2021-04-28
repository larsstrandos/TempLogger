import paho.mqtt.client as mqtt
from datetime import datetime
import sqlite3
from sqlite3 import Error
import pathlib

print()

# Set some variable`s
broker_address = "10.0.0.13"
now = datetime.now()

# Make connection to the Database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def add_temp(conn, temp_data):
    sql = ''' INSERT INTO temperatures_temp(sensor_id,temp,created_date)
            VALUES(?,?,datetime('now')) '''
    cur = conn.cursor()
    cur.execute(sql, temp_data)
    conn.commit
    return cur.lastrowid

# Connect to MQTT Broker

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe("1/dht/temperature")

def on_message(client, userdata, msg):
    database = r"/home/lars/templogger/db.sqlite3"
    conn = create_connection(database)
    with conn:
        m_decode=str(msg.payload.decode("utf-8","ignore"))
        print(m_decode, now)
        tempData = (1, m_decode)
        add_temp(conn, tempData)

def main():
    # MQTT Connect at start prosses
    client = mqtt.Client(client_id="", clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")
    client.on_connect = on_connect
    client.on_message = on_message

    client.username_pw_set(username="arduino_yun", password="thisissomesecurepassword")
    print("Connecting...")
    client.connect(broker_address, 1883, 10)
    client.loop_forever()

if __name__ == '__main__':
    main()
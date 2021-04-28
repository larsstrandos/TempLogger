// Include the required packages to get MQTT Client to work
#include "DHT.h"
#include <Bridge.h>
#include <BridgeClient.h>
#include <PubSubClient.h>

// Some variables
#define MQTT_SERVER "10.0.0.13"
#define MQTT_PUB_TEMP "1/dht/temperature"
#define DHTPIN 2
#define DHTTYPE DHT11

char charTemp[] = "00.00";

DHT dht(DHTPIN, DHTTYPE);

float temp;

unsigned long previousMillis = 0;  // Stores last time temperature was published
const long interval = 10000;       // Interval at which to publish sensor readings

void callback(char* topic, byte* payload, unsigned int length) {
  // handle message arrived
}

BridgeClient yun;
PubSubClient client(MQTT_SERVER, 1883, callback, yun);

void setup() {
  // Starts the Ethernet bridge
  Serial.begin(9600);
  Bridge.begin();
  dht.begin();

  if (client.connect("arduinoClient", "arduino_yun", "thisissomesecurepassword")) {
  }
}

void loop() {
  client.loop();

  unsigned long currentMillis = millis();
  // Every X number of seconds (interval = 10 seconds) 
  // it publishes a new MQTT message
  if (currentMillis - previousMillis >= interval) {
    // Save the last time a new reading was published
    previousMillis = currentMillis;
    // New DHT sensor readings
    // Read temperature as Celsius (the default)
    temp = dht.readTemperature();

    dtostrf(temp, 4, 2, charTemp);
    
    client.publish(MQTT_PUB_TEMP, charTemp);
    Serial.print(temp);
  }
}

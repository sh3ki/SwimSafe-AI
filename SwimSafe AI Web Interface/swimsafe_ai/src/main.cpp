#include <WiFi.h>
#include <WiFiClient.h>

const char* ssid = "SHEKi_5G";
const char* password = "jedijedi";

const int ledPin = 2;
const int buzzerPin = 4;

WiFiServer server(80);

void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  
  // Test the hardware on startup
  Serial.println("Testing hardware...");
  digitalWrite(ledPin, HIGH);
  digitalWrite(buzzerPin, HIGH);
  delay(1000);
  digitalWrite(ledPin, LOW);
  digitalWrite(buzzerPin, LOW);
  Serial.println("Hardware test complete");

  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi ..");
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("Connected!");
  Serial.println(WiFi.localIP());

  server.begin();
}

void loop() {
  WiFiClient client = server.available();
  if (client) {
    Serial.println("New Client!");
    String request = client.readStringUntil('\r');
    Serial.println(request);

    if (request.indexOf("/alarm/on") != -1) {
      Serial.println("Drowning Detected!");
      digitalWrite(ledPin, HIGH);
      digitalWrite(buzzerPin, HIGH);
      Serial.println("LED and Buzzer ON");
    }

    if (request.indexOf("/alarm/off") != -1) {
      Serial.println("Alarm OFF");
      digitalWrite(ledPin, LOW);
      digitalWrite(buzzerPin, LOW);
      Serial.println("LED and Buzzer OFF");
    }

    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: text/html");
    client.println();
    client.println("OK");
    delay(1);
    client.stop();
  }
}

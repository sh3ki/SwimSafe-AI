#include <WiFi.h>
#include <WiFiClient.h>

const char* ssid = "sh3ki";
const char* password = "jedijedi";

const int ledPin = 2;
const int led2Pin = 4;
const int buzzerPin = 5;

WiFiServer server(80);

bool alarmActive = false;

void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);
  pinMode(led2Pin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);

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
    Serial.println("Drowning Detected!");
    String request = client.readStringUntil('\r');
    Serial.println(request);

    if (request.indexOf("/alarm/on") != -1) {
      alarmActive = true;
    }

    if (request.indexOf("/alarm/off") != -1) {
      alarmActive = false;
      digitalWrite(ledPin, LOW);
      digitalWrite(led2Pin, LOW);
      noTone(buzzerPin);  // stop buzzer if using tone
      digitalWrite(buzzerPin, LOW); // fallback
    }

    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: text/html");
    client.println();
    client.println("OK");
    delay(1);
    client.stop();
  }

  // 🔔 Flash logic
  if (alarmActive) {
    digitalWrite(ledPin, HIGH);
    digitalWrite(led2Pin, HIGH);
    digitalWrite(buzzerPin, HIGH);
    delay(300);  // on for 300ms

    digitalWrite(ledPin, LOW);
    digitalWrite(led2Pin, LOW);
    digitalWrite(buzzerPin, LOW);

    delay(300); // off for 300ms
  }
}

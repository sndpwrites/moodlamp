#include "ESP8266WiFi.h"
const char* ssid = "tukilabs_hotspot";
const char* password = "apple1234";


int x;
int y;
int z;

WiFiServer server(80);
const char* host = "192.168.43.183";


const int pin1 = 13;
const int pin2 = 14;
const int pin3 = 15;
const int t = 3000;

void setup() {

  pinMode(pin1, OUTPUT);
  pinMode(pin2, OUTPUT);
  pinMode(pin3, OUTPUT);
  Serial.begin(115200);
  delay(10);

  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid,password);
    while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
 
  // Start the server
  server.begin();
  Serial.println("Server started");
 
  // Print the IP address
  Serial.print("URL");
  Serial.print("http://");
  Serial.print(WiFi.localIP());
  Serial.println("/");
}

void loop() {

  WiFiClient client;
  const int httpPort = 80;
  if (!client.connect(host, httpPort)) {
    Serial.println("connection failed");
    return;
  }

 // We now create a URI for the request
  String url = "/color";
  Serial.print("Requesting URL: ");
  Serial.println(url);
  
  // This will send the request to the server
  client.print(String("GET ") + url + " HTTP/1.1\r\n" +
               "Host: " + host + "\r\n" + 
               "Connection: close\r\n\r\n");
  delay(500);
  String line;
  char buf[15];
  // Read all the lines of the reply from server and print them to Serial
  while(client.available()){
    line = client.readStringUntil('\n');
    Serial.print(line);
  }

//string to c char array converstion
strcpy(buf, line.c_str());

    int i = 0;
    char *p = strtok (buf, ",");
    char *array[3];
//splitting
    while (p != NULL)
    {
        array[i++] = p;
        p = strtok (NULL, ",");
    }

    for (i = 0; i < 3; ++i) 
        Serial.print(array[i]);

//conversion to integer and output to pins
analogWrite(pin1,atoi(array[0]));
analogWrite(pin2,atoi(array[1]));
analogWrite(pin3,atoi(array[2]));

}


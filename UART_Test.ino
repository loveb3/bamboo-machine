#include <Arduino.h>

bool first = true;

void setup() {
  Serial.begin(9600);
}

void loop() {
  delay(1000);
  // if(first){
    Serial.write('P');
  //   first = false;
  // }
}
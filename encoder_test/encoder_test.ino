#include <Encoder.h>
#include <math.h>

// Encoder pins
const int pinA = 2; // Adjust according to your ESP32 setup
const int pinB = 3;

Encoder myEncoder(pinA, pinB);

long prevPosition = 0; // Store the last encoder position
int probe = 4;

void setup() {
  Serial.print("Booting");
  Serial.begin(9600); // Start serial communication
}

void loop() {
  long newPosition = myEncoder.read(); // Read the current encoder position
  
  // Calculate the angle
  // Each pulse represents 0.6 degrees (360 / 600)
  float angle = (newPosition * 360.0) / 2400.0;
  float rad = probe - probe*cos(angle*M_PI/180);

  // For demonstration, let's just print the angle when it changes significantly
  if (abs(newPosition - prevPosition) > 1) { // Adjust sensitivity as needed
    Serial.print("Angle: ");
    Serial.println(angle, 2); // Print angle with 2 decimal places for precision
    Serial.print("Cane Radius: ");
    Serial.println(rad, 2); // Print angle with 2 decimal places for precision
    prevPosition = newPosition; // Update the previous position
  }
  
  delay(100); // Delay to manage loop execution and serial print speed
}


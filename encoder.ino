#include <Encoder.h>
#include <math.h>

// Encoder pins
#define pinA 2
#define pinB 3
#define limitSwitchPin 7

Encoder myEncoder(pinA, pinB);

long prevPosition = 0; // Store the last encoder position
int probe = 4;

void setup() {
  Serial.print("Booting");
  Serial.begin(9600); // Start serial communication
  pinMode(limitSwitchPin, INPUT_PULLUP);
}

void loop() {

  

  
  long newPosition = myEncoder.read(); // Read the current encoder position

  //placeholder value for xPosition
  float xPosition = newPosition;
  
  // Calculate the angle
  // Each pulse represents 0.6 degrees (360 / 600)
  float angle = (newPosition * 360.0) / 2400.0;
  float radius = probe - probe*cos(angle*M_PI/180);

  // For demonstration, let's just print the angle when it changes significantly
  if (abs(newPosition - prevPosition) > 1) { // Adjust sensitivity as needed

    Serial.print("X Position: ");
    Serial.print(xPosition, 2); // Print angle with 2 decimal places for precision
    Serial.print(", Radius: ");
    Serial.print(radius, 2); // Print angle with 2 decimal places for precision
    Serial.print(", Angle: ");
    Serial.println(angle, 2); // Print angle with 2 decimal places for precision  
    prevPosition = newPosition; // Update the previous position
  }

  if (digitalRead(limitSwitchPin) == LOW) { // Limit switch is pressed
    myEncoder.write(0); // Reset the encoder's position
    prevPosition = 0; // Also reset the previous position to avoid immediate repeat prints
    delay(50); //debounce delay
  }
  
  delay(100); // Delay to manage loop execution and serial print speed
}

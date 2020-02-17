import processing.serial.*;

import cc.arduino.*;

Arduino arduino;
boolean b = true; 
void setup() {
  size(470, 200);

  println(Arduino.list());  
  arduino = new Arduino(this, Arduino.list()[0], 57600);

  for (int i = 0; i <= 13; i++)
    arduino.pinMode(i, Arduino.OUTPUT);
}

void draw() {
}

void mousePressed()
{
  int pin = 13;

  if (b) {
    arduino.digitalWrite(pin, Arduino.HIGH);
  } else {
    arduino.digitalWrite(pin, Arduino.LOW);
  }
  
  b=!b;
}
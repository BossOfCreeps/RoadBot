#include <Stepper.h>
Stepper step1(200, 47, 49, 51, 53);
Stepper step2(200, 39, 41, 43, 45);

String V1, V2;
int v1, v2;
int last_v1=0, last_v2=0;

void setup() {
  Serial.begin(9600);
  step1.setSpeed(60);
  step2.setSpeed(60);
}

void loop() {
  if (Serial.available() > 0) {
    V1 = Serial.readStringUntil(' ');
    V2 = Serial.readStringUntil(NULL);

    v1 = V1.toInt();
    v2 = V2.toInt();
    Serial.print(v1);
    Serial.print(" ");
    Serial.println(v2);
    steping(v1, v2);
  }
}

void steping(int val1, int val2) {
  for (int i = last_v1; i != val1; i += znak(val1 - last_v1)) {
    step1.step(znak(val1 - last_v1));
    Serial.println(100 + i);
    delay(50);
  }

  for (int i = last_v2; i != val2; i += znak(val2 - last_v2)) {
    step2.step(znak(val2 - last_v2));
    Serial.println(200 + i);
    delay(50);
  }
  last_v1 = val1;
  last_v2 = val2;

}

int znak(int n) {
  return (n / abs(n));
}


int r = 2;
int y = 3;
int g = 10;
int K = 3;
void setup() {
  // put your setup code here, to run once:
  pinMode(r, OUTPUT);
  pinMode(y, OUTPUT);
  pinMode(g, OUTPUT);
  digitalWrite(r, 1);
  digitalWrite(y, 1);
  digitalWrite(g, 0);
}
void loop() {
  //loop2();
}
void loop2() {
  // stop
  digitalWrite(r, 1);
  digitalWrite(y, 0);
  digitalWrite(g, 0);
  delay(2000 * K);
  // stop + yellow
  digitalWrite(r, 1);
  digitalWrite(y, 1);
  digitalWrite(g, 0);
  delay(500 * K);
  // green
  digitalWrite(r, 0);
  digitalWrite(y, 0);
  digitalWrite(g, 1);
  delay(2000 * K);
  //blinking green
  for (int i = 0; i < 3; i++) {
    digitalWrite(g, 1);
    delay(160 * K);
    digitalWrite(g, 0);
    delay(160 * K);
  }
  // yellow
  digitalWrite(r, 0);
  digitalWrite(y, 1);
  digitalWrite(g, 0);
  delay(1000 * K);
}



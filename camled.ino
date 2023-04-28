char result = '0';

void setup() {
  Serial.begin(9600);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    result = Serial.read();
  }
  switch (result) {
    case '0':
      digitalWrite(7, HIGH);
      digitalWrite(8, LOW);
      break;
    case '1':
      digitalWrite(7, LOW);
      digitalWrite(8, HIGH);
      break;
    case '2':
      digitalWrite(7, HIGH);
      digitalWrite(8, HIGH);
      break;
    default:
      digitalWrite(7, LOW);
      digitalWrite(8, LOW);
  }
}
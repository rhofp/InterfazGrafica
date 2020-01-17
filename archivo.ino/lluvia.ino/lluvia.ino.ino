
bool digitalValue;

void setup(){
  Serial.begin(9600);
}

void loop(){


  // Entrada digital pin 7 arduino
  digitalValue = digitalRead(8);
  if (digitalValue == HIGH)
    Serial.println("nO Esta lloviendo!");
  if (digitalValue == LOW)
    Serial.println("si esta lloviendo!");
  delay(1000);
}

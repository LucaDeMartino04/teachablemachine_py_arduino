void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  if(Serial.available()>0){
  char readSerial = Serial.read();
  if (readSerial == 'a'){
  digitalWrite(13, HIGH);
  }
  if (readSerial == 'l'){
  digitalWrite(13, LOW);
  }
 }
} 

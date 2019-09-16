void setup(){
  pinMode(0,OUTPUT);
  pinMode(1,OUTPUT);
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  }
void loop(){
  digitalWrite(5,LOW);
  digitalWrite(0,HIGH);
  delay(200);
  digitalWrite(0,LOW);
  digitalWrite(1,HIGH);
  delay(200);
  digitalWrite(1,LOW);
  digitalWrite(2,HIGH);
  delay(200);
  digitalWrite(2,LOW);
  digitalWrite(3,HIGH);
  delay(200);
  digitalWrite(3,LOW);
  digitalWrite(4,HIGH);
  delay(200);
  digitalWrite(4,LOW);
  digitalWrite(5,HIGH);
  delay(200);
}

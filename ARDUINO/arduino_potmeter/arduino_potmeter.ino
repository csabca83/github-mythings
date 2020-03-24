// potmetert 0..1023 ertekig tudjun k belaitani
int poti=0;
void setup() {
  // put your setup code here, to run once:

  for(int i=0;i<8;i++){
    pinMode(i,OUTPUT);
  }
  pinMode(A0,INPUT); //JELOLI AZ ANALOG PORTOT
}

void loop() {
  // put your main code here, to run repeatedly:
  poti=analogRead(A0); //BEOLVASSUK A POTMETERT ERTEKET
  if(poti>400){
    for(int i=0;i<8;i++){
      digitalWrite(i,HIGH);
    }
  
  }
  else{
    for(int i=0;i<8;i++){
      digitalWrite(i,LOW);
  }
  }
}

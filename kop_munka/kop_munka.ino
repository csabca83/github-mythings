#include <dht.h>
#include <LiquidCrystal_I2C.h>
#include <DallasTemperature.h>
#define ONE_WIRE_BUS 6 
#define DHT11_PIN 7
LiquidCrystal_I2C lcd = LiquidCrystal_I2C(0x27, 16, 2);
dht DHT;
OneWire oneWire(ONE_WIRE_BUS); // Setup a oneWire instance to communicate with any OneWire devices  
// (not just Maxim/Dallas temperature ICs) 
DallasTemperature sensors(&oneWire);// Pass our oneWire reference to Dallas Temperature. 

int moisture;
int light;
int gomb;
int gomb2;
int allapot=0;
int hang=600;
int fhiba;
int phiba;
int hhiba;
int mhiba;
int vhiba;
void setup(){
  lcd.begin(16, 2);
  lcd.backlight();               //kell egy ertek osszehasonlito az elejen utana egy lcdre kulon iffek
  Serial.begin(9600);
  sensors.begin();
  pinMode(8,INPUT_PULLUP);   
  pinMode(9,OUTPUT);
  pinMode(10,INPUT_PULLUP);
  pinMode(5,OUTPUT);}
void loop(){
  int chk = DHT.read11(DHT11_PIN);
  light=analogRead(A0);
  light=1023-light;
  sensors.requestTemperatures();
  float vizh=sensors.getTempCByIndex(0);
  float homerseklet=DHT.temperature;
  float paratartalom=DHT.humidity;
  moisture=analogRead(A1);
  moisture=1023-moisture;
  Serial.println(moisture);                                                                                 // Serial.println(sensors.getTempCByIndex(0)); //You can have more than one DS18B20 on the same bus.  
                                                                                    // 0 refers to the first IC on the wire 
  gomb2=digitalRead(10);
  if (gomb2==0){
    if (hang==0){
      hang=600;}
    else if (hang==600){
      hang=0;}}
  
  if (light<950){
    fhiba=0;}
  else{fhiba=1;}

  if(homerseklet<32.00){
    hhiba=0;}
  else{hhiba=1;}
  
  if(paratartalom<70.00){
    phiba=0;}
  else{phiba=1;}

  if (moisture>300){
    mhiba=0;}
  else{mhiba=1;}  
 
  if(vizh<30.00){
    vhiba=0;}
  else{vhiba=1;}
  
  
  
  if(fhiba==1 && hhiba==0 && phiba==0 && mhiba==0 && vhiba==0){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nagy a feny");
    lcd.setCursor(0,1);
    lcd.print(light);
    if (hang==0){noTone(9);}
    else{tone(9,hang);}
    digitalWrite(5,LOW);
    delay(20);}
  
  else if(fhiba==0 && hhiba==1 && phiba==0 && mhiba==0 && vhiba==0){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nagy a homerseklet");
    lcd.setCursor(0,1);
    lcd.print(homerseklet);
    if (hang==0){noTone(9);}
    else{tone(9,hang);}
    digitalWrite(5,LOW);
    delay(20);}
  
  else if(fhiba==0 && hhiba==0 && phiba==1 && mhiba==0 && vhiba==0){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nagy a paratartalom");
    lcd.setCursor(0,1);
    lcd.print(paratartalom);
    if (hang==0){noTone(9);}
    else{tone(9,hang);}
    digitalWrite(5,LOW);
    delay(20);}
  
  
  else if(fhiba==0 && hhiba==0 && phiba==0 && mhiba==1 && vhiba==0){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Keves a vizt.");
    lcd.setCursor(0,1);
    lcd.print(moisture);
    if (hang==0){noTone(9);}
    else{tone(9,hang);}
    digitalWrite(5,HIGH);
    delay(20);}
  
  else if(fhiba==0 && hhiba==0 && phiba==0 && mhiba==0 && vhiba==1){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nagy a vizho");
    lcd.setCursor(0,1);
    lcd.print(vizh);
    if (hang==0){noTone(9);}
    else{tone(9,hang);}
    digitalWrite(5,LOW);
    delay(20);}
  
  else if(fhiba==0 && hhiba==1 && phiba==1 && mhiba==0 && vhiba==0){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nagy a homerseklet");
    lcd.setCursor(0,1);
    lcd.print("Nagy a paratartalom");
    if (hang==0){noTone(9);}
    else{tone(9,hang);}
    digitalWrite(5,LOW);
    delay(20);}
  
  else if(fhiba==1 && hhiba==0 && phiba==0 && mhiba==1 && vhiba==0){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nagy a feny");
    lcd.setCursor(0,1);
    lcd.print("Keves a vizt.");
    if (hang==0){noTone(9);}
    else{tone(9,hang);}
    digitalWrite(5,LOW);
    delay(20);}
  
  else if(fhiba==0 && hhiba==1 && phiba==0 && mhiba==1 && vhiba==0){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nagy a homerseklet");
    lcd.setCursor(0,1);
    lcd.print("Keves a vizt.");
    if (hang==0){noTone(9);}
    else{tone(9,hang);}
    digitalWrite(5,LOW);
    delay(20);}
  
  else if(fhiba==0 && hhiba==0 && phiba==1 && mhiba==1 && vhiba==0){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Keves a vizt.");
    lcd.setCursor(0,1);
    lcd.print("Nagy a paratartalom:");
    if (hang==0){noTone(9);}
    else{tone(9,hang);}
    digitalWrite(5,LOW);
    delay(20);}
  
  else if(fhiba==0 && hhiba==0 && phiba==0 && mhiba==1 && vhiba==1){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Keves a vizt.");
    lcd.setCursor(0,1);
    lcd.print("Nagy a vizho");
    if (hang==0){noTone(9);}
    else{tone(9,hang);}
    digitalWrite(5,LOW);
    delay(20);}

  else if(fhiba==1 && hhiba==1 && phiba==0 && mhiba==0 && vhiba==0){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nagy a feny");
    lcd.setCursor(0,1);
    lcd.print("Nagy a homerseklet");
    if (hang==0){noTone(9);}
    else{tone(9,hang);}
    digitalWrite(5,LOW);
    delay(20);}
  
  else if(fhiba==1 && hhiba==0 && phiba==1 && mhiba==0 && vhiba==0){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nagy a feny");
    lcd.setCursor(0,1);
    lcd.print("Nagy a paratartalom:");
    if (hang==0){noTone(9);}
    else{tone(9,hang);}
    digitalWrite(5,LOW);
    delay(20);}
  
 else if(fhiba==1 && hhiba==0 && phiba==0 && mhiba==0 && vhiba==1){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nagy a feny");
    lcd.setCursor(0,1);
    lcd.print("Nagy a vizho:");
    if (hang==0){noTone(9);}
    else{tone(9,hang);}
    digitalWrite(5,LOW);
    delay(20);}
  
  else if(fhiba==0 && hhiba==1 && phiba==0 && mhiba==0 && vhiba==1){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nagy a homerseklet");
    lcd.setCursor(0,1);
    lcd.print("Nagy a vizho");
    if (hang==0){noTone(9);}
    else{tone(9,hang);}
    digitalWrite(5,LOW);
    delay(20);}
  
  else if(fhiba==0 && hhiba==0 && phiba==1 && mhiba==0 && vhiba==1){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nagy a vizho");
    lcd.setCursor(0,1);
    lcd.print("Nagy a paratartalom");
    if (hang==0){noTone(9);}
    else{tone(9,hang);}
    digitalWrite(5,LOW);
    delay(20);}
  
  else if(fhiba==0 && hhiba==0 && phiba==0 && mhiba==0 && vhiba==0){
    noTone(9);
    digitalWrite(5,LOW);}
  
  else{
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("2-nel tobb ertek");
    lcd.setCursor(0,1);
    lcd.print("nem megfelelo!");
    if (hang==0){noTone(9);}
    else{tone(9,hang);}
    digitalWrite(5,LOW);
    delay(20);}  


  
  gomb=digitalRead(8);
  if (gomb==0){
    if (allapot==0){
      allapot=1;}
    else if (allapot==1){
      allapot=2;}
    else if (allapot==2){
      allapot=0;}}
  
 
  if (allapot==0 && fhiba==0 && hhiba==0 && phiba==0 && mhiba==0 && vhiba==0){
   lcd.clear();
   lcd.setCursor(0,0); 
   lcd.print("Temp:");
   lcd.setCursor(9,0);
   lcd.print(homerseklet);
   lcd.print((char)223);
   lcd.print("C");
   lcd.setCursor(0,1);
   lcd.print("Humidity:");
   lcd.print(paratartalom);
   lcd.print("%");
   delay(20);}
  
  if (allapot==1 && fhiba==0 && hhiba==0 && phiba==0 && mhiba==0 && vhiba==0){
   lcd.clear();
   lcd.setCursor(0,0);
   lcd.print("Fenyerosseg:");
   lcd.setCursor(0,1);
   lcd.print(light);
   delay(20);}

  if (allapot==2 && fhiba==0 && hhiba==0 && phiba==0 && mhiba==0 && vhiba==0){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Viztartalom");
    lcd.setCursor(12,0);
    lcd.print(moisture);
    lcd.setCursor(0,1);
    lcd.print("Vizho");
    lcd.setCursor(11,1);
    lcd.print(vizh);
    delay(20);
    }}

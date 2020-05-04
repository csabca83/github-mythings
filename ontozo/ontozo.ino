#include <dht11.h>                              //Be importálom a librariket.
#include <LiquidCrystal_I2C.h>
#include <DallasTemperature.h>
#define ONE_WIRE_BUS 6 
#define DHT11_PIN 7
LiquidCrystal_I2C lcd = LiquidCrystal_I2C(0x27, 16, 2);
dht11 DHT11;
OneWire oneWire(ONE_WIRE_BUS); // Setup a oneWire instance to communicate with any OneWire devices  
// (not just Maxim/Dallas temperature ICs) 
DallasTemperature sensors(&oneWire);// Pass our oneWire reference to Dallas Temperature. 

int moisture;    //szenzorok számai
int light;
int gomb;        //gombok
int gomb2;
int fhiba;   //fény    // szenzorhibak,hogyha nem megfelelő értéket adnak vissza,akkor az értékük 1es lesz
int phiba;   //páratartalom
int hhiba;   //külső hőmérséklet
int mhiba;   // moisture,föld víztartalma
int vhiba;   // víz hőmérséklete 
int allapot=0; // Az lcd-én épp melyik értéket jelenítem meg,gombnyomással nő az értéke 2ig,után kinullázódik.Ha hibajelzés van nincs módunk tovább lépni.
int hang=600;  //Hangszóró értéke

void setup(){
  lcd.begin(16,2);
  lcd.backlight();               //kell egy ertek osszehasonlito az elejen utana egy lcdre kulon iffek
  Serial.begin(9600);
  sensors.begin();
  pinMode(8,INPUT_PULLUP);   
  pinMode(11,OUTPUT);
  pinMode(10,INPUT_PULLUP);
  pinMode(12,INPUT_PULLUP);
  pinMode(5,OUTPUT);}

void loop(){
  int chk = DHT11.read(DHT11_PIN);
  light=analogRead(A3);
  light=1023-light;        // a light resistorjaim fény hatására csökkentették az értéküket,ezután növelni kezdik.
  sensors.requestTemperatures();
  float vizh=sensors.getTempCByIndex(0);
  float homerseklet=DHT11.temperature;
  float paratartalom=DHT11.humidity;
  moisture=analogRead(A1);                                   // adatok bekérése
  moisture=1023-moisture;                                                                                
                                                                                     
  gomb2=digitalRead(12);                   //hibaüzenetnél szól a hangszóró,a gomb lenyomásával némíthassuk
  if (gomb2==0){
    if (hang==0){
      hang=600;}
    else if (hang==600){
      hang=0;}}
  
  if (light<870){                         // ha nem megfelelő az érték,akkor a hibánál 1es lesz
    fhiba=0;}
  else{fhiba=1;}

  if(homerseklet<32.00){
    hhiba=0;}
  else{hhiba=1;}
  
  if(paratartalom<70.00){
    phiba=0;}
  else{phiba=1;}

  if (moisture>150){
    mhiba=0;}
  else{mhiba=1;}  
 
  if(vizh<30.00){
    vhiba=0;}
  else{vhiba=1;}
  
  
  
  if(fhiba==1 && hhiba==0 && phiba==0 && mhiba==0 && vhiba==0){      // minden eshetőségnél kiírja,hogy melyik érték nem stimmel,egyszerre 2 értéket maximum.
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nagy a feny");
    lcd.setCursor(0,1);
    lcd.print(light);
    if (hang==0){noTone(11);}          //ha a hang 0,nemszól a riasztó ellenkező esetben igen.Kikellet kapcsolnom  a riasztót mivel 0 frekvenciánál is adott ki magából hangot.
    else{tone(11,hang);}
    digitalWrite(5,HIGH);               // a relé kikapcsolt állapotban marad,addig amíg csak a föld víztartalma jelez hibát.Ezzel azt oldjuk meg,hogy nem kezd el délben 40 fokos vízzel öntözni :)
    delay(20);}
  
  else if(fhiba==0 && hhiba==1 && phiba==0 && mhiba==0 && vhiba==0){            // A sok if az egyik dolog ami zavar,de mivel minden varációt kiakarok iratni,máskép nem tudtam megoldani.
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nagy a homerseklet");
    lcd.setCursor(0,1);
    lcd.print(homerseklet);
    if (hang==0){noTone(11);}
    else{tone(11,hang);}
    digitalWrite(5,HIGH);
    delay(20);}
  
  else if(fhiba==0 && hhiba==0 && phiba==1 && mhiba==0 && vhiba==0){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nagy a paratartalom");
    lcd.setCursor(0,1);
    lcd.print(paratartalom);
    if (hang==0){noTone(11);}
    else{tone(11,hang);}
    digitalWrite(5,HIGH);
    delay(20);}
  
  
  else if(fhiba==0 && hhiba==0 && phiba==0 && mhiba==1 && vhiba==0){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Keves a vizt.");
    lcd.setCursor(0,1);
    lcd.print(moisture);
    if (hang==0){noTone(11);}
    else{tone(11,hang);}
    digitalWrite(5,LOW);
    delay(20);}
  
  else if(fhiba==0 && hhiba==0 && phiba==0 && mhiba==0 && vhiba==1){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nagy a vizho");
    lcd.setCursor(0,1);
    lcd.print(vizh);
    if (hang==0){noTone(11);}
    else{tone(11,hang);}
    digitalWrite(5,HIGH);
    delay(20);}
  
  else if(fhiba==0 && hhiba==1 && phiba==1 && mhiba==0 && vhiba==0){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nagy a homerseklet");
    lcd.setCursor(0,1);
    lcd.print("Nagy a paratartalom");
    if (hang==0){noTone(11);}
    else{tone(11,hang);}
    digitalWrite(5,HIGH);
    delay(20);}
  
  else if(fhiba==1 && hhiba==0 && phiba==0 && mhiba==1 && vhiba==0){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nagy a feny");
    lcd.setCursor(0,1);
    lcd.print("Keves a vizt.");
    if (hang==0){noTone(11);}
    else{tone(11,hang);}
    digitalWrite(5,HIGH);
    delay(20);}
  
  else if(fhiba==0 && hhiba==1 && phiba==0 && mhiba==1 && vhiba==0){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nagy a homerseklet");
    lcd.setCursor(0,1);
    lcd.print("Keves a vizt.");
    if (hang==0){noTone(11);}
    else{tone(11,hang);}
    digitalWrite(5,HIGH);
    delay(20);}
  
  else if(fhiba==0 && hhiba==0 && phiba==1 && mhiba==1 && vhiba==0){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Keves a vizt.");
    lcd.setCursor(0,1);
    lcd.print("Nagy a paratartalom:");
    if (hang==0){noTone(11);}
    else{tone(11,hang);}
    digitalWrite(5,HIGH);
    delay(20);}
  
  else if(fhiba==0 && hhiba==0 && phiba==0 && mhiba==1 && vhiba==1){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Keves a vizt.");
    lcd.setCursor(0,1);
    lcd.print("Nagy a vizho");
    if (hang==0){noTone(11);}
    else{tone(11,hang);}
    digitalWrite(5,HIGH);
    delay(20);}

  else if(fhiba==1 && hhiba==1 && phiba==0 && mhiba==0 && vhiba==0){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nagy a feny");
    lcd.setCursor(0,1);
    lcd.print("Nagy a homerseklet");
    if (hang==0){noTone(11);}
    else{tone(11,hang);}
    digitalWrite(5,HIGH);
    delay(20);}
  
  else if(fhiba==1 && hhiba==0 && phiba==1 && mhiba==0 && vhiba==0){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nagy a feny");
    lcd.setCursor(0,1);
    lcd.print("Nagy a paratartalom:");
    if (hang==0){noTone(11);}
    else{tone(11,hang);}
    digitalWrite(5,HIGH);
    delay(20);}
  
 else if(fhiba==1 && hhiba==0 && phiba==0 && mhiba==0 && vhiba==1){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nagy a feny");
    lcd.setCursor(0,1);
    lcd.print("Nagy a vizho:");
    if (hang==0){noTone(11);}
    else{tone(11,hang);}
    digitalWrite(5,HIGH);
    delay(20);}
  
  else if(fhiba==0 && hhiba==1 && phiba==0 && mhiba==0 && vhiba==1){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nagy a homerseklet");
    lcd.setCursor(0,1);
    lcd.print("Nagy a vizho");
    if (hang==0){noTone(11);}
    else{tone(11,hang);}
    digitalWrite(5,HIGH);
    delay(20);}
  
  else if(fhiba==0 && hhiba==0 && phiba==1 && mhiba==0 && vhiba==1){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nagy a vizho");
    lcd.setCursor(0,1);
    lcd.print("Nagy a paratartalom");
    if (hang==0){noTone(11);}
    else{tone(11,hang);}
    digitalWrite(5,HIGH);
    delay(20);}
  
  else if(fhiba==0 && hhiba==0 && phiba==0 && mhiba==0 && vhiba==0){  //ha minden érték megfelelő
    noTone(11);
    digitalWrite(5,HIGH);}
  
  else{                                          // hogyha 3 vagy több érték nem megfelelő
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("2-nel tobb ertek");
    lcd.setCursor(0,1);
    lcd.print("nem megfelelo!");
    if (hang==0){noTone(11);}
    else{tone(11,hang);}
    digitalWrite(5,LOW);
    delay(20);}  


  
  gomb=digitalRead(10);   //a gombbal variálom az állapotokat.
  if (gomb==0){
    if (allapot==0){
      allapot=1;}
    else if (allapot==1){
      allapot=2;}
    else if (allapot==2){
      allapot=0;}}
  
 
  if (allapot==0 && fhiba==0 && hhiba==0 && phiba==0 && mhiba==0 && vhiba==0){     //csak akkor érvényesül ha nincs szükség a hibajelzésre.
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

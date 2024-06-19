// Práctica encender y apagar dos LED
const int LED1=13;
const int LED2=12;
void setup()
{
pinMode(LED1,OUTPUT);
pinMode(LED2,OUTPUT);
}
void loop()
{
digitalWrite(LED1,HIGH);
delay(2000);
digitalWrite(LED1,LOW);
delay(2000);
digitalWrite(LED2,HIGH);
delay(2000);
digitalWrite(LED2,LOW);
delay(2000);
}
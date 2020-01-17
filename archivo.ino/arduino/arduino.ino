#include <Servo.h>
#include <LiquidCrystal.h>

Servo puertaVidrio;
Servo porton;
Servo ventana;
LiquidCrystal lcd(13, A0, 22, 48, 42, 38);
char val;
int angulo;
//SEnsor de gotas 
bool digitalValue;
//PUERTAS CONTROLADOR POR PUENTE H 1-----------------MOTOR A------------------
int enableA = 5; //velocidad motor A
int dirmotorA1 = 6; // direccion motor a
int dirmotorA2= 7;  // direccion motor a
//MOTOR---------- B------------ POR PUENTEH 1------------------------------
int enableB = 8; //velocidad motor B
int dirmotorB1 = 9; // direccion motor b
int dirmotorB2= 10; // direccion motor b
int velocidad = 120;
//PUERTA Y VENTILADOR CONTROLADO POR PUENTE H 2-------------------------
int enableC = 28; //velocidad motor A
int dirmotorC1 = 30; // direccion motor a
int dirmotorC2= 32;  // direccion motor a
//MOTOR puerta-------------------------
int enableD = A3; //velocidad motor B
int dirmotorD1 = A4; // direccion motor b
int dirmotorD2= A5; // direccion motor b
int velocidad2 = 120;
//Métodos para el control adelante, atras, derecha
// izquierda y stop
int ledCuarto1 =20;
int ledCuarto2 = 14;
int ledSalaA=4;
int ledSalaB=3;
int ledBanio=21;
int ledPatio=2;

void abrirPuerta1(){
digitalWrite (dirmotorA1,LOW);// GIRA MOTOR A
digitalWrite (dirmotorA2,HIGH);
analogWrite (enableA, velocidad);
digitalWrite (dirmotorB1,LOW);// DETIENE MOTOR B
digitalWrite (dirmotorB2,LOW);
analogWrite (enableB, 120);
delay(700);
//apagado
digitalWrite (dirmotorA1,LOW);// GIRA MOTOR A
digitalWrite (dirmotorA2,LOW);
analogWrite (enableA,0);
digitalWrite (dirmotorB1,LOW);// DETIENE MOTOR B
digitalWrite (dirmotorB2,LOW);
analogWrite (enableB, 0);

}
void cerrarPuerta1(){
digitalWrite (dirmotorA1,HIGH);// gira motor A derecha
digitalWrite (dirmotorA2,LOW);
analogWrite (enableA, velocidad);
digitalWrite (dirmotorB1,LOW);// gira motor B derecha
digitalWrite (dirmotorB2,LOW);
analogWrite (enableB, velocidad);
delay(700);
digitalWrite (dirmotorA1,LOW);// GIRA MOTOR A
digitalWrite (dirmotorA2,LOW);
analogWrite (enableA, 0);
digitalWrite (dirmotorB1,LOW);// DETIENE MOTOR B
digitalWrite (dirmotorB2,LOW);
analogWrite (enableB,0);

}
void abrirPuerta2(){
digitalWrite (dirmotorA1,LOW);// gira motor A izquierda
digitalWrite (dirmotorA2,LOW);
analogWrite (enableA, velocidad);
digitalWrite (dirmotorB1,LOW);// gira motor B izquierda
digitalWrite (dirmotorB2,HIGH);
analogWrite (enableB,velocidad);
delay(700);
digitalWrite (dirmotorA1,LOW);// GIRA MOTOR A
digitalWrite (dirmotorA2,LOW);
analogWrite (enableA, 0);
digitalWrite (dirmotorB1,LOW);// DETIENE MOTOR B
digitalWrite (dirmotorB2,LOW);
analogWrite (enableB,0);
}
void cerrarPuerta2(){
digitalWrite (dirmotorA1,LOW);// para motor A
digitalWrite (dirmotorA2,LOW);
analogWrite (enableA, 120);
digitalWrite (dirmotorB1,HIGH);// para motor B
digitalWrite (dirmotorB2,LOW);
analogWrite (enableB, velocidad);
delay(700);
digitalWrite (dirmotorA1,LOW);// GIRA MOTOR A
digitalWrite (dirmotorA2,LOW);
analogWrite (enableA, 0);
digitalWrite (dirmotorB1,LOW);// DETIENE MOTOR B
digitalWrite (dirmotorB2,LOW);
analogWrite (enableB,0);
}
void abrirPuerta3(){
digitalWrite (dirmotorC1,LOW);// GIRA MOTOR A
digitalWrite (dirmotorC2,LOW);
analogWrite (enableC, 0);
digitalWrite (dirmotorD1,HIGH);// DETIENE MOTOR B
digitalWrite (dirmotorD2,LOW);
analogWrite (enableD, 120);
delay(700);
//apagado
digitalWrite (dirmotorC1,LOW);// GIRA MOTOR A
digitalWrite (dirmotorC2,LOW);
analogWrite (enableC,0);
digitalWrite (dirmotorD1,LOW);// DETIENE MOTOR B
digitalWrite (dirmotorD2,LOW);
analogWrite (enableD, 0);
}
void cerrarPuerta3(){
      digitalWrite(dirmotorC1, LOW);// gira motor A derechaaaaaa
      digitalWrite (dirmotorC2,LOW);
      analogWrite (enableC, 0);
      digitalWrite (dirmotorD1,LOW);// gi
      digitalWrite (dirmotorD2,HIGH);
      analogWrite (enableD, velocidad);
      delay(700);
      digitalWrite (dirmotorC1,LOW);// GIRA MOTOR A
      digitalWrite (dirmotorC2,LOW);
      analogWrite (enableC, 0);
      digitalWrite (dirmotorD1,LOW);// DETIENE MOTOR B
      digitalWrite (dirmotorD2,LOW);
      analogWrite (enableD,0);

}
void prenderVentilador(){
    digitalWrite (dirmotorC1,HIGH);// gira motor A derechaaaaaaxd
    digitalWrite (dirmotorC2,LOW);
    analogWrite (enableC, 120);
    digitalWrite (dirmotorD1,LOW);// gira motor B derecha
    digitalWrite (dirmotorD2,LOW);
    analogWrite (enableD, 0);
  
  }
void apagarVentilador(){
    digitalWrite (dirmotorC1,LOW);// gira motor A derechaaxaxa
    digitalWrite (dirmotorC2,LOW);
    analogWrite (enableC, 0);
    digitalWrite (dirmotorD1,LOW);// gira motor B derecha
    digitalWrite (dirmotorD2,LOW);
    analogWrite (enableD, 0);
  } 
void pararMotores(){
    digitalWrite (dirmotorA1,LOW);// para motor A
    digitalWrite (dirmotorA2,LOW);
    analogWrite (enableA, 0);
    digitalWrite (dirmotorB1,LOW);// para motor B
    digitalWrite (dirmotorB2,LOW);
    analogWrite (enableB, 0);
    digitalWrite (dirmotorC1,LOW);// gira motor A derecha
    digitalWrite (dirmotorC2,LOW);
    analogWrite (enableC, 0);
    digitalWrite (dirmotorD1,LOW);// gira motor B derecha
    digitalWrite (dirmotorD2,LOW);
    analogWrite (enableD, 0);
}
// comenzamos parando los motores
void setup(){
    //Sensor
    Serial.begin(9600);
    lcd;
    lcd.begin(16, 2);
    lcd.setCursor(0,0); 
    lcd.print("Inicializando..."); 
    delay(2000); 
    lcd.clear(); 
   
    int i;
    puertaVidrio.attach(33);
    ventana.attach(A8);
    porton.attach(12);
    for(i=0;i<34;i++){
               pinMode(i, OUTPUT); //poner pin 5,6,7,8,9,10,11 de salida
    }
    Serial.begin(9600);
   pinMode(ledBanio,OUTPUT);
   pinMode(ledCuarto1,OUTPUT);
   pinMode(ledCuarto2,OUTPUT);
   pinMode(28,OUTPUT);
   pinMode(30,OUTPUT);
   pinMode(32,OUTPUT);
   pinMode(A3,OUTPUT);
   pinMode(A4,OUTPUT);
   pinMode(A5,OUTPUT);
   //pinMode(A8,OUTPUT);
   pinMode(12,OUTPUT);
   pinMode(33,OUTPUT);
    }
// Y el bucle principal
void loop() {
  //Sensor
  digitalValue = digitalRead(8);
  if (digitalValue == HIGH)
    Serial.println("nO Esta lloviendo!");
  if (digitalValue == LOW)
    Serial.println("si esta lloviendo!");
    
  delay(1000);
  //termina codigo

  
  if( Serial.available() ) {
          val = Serial.read();
  }
switch (val) {
  case '0':
        digitalWrite(ledCuarto1,HIGH);
        break;
  case '1': 
        digitalWrite(ledCuarto1,LOW);
        break;
  case '2':
        digitalWrite(ledCuarto2,HIGH);
        break;
  case '3':
        digitalWrite(ledCuarto2,LOW);
        break;
  case '5':
        digitalWrite(ledSalaA,LOW);
        break;
  case '4': 
        digitalWrite(ledSalaA,HIGH);
        break;
  case '7':
        digitalWrite(ledSalaB,LOW);
        break;
  case '6': 
        digitalWrite(ledSalaB,HIGH);
        break;
  case '9':
        digitalWrite(ledBanio,LOW);
        break;
  case '8': 
        digitalWrite(ledBanio,HIGH);
        break;
 case 'z':
        break;
  case 'w':
        digitalWrite(ledPatio,LOW);
        break;
  case 'x': 
        digitalWrite(ledPatio,HIGH);
        break;
  case 'a':
         abrirPuerta1();
         break;
  
  case 'b':
         cerrarPuerta1();
         break;
  case 'c':
         abrirPuerta2();
         delay(1000);  
         
         break;
  case 'd':
          cerrarPuerta2();
         break;
  case 'e':
          pararMotores();
          break;
  //Puerta de Vidrio
  case 'f':
          puertaVidrio.write(80);
          //Serial.println("Giro 80");
          break;
  case 'g':
          puertaVidrio.write(0);
          //Serial.println("Giro 0");
          break;
 //Porton
  case 'h':
          porton.write(180);
          break;
  case 'i':
          porton.write(90);
          break;
  case 'k':
          ventana.write(0);
          break;
  case 'l':
          ventana.write(65);
          break;
  //lcd
  case 'm':
          lcd.setCursor(0, 0);
          lcd.print("Bienvenido Miguel");
          delay(2000);
  case 'n':
          lcd.setCursor(0, 1);
          lcd.print("HOLI");
          delay(2000);

  case 'o':
        abrirPuerta3();
        break;
  case 'p':
        cerrarPuerta3();
        break;
  case 'q':
        prenderVentilador();
        break;

  case 'r':
        apagarVentilador();
}
}

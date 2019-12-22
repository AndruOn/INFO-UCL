

int V= 0;
char sender_char[10]= "hello";
int sender_int= 42;

// the setup routine runs once when you press reset:
void setup() {
        // on démarre la liaison
        // en la réglant à une vitesse de 115200 bits par seconde.
        Serial.begin(115200);
}

void loop() {
// Setup pins for input
    if (Serial.read()=='K')
          {
              //tester lequel marche entre print et write
              Serial.print('O');
              Serial.write('O');
              //Serial.print(" Hello i'm the receiver ");
              
              
              delay(1000);
              sender_int= Serial.read();
              Serial.print(" ");
              Serial.println(sender_int);
              //Serial.readBytes(sender_char,10);
              //Serial.print(sender_char);
              
          }
}

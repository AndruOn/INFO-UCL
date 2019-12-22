
int V= 0;

// the setup routine runs once when you press reset:
void setup() {
        // on démarre la liaison
        // en la réglant à une vitesse de 115200 bits par seconde.
        Serial.begin(115200);
}
void loop() {
// Setup pins for input
    if(Serial.read()=='O')
        {
        Serial.print(69);
        delay(10);
        //Serial.print(" hello i'm the slave ");
        //delay(100);
        //Serial.print(" ");
        //Serial.print('K');
        
        }
}

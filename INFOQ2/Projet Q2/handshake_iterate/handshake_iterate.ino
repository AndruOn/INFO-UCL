

int V= 0;

// the setup routine runs once when you press reset:
void setup() {
        // on démarre la liaison
        // en la réglant à une vitesse de 9600 bits par seconde.
        Serial.begin(115200);
}
void loop() {
  // put your main code here, to run repeatedly:

// Setup pins for input
    if(Serial.read()=='K')
        {
          for (int i = 0; i < 6; i++) { 
                
                      int V = analogRead(i);
                      Serial.print(V);
                      Serial.print(" ");
                      Serial.print(i);
                  }
        }
}

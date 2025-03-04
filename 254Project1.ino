#define BLUE_BUZZER 13  // Pin for Blue Buzzer
#define RED_BUZZER 10   // Pin for Red Buzzer

void setup() {
    Serial.begin(9600);  // Initialize serial communication
    pinMode(BLUE_BUZZER, OUTPUT);
    pinMode(RED_BUZZER, OUTPUT);

    Serial.println("Arduino is ready, waiting for input.");
}

void loop() {
    if (Serial.available() > 0) {
        char receivedChar = Serial.read(); // Read the input
        
        if (receivedChar == 'B') { // Recognized face
        digitalWrite(RED_BUZZER, LOW); // turn the red LED off if it is on
        digitalWrite(BLUE_BUZZER, HIGH);  // turn the LED on                     
        }

        else if (receivedChar == 'R') { // Unrecognized face
        digitalWrite(BLUE_BUZZER, LOW); // turn the blue LED off if it is on
        digitalWrite(RED_BUZZER, HIGH);  // turn the LED on                     
        }
    }
}
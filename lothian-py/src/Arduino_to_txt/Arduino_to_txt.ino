void setup() { 
  Serial.begin(9600); // initialize serial communications 
}
 void loop() {
 int sensorPin = A0;    // analog input pin to hook the sensor to
 int sensorValue = 0;  // variable to store the value coming from electrode
 
 sensorValue = analogRead(sensorPin); // read the value from the sensor
  
 Serial.print(millis()); // print the time in milliseconds since the program started
 Serial.print(' ');
 Serial.println(sensorValue); // print to serial
    // wait 
  delay(100);
}


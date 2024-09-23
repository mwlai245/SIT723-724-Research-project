// Pin Definitions
const int solarPanelPin = A0;  // Pin for solar panel via voltage divider
const int piezoPin = A1;       // Pin for piezoelectric sensor

// Resistor values for voltage divider
const float R1 = 5000.0;  // 5k ohms
const float R2 = 10000.0; // 10k ohms

// Arduino Nano 33 IoT reference voltage (3.3V)
const float refVoltage = 3.3;

void setup() {
  // Start serial communication for debugging
  Serial.begin(9600);
  
  // Set the analog pins as input
  pinMode(solarPanelPin, INPUT);
  pinMode(piezoPin, INPUT);
}

void loop() {
  // Read analog values
  int solarRaw = analogRead(solarPanelPin);  // Raw value from solar panel
  int piezoRaw = analogRead(piezoPin);       // Raw value from piezoelectric sensor
  
  // Convert the solar panel analog value to actual voltage
  float solarVoltage = (solarRaw * refVoltage) / 1023.0;
  
  // Since it's a voltage divider, calculate the actual solar panel voltage
  float actualSolarVoltage = solarVoltage * ((R1 + R2) / R1);
  
  // Convert the piezoelectric analog value to voltage
  float piezoVoltage = (piezoRaw * refVoltage) / 1023.0;
  
  // Output the results to the serial monitor
  Serial.print("Solar Panel Voltage: ");
  Serial.print(actualSolarVoltage);
  Serial.println(" V");
  
  Serial.print("Piezoelectric Sensor Voltage: ");
  Serial.print(piezoVoltage);
  Serial.println(" V");
  
  // Small delay before the next reading
  delay(1000);
}

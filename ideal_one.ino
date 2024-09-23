// Resistor values in the voltage divider
const float R1 = 5000.0;  // 5k ohm
const float R2 = 10000.0; // 10k ohm
 
void setup() {
  // Initialize serial communication at 9600 bits per second
  Serial.begin(9600);
}
 
void loop() {
  // Read the analog input on pin A0 (values between 0 and 1023 [max value])
  int sensorValue = analogRead(A0);
 
  // Convert the analog reading to voltage (3.3V reference)
  float measuredVoltage = sensorValue * (3.3 / 1023.0);
 
  // Calculate the actual input voltage (before the divider)
  // Using the voltage divider formula: V_in = V_out * (R1 + R2) / R2
  float actualVoltage = measuredVoltage * ((R1 + R2) / R2);

  // Print the measured voltage (the voltage at the ADC pin)
  Serial.print("Measured Voltage (at ADC pin): ");
  Serial.print(measuredVoltage);
  Serial.println(" V");
 
  // Print the actual voltage (before the voltage divider)
  Serial.print("Actual Voltage (before divider): ");
  Serial.print(actualVoltage);
  Serial.println(" V");
 
  // Wait for 1 second before the next reading
  delay(1000);
}
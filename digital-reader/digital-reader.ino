byte sentState = 0;

void setup()
{
  for (int i = 0; i < 8; i++)
  {
    pinMode(i, INPUT_PULLUP);
    delay(5);
  }
  Serial.begin(115200);
}

void loop()
{
// read current state of digital pins 0-7 
// http://www.arduino.cc/en/Reference/PortManipulation

  byte currentPortD = PIND;
  if (currentPortD != sentState)
  {
    Serial.println(currentPortD, BIN);
    sentState = currentPortD;
  }
  delay(1);
}


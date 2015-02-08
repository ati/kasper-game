int sentState = 0;
const int MIN_PIN=2;
const int MAX_PIN=12;

void setup()
{
  for (int i = MIN_PIN; i <= MAX_PIN; i++)
  {
    pinMode(i, INPUT_PULLUP);
    delay(5);
  }
  Serial.begin(115200);
}


int get_pins()
{
  int cp = 0;
  for (int i = MIN_PIN; i <= MAX_PIN; i++)
  {
    cp = (cp << 1) | digitalRead(i);
  }
  return cp;
}


void loop()
{
// read current state of digital pins 0-7 
// http://www.arduino.cc/en/Reference/PortManipulation

  int currentPins = get_pins();
  if (currentPins != sentState)
  {
    Serial.println(currentPins, BIN);
    sentState = currentPins;
  }
  delay(1);
}


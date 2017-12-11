#include "HX711.h"

const byte channels[] = {A1,A2,A3,A4};

HX711 scale;

void setup() {
  Serial.begin(38400);

  scale.begin(channels, 4, A0);
}

void loop() {
  long *tmp;
  tmp = scale.read_averages();
  Serial.print("readAll: \t\t");
  for (byte i=0;i<4;i++)
  {
    Serial.print("\t");
    Serial.print(long(tmp[i]));
  }
  Serial.println("");
}

const int sensor_pinA0=A0;
const int sensor_pinA1=A1;
const int sensor_pinA2=A2;

int data_counter=0;
int dataA0;
int dataA1;
int dataA2;



void setup()
{
  Serial.begin(9600);
}


void loop()
{
  dataA0=analogRead(sensor_pinA0);
  dataA1=analogRead(sensor_pinA1);
  dataA2=analogRead(sensor_pinA2);
  Serial.println(String(data_counter)+';'+String(dataA0)+';'+String(dataA1)+';'+String(dataA2));
  delay(1000);
  data_counter+=1;
  Serial.flush();
}

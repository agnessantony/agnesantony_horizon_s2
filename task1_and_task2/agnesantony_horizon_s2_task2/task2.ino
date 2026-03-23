#include <Servo.h> // built in library for controlling servos
Servo my_servo; // declare a servo motor variable
const int LED = 13; // LED connected to digital pin 13
int PotPin = A0; // potentiometer connected to analog pin A0
int value; // a variable 'value' which stores the potentiometer angle is declared
bool LEDSTATE; // variable which stores the state of the LED (on/off)
void setup() //used to configure pins and devices, only runs once during the startup
{
  Serial.begin(9600); //set data transfer speed for serial communication
  my_servo.attach(9); //my_servo connected to pin 9
  pinMode(LED, OUTPUT); // defines LED as an output device
}

void loop() //this loop runs continously
{
  value = analogRead(PotPin); //reads analog value from pin A0
  value = map(value, 0, 1023, 0, 180); //map input value to angle for servo
  Serial.print("Potentiometer angle: "); //prints the text on the serial monitor
  Serial.print(value); //prints the value of potentiometer angle on the serial monitor
  Serial.println(" degrees"); //prints the unit
  if (value <= 68) //checks if the servo is at an angle within the safe range
  {
    digitalWrite(LED,LOW); //since the angle is within the safe range, LED remains off.
    my_servo.write(value); // servo angle = potentiometer angle = value
  }
  else // this part is executed if the servo angle exceeds the safe range
  {
    digitalWrite(LED,HIGH); // LED turns on as a warning
  	my_servo.write(68); // servo angle remains 68 degrees and won't rotate further
  }
  Serial.print("Servo angle: "); //prints the text on the serial monitor
  if (value <= 68) //if the angle is within 68 degrees
    Serial.print(value); // that value (angle) is printed on the serial monitor
  else  //if the angle is beyond 68 degrees
    Serial.print(68); // 68 is printed as servo angle on the serial monitor
  Serial.println(" degrees"); //the text that being printed indicates the unit of angle
  bool LEDSTATE = digitalRead(LED); //checks if the LED is ON/OFF
  if(LEDSTATE == LOW) //if the LED is off
    Serial.println("Within the safe limit."); //the text is printed on the serial monitor - indicates that the angle is within the safe limit.
  else //if the LED is on, this part is executed
    Serial.println("WARNING : The safe limit has exceeded."); //the text is printed on the serial monitor - indicates that the angle has exceeded the safe limit.
  Serial.println(""); //for readability
  delay(1000); // a delay of 1000 ms (1 sec) is introduced. 
}
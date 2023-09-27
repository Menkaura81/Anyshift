/*****************************************************************************************
* Arduino sketch for driving a 7 segment display with Anyshift 
*
* Based on the SevSeg library by Dean Reading: https://github.com/DeanIsMe/SevSeg
* 
* Wiring instructions:
* https://circuitdigest.com/microcontroller-projects/interfacing-seven-segment-display-with-Arduino
*
* 2023 Menkaura Soft
******************************************************************************************/
#include "SevSeg.h"


SevSeg sevseg;


void setup()
{
  //Set to 1 for single-digit display
  byte numDigits = 1;
  //defines common pins while using multi-digit display. Left for single digit display
  byte digitPins[] = {};
  //Defines Arduino pin connections in order: A, B, C, D, E, F, G, DP
  byte segmentPins[] = {9,8, 7, 6, 5, 4, 3, 2};
  byte displayType = COMMON_CATHODE; //Use COMMON_ANODE for Common Anode display
  bool resistorsOnSegments = true; //‘false’ if resistors are connected to common pin
  //Initialize sevseg object. Use COMMON_ANODE instead of COMMON_CATHODE for CA display
  sevseg.begin(displayType, numDigits, digitPins, segmentPins, resistorsOnSegments);
  sevseg.setBrightness(90);
  Serial.begin(9600); //Setup serial conection
}


void loop()
{
  if (Serial.available()) 
  {
    //read from serial
    char option = Serial.read();
    //get the number from the char
    option -= '0';  

    //Display the data    
    if (option == 8) //Code for rest position
    {
      sevseg.setChars("-");
      sevseg.refreshDisplay();
    }
    else if (option == 0) //Code for neutral
    {
      sevseg.setChars("n");
      sevseg.refreshDisplay();
    }
    else if (option > 0 && option < 8) //Codes for gears numbers
    {
      sevseg.setNumber(option);
      sevseg.refreshDisplay();
      //delay(1000);  
    }
    else if (option == 9) //Code for blank display
    {
      sevseg.blank();
      sevseg.refreshDisplay();
    }      
  }  
}

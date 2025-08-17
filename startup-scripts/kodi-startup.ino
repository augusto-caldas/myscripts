// Libraries
#include <limits.h>

#include "DigiKeyboard.h"

// Definitions
#define START_WAIT_TIME (15 * 1000) // Seconds
#define LOOP_WAIT_TIME ULONG_MAX

#define LED 1

#define BLINKS 50

// Blink function for the LED
void blink() {

  // Store the LEDS status
  bool status = false;

  // Alternate the LEDs
  int i = 0;
  do {

    // Show the LEDs
    digitalWrite(LED, status ? HIGH : LOW);

    // Flip them
    status = !status;

    // Wait
    DigiKeyboard.delay(START_WAIT_TIME / BLINKS);
    
    ++i;
    
  } while (i < BLINKS);
  
}

void setup() {

  // Initialise the LEDs
  pinMode(LED, OUTPUT);

  // Blink LEDs
  blink();

  // Press the key
  DigiKeyboard.sendKeyStroke(0x3A);
  
}

void loop() {

  // Infinite wait time
  DigiKeyboard.delay(LOOP_WAIT_TIME);
  
}

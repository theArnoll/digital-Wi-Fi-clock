# This project is still under development. Only the core wiring for 7 seg is being experimented.

## A simple clock with Chinese weekday displaying and Wi-Fi automatic time synchronizition

## Features

- HH:MM:SS 7 segment time displaying

- mm/dd 7 segment date displaying

- Chinese weekday 8x8 matrix displayinɢ (一~日)

- Colon displaying by turn the 7 segment display upside down
  With hardware rewiring, the programming would be easier

- Wi-Fi connection provide by onboard Wi-Fi hardware in Raspberry Pi Pico 2 W

- Internet automatic time synchronizition

- DS*1708(To be correct)* time counting chip to prevent when internet isn't availble for a period of time, or maybe, forever

- Color switching with AM/PM
  Thanks to double-colored 7 segment display allowing me to do it
  *The 7 segment display I'm using is a special double color common anode display with special wiring. For detail, please check out the [pinout pictures folder](./PinoutPics).

## BOM (Hardware I'm using)

| Hardware                                      | Amount | Usage / Notes                                                                                                                                                                             |
| --------------------------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Core & Display**                            |        |                                                                                                                                                                                           |
| Raspberry Pi Pico 2 W                         | 1      | The brain of the project                                                                                                                                                                  |
| Double colored 7 segment display              | 10     | 2.1-inch Common Anode. 6 (time) + 4 (date).                                                                                                                                               |
| 8x8 matrix display                            | 1      | Chinese weekday displayment                                                                                                                                                               |
| 1*10 segment bar display                      | 1      | For debuging<br/>Referred to as "debug bar" in everywhere in this project                                                                                                                 |
| 5V 3A power supply                            | 1      | Well, its name is power supply                                                                                                                                                            |
| **ICs**                                       |        |                                                                                                                                                                                           |
| TPIC6B595                                     | 2      | Segment displaying<br/>1 for hour and minutes + 1 for second and date, because the usage of 74HC595 below. For detail, check out the [schematic](./Schematic/wDark/DigitalWiFiClock.svg). |
| 74HC595*                                      | 2      | For common anode grounding selection,<br/>or maybe should say for controlling UDN2981A below                                                                                              |
| UDN2981A*                                     | 2      | A buffer for common anode sourcing,<br/>or can maybe be explained as to control the color of the 7 segments and whether those should be lighted from the signal 74HC595 gave              |
| MAX7219                                       | 1      | Matrix display driving<br/>!!!***TODO: Confirm the pin usage of ISET pin***!!!                                                                                                            |
| *Logic level shifter* **                      | 1      | *4* channel 3.3V to 5V logic level shifter for TPIC6B595 and MAX7219 *to be confirmed*                                                                                                    |
| **Passives**                                  |        |                                                                                                                                                                                           |
| 10Ω resistor array                            | 4      | Independent type (B-type) (4 resistors per SIP)<br/>2 for the first 4 segment displays in the time section, and 2 for last 2 segment displays in the time section and the date section    |
| 300Ω resistor array                           | 3      | Independent type (B-type) (4 resistors per SIP)<br/>For the debug bar eariler said<br/>Feel free to use normal 300Ω resistor ×10. I use array simply because I had it on hand.            |
| 130Ω resistor                                 | 2      | For DPs in [2 sets](./Schematic/wDark/DigitalWiFiClock.svg) of segment displays                                                                                                           |
| ***TODO: 10k?*** Ω resistor                   | 1      | For the ISET pin in MAX7219 to determine the current for matrix display                                                                                                                   |
| ***TODO: 10~100*** μF electrolytic capacitors | 1      | Connect it to the power supply                                                                                                                                                            |
| 0.1μF ceramic capacitors                      | 8      | Connect it to the power source of Raspberry Pi Pico 2 W and every ICs                                                                                                                     |
| **Production Materials**                      |        |                                                                                                                                                                                           |
| 20x30cm Double-sided FR-4 Perfboard           | 1      | The main carrier.                                                                                                                                                                         |
| DIP-16 IC Sockets                             | 2      | 74HC595                                                                                                                                                                                   |
| DIP-18 IC Sockets                             | 2      | UDN2981A                                                                                                                                                                                  |
| DIP-20 IC Sockets                             | 2      | TPIC6B595                                                                                                                                                                                 |
| DIP-24 IC Sockets                             | 1      | MAX7219                                                                                                                                                                                   |
| 0.5mm tinned copper wire                      |        | Routing                                                                                                                                                                                   |
| 0.35mm solid core wire                        |        | Routing and jumps<br/>Used simply because I had it on hand. Feel free to use 0.5mm ones, and that would be even better                                                                    |
| 0.8MM tinned copper wire                      |        | Main power supply                                                                                                                                                                         |
| Solder                                        |        | Why don't you need?                                                                                                                                                                       |
| Soldering iron                                | 1      | Why don't you need?<br/>BTW I'm using a FNISRI HS-01 and setted it to 370°C                                                                                                               |

*74HC595 --Signal--> UDN2981A --Power--> The common node that needs to be controlled
** TODO: To be determine the actual model

---

#### Wrote with MicroPython

Normally I'm a C++ fan, but I want to develop it quickly, and trying MicroPython out of curiosity

---

Not sure if you're concern about it or not, but everything is made by Taiwanese, not Chinese. Feel free to use it ^_<

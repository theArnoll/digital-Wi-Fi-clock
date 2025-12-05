from machine import Pin
import utime

pin = Pin("LED", Pin.OUT)

segment_numbers = { # 0~9, empty, N, O, W, I, F, E, R
    0: 0X3F, 1: 0x06, 2: 0x5B, 3: 0x4F, 4: 0x66,
    5: 0x6D, 6: 0x7C, 7: 0x27, 8: 0x7F, 9: 0x6F,
    "empty": 0x00, "full": 0xFF,
    'N': 0x54, 'O': 0x3F,
    'W': 0x7E, 'I': 0x30, 'F': 0x71, # NOWIFI
    'E': 0x79, 'R': 0x50, # ERROR
    'A': 0x77 # WAIT
}
dot = 0b00000001

segmentTPIC = [Pin(20, Pin.OUT), Pin(18, Pin.OUT), Pin(19, Pin.OUT)]
grounding595 = [Pin(22, Pin.OUT), Pin(26, Pin.OUT), Pin(27, Pin.OUT)]

def update_shift_register(pinSetup, value): # pinSetup[latch (RCLK), clock (SRCLK), data (SER)]
    pinSetup[0].value(0)
    for i in range(8):
        pinSetup[1].value(0)
        pinSetup[2].value((value >> (7 - i)) & 1)
        pinSetup[1].value(1)
    pinSetup[0].value(1)
# https://how2electronics.com/shift-register-74hc595-with-raspberry-pi-pico-micropython/

test  = [0, 2, 4, 6, 8, "empty","N", "W", "F", "R"]
test2 = [1, 3, 5, 7, 9, "full", "O", "I", "E", "A"]

while True:
    re = utime.ticks_ms() // 750 % len(test)
    try:
        update_shift_register(grounding595, 0b00000000)
        update_shift_register(segmentTPIC, segment_numbers[test[re]])
        update_shift_register(grounding595, 0b00000001)
        utime.sleep_us(1500)
        update_shift_register(grounding595, 0b00000000)
        update_shift_register(segmentTPIC, segment_numbers[test2[re]])
        update_shift_register(grounding595, 0b00000100)
        utime.sleep_us(1500)
        # pin.on()
        # sleep(0.5)
    except KeyboardInterrupt:
        break
pin.off()
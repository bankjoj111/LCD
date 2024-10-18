import RPi.GPIO as GPIO
import drivers
from time import sleep

SW1 = 27
SW2 = 17

members = [
    ("Thitikorn ", "116630462002-2"),
    ("Disorn ", "116630462040-2"),
    ("Thanarat", "116630462014-7")
]
current_member = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

display = drivers.Lcd()
display.lcd_clear()

try:
    while True:
        if GPIO.input(SW1) == GPIO.LOW:
            name, id = members[current_member]
            display.lcd_clear()
            display.lcd_display_string(name, 1)
            display.lcd_display_string(id, 2)
            current_member = (current_member + 1) % len(members)
            sleep(0.3)  
        

        if GPIO.input(SW2) == GPIO.LOW:
            print("Bye")
            break

        sleep(0.1) 

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
    display.lcd_clear()
    print("\nBye...")

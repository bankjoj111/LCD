import RPi.GPIO as GPIO
import time
import drivers 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
SW1 = 17
SW2 = 27
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
lcd = drivers.Lcd()  
message = "LAB 7"  
pos = 0  
def display_message():
    lcd.lcd_clear()  
    lcd.lcd_display_string(" " * pos + message, 1)  
display_message()  
try:
    while True:
        if GPIO.input(SW2) == GPIO.LOW:  
            if pos < 16 - len(message): 
                pos += 1
            display_message()
            time.sleep(0.2)  

        if GPIO.input(SW1) == GPIO.LOW:  
            if pos > 0: 
                pos -= 1
            display_message()
            time.sleep(0.2)
except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()  

from machine import Pin, PWM
from time import sleep, ticks_us, ticks_diff

servo = PWM(Pin(15))
servo.freq(50)

def set_angle(angle):
    duty = int(1800 + (angle / 180) * 6200)
    servo.duty_u16(duty)

trig = Pin(2, Pin.OUT)
echo = Pin(3, Pin.IN)

def distance():
    trig.low()
    sleep(0.000002)

    trig.high()
    sleep(0.00001)
    trig.low()

    while echo.value() == 0:
        start = ticks_us()

    while echo.value() == 1:
        end = ticks_us()

    duration = ticks_diff(end, start)
    return duration * 0.0343 / 2


while True:

    d = distance()

    if d < 30:

        print("\nCat detected:", round(d, 1), "cm")

        for i in range(10):
            set_angle(45)
            sleep(0.5)

            set_angle(135)
            sleep(0.5)

        set_angle(90)

    else:
        set_angle(90)
        sleep(0.2)

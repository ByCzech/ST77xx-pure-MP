import dht, machine, time, random
from machine import Pin, SPI
import st7789

display = st7789.ST7789(
    SPI(1, baudrate=40000000, phase=0, polarity=0),
    128, 160,
    reset=machine.Pin(2, machine.Pin.OUT),
    dc=machine.Pin(4, machine.Pin.OUT),
    cs=machine.Pin(10, machine.Pin.OUT),
    inversion = False,
    mono=True
)

display.init()
backlight = Pin(5,Pin.OUT)
backlight.on()

color = display.color565(0,0,0)
display.raw_fill(color)
color = display.color565(255,0,0)

while True:
    start = time.ticks_ms()
    for i in range(1000):
        x = random.getrandbits(7)
        y = random.getrandbits(7)
        display.raw_pixel(x,y,color)
    elapsed = time.ticks_ms()-start
    print(f"1k pixels in {elapsed} ms")

    for i in range(20):
        display.line(
            random.getrandbits(7),
            random.getrandbits(7),
            random.getrandbits(7),
            random.getrandbits(7),
            1)
        display.show()

while True:
    print("HERE")
    time.sleep(1)

while False:
    d = dht.DHT22(Pin(12))
    time.sleep(1)
    d.measure()
    print("%.1f, %.1f" % (d.temperature(), d.humidity()))

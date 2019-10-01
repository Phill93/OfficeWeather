import time
import adafruit_bme680
import board
from adafruit_seesaw.seesaw import Seesaw
from busio import I2C

# Create library object using our Bus I2C port
i2c = I2C(board.SCL, board.SDA)
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, address=0x76, debug=False)
ss1 = Seesaw(i2c, addr=0x36)
ss2 = Seesaw(i2c, addr=0x37)
ss3 = Seesaw(i2c, addr=0x38)

# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1014

while True:
    print("\nTemperature: %0.1f C" % bme680.temperature)
    print("Gas: %d ohm" % bme680.gas)
    print("Humidity: %0.1f %%" % bme680.humidity)
    print("Pressure: %0.3f hPa" % bme680.pressure)
    print("Altitude = %0.2f meters" % bme680.altitude)
    touch = ss1.moisture_read()
    temp = ss1.get_temp()
    print("1:   temp: " + str(temp) + "  moisture: " + str(touch))
    touch = ss2.moisture_read()
    temp = ss2.get_temp()
    print("2:   temp: " + str(temp) + "  moisture: " + str(touch))
    touch = ss3.moisture_read()
    temp = ss3.get_temp()
    print("3:   temp: " + str(temp) + "  moisture: " + str(touch))
    time.sleep(1)

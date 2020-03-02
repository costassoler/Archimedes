import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1115()
GAIN=1

while True:
    Voltage =adc.read_adc(0,gain = GAIN)
   
    
    print(Voltage*11.4/18138)
    

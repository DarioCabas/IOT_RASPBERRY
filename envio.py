import sys
import os
import thingspeak
import time
import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085

channel_id = 992285  # PUT CHANNEL ID HERE
write_key  = 'EV3BMJDLOVOTMDR0' # PUT YOUR WRITE KEY HERE
read_key   = 'HNUY60YMJJXVG6KS' # PUT YOUR READ KEY HER
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4


def envio(channel):
    try:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        sensor = BMP085.BMP085()
        #print("Temperatura={0:0.1f}*C\nHumedad={1:0.1f}%".format(temperature, humidity))
        time.sleep(20)
        T1 = temperature
        H1 = humidity
        P1 = sensor.read_pressure()
        time.sleep(20)
        T2 = temperature
        H2 = humidity
        P2 = sensor.read_pressure()
        time.sleep(20)
        T3 = temperature
        H3 = humidity
        P3 = sensor.read_pressure()
        SumT = T1+T2+T3
        SumH = H1+H2+H3
        SumP = P1+P2+P3
        Temperatura = SumT/3
        Humedad = SumH/3
        Presion = SumP/3
        #f = open('datos.csv','a+')  # w : writing mode  /  r : reading mode  /  a  :  appending mode
        #f.write('T:''{}'.format(Temperatura))
        #f.write('Date,Time,Temperatura,Humedad,Presion\r\n')
        #f.write('{0},{1},{2:0.1f}*C,{3:0.1f}%,{4:0.1f}Pa\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), Temperatura,Humedad,Presion))
        #f.write('H:''{}'.format(Humedad))
        #f.write('P:''{}'.format(Presion))
        #f.close()
        #print "Temperatura={0:0.1f}*C".format(Temperatura)
        #print "Humedad={0:0.1f}%".format(Humedad)
        #print 'Temp = {0:0.2f} *C'.format(sensor.read_temperature())
        #print 'Presion = {0:0.2f} Pa'.format(Presion)
        #print 'Altitude = {0:0.2f} m'.format(sensor.read_altitude())
        #print 'Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure())
        # write
        response = channel.update({'field1': Temperatura, 'field2': Humedad, 'field3': Presion})
    except:
        print("Coneccion Fallida")



if __name__ == "__main__":
    channel = thingspeak.Channel(id=channel_id, write_key=write_key, api_key=read_key)
    envio(channel)
        # free account has an api limit of 15sec




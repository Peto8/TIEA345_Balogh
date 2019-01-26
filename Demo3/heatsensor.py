import gspread
from oauth2client.service_account import ServiceAccountCredentials
import Adafruit_DHT
import datetime

# opening google sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('balogh-peter-tiea345-9375f6db7fe3.json', scope)
client = gspread.authorize(credentials)

sheet = client.open("SensoriDataa").sheet1 #the sheet itself

#######################################################################

def write_measurement_online(humid, temp):
    now = datetime.datetime.now()
    time = now.strftime("%H:%M - %d.%m.%Y")
    data = [time, temp, humid]
    sheet.append_row(data)

#######################################################################

#The sensor

sensor = Adafruit_DHT.DHT11

#pin number
pin = 24

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    write_measurement_online(humidity, temperature)
else:
    print('Failed to get reading. Try again!')





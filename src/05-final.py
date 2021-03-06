import serial
from flask import *

arduino = serial.Serial('/dev/ttyACM0', 9600)

app = Flask(__name__)
@app.route("/")
def index():
  return send_from_directory('/home/aruiz/src/arduino-web/src/', 'index.html')

@app.route("/js/<path:script>")
def js(script):
  return send_from_directory('/home/aruiz/src/arduino-web/src/', script)

@app.route("/luminosidad")
def luminosidad():
  arduino.write("GET\n")
  luz = arduino.readline()
  return luz

app.run (host='localhost',  port=8080)

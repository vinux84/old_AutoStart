from flask import Flask, render_template
app = Flask(__name__)

import RPi.GPIO as GPIO
import time

def gpio_settings():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    start_relay_ch1 = 26
    brake_relay_ch2 = 20
    GPIO.setup(start_relay_ch1, GPIO.OUT)
    GPIO.setup(brake_relay_ch2, GPIO.OUT)
    
@app.route('/')
def index():
    templateData = {
       'title' : 'Remote Start'
       }
    return render_template('index.html', **templateData)

@app.route("/engine_on")
def engine_on():
    #gpio_settings()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    start_relay_ch1 = 26
    brake_relay_ch2 = 20
    GPIO.setup(start_relay_ch1, GPIO.OUT)
    GPIO.setup(brake_relay_ch2, GPIO.OUT)
    GPIO.output(brake_relay_ch2, GPIO.LOW)
    GPIO.output(start_relay_ch1, GPIO.LOW)
    time.sleep(1.75) 
    # how long does this need to be on?
    # need something to confirm engine is on before power is cut on 3rd relay. Tachometer? 
    GPIO.output(start_relay_ch1, GPIO.HIGH)
    GPIO.output(brake_relay_ch2, GPIO.HIGH)
    GPIO.cleanup()
    templateData = {
        'engine_status' : 'Vehicle has Started'
    }
    return render_template('index.html', **templateData)

"""
@app.route("/engine_off")
def engine_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    start_relay_ch1 = 26
    brake_relay_ch2 = 20
    GPIO.setup(start_relay_ch1, GPIO.OUT)
    GPIO.setup(brake_relay_ch1, GPIO.OUT)
    GPIO.output(brake_relay_ch2, GPIO.LOW)
    GPIO.output(start_relay_ch1, GPIO.LOW)
    time.sleep(1.50)
    GPIO.output(start_relay_ch1, GPIO.HIGH)
    GPIO.output(brake_relay_ch2, GPIO.HIGH)
    GPIO.cleanup()
    templateData = {
       'engine_status' : 'Vehicle has Stopped'
    }
    return render_template('index.html', **templateData)
"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)



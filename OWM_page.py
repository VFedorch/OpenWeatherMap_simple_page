from weather import *
from flask import Flask, render_template, request
import logging, logging.config

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

logconsole = logging.getLogger("console")
logfile = logging.getLogger("logfile")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/weather_display", methods = ['POST', 'GET'])
def weather_display():
    form_or_button = request.form.get('location_form')
    users_ip = request.remote_addr
    weather_info = weather(form_or_button, users_ip)
    curent_weather = weather_info[0]
    seven_days_forecast = weather_info[1]
    #logconsole.info("%s: {'Current weather': %s 'Forecast': %s}", users_ip, curent_weather, seven_days_forecast)
    logfile.info("%s: {'Current weather': %s 'Forecast': %s}", users_ip, curent_weather, seven_days_forecast)
    return render_template('weather_display.html', item=curent_weather, forecast_items=seven_days_forecast)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

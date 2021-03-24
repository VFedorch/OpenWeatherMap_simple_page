from weather import *
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html', )

@app.route("/", methods=["GET"])
def get_visitor_ip():
    return request.remote_addr

@app.route("/weather_display", methods = ['POST', 'GET'])
def weather_display():
    # visitors_ip = get_visitor_ip()
    # print(visitors_ip)
    form_or_button = request.form.get('location_form')
    weather_info = weather(form_or_button)
    curent_weather = weather_info[0]
    seven_days_forecast = weather_info[1]
    return render_template('weather_display.html', item=curent_weather, forecast_items=seven_days_forecast)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

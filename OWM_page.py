from weather import *
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/", methods=["GET"])
def get_visitor_ip():
    return request.remote_addr

@app.route("/weather_display")
def weather_display():
    print("\nVisitor's IP: " + get_visitor_ip() + "\n")
    weather_info = weather()
    curent_weather = weather_info[0]
    seven_days_forecast = weather_info[1]
    return render_template('weather_display.html', item=curent_weather, forecast_items=seven_days_forecast)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

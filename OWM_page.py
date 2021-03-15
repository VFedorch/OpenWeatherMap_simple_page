from weather import *
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    # Visitor_ip = get_visitor_ip()
    # print("\nVisitor's IP: " + Visitor_ip + "\n")
    weather_info = weather()
    curent_weather = weather_info[0]
    seven_days_forecast = weather_info[1]
    return render_template('index.html', item=curent_weather)

@app.route("/", methods=["GET"])
def get_visitor_ip():
    return request.remote_addr

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

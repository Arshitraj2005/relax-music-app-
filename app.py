from flask import Flask, render_template
from utils.weather_fetcher import get_weather_data
from generator.music_engine import generate_music

app = Flask(__name__)

@app.route("/")
def home():
    weather = get_weather_data()
    generate_music(weather)
    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)

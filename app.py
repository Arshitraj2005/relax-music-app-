from flask import Flask, render_template, send_from_directory
from generator.music_engine import generate_music
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate():
    generate_music()
    return render_template('index.html', generated=True)

@app.route('/download')
def download():
    return send_from_directory('static/audio', 'generated_track.wav', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

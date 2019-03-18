from flask import Flask, render_template
import random

app = Flask(__name__)

# list of office gifs
images = [
    "https://media.giphy.com/media/12XMGIWtrHBl5e/giphy.gif",
    "https://media.giphy.com/media/5wWf7GR2nhgamhRnEuA/giphy.gif",
    "https://media.giphy.com/media/RdKjAkFTNZkWUGyRXF/giphy.gif",
    "https://media.giphy.com/media/eMeMQ0Y4DHS2k/giphy.gif",
    "https://media.giphy.com/media/JO8y56O9mTmeY/giphy.gif",
    "https://media.giphy.com/media/VNV40MHt8gzug/giphy.gif",
    "https://media.giphy.com/media/INJ6HvPXUtmKc/giphy.gif",
    "https://media.giphy.com/media/Uk8VmSYTkhkbK/giphy.gif",
    "https://media.giphy.com/media/AGD9a7IfDHXqg/giphy.gif",
    "https://media.giphy.com/media/h7No5m3tAeV4Q/giphy.gif",
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
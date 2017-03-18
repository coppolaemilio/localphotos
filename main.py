import os
from flask import Flask, render_template
app = Flask(__name__)
app.debug = True

photos_path = './static/photos/'

photos = os.listdir(photos_path)
current_index = 0
current_photo = photos[current_index]



@app.route('/')
def index():
    return render_template('main.html', photo_url=current_photo)

@app.route('/next')
def next():
    global photos
    global current_index
    global current_photo
    current_index += 1
    if current_index > len(photos) - 1:
        current_index = 0
    current_photo = photos[current_index]
    return render_template('main.html', photo_url=current_photo)


if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)
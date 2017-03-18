import os
from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)
app.debug = True

file_list = os.listdir(app.static_folder)
current_index = 0
current_file = file_list[current_index]

@app.route('/')
def index():
    return render_template('main.html', file_url=current_file, current_index = current_index)

@app.route('/next')
def next():
    global file_list
    global current_index
    global current_file
    current_index += 1
    if current_index > len(file_list) - 1:
        current_index = 0
    current_file = file_list[current_index]
    return redirect(url_for('index'))

@app.route('/previous')
def previous():
    global file_list
    global current_index
    global current_file
    
    if current_index - 1 < 0:
        current_index = len(file_list) -1
    else:
        current_index -= 1
    current_file = file_list[current_index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port, threaded=True)
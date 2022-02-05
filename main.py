from flask import Flask, request
import queueManager


app = Flask(__name__)



htmlsrc = open('index.html', 'r')
htmlsrc = htmlsrc.read()


@app.route('/style.css')
def css():
    style = open('style.css', 'r')
    style = style.read()
    return f'{style}'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return f'{htmlsrc}'
    elif request.method == "POST":
        get_champ_id1 = request.form['get-id1']
        get_champ_id2 = request.form['get-id2']
        get_champ_id3 = request.form['get-id3']
        print(get_champ_id)
        return f'{htmlsrc}'

@app.route('/start_queue')
def start_queue():
    print('tome')
    queueManager.run()
    return ''

if __name__ == '__main__':

    app.run(host='127.0.0.1', port=5000, debug_mode=on)
try:
    print(get_champ)
except:
    print('nao deu')

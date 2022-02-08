from flask import Flask, jsonify, render_template, request
from buttons import *



app = Flask(__name__)

htmlsrc = open('index.html', 'r')
htmlsrc = htmlsrc.read()

@app.route('/')
def index():
    return f'{htmlsrc}'

##########################################

@app.route('/closeLolOn')
def textbox_event_on():
    closeLol = button('closeLol.exe')
    closeLol.run()
    return ''

@app.route('/closeLolOff')
def textbox_event_off():
    closeLol = button('closeLol.exe')
    closeLol.exit()
    return ''

##########################################

@app.route('/closeOperaOn')
def textbox_event_on():
    closeOpera = button('closeOpera.exe')
    closeOpera.run()
    return ''

@app.route('/closeOperaOff')
def textbox_event_off():
    closeOpera = button('closeOpera.exe')
    closeOpera.exit()
    return ''

##########################################

@app.route('/ctrlwOn')
def textbox_event_on():
    ctrlw = button('ctrlw.exe')
    ctrlw.run()
    return ''

@app.route('/ctrlwOff')
def textbox_event_off():
    ctrlw = button('ctrlw.exe')
    ctrlw.exit()
    return ''

##########################################

@app.route('/eqrOn')
def textbox_event_on():
    eqr = button('eqr.exe')
    eqr.run()
    return ''

@app.route('/eqrOff')
def textbox_event_off():
    eqr = button('eqr.exe')
    eqr.exit()
    return ''


##########################################

@app.route('/qCtrl3On')
def textbox_event_on():
    qCtrl3 = button('qCtrl3.exe')
    qCtrl3.run()
    return ''

@app.route('/qCtrl3Off')
def textbox_event_off():
    qCtrl3 = button('qCtrl3.exe')
    qCtrl3.exit()
    return ''

##########################################

@app.route('/textboxOn')
def textbox_event_on():
    textbox = button('textbox.exe')
    textbox.run()
    return ''

@app.route('/textboxOff')
def textbox_event_off():
    textbox = button('textbox.exe')
    textbox.exit()
    return ''

if __name__ == '__main__':

    app.run(host='127.0.0.1', port=5000)
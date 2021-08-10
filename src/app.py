from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('views/index.html')

@app.route('/us')
def us():
    return render_template('views/us.html')

@app.route('/services')
def services():
    return render_template('views/services.html')

@app.route('/contact')
def contact():
    return render_template('views/contact.html')
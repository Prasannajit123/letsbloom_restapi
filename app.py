from flask import Flask
app= Flask(__name__)

@app.route('/')
def welcome():
    return 'Wroelcome to Flask'
@app.route('/home')
def home():
    return 'Welcome to home'

from controller import user_controller
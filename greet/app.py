from flask import Flask, request


app = Flask(__name__)

@app.route("/welcome")
def show_welcome():
    return f"welcome"

@app.route("/welcome/back")
def show_welcome_back():
    return f"welcome back"

@app.route("/welcome/home")
def show_welcome_home():
    return f"welcome home"
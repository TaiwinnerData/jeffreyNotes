from flask_login import LoginManager, logout_user, login_user
from flask import Flask, render_template, request, url_for, redirect, session, Response


app = Flask(__name__)


# add static path or other useful function into app.py
app._static_folder_url_path = "./templates"


# create variable as the status
@app.route("/testSend")
def testSend():
    return render_template("index.html", testVar)


@app.route("/testFunct")
def testFunct():
    print("test successful")
    return render_template("index.html")


@app.route("/testRun")
def testRun():
    for i in range(100000):
        print("test running")
        print(i)
    return "what the??"



    

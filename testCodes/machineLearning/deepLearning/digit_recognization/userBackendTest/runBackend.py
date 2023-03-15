from flask_login import LoginManager, logout_user, login_user
from flask import Flask, render_template, request, url_for, redirect, session, Response, jsonify
import os
import subprocess


# Backend test codes
# -------------------------------------------------------
app = Flask(__name__)

# add static into app.py
app._static_folder = "./templates/static"
app._static_url_path = "./templates"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/textdata', methods=['POST', 'GET'])
def get_image():
    data = request.get_json()
    text = data['text']
    result = jsonify({'message': f'The text you entered is: {text}'})
    print(result)
    print(type(result))
    return result

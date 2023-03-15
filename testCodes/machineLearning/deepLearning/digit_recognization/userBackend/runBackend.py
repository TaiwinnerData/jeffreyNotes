from flask_login import LoginManager, logout_user, login_user
from flask import Flask, render_template, request, url_for, redirect, session, Response
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


@app.route('/process-image', methods=['POST', 'GET'])
def get_image():
    img_data = request.get_json()
    img_url = img_data['img']
#    img_data = "test"
    
    print(img_data)
    return render_template("index.html")






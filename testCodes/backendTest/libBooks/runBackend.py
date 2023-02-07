from flask_login import LoginManager, logout_user, login_user
from flask import Flask, render_template, request, url_for, redirect, session, Response
import os


app = Flask(__name__)

# add static into app.py
app._static_folder = "./templates/static"
app._static_url_path = "./templates"
app.secret_key = "superSecretKey"
app.config['SESSION_TYPE'] = 'filesystem'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.auto_reload = True


# user secrutiy data
users = {'jeffrey': {'password': '20220820'}}
login_key = "testKey"




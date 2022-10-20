from flask_login import LoginManager
from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)

# add static into app.py
app._static_folder = "./templates/static"






@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/test_run_python", methods=['POST'])
def test_run_python():
    # the code you want to execute in back end machine.
    for i in range(10):
        print("test succeed!")

    return render_template("index.html")


@app.route("/test_ajax", methods=['POST'])
def test_ajax():
    for i in range(10):
        print("test ajax")
    return render_template("index.html")


@app.route("/test_get_element_path")
def render_test_get_element():
    return render_template("test_get_element.html")



@app.route("/test_get_element", methods=['POST'])
def test_get_element():
    #username = request.form.get("username")
    #print(username)
    #return redirect(url_for('login_success', username=username))

    return redirect(url_for('login_success'))



@app.route("/login_success")
def login_success():
    return render_template("login_success_test.html")



    


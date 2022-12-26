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


# user data
users = {'testUser': {'password': 'testPass'}}

testWeb2_taskStatus = 1

#@app.route("/testWeb")
def testWeb():
#    if request.method == "GET":
#        resp = Response(response='4', status=200, content_type='text/html;charset=utf-8')
#        return resp
    f_task_status = 0;
    
    for i in range(1000):
        print("test successful")

    f_task_status = 1;

    print("test1")
    return render_template("test1.html", taskStatus=f_task_status)


# Tset the different variable that can change the templates result.
@app.route("/testWeb")
def testWeb2():
    print("test2")
    return render_template("test2.html")

@app.route("/testRun")
def testWeb3():
    global testWeb2_taskStatus
    if testWeb2_taskStatus == 1:
        testWeb2_taskStatus = 0
    elif testWeb2_taskStatus == 0:
        testWeb2_taskStatus = 1
#    return redirect(url_for("testWeb2", testVar=testWeb2_taskStatus))
#    return redirect("/testWeb", testVar=testWeb2_taskStatus)
    print(testWeb2_taskStatus)
    return str(testWeb2_taskStatus)


@app.route("/read_file")
def read_file():
    with open("test1.txt", 'r') as file:
        file_content = file.read()
    return file_content



@app.route("/")
def index():
    if session["user data"] == "testKey":
        return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('username') in users:
            if request.form.get('password') in users[request.form.get('username')]['password']:
                print("password pass")
                session["user data"] = "testKey"
                print("login success")
                return redirect(url_for('index'))
            else:
                print("password fail")
                return render_template('login.html', alertOn=1)
        else:
            print("username fail")
            return render_template('login.html', alertOn=1)
    return render_template("login.html")

@app.route("/logout")
def logout():
    # In theory, logout_user() function would deleta all the information about user in session.
    # logout\_user會將所有的相關session資訊給pop掉
    session["user data"] = ""
    return render_template('login.html')
#    return "logged out."


@app.route("/test_run_python", methods=['POST'])
def test_run_python():
    f_task_status = 0
    # the code you want to execute in back end machine.
    print("start running")
    pid = str(os.getpid())
    print(pid)



    for i in range(1000):
        print("test succeed!")
    
    print("end running")
    f_task_status = 1

    return render_template("index.html", taskStatus=f_task_status)
#    return redirect(url_for("index.html", taskStatus=f_task_status))


@app.route("/test_ajax", methods=['POST'])
def test_ajax():
    for i in range(10):
        print("test ajax")
    return render_template("index.html")


@app.route("/test_get_element_path")
def render_test_get_element():
    return render_template("test_get_element.html")



#@app.route("/test_get_element", methods=['POST'])
@app.route("/test_get_element", methods=['POST'])
def test_get_element():
    #username = request.form.get("username")
    #print(username)
    #return redirect(url_for('login_success', username=username))

    return redirect(url_for('login_success'))


@app.route("/runCostLiving", methods=['POST'])
def run_cost_living():
    print("start running.")
    os.system("cd ..&& cd runETL\\runCompose&& python runCostLiving.py t")
    print("end running.")
    

#    os.system("cd runETL\\runCompose")
#    os.system("python runModule.py t")
    return render_template("index.html")



@app.route("/login_success")
def login_success():
    return render_template("login_success_test.html")





    


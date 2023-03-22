from flask_login import LoginManager, logout_user, login_user
from flask import Flask, render_template, request, url_for, redirect, session, Response, jsonify
import os
import subprocess
import base64
import numpy as np
from PIL import Image
from io import BytesIO


# Backend test codes
# -------------------------------------------------------
app = Flask(__name__, 
        static_url_path='/static'
        )

# add static into app.py
app._static_folder = "./static"
app._static_url_path = "./static"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process-image', methods=['POST', 'GET'])
def get_image():
    img_data = request.get_json()
    img_url = img_data['img']
#    img_string = jsonify({'message': f'The text you entered is: {img_url}'})
    img_string = img_url
    print("show img_url")
    print(type(img_url))
    print(img_url)
    img_raw = base64.b64decode(img_url.split(',')[1])
    img = Image.open(BytesIO(img_raw))
    img = img.convert("L")
    img_array = np.array(img)
    print(img_array)
    print(type(img_array))
    print(len(img_array))




#    img_array = np.frombuffer(img_raw, np.uint8)
#    print("show img_array")
#    print(img_array)
#    print("show the lengh of the array")
#    print(len(img_array))


#    img_string = img_string.data
#    img_string = img_string.decode('utf-8')
#    print("image string")
#    print(img_string)
#    print("show the type of image string")
#    print(type(img_string))
#    img_array = base64.b64decode(img_string)
#    print("img_array")
#    print(img_array)

#    img_raw_data = base64.b64decode(img_string.data)
#    img_array = np.frombuffer(img_raw_data, np.uint8)
#    print(img_array)
#    print(type(img_array))



    return img_url






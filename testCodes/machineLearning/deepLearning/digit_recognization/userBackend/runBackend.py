from flask_login import LoginManager, logout_user, login_user
from flask import Flask, render_template, request, url_for, redirect, session, Response, jsonify
import os
import subprocess
import base64
import numpy as np
from PIL import Image
from io import BytesIO
import cv2
import json


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
    img = request.get_json()
    img_data = request.get_json()['img']
    print(img_data)
    data_bytes = base64.b64decode(img_data)

    image = Image.open(BytesIO(data_bytes))
    image_np = np.array(image)
    print("image_np")
    print(image_np)

    img_np = np.frombuffer(data_bytes, dtype=np.uint8)
    print(img_np)
    img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)

    print(img)


#    img_string = jsonify({'message': f'The text you entered is: {img_url}'})

#    img_string = img_url
#    img_raw = base64.b64decode(img_url.split(',')[1])
#    img = Image.open(BytesIO(img_raw))
#    img = img.convert("L")
#    img_array = np.array(img)




#    img_array = np.frombuffer(img_raw, np.uint8)


#    img_string = img_string.data
#    img_string = img_string.decode('utf-8')
#    img_array = base64.b64decode(img_string)

#    img_raw_data = base64.b64decode(img_string.data)
#    img_array = np.frombuffer(img_raw_data, np.uint8)


    result = {'img': 'test'}
    return json.dumps(result)
#    return "done"






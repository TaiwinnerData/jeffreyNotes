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
    img = image_np


    if img.shape[2] == 4:
        # Create a mask of the transparent pixels
        alpha_mask = img[:, :, 3] == 0

        # Replace the transparent pixels with white
        img[alpha_mask] = [255, 255, 255, 255]
    # invert the color
    inv_img = cv2.bitwise_not(img)
    # convert the image to grayscale
    gray_img = cv2.cvtColor(inv_img, cv2.COLOR_BGR2GRAY)
    result_img = gray_img




    print("image_np")
    print(image_np)


    result = {'img': 'test'}
    return json.dumps(result)






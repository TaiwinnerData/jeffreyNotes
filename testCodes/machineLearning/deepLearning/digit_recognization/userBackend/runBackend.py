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
import digit_recognization4 as dig_reco


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

    print(image_np)
    print(img)


#    if img.shape[2] == 4:
#        # Create a mask of the transparent pixels
#        alpha_mask = img[:, :, 3] == 0
#
#        # Replace the transparent pixels with white
#        img[alpha_mask] = [255, 255, 255, 255]
#    inv_img = cv2.bitwise_not(img)
    img = img[:, :,3:4]
    print("image after mask")
    print(img)
    # invert the color
    inv_img = cv2.bitwise_not(img)
    inv_img = cv2.bitwise_not(inv_img)
    print("inv_img")
    print(inv_img)
    # convert the image to grayscale
#    gray_img = cv2.cvtColor(inv_img, cv2.COLOR_BGR2GRAY)
#    gray_img = cv2.cvtColor(inv_img, cv2.COLOR_RGBA2RGB)
#    result_img = gray_img
    result_img = inv_img
    print("show result image")
    print(result_img)


    # load the machine learning model
    testNN = dig_reco.NN()
    testNN.load_trainMD()
    result_img = result_img.flatten()
    result_img = result_img/5
    test_X = np.array([result_img])
    predict_result = testNN.predict(test_X)
    print(predict_result)





    result = {'img': 'test'}
    return json.dumps(result)






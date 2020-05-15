from __future__ import division, print_function
# coding=utf-8

import sys
import os
import glob
import re
import numpy as np

# Keras

from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image

 
# # Flask utils
from flask import Flask, redirect, url_for, request, render_template, redirect
from werkzeug.utils import secure_filename
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config["IMAGE_UPLOADS"] = "images"

 
print('Model loaded. Check http://127.0.0.1:5000/')

def predictskin(imagepath):

    MODEL_PATH = 'models/model.h5'
    model = load_model(MODEL_PATH)
    print("hi")
    test_image = image.load_img(imagepath, target_size = (75, 100)) 
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = model.predict(test_image)
    return result

# def predictbone(imagepath):
#     MODEL_PATH = 'models/scratchModel.h5'
#     model = load_model(MODEL_PATH)
#     print("hi")
#     test_image = image.load_img(imagepath, target_size = (75, 100)) 
#     test_image = image.img_to_array(test_image)
#     test_image = np.expand_dims(test_image, axis = 0)
#     result = model.predict(test_image)
#     return result

def predictpneumonia(imagepath):
    
    MODEL_PATH = 'models/model123.h5'
    model = load_model(MODEL_PATH)
    print("hi")
    test_image = image.load_img(imagepath, target_size = (75, 100)) 
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = model.predict(test_image)
    return result
    
@app.route('/', methods=['GET'])
def index():
    # Main page
    
    return render_template("index.html")


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            image = request.files["image"]
            filepath=os.path.join(app.config["IMAGE_UPLOADS"], image.filename)
            print(filepath)
            image.save(filepath)
            print("Image saved")
            print(filepath)
            result=predictskin(filepath)
            print(result)
            return render_template("index.html",result=result) 

    return render_template("index.html")  

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,threaded=False)


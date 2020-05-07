from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np

# Keras
# from keras.applications.imagenet_utils import preprocess_input, decode_predictions
# from keras.models import load_model
# from keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template, redirect
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
 
from flask import request, redirect


import os

# Define a flask app



app = Flask(__name__)
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
MODEL_PATH = 'models/model.h5'
app.config["IMAGE_UPLOADS"] = "images"
# Load your trained model
# model = load_model(MODEL_PATH)
 
print('Model loaded. Check http://127.0.0.1:5000/')
def allowed_image(filename):
    
    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

# test_image = image.load_img("images/img.jpg", target_size = (75, 100)) 
# test_image = image.img_to_array(test_image)
# test_image = np.expand_dims(test_image, axis = 0)

# #predict the result
# result = model.predict(test_image)
result=0
print(result)
@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template("index.html",result=result)


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            image = request.files["image"]

            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))

            print("Image saved")

            return redirect(request.url)

    return render_template("index.html")  
if __name__ == '__main__':
    app.run(debug=True)
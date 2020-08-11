
import sys
import os
import glob
import re
import numpy as np
import math
# Keras

from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image
import cv2
import tensorflow as tf
 
# # Flask utils
from flask import Flask, redirect, url_for, request, render_template, redirect
from werkzeug.utils import secure_filename
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config["IMAGE_UPLOADS"] = "images"

# test_image = image.load_img("/images/x-ray.jpg", target_size = (224, 224)) 
# test_image = image.img_to_array(test_image)
# test_image = np.expand_dims(test_image, axis = 0)
# prediction = model.predict(test_image)
# print(prediction)

print('Model loaded. Check http://127.0.0.1:5000/')

def preparepic(filepath,size1,size2):
    test_image = image.load_img(filepath, target_size = (size1, size2)) 
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    return test_image

def predictskin(imagepath):

    MODEL_PATH = 'models/model.h5'
    model = load_model(MODEL_PATH)
    prediction = model.predict(preparepic(imagepath,75,100))
    print(prediction)
    return prediction
    
def predictbone(imagepath):
    MODEL_PATH = 'models/scratchModel.h5'
    model = model = tf.keras.models.load_model(MODEL_PATH)
    prediction = model.predict(preparepic(imagepath,224,224))
    return prediction
    
def predictpneumonia(imagepath):
    
    MODEL_PATH = 'models/model123.h5'
    model = load_model(MODEL_PATH)
    prediction = model.predict([preparepic(imagepath,150,150)])
    print(math.ceil(prediction[0][0]))
 
    return math.ceil(prediction[0][0])
    
@app.route('/', methods=['GET'])
def index():
    # Main page
    
    return render_template("index.html")


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            image = request.files["image"]
            app.config["filepath"]=os.path.join(app.config["IMAGE_UPLOADS"], image.filename)
            filepath=app.config["filepath"]
            print(filepath)
            image.save(filepath)
            print("Image saved")
            print(filepath)
            # predictskin(filepath)
            
            return render_template("index.html") 

    return render_template("index.html")  
@app.route("/upload-image/skin", methods=["GET", "POST"])
def skin_cancer():
    arr=["1. Melanocytic nevi","Melanoma","Benign keratosis-like lesions","Basal cell carcinoma","Actinic keratoses","Vascular lesions"
,"Dermatofibroma"]
    app.config["filepath"]
    print(app.config['filepath'])
    if(app.config["filepath"]!=""):
        print("hi")
        result=predictskin(app.config["filepath"])
        print(type(result))
        count=0;
        for i in result:
            for x in i:
                if(x>=1):
                    print(arr[count])
                    result=arr[count]
                    break
                count=count+1
        
        return render_template("index.html",result=result) 
    # else:print(app.config['filepath'])
    return render_template("index.html",result=result)  
@app.route("/upload-image/bone", methods=["GET", "POST"])
def bone_dig():
    app.config["filepath"]
    print(app.config['filepath'])
    if(app.config["filepath"]!=""):
        print("hi")
        result=predictbone(app.config['filepath'])
        print(result)
        arr=[ "bones abnormality classification","elbow ","_finger_hand_humerus_forearm_shoulder_wrist"]
       
        count=0;
        for i in result:
            for x in i:

                if(x>=1):
                    print(arr[count])
                    result=arr[count]
                    break
                count=count+1

        return render_template("index.html",result=result) 
    # else:print(app.config['filepath'])
    return render_template("index.html",result=result)  
@app.route("/upload-image/pneumonia", methods=["GET", "POST"])
def pen_dig():
    print(app.config['filepath'])
    if(app.config["filepath"]!=""):
        print("hi")
        result=predictpneumonia(app.config['filepath'])
        print(result)
        arr=[ "normal", "pneumonia"]
        if (result==0):
            result=arr[0]
        else:
            result=arr[1];
        return render_template("index.html",result=result) 
    # else:print(app.config['filepath'])
    return render_template("index.html",result=result)  

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000,threaded=False)


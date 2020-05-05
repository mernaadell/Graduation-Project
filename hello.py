from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np

# Keras
from keras.models import load_model
from keras.preprocessing import image

import keras as k
#     test_image = image.load_img("img.jpg", target_size = (75, 100)) 
#     test_image = image.img_to_array(test_image)
#     test_image = np.expand_dims(test_image, axis = 0)
# #predict the result
#     result = model.predict(test_image)
import cv2
import numpy as np
import keras
import tensorflow as tf
from PIL import Image
model = tf.keras.models.load_model('tfvgg.h5')

def tfpreduh(temp):
    image = Image.open(temp)
    img = cv2.imread(temp)
    img = cv2.resize(img, (224,224))
    img = np.reshape(img, [1, 224, 224, 3])
    prob = model.predict(img)
    Classuh = prob.argmax()
    Classuh=int(Classuh)
    return Classuh
    

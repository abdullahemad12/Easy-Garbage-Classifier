import numpy as np
import tensorflow as tf
from tensorflow.keras import datasets, layers, models, regularizers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import cv2

import matplotlib.pyplot as plt

def load_model():
	model= models.Sequential()
	model.add(layers.Conv2D(32,(3,3), padding='same',input_shape=(300,300,3),activation='relu'))
	model.add(layers.MaxPooling2D(pool_size=2)) 
	model.add(layers.Conv2D(64,(3,3), padding='same',activation='relu'))
	model.add(layers.MaxPooling2D(pool_size=2)) 
	model.add(layers.Conv2D(32,(3,3), padding='same',activation='relu'))
	model.add(layers.MaxPooling2D(pool_size=2)) 
	model.add(layers.Flatten())
	model.add(layers.Dense(64,activation='relu'))
	model.add(layers.Dense(6,activation='softmax'))
	
	model.load_weights('./trained_model.h5')
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])

	return model

def predict(model, image_arr): 
	labels = {0: 'cardboard', 1: 'glass', 2: 'metal', 3: 'paper', 4: 'plastic', 5: 'trash'}
	preds = model.predict(image_arr)
	index = np.argmax(preds[0])

	return labels[index]






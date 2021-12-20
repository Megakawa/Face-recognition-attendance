from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import AveragePooling2D
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from sklearn.svm import SVC
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from imutils import paths
import tensorflow as tf
from tensorflow import keras

import matplotlib.pyplot as plt
import numpy as np
import os
import glob
import random
import shutil
import cv2
from os import listdir
import pickle

def load_faces(directory):
	faces = []
	for filename in listdir(directory):
		path = directory + "/" + filename
		print(path)
		face = cv2.imread(path)
		face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
		face = cv2.resize(face, (160,160))
		face = img_to_array(face)
		faces.append(face)
	faces = np.array(faces, dtype="float32")
	return faces

def load_dataset(directory):
	X = []
	y = []
	for subdir in listdir(directory):
		path = directory + "/" + subdir
		faces = load_faces(path)
		labels = [subdir for _ in range(len(faces))]
		print('>loaded %d examples for class: %s' % (len(faces), subdir))
		X.extend(faces)
		y.extend(labels)
	return np.asarray(X), np.asarray(y)

def get_embedding(model, face_pixels):
	mean, std = face_pixels.mean(), face_pixels.std()
	face_pixels = (face_pixels - mean) / std
	samples = np.expand_dims(face_pixels, axis=0)
	yhat = model.predict(samples)
	return yhat[0]

X,y = load_dataset("D:\PBL4\Face_Rec_Data\Train")

keras_model = load_model(r"D:\PBL4\Models\facenet_keras2")

newX = []
for face_pixels in X:
	embedding = get_embedding(keras_model, face_pixels)
	newX.append(embedding)
newX = np.asarray(newX)
print(newX.shape)

svm_model = SVC(kernel='linear', probability=True)
svm_model.fit(newX, y)

pkl_filename = "D:\PBL4\Models\svm_model.pkl"
with open(pkl_filename, 'wb') as file:
    pickle.dump(svm_model, file)
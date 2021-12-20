from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import numpy as np
import imutils
import time
import cv2
import os
import matplotlib.pyplot as plt
import pickle
import json
import pyttsx3
import time
import FirebaseAPI
import DB_BLL

def LoadModels():
	prototxtPath = r"D:\PBL4\Models\deploy.prototxt"
	weightsPath = r"D:\PBL4\Models\res10_300x300_ssd_iter_140000.caffemodel"
	faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)
	keras_model = load_model(r"D:\PBL4\Models\facenet_keras2")
	mask_detector_model = load_model(r"D:\PBL4\Models\mask_detector_model.h5")
	with open(r"D:\PBL4\Models\svm_model.pkl", 'rb') as file:
		svm_model = pickle.load(file)
	return faceNet,keras_model,mask_detector_model,svm_model

#////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////////	

def detect_face(frame, faceNet):
	(h, w) = frame.shape[:2] 
	blob = cv2.dnn.blobFromImage(frame, 1.0, (224, 224),(104.0, 177.0, 123.0))

	faceNet.setInput(blob)
	detections = faceNet.forward()

	faces = []
	locs = []

	for i in range(0, detections.shape[2]):
		confidence = detections[0, 0, i, 2]

		if confidence > 0.5:

			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")

			(startX, startY) = (max(0, startX), max(0, startY))
			(startX, startY) = (min(w-1, startX), min(h-1, startY))
			(endX, endY) = (max(0, endX), max(0, endY))
			(endX, endY) = (min(w - 1, endX), min(h - 1, endY))

			if startX==endX or startY==endY:
				break

			face = frame[startY:endY, startX:endX].copy()
			faces.append(face)
			locs.append((startX, startY, endX, endY))

	return (locs, faces)

#////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////////

def detect_mask(face1,mask_detector_model):
	face = face1.copy() 
	face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
	face = cv2.resize(face, (224, 224))
	face = img_to_array(face)
	face = preprocess_input(face)
	pred = mask_detector_model.predict(np.array([face]))
	m,w = pred[0]
	return m>w

#////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////////

def get_embedding(model, face1):
	face_pixels = face1.copy()
	face_pixels = cv2.cvtColor(face_pixels, cv2.COLOR_BGR2RGB)
	face_pixels = cv2.resize(face_pixels, (160,160))
	face_pixels = img_to_array(face_pixels)
	mean, std = face_pixels.mean(), face_pixels.std()
	face_pixels = (face_pixels - mean) / std
	samples = np.expand_dims(face_pixels, axis=0)
	yhat = model.predict(samples)
	return yhat[0]

#////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////////

def run_camera():
    
    faceNet,keras_model,mask_detector_model,svm_model = LoadModels()
 
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    vi_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An"
    engine.setProperty("voice",vi_voice_id)
 
    labels = svm_model.classes_
    with open("D:\PBL4\data.txt") as f:
        data = f.read()
    X = json.loads(data)
 
    count = 0
    plb = ""
    vs = VideoStream(src=0).start()
    while True:
        frame = vs.read()
 
        h,w = frame.shape[:2]
 
        (locs, faces) = detect_face(frame, faceNet)
 
        for (box, face) in zip(locs, faces):
            lb = ""
            color = (0,0,0)
            (startX, startY, endX, endY) = box
 
            if abs(startX-endX)*abs(startY-endY) < 0.25*h*w:
                continue
 
            if detect_mask(face,mask_detector_model):
                lb = "Mask"
                color = (255,0,0)
            else:
                yhat = get_embedding(keras_model,face)
                yhat_class = svm_model.predict(np.asarray([yhat]))
                
                temp = str(yhat_class[0])
                yhat1 = X[temp]
                yhat1 = np.asarray(yhat1)
                if sum((yhat1-yhat)**2) < 50:
                    color = (0,255,0)
                    lb = temp
 
                    if lb == plb:
                        count = count + 1
                    else:
                        count = 0
                        plb = lb
 
                    if count == 10:
                        count = 0
                        plb = ""
                        if (DB_BLL.CheckAttend(lb)==[]):
                            DB_BLL.ChangeAttendSV(lb,1)
                            FirebaseAPI.SendData(lb)
                        engine.say(lb)
                        engine.runAndWait()
 
                    
 
                else:
                    color = (0,0,255)
                    lb = "Undefined"
                    count = 0
            
            cv2.putText(frame, lb, (startX, startY - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
            cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)
 
        cv2.imshow("Camera(An phim q de ket thuc !!!)", frame)
        key = cv2.waitKey(1) & 0xFF
 
        if key == ord("q"):
            break
 
    cv2.destroyAllWindows()
    vs.stop()

# if __name__ == "__main__":
# 	run_camera()
# 	print("Ket thuc!!!")
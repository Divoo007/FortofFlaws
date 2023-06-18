import cv2
import keras
from keras.models import load_model
from dict import labels_dict, arr
from read import readimg

model = keras.models.load_model("asl_classifier.h5")
source=cv2.VideoCapture(0)

readimg(source, arr, labels_dict, model)
import cv2
from keras.models import load_model
#from keras.preprocessing.image import load_img, img_to_array
import keras.preprocessing.image
import numpy as np
import tensorflow as tf
from texttospeech import texttospeech
import keras

def readimg(source, arr, labels_dict, model):
    while(True):
        ret,img=source.read()
        cv2.rectangle(img,(25,25),(250 , 250),arr[4],2)
        grayscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cropped=grayscale[25:250,25:250]
        arr[0] = arr[0] + 1
        if(arr[0] % 100 == 0):
            arr[3] = arr[0]
        cv2.putText(img, str(int(arr[3]/100)), (600, 300),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1.5,(255,255,255),2) 
        gausblur = cv2.GaussianBlur(cropped,(5,5),2)
        thres = cv2.adaptiveThreshold(gausblur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
        ret, res = cv2.threshold(thres, arr[6], 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        resized=cv2.resize(res,(arr[5],arr[5]))
        normalized=resized/255.0
        reshaped=np.reshape(normalized,(1,arr[5],arr[5],1))
        predicted = model.predict(reshaped)
        label=np.argmax(predicted,axis=1)[0]
        if(arr[0] == 300):
            arr[0] = 99
            arr[2]= labels_dict[label] 
            if(label == 0):
                arr[1] = arr[1] + " "
            else:
                arr[1] = arr[1] + arr[2]
        cv2.imshow('Video Feed',img)
        cv2.imshow("Converted Image",res) 
        key=cv2.waitKey(1)
        if(key==27):
            texttospeech(arr[1])
            print(arr[1])   
            break     
    cv2.destroyAllWindows()
    source.release()
    cv2.destroyAllWindows()
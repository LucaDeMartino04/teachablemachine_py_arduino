import cvzone
import cv2
import serial

arduino = serial.Serial("COM6", 9600, timeout=0.1) # write COM
cap = cv2.VideoCapture(0)
myClassifier = cvzone.Classifier('MyModel/keras_model.h5','MyModel/labels.txt')

while True:
    _, img = cap.read()
    predictions = myClassifier.getPrediction(img)
    list, num = predictions #divide predictions in two groups

    if (num == 0):
        arduino.write(b'a')
    if (num == 1):
        arduino.write(b'l')

    cv2.imshow("Image", img)
    cv2.waitKey(1)




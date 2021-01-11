# -*- coding: utf-8 -*-

"""
@File    : face.py
@Author  : juliali2000@163.com
@Time    : 2021/1/9 9:57
"""

import cv2

# 分类器下载地址 https://github.com/opencv/opencv/tree/master/data/haarcascades
# 使用OpenCV输入人脸识别分类器的位置
face_cascade = cv2.CascadeClassifier("C://Program Files//Python38//Lib//opencv-master//data//haarcascades//haarcascade_frontalface_default.xml")

#输入待识别的图片
img = cv2.imread("C://Users//Apple//Desktop//face.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 1)
# faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=0, minSize=(32, 32))
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('Julia',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


>>> import numpy as np
>>> import cv2
>>> img = cv2.imread(r"C:\Users\edgar\OneDrive\Documentos\GitHub\Vision-Artificial-2025\Practicas-vison-2025\002_P3_IMAGE_OPERATIOS\watch.jpg")
>>> img[55,55] = [255,255,255]
>>> px = img[55,55]
>>> img[100:150,100:150] = [255,255,255]
>>> watch_face = img[37:111,107:194]
>>> img[0:74,0:87] = watch_face
>>>
>>> cv2.imshow('image',img)
>>> cv2.waitKey(0)

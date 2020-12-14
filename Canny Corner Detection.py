import cv2 
import numpy as np 
  
 
image = cv2.imread('hey.jpg') 
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 
 
lower = np.array([30,150,50]) 
upper = np.array([255,255,180]) 
      
 
mask = cv2.inRange(hsv, lower, upper) 

res = cv2.bitwise_and(hsv,hsv, mask= mask) 

edges = cv2.Canny(hsv,100,200) 
  
    
cv2.imshow('Edges',edges) 
  

cv2.waitKey(0)
cv2.destroyAllWindows() 

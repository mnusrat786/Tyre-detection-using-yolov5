




import os
import cv2

arr = os.listdir("folder11/")
#for loop
#aaaa
for aa in arr:
    aaa = aa.split('.')[0]
    img = cv2.imread(f"folder11/{aa}")
    ress = cv2.resize(img,(640,640))
    cv2.imwrite(f"folder3/{aaa}.png",ress) 

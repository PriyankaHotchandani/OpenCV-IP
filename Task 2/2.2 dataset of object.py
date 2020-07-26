import cv2
import numpy as np

cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    cv2.imshow('window',frame)
    count = count + 1
    cv2.imwrite('img_'+str(count)+'.jpg', frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()    
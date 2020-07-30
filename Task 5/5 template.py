import cv2
import numpy as np

cap = cv2.VideoCapture(0)

points = []
cropping = False
roi = np.zeros((), np.uint8)

def drag_crop(event,x,y,flags,params):
    global points, cropped, roi
    if event == cv2.EVENT_LBUTTONDOWN:
        points = [(y,x)]
        cropping = True

    elif event == cv2.EVENT_LBUTTONUP:
        points.append((y,x))
        cropping = False

        if len(points) == 2:
            roi = frame[points[0][1]:points[1][1], points[0][0]:points[1][0]]
            cv2.imshow("Crop",roi)


cv2.namedWindow('Frame')
cv2.setMouseCallback("Frame",drag_crop)


while True:
    ret,frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if len(points)==2:
        cv2.imshow("Crop",roi)
        template = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        w, h = template.shape[::-1]
        
        res = cv2.matchTemplate(frame_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8

        loc = np.where(res>=threshold)
        for (x,y) in zip(*loc[::-1]):
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
            cv2.putText(frame, "Object", (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, (0,205,0), 2)   

    if not cropping:
        cv2.imshow('Frame',frame)
    elif cropping:
        cv2.rectangle(frame, points[0], points[1], (0,0,0), 1)
        cv2.imshow('Frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows
cap.release
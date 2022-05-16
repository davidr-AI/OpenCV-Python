import cv2
import numpy as np
from pyzbar.pyzbar import decode

# img = cv2.imread("resources/1.png")

# using webcam to capture the code
cap = cv2.VideoCapture(0)
# set the width and height

cap.set(3, 640)
cap.set(4, 480)

while True:

    success, img = cap.read()
    # Creating a Loop
    for barCode in decode(img):
        # decode since barcode.data is in bytes
        # converting into string
        myData = barCode.data.decode('utf-8')
        # print(barcode.rect) ==shows the size of the barcode
        print(myData)
        # adding the bounding bx
        pts = np.array([barCode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))

        cv2.polylines(img, [pts], True, (0, 0, 255), 5)
        pts2 = barCode.rect
        # Put the text
        cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_PLAIN,
                    2, (255, 0, 0), 3)

    cv2.imshow('Result', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

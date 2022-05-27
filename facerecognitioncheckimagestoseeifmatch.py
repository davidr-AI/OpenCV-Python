import cv2
import numpy as np
import face_recognition

# loading images and convert to RGB..
# we getting image in BGR but library understand RGB

imgVince = face_recognition.load_image_file("images/carter.jpg")
imgVince = cv2.cvtColor(imgVince, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file("images/carter.png")
imgTest = cv2.resize(imgTest, (500, 500), None, 0.2, 0.2)
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGRA2RGB)

# find faces in our image and then finding the encoding
# single image so we put 0 to get first element
faceLoc = face_recognition.face_locations(imgVince)[0]
print(faceLoc)
encodeVince = face_recognition.face_encodings(imgVince)[0]

# to see where we have detected the faces

cv2.rectangle(imgVince, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (0, 0, 0), 2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
print(faceLocTest)
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (0, 0, 0), 2)

result = face_recognition.compare_faces([encodeVince], encodeTest)
print(result)
faceDis = face_recognition.face_distance([encodeVince], encodeTest)
print(faceDis)
# show the result
cv2.putText(imgTest, f'{result} {round(faceDis[0], 2)}', (170, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
cv2.imshow("img1", imgVince)

cv2.imshow("img2", imgTest)
cv2.waitKey(0)

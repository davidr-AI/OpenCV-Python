import cv2
import numpy as np
import os

path = "ImagesQuery"
orb = cv2.ORB_create(nfeatures=1000)

# importing images
# Creating a list
images = []
classNames = []

# find the list of names that we have in our path which is in ImagesQuery
myList = os.listdir(path)
print(myList)
print("Total Classes Detected:", len(myList))

# Running a loop to import our images
for cl in myList:
    # importing in gray scale so we will have 0
    imgCur = cv2.imread(f'{path}/{cl}', 0)
    # append current image
    images.append(imgCur)
    # append names and storing the names of the file without extension
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


# find all descriptors of our given image
# create a function that will take the list of images and one by one
# it will create descriptors and create a new list

def findDes(images):
    deslist = []
    # loop through all the images
    for img in images:
        # find the keypoint and descriptors
        # using ORB........
        kp, des = orb.detectAndCompute(img, None)
        deslist.append(des)
    return deslist


def findId(img, deslist, thres=15):
    kp2, des2 = orb.detectAndCompute(img, None)
    bf = cv2.BFMatcher()
    matchList = []
    finalVal = -1
    try:
        for des in deslist:
            matches = bf.knnMatch(des, des2, k=2)
            good = []
            for m, n in matches:
                if m.distance < 0.75 * n.distance:
                    good.append([m])
            matchList.append(len(good))
    except:
        pass

    # print(matchList)

    # check if it's empty list or not
    if len(matchList) != 0:
        if max(matchList) > thres:
            finalVal = matchList.index(max(matchList))
    return finalVal


# calling the above function
deslist = findDes(images)
print(len(deslist))

# getting the camera
cap = cv2.VideoCapture(0)

while True:
    success, img2 = cap.read()
    # first copy then..
    imgOriginal = img2.copy()
    # converting to grayscale
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGRA2GRAY)
    id = findId(img2, deslist)
    if id != -1:
        cv2.putText(imgOriginal, classNames[id], (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

    cv2.imshow('img2', imgOriginal)
    cv2.waitKey(1)

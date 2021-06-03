import os
import cv2 as cv
import numpy as np
from PIL import Image

recognizer = cv.face.LBPHFaceRecognizer_create()

datasetFolderPath = 'src/Dataset'
recognizerFolderPath = 'src/Recognizer'


def getImageFileList(directory):

    imgPathList = [os.path.join(directory, f) for f in os.listdir(directory)]

    faceNPs = []
    IDs = []

    for imgPath in imgPathList:

        faceImg = Image.open(imgPath).convert('L')

        faceNP = np.array(faceImg, 'uint8')

        faceNPs.append(faceNP)

        ID = int(os.path.split(imgPath)[-1].split('_')[0])

        IDs.append(ID)

        cv.imshow('Training in progress...', faceNP)
        cv.waitKey(10)

    print('Training completed!')
    return faceNPs, IDs


def train():
    faces, ids = getImageFileList(datasetFolderPath)

    recognizer.train(faces, np.array(ids))

    if not os.path.exists(recognizerFolderPath):
        os.mkdir(recognizerFolderPath)

    recognizer.save(f'{recognizerFolderPath}/Training Data.yml')


train()

cv.destroyAllWindows()

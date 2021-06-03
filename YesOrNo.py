import cv2 as cv
import time

openPalmDetector = cv.CascadeClassifier('src\Cascade\palm.xml')
cap = cv.VideoCapture(0, cv.CAP_DSHOW)


def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)


change_res(1280, 720)


def stopModule():
    cap.release()
    cv.destroyAllWindows()


def getChoice():

    checkCounter = 0
    choice = {'Yes': 0, 'No': 0}

    while(True):

        _, img = cap.read()
        img = cv.flip(img, 1)

        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        OpenPalm = openPalmDetector.detectMultiScale(gray, 1.3, 5)

        for x, y, w, h in OpenPalm:
            cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # if checkCounter >= 3:
            #     stopModule()
            #     return max(choice, key=choice.get)

            if x > 640:
                stopModule()
                return 'No'
                # choice['No'] +=1
            else:
                stopModule()
                return 'Yes'
                # choice['Yes'] += 1

            # checkCounter += 1

        # cv.imshow("Yes Or No?", img)
        cv.waitKey(3)


def test():
    choice = getChoice()
    print(choice)

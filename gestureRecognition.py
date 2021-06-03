import cv2 as cv
import time
import pyautogui

openPalmDetector = cv.CascadeClassifier('src\Cascade\palm.xml')
closedPalmDetector = cv.CascadeClassifier('src\Cascade\closed_palm.xml')
doneDetector = cv.CascadeClassifier('src\Cascade\\thumb.xml')

cap = cv.VideoCapture(0, cv.CAP_DSHOW)


def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)


change_res(1280, 720)

fontface = cv.FONT_HERSHEY_SIMPLEX
fontscale = 1.5
fontcolor = (0, 0, 0)
fontsize = 14

firstPalmDetected = False
secondPalmDetected = False
counter = 0
checkIfDone = 0
checkIfCancel = 0


def reset():
    return False, False, 0, 0, 0


initialTime = time.time()
clicked = False

while(True):

    if firstPalmDetected:
        if time.time() - initialTime > 5:
            initialTime = time.time()
            firstPalmDetected, secondPalmDetected, counter, checkIfDone, checkIfCancel = reset()

    _, img = cap.read()
    img = cv.flip(img, 1)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    OpenPalm = openPalmDetector.detectMultiScale(gray, 1.3, 5)
    checkCancel = closedPalmDetector.detectMultiScale(gray, 1.3, 5)

    if str(checkCancel) != '()':
        checkIfCancel += 1
        # print(checkIfCancel)
        if checkIfCancel >= 3:
            for x, y, w, h in checkCancel:
                if x >= 850 and y >= 300:
                    pyautogui.click(1157, 883)
                    print('click')
                    clicked = True
                elif x <= 420 and y >= 300:
                    pyautogui.click(830, 888)
                    print('click')
                    clicked = True
            if clicked:
                time.sleep(2)
                break

    if secondPalmDetected:
        counter += 1
        if counter >= 15:
            secondPalmDetected = False
            counter = 0

    for x, y, w, h in OpenPalm:
        cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv.putText(img, "Open Palm", (50, 50), fontface,
                   fontscale, fontcolor, thickness=2)
        cv.putText(img, f'({x},{y})', (50, 500), fontface,
                   fontscale, fontcolor, thickness=2)

        if not firstPalmDetected and not secondPalmDetected:
            sx = x
            sy = y
            sw = w
            sh = h
            firstPalmDetected = True
            print('Detected First Palm')
        else:
            if not secondPalmDetected:
                if (sx - x) > 400:
                    # Command here
                    print("See right")
                    pyautogui.keyDown('ctrl')
                    pyautogui.click(pyautogui.size()[
                                    0]//2, pyautogui.size()[1]//2)
                    pyautogui.keyUp('ctrl')

                    cv.putText(img, 'See right', (50, 250), fontface,
                               fontscale, fontcolor, thickness=2)
                    secondPalmDetected = True
                    firstPalmDetected = False
                    recheckIfDone = 0

                elif (sx - x) < -400:
                    # Command here
                    print("See left")
                    pyautogui.keyDown('shift')
                    pyautogui.click(pyautogui.size()[
                                    0]//2, pyautogui.size()[1]//2)
                    pyautogui.keyUp('shift')

                    cv.putText(img, 'See left', (50, 250), fontface,
                               fontscale, fontcolor, thickness=2)
                    secondPalmDetected = True
                    firstPalmDetected = False
                    recheckIfDone = 0

                # Select
                else:
                    if ((w * h) / (sw * sh)) > 2:
                        print('Select')
                        pyautogui.click(pyautogui.size()[
                                        0]//2, pyautogui.size()[1]//2)

                        cv.putText(img, 'Select', (50, 250), fontface,
                                   fontscale, fontcolor, thickness=2)
                        secondPalmDetected = True
                        firstPalmDetected = False
                        recheckIfDone = 0

        # cv.waitKey(500)

    # for x, y, w, h in closedPalm:
    #     # cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
    #     cv.putText(img, "Closed Palm", (50, 50), fontface, fontscale, fontcolor, thickness=2)
    #     # cv.putText(img, f'({x},{y})', (50, 500), fontface, fontscale, fontcolor, thickness=2)

    # cv.imshow("Hand Detector", img)

    if (cv.waitKey(5) == ord('q')):
        break

cap.release()
cv.destroyAllWindows()

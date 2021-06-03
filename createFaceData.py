import cv2 as cv
import os
import sqlite3

faceDetector = cv.CascadeClassifier('src/Cascade/frontal_face.xml')

cameraman = cv.VideoCapture(0, cv.CAP_DSHOW)

def INSERT_OR_UPDATE_DATA(userID, username):
    try:
        connection = sqlite3.connect('src/User Database.db')
    except:
        print('Please create a database first using SQLite Studio or DB Browser for SQLite')
        quit()
    
    USER_ID = str(userID)
    USER_NAME = str(username)

    sql = f'SELECT * FROM User WHERE ID = {USER_ID}'

    selection = connection.execute(sql)

    recordExist = False

    for row in selection:
        recordExist = True
    if recordExist:
        sql = f'UPDATE User SET Name = {USER_NAME} WHERE ID = {USER_ID}'
    else:
        sql = f'INSERT INTO User(ID, Name) Values({USER_ID},{USER_NAME})'
    
    connection.execute(sql)
    connection.commit()
    connection.close()

while(True):
    try:
        userID = input('Enter your id in digit: ')
        break
    except:
        print('Please enter id in digit only!\n')

datasetFolderPath = 'src/Dataset'

totalImageNumber = 50

imageNumber = 0

if not os.path.exists(datasetFolderPath):
    print('Dataset folder not found, creating dataset folder...')
    os.mkdir(datasetFolderPath)
    print('Dataset folder created successfully.')

while(True):

    _, img = cameraman.read()

    img = cv.flip(img, 1)

    if imageNumber == totalImageNumber:
        break

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    face = faceDetector.detectMultiScale(gray, 1.3, 5)

    for x, y, w, h in face:
        imageNumber += 1
        cv.imwrite(f"{datasetFolderPath}/{userID}_{imageNumber}.jpg", gray[y:y+h, x:x+w])
        cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        cv.waitKey(100)

    cv.imshow("Creating Face ID", img)
    cv.waitKey(5)

print('Your face ID data is created. We will process it and recognize you soon.')

"""IMPORTANT"""
cameraman.release()
cv.destroyAllWindows()

import cv2 as cv
import numpy as np
import sqlite3

faceDetector = cv.CascadeClassifier('src/Cascade/frontal_face.xml')
cameraman = cv.VideoCapture(0, cv.CAP_DSHOW)
recognizer = cv.face.LBPHFaceRecognizer_create()

recognizer.read('src/Recognizer/Training Data.yml')

def getProfileInfo(userID):
    connection = sqlite3.connect('src/User Database.db')
    sql = f'SELECT * FROM User WHERE ID = {userID}'
    selection = connection.execute(sql)
    
    profile = None

    for row in selection:
        profile = row
    connection.close()
    return profile

fontface = cv.FONT_HERSHEY_SIMPLEX
fontscale = 1.5
fontcolor = (0, 0, 0)
fontsize = 14

def age_gender_prediction(img):

    age_model = cv.dnn.readNetFromCaffe('src/age.prototxt.txt','src/dex_chalearn_iccv2015.caffemodel') #Model structure, weights
    gender_model = cv.dnn.readNetFromCaffe('src/gender.prototxt.txt', 'src/gender.caffemodel')

    #img = cv.imread(path)

    # Need to convert RGB to BGR format to be used in openCV
    img = img[:,:,::-1]

    detector_path = "src/Cascade/frontal_face.xml"
    detector = cv.CascadeClassifier(detector_path)

    faces = detector.detectMultiScale(img, 1.1, 5)

    # Grab the first faces, assuming there's only one face in the image
    if len(faces) > 0:
        x, y, w, h = faces[0]
    else:
        return (-1,-1)

    detected_face = img[int(y):int(y+h), int(x):int(x+w)]

    detected_face = detected_face[:,:,::-1]

    detected_face = cv.resize(detected_face, (224, 224))

    detected_face_blob = cv.dnn.blobFromImage(detected_face)

    # Using age_model and gender_model
    age_model.setInput(detected_face_blob)
    age_result = age_model.forward()

    gender_model.setInput(detected_face_blob)
    gender_result = gender_model.forward()

    # age = 0 for female, 1 for male
    if np.argmax(gender_result[0]) == 0:
        print("woman with probability", gender_result[0])
        gender = 0
    else:
        print("man with probability", gender_result[0])
        gender = 1

    length = len(age_result[0])
    indexes = np.array([i for i in range(0, length)])

    apparent_age = np.sum(age_result[0] * indexes)
    print(apparent_age, "years old")

    return (gender, apparent_age)

def stopRecognizing():
    cameraman.release()
    cv.destroyAllWindows()

def detectFace():
    
    detectedCustomer = False; checkTime = 6; recheckCustomer = checkTime; customerAge = []; customerGender = [] # For stranger / New customer
    existingCustomer = []

    while True:
        _, img = cameraman.read()
        img = cv.flip(img, 1)

        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        face = faceDetector.detectMultiScale(gray, 1.3, 5)

        for x, y, w, h in face:
            
            cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
            
            userID, conf = recognizer.predict(gray[y:y+h,x:x+w])

            """
            SQLite3 get the user information
            """
            profile = getProfileInfo(userID)

            if profile != None and conf < 80:
                # In the cv2 api, images are arrays, so you don't need to convert fromarray
                cv.putText(img, str(profile[1]), (x, y+h), fontface, fontscale, fontcolor, thickness=2)
                cv.putText(img, str(profile[2]), (x, y+h+30), fontface, fontscale, fontcolor, thickness=2)
                cv.putText(img, str(profile[3]), (x, y+h+60), fontface, fontscale, fontcolor, thickness=2)
                
                existingCustomer.append(userID)
                if len(existingCustomer) == 20:
                    highestAccuracyCustomer = max(existingCustomer, key=existingCustomer.count)
                    retrieveProfile = getProfileInfo(highestAccuracyCustomer)
                    stopRecognizing()

                    # Getting the favorite drink
                    connection = sqlite3.connect('src/User Database.db')
                    sql = f'SELECT * FROM User'
                    cursor = connection.execute(sql)
                    allColNames = [desc[0] for desc in cursor.description]
                    connection.close()

                    drinkNameList = allColNames[4:]
                    numberOfPurchase = retrieveProfile[4:]
                    favDrink = drinkNameList[numberOfPurchase.index(max(numberOfPurchase))]

                    return str(retrieveProfile[1]), retrieveProfile[2], retrieveProfile[3], favDrink
                    
            # New Customer / Stranger
            else:
                if recheckCustomer > 0:
                    cv.putText(img, 'Unknown', (x, y+h), fontface, fontscale, fontcolor, thickness=2)
                    cv.putText(img, 'Age: Estimating', (x, y+h+30), fontface, fontscale, fontcolor, thickness=2)
                    cv.putText(img, 'Gender: Detecting', (x, y+h+60), fontface, fontscale, fontcolor, thickness=2)
                
                # Detect age and gender by cropping the image
                crop_img = img[y-100:y+h+100, x-100:x+w+100]
                if not detectedCustomer and recheckCustomer > 0:
                    if recheckCustomer == checkTime:
                        recheckCustomer -= 1
                        continue
                    gender_int, age = age_gender_prediction(crop_img)

                    if gender_int == -1:
                        continue
                    elif gender_int == 0:
                        customerGender.append('F')
                        customerAge.append(int(age))
                    else:
                        customerGender.append('M')
                        customerAge.append(int(age))

                    recheckCustomer -= 1
                
                if recheckCustomer == 0:
                    customerAge.sort()
                    finalCustomerAge = customerAge[(checkTime//2)]
                    finalCustomerGender = max(customerGender, key=customerGender.count)

                    cv.putText(img, 'New Customer', (x, y+h), fontface, fontscale, fontcolor, thickness=2)
                    cv.putText(img, f'Age: {finalCustomerAge}', (x, y+h+30), fontface, fontscale, fontcolor, thickness=2)
                    cv.putText(img, f'Gender: {finalCustomerGender}', (x, y+h+60), fontface, fontscale, fontcolor, thickness=2)
                    stopRecognizing()
                    return 'New Customer', finalCustomerGender, finalCustomerAge, ''

        cv.imshow('Detecting face', img)

        if cv.waitKey(5) == ord('q'):
            stopRecognizing()
            break

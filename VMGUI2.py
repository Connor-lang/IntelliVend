from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
import numpy as np
import pyautogui

drinkFolder = "src/Catalogue/"
sprite = drinkFolder+"sprite.png"
cola = drinkFolder+"coca-cola.png"
coffee = drinkFolder+"coffee.png"
plus = drinkFolder+"plus.png"
americano = drinkFolder+"americano.png"
cappuccino = drinkFolder+"cappuccino.png"
fanta = drinkFolder+"fanta.png"
latte = drinkFolder+"latte.png"
redbull = drinkFolder+"redbull.png"
tea = drinkFolder+"tea.png"

itemPrices =  {
    sprite: 1.50,
    cola: 1.80,
    coffee: 2.00,
    plus: 2.00,
    americano: 3.50,
    cappuccino: 3.00,
    fanta: 1.90,
    latte: 3.50,
    redbull: 2.50,
    tea: 3.00
}

class ClickableLabel(QLabel):
    clicked = pyqtSignal(str)

    def mousePressEvent(self, event):
        self.clicked.emit(self.objectName())

class SmallerClickableLabel(QLabel): 
    clicked = pyqtSignal(str)

    def __init__(self, width, height, path):
        super(SmallerClickableLabel, self).__init__()
        pixmap = QPixmap(path)
        rescaled_Pixmap = pixmap.scaled(width, height, Qt.KeepAspectRatio)
        self.setPixmap(rescaled_Pixmap)
        self.setObjectName(path)

    def mousePressEvent(self, event):
        self.clicked.emit(self.objectName())

class SelectionArea(QWidget):
    totalCostChange = pyqtSignal(float)
    itemAddition = pyqtSignal(str)

    def __init__(self):
        super(SelectionArea, self).__init__()
        self.setFixedSize(640, 620)
        self.label1 = ClickableLabel(self)
        lb1pixmap = QPixmap(sprite)
        self.label1.setPixmap(lb1pixmap)
        self.label1.setObjectName(sprite)
        self.label1.clicked.connect(self.handleLabelClicked)
        self.label1.move(30, 0)
        self.label1Animation = QPropertyAnimation(self.label1, b'pos')
        self.price1 = QLabel('1.50', self)
        self.price1.setFont(QFont('Arial', 20)) 
        self.price1Animation = QPropertyAnimation(self.price1, b'pos')
        self.price1.move(280, 585)

        self.label2 = ClickableLabel(self)
        lb2pixmap = QPixmap(cola)
        self.label2.setPixmap(lb2pixmap)
        self.label2.setObjectName(cola)
        self.label2.clicked.connect(self.handleLabelClicked)
        self.label2.move(-580, 0)
        self.label2Animation = QPropertyAnimation(self.label2, b'pos')
        self.price2 = QLabel('1.50', self)
        self.price2.setFont(QFont('Arial', 20)) 
        self.price2Animation = QPropertyAnimation(self.price2, b'pos')
        self.price2.move(-330, 585)

        self.label3 = ClickableLabel(self)
        lb3pixmap = QPixmap(coffee)
        self.label3.setPixmap(lb3pixmap)
        self.label3.setObjectName(coffee)
        self.label3.clicked.connect(self.handleLabelClicked)
        self.label3.move(640, 0)
        self.label3Animation = QPropertyAnimation(self.label3, b'pos')
        self.price3 = QLabel('1.50', self)
        self.price3.setFont(QFont('Arial', 20)) 
        self.price3Animation = QPropertyAnimation(self.price3, b'pos')
        self.price3.move(890, 585)
    
    def start(self):
        self.label1Animation.setStartValue(self.label1.pos()) 
        self.label1Animation.setEndValue(QPoint(self.label1.x() + 610, 0))
        self.label1Animation.setDuration(500)
        self.label1.move(self.label1.x() + 610, 0)
        self.price1Animation.setStartValue(self.price1.pos())
        self.price1Animation.setEndValue(QPoint(self.price1.x() + 610, 585))
        self.price1.move(self.price1.x() + 610, 0)
        self.price1Animation.setDuration(500)
        
        self.label2Animation.setStartValue(self.label2.pos()) 
        self.label2Animation.setEndValue(QPoint(self.label2.x() + 610, 0))
        self.label2Animation.setDuration(500)
        self.label2.move(self.label2.x() + 610, 0)
        self.price2Animation.setStartValue(self.price2.pos())
        self.price2Animation.setEndValue(QPoint(self.price2.x() + 610, 585))
        self.price2.move(self.price2.x() + 610, 0)
        self.price2Animation.setDuration(500)

        self.label3Animation.setStartValue(self.label3.pos()) 
        self.label3Animation.setEndValue(QPoint(self.label3.x() + 610, 0))
        self.label3Animation.setDuration(500)
        self.label3.move(self.label3.x() + 610, 0)
        self.price3Animation.setStartValue(self.price3.pos())
        self.price3Animation.setEndValue(QPoint(self.price3.x() + 610, 585))
        self.price3.move(self.price3.x() + 610, 0)
        self.price3Animation.setDuration(500)
        
        self.label1Animation.start()
        self.label2Animation.start()
        self.label3Animation.start()
        self.price1Animation.start()
        self.price2Animation.start()
        self.price3Animation.start()

    def reverse(self):
        self.label1Animation.setStartValue(self.label1.pos()) 
        self.label1Animation.setEndValue(QPoint(self.label1.x() - 610, 0))
        self.label1Animation.setDuration(500)
        self.label1.move(self.label1.x() - 610, 0)
        self.price1Animation.setStartValue(self.price1.pos())
        self.price1Animation.setEndValue(QPoint(self.price1.x() - 610, 585))
        self.price1.move(self.price1.x() - 610, 0)
        self.price1Animation.setDuration(500)

        self.label2Animation.setStartValue(self.label2.pos()) 
        self.label2Animation.setEndValue(QPoint(self.label2.x() - 610, 0))
        self.label2Animation.setDuration(500)
        self.label2.move(self.label2.x() - 610, 0)
        self.price2Animation.setStartValue(self.price2.pos())
        self.price2Animation.setEndValue(QPoint(self.price2.x() - 610, 585))
        self.price2.move(self.price2.x() - 610, 0)
        self.price2Animation.setDuration(500)

        self.label3Animation.setStartValue(self.label3.pos()) 
        self.label3Animation.setEndValue(QPoint(self.label3.x() - 610, 0))
        self.label3Animation.setDuration(500)
        self.label3.move(self.label3.x() - 610, 0)
        self.price3Animation.setStartValue(self.price3.pos())
        self.price3Animation.setEndValue(QPoint(self.price3.x() - 610, 585))
        self.price3.move(self.price3.x() - 610, 0)
        self.price3Animation.setDuration(500)

        self.label1Animation.start()
        self.label2Animation.start()
        self.label3Animation.start()
        self.price1Animation.start()
        self.price2Animation.start()
        self.price3Animation.start()

    def handleLabelClicked(self):
        item = self.sender()
        print(item.objectName())
        modifiers = QApplication.keyboardModifiers()
        if modifiers == Qt.ShiftModifier:
            print('ShiftClick')
            self.start()
        elif modifiers == Qt.ControlModifier:
            print('CtrlClick')
            self.reverse()
        else:
            itemPrice = float(itemPrices[item.objectName()])
            self.totalCostChange.emit(itemPrice)
            self.itemAddition.emit(item.objectName())

class FavDrinkYesNoWindows(QWidget):
    def __init__(self, username):
        super(FavDrinkYesNoWindows, self).__init__()

        if username == 'New Customer':
            recommendation = QLabel(f"Welcome {username}! Do you want this recommendation?")
        else:
            recommendation = QLabel(f"Welcome {username}! Do you want your usual?")

        recommendation.setFont(QFont('Arial', 20)) 
        recommendation.setAlignment(Qt.AlignCenter)

        # if (globalDrinkPath) not in list(itemPrices.keys()):
        #     import random
        #     globalDrinkPath = random.choice(list(itemPrices.keys()))

        drink = QPushButton()
        drink.setIcon(QIcon(globalDrinkPath))
        drink.setIconSize(QSize(300, 400))

        yesButton = QPushButton()
        yesButton.setIcon(QIcon('src/Catalogue/tick.png'))
        yesButton.setIconSize(QSize(300, 300))
        yesButton.clicked.connect(self.yes)

        noButton = QPushButton()
        noButton.setIcon(QIcon('src/Catalogue/cross.png'))
        noButton.setIconSize(QSize(300, 300))
        noButton.clicked.connect(self.no)
        
        hbox = QHBoxLayout()
        hbox.addWidget(recommendation)
        hbox.setSpacing(0)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(drink)
        hbox1.setSpacing(0)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(yesButton)
        hbox2.addWidget(noButton)

        a = QVBoxLayout()
        a.addLayout(hbox)
        a.addLayout(hbox1)
        a.addLayout(hbox2)
        self.setLayout(a)

    def yes(self):
        print('test', globalDrinkPath)
        print('yes')
        # bug bug bug bug bug bug bug bug bug bug bug bug bug bug bug bug bug bug
        aniWindow.transactionDisplay(value=itemPrices[globalDrinkPath])
        aniWindow.addBlock(globalDrinkPath)
        self.close()
    
    def no(self):
        print('no')
        self.close()

class AniWindow(QWidget):
    def __init__(self):
        super(AniWindow, self).__init__()
        self.totalCost = 0.00
        okButton = QPushButton()
        # okButton.setFont(QFont('Times', 10))
        okButton.setIcon(QIcon('src/Catalogue/tick.png'))
        okButton.setIconSize(QSize(200, 200))
        okButton.clicked.connect(self.onPurchase)
        self.dialog = PurchaseWindow(self)

        cancelButton = QPushButton()
        # cancelButton.setFont(QFont('Times', 10))
        cancelButton.setIcon(QIcon('src/Catalogue/cross.png'))
        cancelButton.setIconSize(QSize(200, 200))
        cancelButton.clicked.connect(lambda:self.close())
        hbox = QHBoxLayout()
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton) 
        
        self.dialogPurchaseWindow = PurchaseWindow(self)

        yourCart = QLabel("YOUR CART")
        yourCart.setStyleSheet("background-color: black; color: white")
        yourCart.setAlignment(Qt.AlignLeft)
        self.totalCostDisplay = QLabel("RM {:.2f}".format(self.totalCost))
        self.totalCostDisplay.setAlignment(Qt.AlignRight)
        self.totalCostDisplay.setStyleSheet("background-color: black; color: white")
        hbox2 = QHBoxLayout() 
        hbox2.setSpacing(0)
        hbox2.addWidget(yourCart)
        hbox2.addWidget(self.totalCostDisplay)

        filler = QLabel()
        self.itemCart = QHBoxLayout()
        self.itemCart.setContentsMargins(0, 0, 0, 0)
        self.itemCart.setSpacing(0)
        self.itemCart.addStretch(0)
        self.itemCart.addWidget(filler)

        layout = QVBoxLayout()
        self.setLayout(layout)
        self.selectionArea = SelectionArea()
        layout.addWidget(self.selectionArea)
        layout.addLayout(hbox2)
        layout.addLayout(self.itemCart)
        layout.addLayout(hbox)
        self.setLayout(layout)

        self.selectionArea.totalCostChange.connect(self.transactionDisplay)
        self.selectionArea.itemAddition.connect(self.addBlock)

    def onPurchase(self): 
        widget = PurchaseWindow()
        widget.exec_()

    def transactionDisplay(self, value):
        self.totalCost += value
        self.totalCostDisplay.setText("RM {:.2f}".format(self.totalCost))

    def addBlock(self, path): 
        self.newBlock = SmallerClickableLabel(50, 50, path)  
        self.newBlock.clicked.connect(self.delete_widget)
        self.itemCart.addWidget(self.newBlock)

    def delete_widget(self):
        item = self.sender()
        item.deleteLater()
        self.itemCart.removeWidget(item)
        itemPrice = float(itemPrices[item.objectName()])
        self.totalCost -= itemPrice
        self.totalCostDisplay.setText("RM {:.2f}".format(self.totalCost))

class PurchaseWindow(QDialog):
    def __init__(self, parent=None): 
        super(PurchaseWindow, self).__init__(parent)
        self.setStyleSheet("background-color: white")
        self.setGeometry(750, 200, 500, 700)
        pVBox = QVBoxLayout()
        # pvaButton = QPushButton("\nPay via App\n")
        # pvaButton.setFont(QFont('Times', 50))
        pcButton = QPushButton("\nThank you!\n")
        pcButton.setFont(QFont('Times', 50))
        # pVBox.addWidget(pvaButton)
        pVBox.addWidget(pcButton)
        # pvaButton.clicked.connect(self.onPayViaApp)
        pcButton.clicked.connect(lambda:self.close())
        self.setLayout(pVBox)

    def onPayViaApp(self): 
        widget = VideoCaptureWindow()
        widget.exec_()

class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture(0)
        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)
        # shut down capture system
        cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()

class VideoCaptureWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle("Qt live label demo")
        self.disply_width = 640
        self.display_height = 480
        # create the label that holds the image
        self.image_label = QLabel(self)
        self.image_label.resize(self.disply_width, self.display_height)
        # create a text label
        self.textLabel = QLabel('Webcam')

        # create a vertical box layout and add the two labels
        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)
        vbox.addWidget(self.textLabel)
        # set the vbox layout as the widgets layout
        self.setLayout(vbox)

        # create the video capture thread
        self.thread = VideoThread()
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        self.thread.start()

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)
    
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

globalDrinkPath = ''

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    aniWindow = AniWindow()

    # Resizing Ref: https://www.youtube.com/watch?v=_xbi5uvjcYs
    aniWindow.resize(600,900)
    aniWindow.show()

    ### Integration
    import recognizingFace as recognizer
    name, gender, age, favDrink = recognizer.detectFace()

    favDrink = favDrink.replace(' ', '').replace('100', '')

    print(favDrink)

    if favDrink != '':
        globalDrinkPath = 'src/Catalogue/'+favDrink.lower()+'.png'

    print(globalDrinkPath)

    if gender == 'M' or gender == 'Male':
        gender = 0
    else:
        gender = 1

    if name != 'New Customer':

        '''
        A window pop out with 2 button yes or no
        '''
        FavDrinkYesNoWindows = FavDrinkYesNoWindows(username=name)
        FavDrinkYesNoWindows.move(650,100)
        FavDrinkYesNoWindows.show()

        import YesOrNo
        choice = YesOrNo.getChoice()
        
        # Click left or right
        if choice == 'Yes':
            pyautogui.click(820,770)
        else:
            pyautogui.click(1140, 770)

    else:
        import pickle
        loaded_model = pickle.load(open('src\Logistic_regression_model.pkl','rb'))
        # 0 is male, 1 is female
        favDrink=loaded_model.predict([[gender,age]])[0]

        favDrink = favDrink.replace(' ', '').replace('100', '')

        globalDrinkPath = 'src/Catalogue/'+favDrink.lower()+'.png'
        FavDrinkYesNoWindows = FavDrinkYesNoWindows(username=name)

        FavDrinkYesNoWindows.move(650,100)
        FavDrinkYesNoWindows.show()

        import YesOrNo
        choice = YesOrNo.getChoice()
        
        # Click left or right
        if choice == 'Yes':
            pyautogui.click(820,770)
        else:
            pyautogui.click(1140, 770)

    import gestureRecognition as gestureReg
    gestureReg
    #####

    sys.exit(app.exec_())
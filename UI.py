import sys,PIL, os
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QApplication, QFileDialog, QMainWindow
from PyQt5.QtGui import QPixmap, QImage, QIcon
import cv2
from PIL import Image
from PyQt5.QtWidgets import QApplication
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2

# Welcome Screen
class WelcomeScreen(QMainWindow):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi(os.path.join("UIFiles","home.ui"),self)
        self.predict_button.clicked.connect(self.gotopredict_button) 
        
    def gotopredict_button(self):
        plot_window = MainWindow()
        widget.addWidget(plot_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.VBL = QVBoxLayout()

        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)

        self.CancelBTN = QPushButton("Cancel")
        self.CancelBTN.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.CancelBTN)

        self.Worker1 = Worker1()

        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)

    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def CancelFeed(self):
        self.Worker1.stop()

class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
	
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
		
		
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(1200, 800, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.quit()
		
# class MainWindow(QWidget):
#     def __init__(self):
#         super(MainWindow, self).__init__()

#         self.VBL = QVBoxLayout()

#         self.FeedLabel = QLabel()
#         self.VBL.addWidget(self.FeedLabel)

#         self.CancelBTN = QPushButton("Cancel")
#         self.CancelBTN.clicked.connect(self.CancelFeed)
#         self.VBL.addWidget(self.CancelBTN)

#         self.Worker1 = Worker1()

#         self.Worker1.start()
#         self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
#         self.setLayout(self.VBL)

#     def ImageUpdateSlot(self, Image):
#         self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

#     def CancelFeed(self):
#         self.Worker1.stop()

# class Worker1(QThread):
#     ImageUpdate = pyqtSignal(QImage)
#     def run(self):
#         self.ThreadActive = True
#         Capture = cv2.VideoCapture(0)
#         while self.ThreadActive:
#             ret, frame = Capture.read()
#             if ret:
#                 Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#                 FlippedImage = cv2.flip(Image, 1)
#                 ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
#                 Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
#                 self.ImageUpdate.emit(Pic)
#     def stop(self):
#         self.ThreadActive = False
#         self.quit()

# if __name__ == "__main__":
#     App = QApplication(sys.argv)
#     Root = MainWindow()
#     Root.show()
#     sys.exit(App.exec())

# class Createtwodimensionplotting(QMainWindow):
#     def __init__(self):
#         super(Createtwodimensionplotting, self).__init__()
#         loadUi(os.path.join("UIFiles","tracking2.ui"),self)

#         self.path = ''
#         self.folderselect.clicked.connect(self.open_dialog_box)
#         self.dimselector.clicked.connect(self.go_to_error)
#         self.cancel_trackingtwo.clicked.connect(self.go_to_backhome)
    
#     def go_to_backhome(self):
#         back_to_home1 = WelcomeScreen()
#         widget.addWidget(back_to_home1)
#         widget.setCurrentIndex(widget.currentIndex() + 1)

#     def open_dialog_box(self):
#         filename = QFileDialog.getOpenFileName()

#         self.path = filename[0]
#         pathto = filename[0]

#         if len(pathto) > 1:
#             self.pathlabel.setText(pathto)

#     def go_to_error(self):
#         if self.path == '':
#             self.error.setText("Please Select the Path to Video")
        
#         elif self.path[-3:] not in ['avi', 'mp4']:
#             self.error.setText('Select Appropriate File Format')
            
#         else:
#             self.error.setText('')
#             cam = cv2.VideoCapture(self.path)
#             while(True):
#                 ret,frame = cam.read()
  
#                 if ret:
#                     # if video is still left continue creating images
#                     path_to_img_file = './Temporary Files/' + str(self.path.split('/')[-1][:-4]) + '.jpg'
            
#                     cv2.imwrite(path_to_img_file, frame)
#                     break
#                 break

#             popup_window =  createpopupforimage(path_to_img_file,self.path)
#             widget.addWidget(popup_window)
#             widget.setCurrentIndex(widget.currentIndex() + 1)

# class createpopupforimage(QMainWindow):
#     def __init__(self,path_to_img_file,path):
#         super(createpopupforimage, self).__init__()
#         loadUi(os.path.join("UIFiles","dimensionselect.ui"), self)
#         cropping = False
#         self.path_to_img_file = path_to_img_file
#         self.vidpath=path

#         img = Image.open(path_to_img_file)
#         img=img.resize((720, 480), PIL.Image.ANTIALIAS)
#         file_cropped_save_name = path_to_img_file[:-4]+'resized_image.jpg'
#         img.save(file_cropped_save_name)

#         self.image = cv2.imread(file_cropped_save_name)
#         oriImage =self.image.copy()
#         self.oriImage2 =self.image.copy()

#         x_start, y_start, x_end, y_end = 0, 0, 0, 0
#         def mouse_crop(event, x, y, flags, param):
#             global x_start, y_start, x_end, y_end, cropping

#             if event == cv2.EVENT_LBUTTONDOWN:
#                 x_start, y_start, x_end, y_end = x, y, x, y
#                 cropping = True

#             elif event == cv2.EVENT_MOUSEMOVE:
#                 try:
#                     if cropping == True:
#                         x_end, y_end = x, y
#                 except:
#                     pass

#             elif event == cv2.EVENT_LBUTTONUP:
                
#                 x_end, y_end = x, y
#                 cropping = False  

#                 refPoint = [(x_start, y_start), (x_end, y_end)]
#                 print(refPoint)
#                 if len(refPoint) == 2:  
#                     self.roi = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0],:]
#                     cv2.cvtColor(self.roi, cv2.COLOR_BGR2RGB, self.roi)
#                     self.roi=cv2.resize(self.roi, (720,480), interpolation = cv2.INTER_AREA)
                    
#                     self.roi = QImage(self.roi.data.tobytes(), self.roi.shape[1],self.roi.shape[0],QImage.Format_RGB888)
#                     self.image_project_label.setPixmap(QPixmap.fromImage(self.roi))
#                     self.image_project_label.setScaledContents(True)
#                     self.retrybuttondim.clicked.connect(self.crop_again)
#                     self.dimcancel.clicked.connect(self.go_back_to_2D)
#                     self.dimok.clicked.connect(self.goto2DPredicting)
#                     cv2.destroyAllWindows()
                    
                    
#         cv2.namedWindow("image")
#         cv2.setMouseCallback("image", mouse_crop)
        
#         while True:
#             self.i = self.image.copy()

#             if not cropping:
#                 cv2.imshow("image", self.image)
                

#             elif cropping:
#                 cv2.rectangle(self.i, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)
#                 cv2.imshow("image", self.i)
#             break


#     def crop_again(self):
#         x_start, y_start, x_end, y_end = 0, 0, 0, 0
#         def mouse_crop(event, x, y, flags, param):
#             global x_start, y_start, x_end, y_end, cropping

#             if event == cv2.EVENT_LBUTTONDOWN:
#                 x_start, y_start, x_end, y_end = x, y, x, y
#                 cropping = True

#             elif event == cv2.EVENT_MOUSEMOVE:
#                 try:
#                     if cropping == True:
#                         x_end, y_end = x, y
#                 except:
#                     pass

#             elif event == cv2.EVENT_LBUTTONUP:
                
#                 x_end, y_end = x, y
#                 cropping = False  

#                 refPoint = [(x_start, y_start), (x_end, y_end)]
#                 print(refPoint)
#                 if len(refPoint) == 2:  
#                     self.roi = self.oriImage2[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0],:]
                    
#                     cv2.cvtColor(self.roi, cv2.COLOR_BGR2RGB, self.roi)
#                     self.roi=cv2.resize(self.roi, (720,480), interpolation = cv2.INTER_AREA)
                    
#                     self.roi = QImage(self.roi.data.tobytes(), self.roi.shape[1],self.roi.shape[0],QImage.Format_RGB888)
#                     self.image_project_label.setPixmap(QPixmap.fromImage(self.roi))
#                     self.image_project_label.setScaledContents(True)
                    
#                     cv2.destroyAllWindows()
#                     self.retrybuttondim.clicked.connect(self.crop_again)
#                     self.dimcancel.clicked.connect(self.go_back_to_2D)
#                     self.dimok.clicked.connect(self.goto2DPredicting)
                    
#         cv2.namedWindow("image")
#         cv2.setMouseCallback("image", mouse_crop)
        
#         while True:
#             self.i = self.image.copy()

#             if not cropping:
#                 cv2.imshow("image", self.image)
                
#             elif cropping:
#                 cv2.rectangle(self.i, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)
#                 cv2.imshow("image", self.i)
#             break

pic= """WelcomeScreen
{
	background-image:url(UIFiles/welding_pi.png)
}
"""
app = QApplication(sys.argv)
app.setStyleSheet(pic)
welcome = WelcomeScreen()

widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.setWindowTitle('welding')
widget.setWindowIcon(QIcon(os.path.join('icons','icon.png')))
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")
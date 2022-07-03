import sys
#from typing_extensions import self
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFileDialog, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
import cv2
import numpy as np
from matplotlib import image, pyplot as plt
from os import listdir
from os.path import isfile, join

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(Self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1111, 400)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        Self.centralwidget = QtWidgets.QWidget(MainWindow)
        Self.centralwidget.setObjectName("centralwidget")
        Self.pushButton = QtWidgets.QPushButton(Self.centralwidget)
        Self.pushButton.setGeometry(QtCore.QRect(870, 300, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        Self.pushButton.setFont(font)
        Self.pushButton.setObjectName("pushButton")
        Self.pushButton.clicked.connect(Self.pushButton_handler)
        

        Self.Gambarasli = QtWidgets.QLabel(Self.centralwidget)
        Self.Gambarasli.setGeometry(QtCore.QRect(20, 50, 400, 300))
        Self.Gambarasli.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        Self.Gambarasli.setFont(font)
        Self.Gambarasli.setFrameShape(QtWidgets.QFrame.WinPanel)
        Self.Gambarasli.setFrameShadow(QtWidgets.QFrame.Sunken)
        Self.Gambarasli.setText("")
        Self.Gambarasli.setObjectName("Gambarasli")
        

        

        Self.label_2 = QtWidgets.QLabel(Self.centralwidget)
        Self.label_2.setGeometry(QtCore.QRect(180, 19, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        Self.label_2.setFont(font)
        Self.label_2.setObjectName("label_2")
        

        Self.label_3 = QtWidgets.QLabel(Self.centralwidget)
        Self.label_3.setGeometry(QtCore.QRect(440, 50, 400, 300))
        font = QtGui.QFont()
        font.setPointSize(13)
        Self.label_3.setFont(font)
        Self.label_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        Self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        Self.label_3.setText("")
        Self.label_3.setObjectName("label_3")

        Self.label_4 = QtWidgets.QLabel(Self.centralwidget)
        Self.label_4.setGeometry(QtCore.QRect(630, 19, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        Self.label_4.setFont(font)
        Self.label_4.setObjectName("label_4")

        Self.label_5 = QtWidgets.QLabel(Self.centralwidget)
        Self.label_5.setGeometry(QtCore.QRect(870, 50, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        Self.label_5.setFont(font)
        Self.label_5.setObjectName("label_5")
        Self.label_6 = QtWidgets.QLabel(Self.centralwidget)
        Self.label_6.setGeometry(QtCore.QRect(870, 80, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        Self.label_6.setFont(font)
        Self.label_6.setObjectName("label_6")
        Self.label_7 = QtWidgets.QLabel(Self.centralwidget)
        Self.label_7.setGeometry(QtCore.QRect(870, 110, 55, 16))
        Self.label_7.setObjectName("label_7")
        Self.label_8 = QtWidgets.QLabel(Self.centralwidget)
        Self.label_8.setGeometry(QtCore.QRect(870, 140, 55, 16))
        Self.label_8.setObjectName("label_8")
        Self.label_9 = QtWidgets.QLabel(Self.centralwidget)
        Self.label_9.setGeometry(QtCore.QRect(870, 170, 55, 16))
        Self.label_9.setObjectName("label_9")
        Self.label_10 = QtWidgets.QLabel(Self.centralwidget)
        Self.label_10.setGeometry(QtCore.QRect(870, 200, 55, 16))
    
        font = QtGui.QFont()
        font.setPointSize(10)
        Self.label_10.setFont(font)
        Self.label_10.setLineWidth(1)
        Self.label_10.setObjectName("label_10")
        Self.label_11 = QtWidgets.QLabel(Self.centralwidget)
        Self.label_11.setGeometry(QtCore.QRect(870, 230, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        Self.label_11.setFont(font)
        Self.label_11.setObjectName("label_11")
        Self.lineEdit = QtWidgets.QLineEdit(Self.centralwidget)
        Self.lineEdit.setGeometry(QtCore.QRect(930, 50, 113, 22))
        Self.lineEdit.setObjectName("lineEdit")
        Self.lineEdit_2 = QtWidgets.QLineEdit(Self.centralwidget)
        Self.lineEdit_2.setGeometry(QtCore.QRect(930, 80, 113, 22))
        Self.lineEdit_2.setObjectName("lineEdit_2")
        Self.lineEdit_3 = QtWidgets.QLineEdit(Self.centralwidget)
        Self.lineEdit_3.setGeometry(QtCore.QRect(930, 110, 113, 22))
        Self.lineEdit_3.setObjectName("lineEdit_3")
        Self.lineEdit_4 = QtWidgets.QLineEdit(Self.centralwidget)
        Self.lineEdit_4.setGeometry(QtCore.QRect(930, 140, 113, 22))
        Self.lineEdit_4.setObjectName("lineEdit_4")
        Self.lineEdit_5 = QtWidgets.QLineEdit(Self.centralwidget)
        Self.lineEdit_5.setGeometry(QtCore.QRect(930, 170, 113, 22))
        Self.lineEdit_5.setObjectName("lineEdit_5")
        Self.lineEdit_6 = QtWidgets.QLineEdit(Self.centralwidget)
        Self.lineEdit_6.setGeometry(QtCore.QRect(930, 200, 113, 22))
        Self.lineEdit_6.setObjectName("lineEdit_6")
        Self.lineEdit_7 = QtWidgets.QLineEdit(Self.centralwidget)
        Self.lineEdit_7.setGeometry(QtCore.QRect(930, 230, 113, 22))
        Self.lineEdit_7.setObjectName("lineEdit_7")
        Self.lineEdit_8 = QtWidgets.QLineEdit(Self.centralwidget)
        Self.lineEdit_8.setGeometry(QtCore.QRect(930, 260, 113, 22))
        Self.lineEdit_8.setObjectName("lineEdit_8")
        Self.label = QtWidgets.QLabel(Self.centralwidget)
        Self.label.setGeometry(QtCore.QRect(870, 260, 55, 16))
        Self.label.setObjectName("label")
        MainWindow.setCentralWidget(Self.centralwidget)
        Self.menubar = QtWidgets.QMenuBar(MainWindow)
        Self.menubar.setGeometry(QtCore.QRect(0, 0, 1134, 26))
        Self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(Self.menubar)
        Self.statusbar = QtWidgets.QStatusBar(MainWindow)
        Self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(Self.statusbar)

        Self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(Self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Compare Histogram"))
        Self.pushButton.setText(_translate("MainWindow", "Select Image"))
        Self.label_2.setText(_translate("MainWindow", "Gambar asli"))
        Self.label_4.setText(_translate("MainWindow", "Hasil"))
        Self.label_5.setText(_translate("MainWindow", "20 ML"))
        Self.label_6.setText(_translate("MainWindow", "40 ML"))
        Self.label_7.setText(_translate("MainWindow", "60 ML"))
        Self.label_8.setText(_translate("MainWindow", "80 ML"))
        Self.label_9.setText(_translate("MainWindow", "100 ML"))
        Self.label_10.setText(_translate("MainWindow", "125 ML"))
        Self.label_11.setText(_translate("MainWindow", "-"))
        Self.label.setText(_translate("MainWindow", "ML - CC"))

    def pushButton_handler(Self):
        image = QFileDialog.getOpenFileName(None, 'OpenFile', '...\\Dataset\\Sample\\OK ML', "Image file(*.jpg)") #Pemilihan gambar yang akan di test
        
        imagePath = image[0] #Memasukan path gambar ke variable

        #Variable untuk menjadi checklist deteksi
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0
        g = 0
        i = 0

        img = cv2.imread(imagePath) #Membaca gambar pada Path
        imgOri = cv2.imread(imagePath) #Membaca gambar pada Path
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Memfilter gambar menjadi grayscale

        #Path template yang akan digunakan untuk testing gabar
        mypath1='...\\Dataset\\Template\\20 ML'
        mypath2='...\\Dataset\\Template\\40 ML'
        mypath3='...\\Dataset\\Template\\60 ML'
        mypath4='...\\Dataset\\Template\\80 ML'
        mypath5='...\\Dataset\\Template\\100 ML'
        mypath6='...\\Dataset\\Template\\125 ML'
        mypath7='...\\Dataset\\Template\\-'
        mypath8='...\\Dataset\\Template\\ML - CC'

        #Memasukan gambar pada folder ke variable
        onlyfiles1 = [ f for f in listdir(mypath1) if isfile(join(mypath1,f)) ]
        onlyfiles2 = [ f for f in listdir(mypath2) if isfile(join(mypath2,f)) ]
        onlyfiles3 = [ f for f in listdir(mypath3) if isfile(join(mypath3,f)) ]
        onlyfiles4 = [ f for f in listdir(mypath4) if isfile(join(mypath4,f)) ]
        onlyfiles5 = [ f for f in listdir(mypath5) if isfile(join(mypath5,f)) ]
        onlyfiles6 = [ f for f in listdir(mypath6) if isfile(join(mypath6,f)) ]
        onlyfiles7 = [ f for f in listdir(mypath7) if isfile(join(mypath7,f)) ]
        onlyfiles8 = [ f for f in listdir(mypath8) if isfile(join(mypath8,f)) ]

        compare_method = cv2.HISTCMP_CORREL #Metode compare histogram yang akan digunakan

        def comparation(mypath, onlyfiles, threshold): #Fungsi yang akan digunakan untuk compare histogram
            checked = 0 #Deklarasi Variable checklist
            txt = 0 #Deklarasi Variable text
            template = np.empty(len(onlyfiles), dtype=object) #Deklarasi Variable template
            for n in range(0, len(onlyfiles)): #Untuk semua gambar yang berada pada folder
                template[n] = cv2.imread(join(mypath,onlyfiles[n])) #Membaca gambar n pada folder
                templategray = cv2.cvtColor(template[n], cv2.COLOR_BGR2GRAY) #Memfilter gambar n menjadi grayscale
                w, h = templategray.shape[::-1] #Mengambil panjang dan lebar gambar template
                res = cv2.matchTemplate(img_gray,templategray,cv2.TM_CCOEFF_NORMED) #Template match gambar awal dengan template, template matching menggunakan gambar grayscale
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res) #Mengambil nilai terkecil, nilai terbesar, koordinat nilai terkecil dan koordinat nilai terbesar dari hasil template matching
                cropped_image = (img [max_loc[1]:max_loc[1] + h, max_loc[0]:max_loc[0] + w]) #Cropping gambar pada koordinat dengan nilai template matching tertinggi
                hist1 = cv2.calcHist([template[n]], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256]) #Membuat histogram gambar template
                hist1 = cv2.normalize(hist1, hist1).flatten()
                hist11 = cv2.calcHist([cropped_image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256]) #Membuat histogram dari hasil crop
                hist11 = cv2.normalize(hist11, hist11).flatten()
                comp = cv2.compareHist(hist1, hist11, compare_method) #Membandingkan histogram dari 2 gambar sebelumnya
                txt = comp * 100 #Membuat nilai hasil perbandingan menjadi persen
                txt = round(txt, ndigits=2) #Membulatkan nilai menjadi hanya 2 angka dibelakang koma
                txt = str(txt) #Mengubah nilai dari int menjadi string
                txt = txt + '%' #Menambahkan tanda %
                if comp > threshold : #Jika nilai perbandingan melebihi threshold yang di tentukan
                    cv2.rectangle(img, max_loc, (max_loc[0] + w, max_loc[1] + h), (255,0,0), 2) #Membuat box pada lokasi gambar yang di crop
                    checked = 1 #Membuat tanda bahwa gambar OK
                    break #Program For berhenti
            return checked, txt #Mengembalikan nilai checklist dan nilai template matching        
       
        template7 = np.empty(len(onlyfiles7), dtype=object) #Deklarasi Variable template
        for n in range(0, len(onlyfiles7)): #Untuk semua gambar yang berada pada folder
            template7[n] = cv2.imread(join(mypath7,onlyfiles7[n])) #Membaca gambar n pada folder
            templategray = cv2.cvtColor(template7[n], cv2.COLOR_BGR2GRAY) #Memfilter gambar n menjadi grayscale
            w7, h7 = templategray.shape[::-1] #Mengambil panjang dan lebar gambar template
            res7 = cv2.matchTemplate(img_gray,templategray,cv2.TM_CCOEFF_NORMED) #Template match gambar awal dengan template, template matching menggunakan gambar grayscale
            loc7 = np.where( res7 >= 0.9) #loc7 sama dengan koordinat dimana nilai template matching melebihi nilai threshold yang ditentukan
            for pt in zip(*loc7[::-1]): #Untuk koordinat yang melebihi nilai threshold
                cropped_image7 = (img [pt[1]:pt[1] + h7, pt[0]:pt[0] + w7]) #Cropping gambar pada koordinat dengan nilai template matching melebihi threshold
                hist7 = cv2.calcHist([template7[n]], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256]) #Membuat histogram gambar template
                hist7 = cv2.normalize(hist7, hist7).flatten()
                hist71 = cv2.calcHist([cropped_image7], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256]) #Membuat histogram dari hasil crop
                hist71 = cv2.normalize(hist71, hist71).flatten()
                comp7 = cv2.compareHist(hist7, hist71, compare_method) #Membandingkan histogram dari 2 gambar sebelumnya
                txt7 = comp7 * 100 #Membuat nilai hasil perbandingan menjadi persen
                txt7 = round(txt7, ndigits=2) #Membulatkan nilai menjadi hanya 2 angka dibelakang koma
                txt7 = str(txt7) #Mengubah nilai dari int menjadi string
                txt7 = txt7 + '%' #Menambahkan tanda %
                if comp7 > 0.9 : #Jika nilai perbandingan melebihi threshold yang di tentukan
                    cv2.rectangle(img, pt, (pt[0] + w7, pt[1] + h7), (255,0,0), 2) #Membuat box pada lokasi gambar yang di crop
                    g = g + 1 #Membuat tanda bahwa gambar OK
                    break #Program For berhenti
            
        

        a, txt1 = comparation(mypath1, onlyfiles1, 0.9) #Menjalankan fungsi untuk template 20 ML
        b, txt2= comparation(mypath2, onlyfiles2, 0.9948978878676819) #Menjalankan fungsi untuk template 40 ML
        c, txt3= comparation(mypath3, onlyfiles3, 0.991901728279413) #Menjalankan fungsi untuk template 60 ML
        d, txt4= comparation(mypath4, onlyfiles4, 0.9961605923328304) #Menjalankan fungsi untuk template 80 ML
        e, txt5= comparation(mypath5, onlyfiles5, 0.9946542031203938) #Menjalankan fungsi untuk template 100 ML
        f, txt6= comparation(mypath6, onlyfiles6, 0.990967653832662) #Menjalankan fungsi untuk template 125 ML
        i, txt8= comparation(mypath8, onlyfiles8, 0.998127428399572) #Menjalankan fungsi untuk template ML - CC
        
        if b > 0 and c > 0 and d > 0 and e > 0 and f > 0 and i > 0: #Jika semua hasil bertanda OK
            Self.label_4.setText('BARANG OK') #Merubah label menjadi "Barang OK"
            Self.label_4.adjustSize()  
        else : #Jika ada satu yang tidak bertanda OK
            Self.label_4.setText('BARANG NG') #Merubah label menjadi "Barang NG"
            Self.label_4.adjustSize()

        width = int(400) #Panjang untuk resize gambar
        height = int(300) #Lebar untuk resize gambar
        dim = (width, height) #Memasukan panjang dan lebar ke dalam variable

        resizedImage = cv2.resize(img, dim, interpolation = cv2.INTER_AREA) #Resize gambar hasil compare histogram 
        resizedOri = cv2.resize(imgOri, dim, interpolation = cv2.INTER_AREA) #Resize gambar awal/original
        cv2.imwrite('res.jpg',resizedImage) #Menyimpan hasil resize gambar compare histogram 
        cv2.imwrite('resOri.jpg',resizedOri) #Menyimpan hasil resize gambar awal/original
        pixmap = QPixmap('res.jpg') #Memasukan gambar compare histogram resize ke variable
        pixmapOri = QPixmap('resOri.jpg') #Memasukan gambar awal/original resize ke variable
        Self.Gambarasli.setPixmap(pixmapOri) #Menampilkan gambar awal/original pada GUI
        Self.Gambarasli.adjustSize

        Self.label_3.setPixmap(pixmap) #Menampilkan gambar compare histogram pada GUI
        Self.Gambarasli.adjustSize

        #Menampilkan nilai nilai compare histogram pada GUI
        Self.lineEdit.setText(txt1)
        Self.lineEdit_2.setText(txt2)
        Self.lineEdit_3.setText(txt3)
        Self.lineEdit_4.setText(txt4)
        Self.lineEdit_5.setText(txt5)
        Self.lineEdit_6.setText(txt6)
        Self.lineEdit_7.setText(txt7)
        Self.lineEdit_8.setText(txt8)
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

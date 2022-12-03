from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from Logic import IndianPoker
from PyQt5.QtCore import QSize
import sys
from qt_material import apply_stylesheet

class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.cnt = 0
        self.IP = IndianPoker()
        self.setupUi(MainWindow)
        
    
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(QSize(650, 800)) #크기 조정 못하게 함.
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.GameName = QtWidgets.QLabel(self.centralwidget)
        self.GameName.setGeometry(QtCore.QRect(270, 30, 100, 20))
        font = QtGui.QFont()
        font.setFamily("HY신명조")
        font.setPointSize(10)
        self.GameName.setFont(font)
        self.GameName.setObjectName("GameName")
        
        self.Player1 = QtWidgets.QLabel(self.centralwidget)
        self.Player1.setGeometry(QtCore.QRect(60, 75, 81, 21))
        self.Player1.setFont(font)
        self.Player1.setObjectName("Player1")
        
        self.Result = QtWidgets.QTextBrowser(self.centralwidget)
        self.Result.setGeometry(QtCore.QRect(50, 380, 550, 300))
        self.Result.setFont(font)
        self.Result.setObjectName("Result")
        self.Result.setAlignment(Qt.AlignCenter)
       
        
        self.Player2 = QtWidgets.QLabel(self.centralwidget)
        self.Player2.setFont(font)
        self.Player2.setGeometry(QtCore.QRect(360, 75, 81, 16))
        self.Player2.setObjectName("Player2")
        
        self.Reset = QtWidgets.QPushButton(self.centralwidget)
        self.Reset.setGeometry(QtCore.QRect(140, 700, 90, 30))
        self.Reset.setObjectName("Reset")
        self.Reset.setFont(font)
        self.Reset.clicked.connect(self.buttonClicked)
        
        self.Next = QtWidgets.QPushButton(self.centralwidget)
        self.Next.setGeometry(QtCore.QRect(420, 700, 90, 30))
        self.Next.setObjectName("Next")
        self.Next.setFont(font)
        self.Next.clicked.connect(self.buttonClicked)
        
        self.Card1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Card1.setGeometry(QtCore.QRect(60, 160, 221, 51))
        self.Card1.setObjectName("Card1")
        self.Card1.setFont(font)
        
       
        
        self.Chip1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Chip1.setGeometry(QtCore.QRect(170, 70, 110, 30))
        self.Chip1.setObjectName("Chip1")
        self.Chip1.setFont(font)
        
        
        
        self.Open1 = QtWidgets.QPushButton(self.centralwidget)
        self.Open1.setGeometry(QtCore.QRect(60, 220, 95, 30))
        self.Open1.setObjectName("Open1")
        self.Open1.setFont(font)
        self.Open1.clicked.connect(self.buttonClicked)
        
        self.Betting1 = QtWidgets.QLineEdit(self.centralwidget)
        self.Betting1.setGeometry(QtCore.QRect(60, 260, 90, 90))
        self.Betting1.setObjectName("Betting1") 
        self.Betting1.setFont(font)
        self.Betting1.setAlignment(Qt.AlignCenter)
        
        self.Call1 = QtWidgets.QPushButton(self.centralwidget)
        self.Call1.setGeometry(QtCore.QRect(190, 260, 95, 28))
        self.Call1.setObjectName("Call1")
        self.Call1.setFont(font)
        self.Call1.clicked.connect(self.buttonClicked)
        
        self.Card2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Card2.setGeometry(QtCore.QRect(360, 160, 221, 51))
        self.Card2.setFont(font)
        self.Card2.setObjectName("Card2")
        
        
        self.Open2 = QtWidgets.QPushButton(self.centralwidget)
        self.Open2.setGeometry(QtCore.QRect(360, 220, 95, 30))
        self.Open2.setObjectName("Open2")
        self.Open2.setFont(font)
        self.Open2.clicked.connect(self.buttonClicked)
        
        self.Betting2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Betting2.setGeometry(QtCore.QRect(360, 260, 90, 90))
        self.Betting2.setObjectName("Betting2")
        self.Betting2.setFont(font)
        self.Betting2.setAlignment(Qt.AlignCenter)
        
        self.Raise1 = QtWidgets.QPushButton(self.centralwidget)
        self.Raise1.setGeometry(QtCore.QRect(190, 290, 95, 28))
        self.Raise1.setObjectName("Raise1")
        self.Raise1.setFont(font)
        self.Raise1.clicked.connect(self.buttonClicked)
        
        self.Die1 = QtWidgets.QPushButton(self.centralwidget)
        self.Die1.setGeometry(QtCore.QRect(190, 320, 95, 28))
        self.Die1.setObjectName("Die1")
        self.Die1.setFont(font)
        self.Die1.clicked.connect(self.buttonClicked)
        
        self.Call2 = QtWidgets.QPushButton(self.centralwidget)
        self.Call2.setGeometry(QtCore.QRect(490, 260, 95, 28))
        self.Call2.setObjectName("Call2")
        self.Call2.setFont(font)
        self.Call2.clicked.connect(self.buttonClicked)
        
        self.Raise2 = QtWidgets.QPushButton(self.centralwidget)
        self.Raise2.setGeometry(QtCore.QRect(490, 290, 95, 28))
        self.Raise2.setObjectName("Raise2")
        self.Raise2.setFont(font)
        self.Raise2.clicked.connect(self.buttonClicked)
        
        self.Die2 = QtWidgets.QPushButton(self.centralwidget)
        self.Die2.setGeometry(QtCore.QRect(490, 320, 95, 28))
        self.Die2.setObjectName("Die2")
        self.Die2.setFont(font)
        self.Die2.clicked.connect(self.buttonClicked)
        
        self.Chip2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Chip2.setGeometry(QtCore.QRect(470, 70, 110, 30))
        self.Chip2.setObjectName("Chip2")
        self.Chip2.setFont(font)
        
        
        self.Close1 = QtWidgets.QPushButton(self.centralwidget)
        self.Close1.setGeometry(QtCore.QRect(190, 220, 95, 30))
        self.Close1.setObjectName("Close1")
        self.Close1.setFont(font)
        self.Close1.clicked.connect(self.buttonClicked)
        
        self.Close2 = QtWidgets.QPushButton(self.centralwidget)
        self.Close2.setGeometry(QtCore.QRect(490, 220, 95, 30))
        self.Close2.setObjectName("Close2")
        self.Close2.setFont(font)
        self.Close2.clicked.connect(self.buttonClicked)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Result.setText(self.IP.Bettingresult())
        self.statusUpdate()
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.GameName.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">인디언 포커</span></p></body></html>"))
        self.Player1.setText(_translate("MainWindow", "Player 1"))
        self.Player2.setText(_translate("MainWindow", "Player 2"))
        self.Reset.setText(_translate("MainWindow", "Reset"))
        self.Next.setText(_translate("MainWindow", "Next"))
        self.Open1.setText(_translate("MainWindow", "Open1"))
        self.Call1.setText(_translate("MainWindow", "Call1"))
        self.Open2.setText(_translate("MainWindow", "Open2"))
        self.Raise1.setText(_translate("MainWindow", "Raise1"))
        self.Die1.setText(_translate("MainWindow", "Die1"))
        self.Call2.setText(_translate("MainWindow", "Call2"))
        self.Raise2.setText(_translate("MainWindow", "Raise2"))
        self.Die2.setText(_translate("MainWindow", "Die2"))
        self.Close1.setText(_translate("MainWindow", "Close1"))
        self.Close2.setText(_translate("MainWindow", "Close2"))
        
    def buttonClicked(self):
        try:
            button=self.sender()
            key=button.text()
            if self.IP.status == True: # 게임 중일 떄만 가능하도록 #처음에 call, Die를 누르지 않도록 하기 위해서
                if key=="Call1":
                    if self.cnt != 0:
                        self.IP.Call(1)
                        self.Result.setText(self.IP.roundResult())
                    else:
                        self.Result.setText("처음에는 Raise만 가능합니다.")
                    
                if key=="Call2":
                    if self.cnt != 0:
                        self.IP.Call(2)
                        self.Result.setText(self.IP.roundResult())
                    else:
                        self.Result.setText("처음에는 Raise만 가능합니다.")
                
                if key=="Die1":
                    self.Result.setText(self.IP.P1die())
                    
                        
                if key=="Die2":                
                    self.Result.setText(self.IP.P2die())
                    
                        
                if key=="Raise1":
                    a=self.IP.Raise(1, self.Betting1.text())
                    self.Result.setText("")
                    if a =="low":
                        self.Result.setText("배팅액이 너무 적습니다. 다시 입력하시오.")
                    elif a =="high":
                        self.Result.setText("배팅액이 너무 많습니다. 다시 입력하시오.")
                    elif a == "다시 입력해주세요":
                        self.Result.setText("다시 입력해주세요")
                    else:
                        self.Result.setText(self.IP.Bettingresult())
                        self.cnt += 1
                    self.Betting1.setText("")
                    
                if key=="Raise2":
                    a=self.IP.Raise(2, self.Betting2.text())
                    self.Result.setText("")
                    if a=="low":
                        self.Result.setText("배팅액이 너무 적습니다. 다시 입력하시오.")
                    elif a=="high":
                        self.Result.setText("배팅액이 너무 많습니다. 다시 입력하시오.")
                    elif a == "다시 입력해주세요":
                        self.Result.setText("다시 입력해주세요")
                    else:
                        self.Result.setText(self.IP.Bettingresult())
                        self.cnt += 1 #정상적으로 실행될때만 다음으로 넘어가도록 하기 위해서
                    self.Betting2.setText("")
                
                if key=="Open1":
                    self.Card1.setText(str(self.IP.getCard(2)))
                    self.Card1.setAlignment(Qt.AlignCenter)
                   
                    
                if key=="Close1":
                    self.Card1.setText("")
                    
                if key=="Open2":
                    self.Card2.setText(str(self.IP.getCard(1)))
                    self.Card2.setAlignment(Qt.AlignCenter)
                    
                    
                if key=="Close2":
                    self.Card2.setText("")
            
            if key=="Next":
                self.Result.setText(self.IP.nextRound())
                self.cnt = 0
            
            if key=="Reset":
                self.Result.setText(self.IP.resetGame())
                self.cnt = 0
            self.statusUpdate()
        except Exception as e:
            print("buttonClicked", e)
            
    def statusUpdate(self):
        self.Chip1.setText(str(self.IP.getChip(1)))
        self.Chip1.setAlignment(Qt.AlignCenter)
        
        self.Chip2.setText(str(self.IP.getChip(2)))
        self.Chip2.setAlignment(Qt.AlignCenter)

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
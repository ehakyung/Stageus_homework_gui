import sys, Menu, User, Game
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def __init__(self):
        self.setupUi()

    def setupUi(self):
        self.mainWindow = QtWidgets.QMainWindow()
        self.mainWindow.setObjectName("MainWindow")
        self.mainWindow.resize(480, 320)

        self.centralwidget = QtWidgets.QWidget(self.mainWindow)
        self.centralwidget.setObjectName("centralwidget")

#==============================================================================
#==============================================================================
        # 각종 menu를 포함한 stacked widget
        self.menu = QtWidgets.QStackedWidget(self.centralwidget)
        self.menu.setGeometry(QtCore.QRect(0, 0, 480, 320))
        self.menu.setObjectName("menu")
        self.menu.setCurrentIndex(0)

        # menu의 첫번째 페이지
        self.homeScreen = QtWidgets.QWidget()
        self.homeScreen.setObjectName("homeScreen")
        self.menu.addWidget(self.homeScreen)

        self.join = QtWidgets.QPushButton(self.homeScreen)
        self.join.setGeometry(QtCore.QRect(340, 32, 120, 40))
        self.join.setObjectName("join")

        self.login = QtWidgets.QPushButton(self.homeScreen)
        self.login.setGeometry(QtCore.QRect(340, 104, 120, 40))
        self.login.setObjectName("login")

        self.findInfo = QtWidgets.QPushButton(self.homeScreen)
        self.findInfo.setGeometry(QtCore.QRect(340, 176, 120, 40))
        self.findInfo.setObjectName("findInfo")

        self.quit = QtWidgets.QPushButton(self.homeScreen)
        self.quit.setGeometry(QtCore.QRect(340, 248, 120, 40))
        self.quit.setObjectName("quit")

#==============================================================================
        #로그인 전 화면전환을 위한 stacked widget
        self.beforeLogin = QtWidgets.QStackedWidget(self.homeScreen)
        self.beforeLogin.setGeometry(QtCore.QRect(20, 32, 300, 256))
        self.beforeLogin.setStyleSheet("background: rgb(255, 255, 255);")
        self.beforeLogin.setFrameShape(QtWidgets.QFrame.Box)
        self.beforeLogin.setObjectName("beforeLogin")
        self.beforeLogin.setCurrentIndex(0)

#------------------------------------------------------------------------------
        #beforeLogin의 첫번째 페이지
        self.beforeLogindefaultPage = QtWidgets.QWidget()
        self.beforeLogindefaultPage.setObjectName("beforeLogindefaultPage")
        self.beforeLogin.addWidget(self.beforeLogindefaultPage)

        self.nameOfGameLabel = QtWidgets.QLabel(self.beforeLogindefaultPage)
        self.nameOfGameLabel.setGeometry(QtCore.QRect(50, 103, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.nameOfGameLabel.setFont(font)
        self.nameOfGameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameOfGameLabel.setObjectName("nameOfGameLabel")

#------------------------------------------------------------------------------
        #beforeLogin의 두번째 페이지
        self.joinPage = QtWidgets.QWidget()
        self.joinPage.setObjectName("joinPage")
        self.beforeLogin.addWidget(self.joinPage)

        self.idForJoinInput = QtWidgets.QLineEdit(self.joinPage)
        self.idForJoinInput.setGeometry(QtCore.QRect(60, 70, 151, 20))
        self.idForJoinInput.setStyleSheet("background: rgb(235, 235, 235);")
        self.idForJoinInput.setObjectName("idForJoinInput")

        self.idForJoinLabel = QtWidgets.QLabel(self.joinPage)
        self.idForJoinLabel.setGeometry(QtCore.QRect(30, 70, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.idForJoinLabel.setFont(font)
        self.idForJoinLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.idForJoinLabel.setObjectName("idForJoinLabel")

        self.pwForJoinLabel = QtWidgets.QLabel(self.joinPage)
        self.pwForJoinLabel.setGeometry(QtCore.QRect(30, 100, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pwForJoinLabel.setFont(font)
        self.pwForJoinLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pwForJoinLabel.setObjectName("pwForJoinLabel")

        self.pwForJoinInput = QtWidgets.QLineEdit(self.joinPage)
        self.pwForJoinInput.setGeometry(QtCore.QRect(60, 100, 210, 20))
        self.pwForJoinInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwForJoinInput.setStyleSheet("background: rgb(235, 235, 235);")
        self.pwForJoinInput.setObjectName("pwForJoinInput")

        self.joinFailLabel = QtWidgets.QLabel(self.joinPage)
        self.joinFailLabel.setEnabled(True)
        self.joinFailLabel.setGeometry(QtCore.QRect(0, 40, 300, 20))
        self.joinFailLabel.setStyleSheet("color: rgb(255, 24, 13);")
        self.joinFailLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.joinFailLabel.setObjectName("joinFailLabel")

        self.nameForJoinInput = QtWidgets.QLineEdit(self.joinPage)
        self.nameForJoinInput.setGeometry(QtCore.QRect(60, 130, 210, 20))
        self.nameForJoinInput.setStyleSheet("background: rgb(235, 235, 235);")
        self.nameForJoinInput.setObjectName("nameForJoinInput")

        self.nameForJoinLabel = QtWidgets.QLabel(self.joinPage)
        self.nameForJoinLabel.setGeometry(QtCore.QRect(9, 130, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.nameForJoinLabel.setFont(font)
        self.nameForJoinLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nameForJoinLabel.setObjectName("nameForJoinLabel")

        self.ageForJoinInput = QtWidgets.QLineEdit(self.joinPage)
        self.ageForJoinInput.setGeometry(QtCore.QRect(60, 160, 210, 20))
        self.ageForJoinInput.setStyleSheet("background: rgb(235, 235, 235);")
        self.ageForJoinInput.setObjectName("ageForJoinInput")

        self.ageForJoinLabel = QtWidgets.QLabel(self.joinPage)
        self.ageForJoinLabel.setGeometry(QtCore.QRect(20, 160, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ageForJoinLabel.setFont(font)
        self.ageForJoinLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ageForJoinLabel.setObjectName("ageForJoinLabel")

        self.mailForJoinLabel = QtWidgets.QLabel(self.joinPage)
        self.mailForJoinLabel.setGeometry(QtCore.QRect(19, 190, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.mailForJoinLabel.setFont(font)
        self.mailForJoinLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mailForJoinLabel.setObjectName("mailForJoinLabel")

        self.mailForJoinInput = QtWidgets.QLineEdit(self.joinPage)
        self.mailForJoinInput.setGeometry(QtCore.QRect(60, 190, 151, 20))
        self.mailForJoinInput.setStyleSheet("background: rgb(235, 235, 235);")
        self.mailForJoinInput.setObjectName("mailForJoinInput")

        self.joinBtn = QtWidgets.QPushButton(self.joinPage)
        self.joinBtn.setGeometry(QtCore.QRect(110, 220, 100, 20))
        self.joinBtn.setStyleSheet("background-color: rgb(191, 191, 191)")
        self.joinBtn.setObjectName("joinBtn")

        self.checkForIdBtn = QtWidgets.QPushButton(self.joinPage)
        self.checkForIdBtn.setGeometry(QtCore.QRect(219, 70, 51, 20))
        self.checkForIdBtn.setStyleSheet("background-color: rgb(191, 191, 191)")
        self.checkForIdBtn.setObjectName("checkForIdBtn")

        self.checkForMailBtn = QtWidgets.QPushButton(self.joinPage)
        self.checkForMailBtn.setGeometry(QtCore.QRect(220, 190, 51, 20))
        self.checkForMailBtn.setStyleSheet("background-color: rgb(191, 191, 191)")
        self.checkForMailBtn.setObjectName("checkForMailBtn")

#------------------------------------------------------------------------------
        #beforeLogin의 세번째 페이지
        self.loginPage = QtWidgets.QWidget()
        self.loginPage.setObjectName("loginPage")
        self.beforeLogin.addWidget(self.loginPage)

        self.idForLoginLabel = QtWidgets.QLabel(self.loginPage)
        self.idForLoginLabel.setGeometry(QtCore.QRect(30, 90, 20, 20))
        self.idForLoginLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.idForLoginLabel.setObjectName("idForLoginLabel")

        self.idForLoginInput = QtWidgets.QLineEdit(self.loginPage)
        self.idForLoginInput.setGeometry(QtCore.QRect(60, 90, 210, 20))
        self.idForLoginInput.setStyleSheet("background: rgb(235, 235, 235);")
        self.idForLoginInput.setObjectName("idForLoginInput")

        self.pwForLoginInput = QtWidgets.QLineEdit(self.loginPage)
        self.pwForLoginInput.setGeometry(QtCore.QRect(60, 120, 210, 20))
        self.pwForLoginInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwForLoginInput.setStyleSheet("background: rgb(235, 235, 235);")
        self.pwForLoginInput.setObjectName("pwForLoginInput")

        self.pwForLoginLabel = QtWidgets.QLabel(self.loginPage)
        self.pwForLoginLabel.setGeometry(QtCore.QRect(30, 120, 20, 20))
        self.pwForLoginLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pwForLoginLabel.setObjectName("pwForLoginLabel")

        self.loginBtn = QtWidgets.QPushButton(self.loginPage)
        self.loginBtn.setGeometry(QtCore.QRect(110, 150, 100, 20))
        self.loginBtn.setStyleSheet("background-color: rgb(191, 191, 191)")
        self.loginBtn.setObjectName("loginBtn")

        self.loginFailLabel = QtWidgets.QLabel(self.loginPage)
        self.loginFailLabel.setGeometry(QtCore.QRect(60, 60, 210, 20))
        self.loginFailLabel.setStyleSheet("color: rgb(255, 24, 13);")
        self.loginFailLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loginFailLabel.setObjectName("loginFailLabel")

#------------------------------------------------------------------------------
        #beforeLogin의 네번째 페이지
        self.findInfoPage = QtWidgets.QWidget()
        self.findInfoPage.setObjectName("findInfoPage")
        self.beforeLogin.addWidget(self.findInfoPage)

        self.findIdBtn = QtWidgets.QPushButton(self.findInfoPage)
        self.findIdBtn.setGeometry(QtCore.QRect(60, 60, 100, 20))
        self.findIdBtn.setStyleSheet("background-color: rgb(191, 191, 191)")
        self.findIdBtn.setObjectName("findIdBtn")

        self.findPwBtn = QtWidgets.QPushButton(self.findInfoPage)
        self.findPwBtn.setGeometry(QtCore.QRect(170, 60, 100, 20))
        self.findPwBtn.setStyleSheet("background-color: rgb(191, 191, 191)")
        self.findPwBtn.setObjectName("findPwBtn")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        self.find = QtWidgets.QStackedWidget(self.findInfoPage)
        self.find.setGeometry(QtCore.QRect(19, 90, 250, 150))
        self.find.setObjectName("find")
        self.find.setCurrentIndex(0)

        #find의 첫번째 페이지
        self.findIdPage = QtWidgets.QWidget()
        self.findIdPage.setObjectName("findIdPage")
        self.find.addWidget(self.findIdPage)

        self.mailForFindIdInput = QtWidgets.QLineEdit(self.findIdPage)
        self.mailForFindIdInput.setGeometry(QtCore.QRect(40, 10, 210, 20))
        self.mailForFindIdInput.setStyleSheet("background: rgb(235, 235, 235);")
        self.mailForFindIdInput.setObjectName("mailForFindIdInput")

        self.mailForFindIdLabel = QtWidgets.QLabel(self.findIdPage)
        self.mailForFindIdLabel.setGeometry(QtCore.QRect(-1, 10, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.mailForFindIdLabel.setFont(font)
        self.mailForFindIdLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mailForFindIdLabel.setObjectName("mailForFindIdLabel")

        self.findIdFailLabel = QtWidgets.QLabel(self.findIdPage)
        self.findIdFailLabel.setEnabled(True)
        self.findIdFailLabel.setGeometry(QtCore.QRect(40, 40, 210, 20))
        self.findIdFailLabel.setStyleSheet("color: rgb(255, 24, 13);")
        self.findIdFailLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.findIdFailLabel.setObjectName("findIdFailLabel")

        self.findBtnForFindId = QtWidgets.QPushButton(self.findIdPage)
        self.findBtnForFindId.setGeometry(QtCore.QRect(100, 70, 100, 20))
        self.findBtnForFindId.setStyleSheet("background-color: rgb(191, 191, 191)")
        self.findBtnForFindId.setObjectName("findBtnForFindId")

        #find의 첫번째 페이지
        self.findPwPage = QtWidgets.QWidget()
        self.findPwPage.setObjectName("findPwPage")
        self.find.addWidget(self.findPwPage)

        self.idForFindPwInput = QtWidgets.QLineEdit(self.findPwPage)
        self.idForFindPwInput.setGeometry(QtCore.QRect(40, 10, 210, 20))
        self.idForFindPwInput.setStyleSheet("background: rgb(235, 235, 235);")
        self.idForFindPwInput.setObjectName("idForFindPwInput")

        self.mailForFindPwInput = QtWidgets.QLineEdit(self.findPwPage)
        self.mailForFindPwInput.setGeometry(QtCore.QRect(40, 40, 210, 20))
        self.mailForFindPwInput.setStyleSheet("background: rgb(235, 235, 235);")
        self.mailForFindPwInput.setObjectName("mailForFindPwInput")

        self.idForFindPwLabel = QtWidgets.QLabel(self.findPwPage)
        self.idForFindPwLabel.setGeometry(QtCore.QRect(-1, 10, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.idForFindPwLabel.setFont(font)
        self.idForFindPwLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.idForFindPwLabel.setObjectName("idForFindPwLabel")

        self.mailForFindPwLabel = QtWidgets.QLabel(self.findPwPage)
        self.mailForFindPwLabel.setGeometry(QtCore.QRect(-1, 40, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.mailForFindPwLabel.setFont(font)
        self.mailForFindPwLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mailForFindPwLabel.setObjectName("mailForFindPwLabel")

        self.findPwFailLabel = QtWidgets.QLabel(self.findPwPage)
        self.findPwFailLabel.setEnabled(True)
        self.findPwFailLabel.setGeometry(QtCore.QRect(40, 70, 210, 20))
        self.findPwFailLabel.setStyleSheet("color: rgb(255, 24, 13);")
        self.findPwFailLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.findPwFailLabel.setObjectName("findPwFailLabel")

        self.findBtnForFindPw = QtWidgets.QPushButton(self.findPwPage)
        self.findBtnForFindPw.setGeometry(QtCore.QRect(100, 100, 100, 20))
        self.findBtnForFindPw.setStyleSheet("background-color: rgb(191, 191, 191)")
        self.findBtnForFindPw.setObjectName("findBtnForFindPw")

#------------------------------------------------------------------------------
        #beforeLogin의 다섯번째 페이지
        self.quitPage = QtWidgets.QWidget()
        self.quitPage.setObjectName("quitPage")
        self.beforeLogin.addWidget(self.quitPage)

        self.quitLabel = QtWidgets.QLabel(self.quitPage)
        self.quitLabel.setEnabled(True)
        self.quitLabel.setGeometry(QtCore.QRect(0, 100, 300, 20))
        self.quitLabel.setStyleSheet("")
        self.quitLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.quitLabel.setObjectName("quitLabel")

        self.quitBtn = QtWidgets.QPushButton(self.quitPage)
        self.quitBtn.setGeometry(QtCore.QRect(100, 140, 100, 20))
        self.quitBtn.setStyleSheet("background-color: rgb(191, 191, 191)")
        self.quitBtn.setObjectName("quitBtn")

#==============================================================================
        # menu의 두번째 페이지
        self.loggedInScreen = QtWidgets.QWidget()
        self.loggedInScreen.setObjectName("loggedInScreen")
        self.menu.addWidget(self.loggedInScreen)

        self.logout = QtWidgets.QPushButton(self.loggedInScreen)
        self.logout.setGeometry(QtCore.QRect(340, 248, 120, 40))
        self.logout.setObjectName("logout")

        self.myInfo = QtWidgets.QPushButton(self.loggedInScreen)
        self.myInfo.setGeometry(QtCore.QRect(340, 104, 120, 40))
        self.myInfo.setObjectName("myInfo")

        self.playGame = QtWidgets.QPushButton(self.loggedInScreen)
        self.playGame.setGeometry(QtCore.QRect(340, 32, 120, 40))
        self.playGame.setObjectName("playGame")

        self.ranking = QtWidgets.QPushButton(self.loggedInScreen)
        self.ranking.setGeometry(QtCore.QRect(340, 176, 120, 40))
        self.ranking.setObjectName("ranking")
#==============================================================================
        #로그인 후 화면전환을 위한 stacked widget
        self.afterLogin = QtWidgets.QStackedWidget(self.loggedInScreen)
        self.afterLogin.setGeometry(QtCore.QRect(20, 32, 300, 256))
        self.afterLogin.setStyleSheet("background: rgb(255, 255, 255);")
        self.afterLogin.setFrameShape(QtWidgets.QFrame.Box)
        self.afterLogin.setObjectName("afterLogin")
        self.afterLogin.setCurrentIndex(0)
#------------------------------------------------------------------------------
        #afterLogin의 첫번째 페이지
        self.afterLogindefaultPage = QtWidgets.QWidget()
        self.afterLogindefaultPage.setObjectName("afterLogindefaultPage")
        self.afterLogin.addWidget(self.afterLogindefaultPage)

        self.helloLabel = QtWidgets.QLabel(self.afterLogindefaultPage)
        self.helloLabel.setGeometry(QtCore.QRect(0, 103, 300, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.helloLabel.setFont(font)
        self.helloLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.helloLabel.setObjectName("helloLabel")

#------------------------------------------------------------------------------
        #afterLogin의 두번째 페이지
        self.gamePage = QtWidgets.QWidget()
        self.gamePage.setObjectName("gamePage")
        self.afterLogin.addWidget(self.gamePage)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.game = QtWidgets.QStackedWidget(self.gamePage)
        self.game.setGeometry(QtCore.QRect(0, 20, 300, 236))
        self.game.setObjectName("game")

        #game의 첫번째 페이지
        self.standbyPage = QtWidgets.QWidget()
        self.standbyPage.setObjectName("standbyPage")
        self.game.addWidget(self.standbyPage)

        self.explainGame = QtWidgets.QTextBrowser(self.standbyPage)
        self.explainGame.setGeometry(QtCore.QRect(0, 30, 300, 121))
        self.explainGame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.explainGame.setLineWidth(1)
        self.explainGame.setObjectName("explainGame")

        #game의 두번째 페이지
        self.playPage = QtWidgets.QWidget()
        self.playPage.setObjectName("playPage")
        self.game.addWidget(self.playPage)

        self.trialLabel = QtWidgets.QLabel(self.playPage)
        self.trialLabel.setEnabled(True)
        self.trialLabel.setGeometry(QtCore.QRect(0, 45, 300, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.trialLabel.setFont(font)
        self.trialLabel.setStyleSheet("")
        self.trialLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.trialLabel.setObjectName("trialLabel")

        self.putAnswerLabel = QtWidgets.QLabel(self.playPage)
        self.putAnswerLabel.setEnabled(True)
        self.putAnswerLabel.setGeometry(QtCore.QRect(0, 75, 300, 20))
        self.putAnswerLabel.setStyleSheet("")
        self.putAnswerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.putAnswerLabel.setObjectName("putAnswerLabel")

        self.answerInput = QtWidgets.QLineEdit(self.playPage)
        self.answerInput.setGeometry(QtCore.QRect(80, 110, 151, 20))
        self.answerInput.setStyleSheet("background: rgb(235, 235, 235);")
        self.answerInput.setObjectName("answerInput")

        self.answerFailLabel = QtWidgets.QLabel(self.playPage)
        self.answerFailLabel.setEnabled(True)
        self.answerFailLabel.setGeometry(QtCore.QRect(0, 145, 300, 20))
        self.answerFailLabel.setStyleSheet("color: rgb(255, 24, 13);")
        self.answerFailLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.answerFailLabel.setObjectName("answerFailLabel")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.btn = QtWidgets.QStackedWidget(self.gamePage)
        self.btn.setGeometry(QtCore.QRect(0, 190, 300, 66))
        self.btn.setObjectName("btn")

        #btn의 첫번째 페이지
        self.playBtnPage = QtWidgets.QWidget()
        self.playBtnPage.setObjectName("playBtnPage")
        self.btn.addWidget(self.playBtnPage)

        self.playBtn = QtWidgets.QPushButton(self.playBtnPage)
        self.playBtn.setGeometry(QtCore.QRect(100, 10, 100, 20))
        self.playBtn.setStyleSheet("background-color: rgb(191, 191, 191)")
        self.playBtn.setObjectName("playBtn")

        #btn의 두번째 페이지
        self.enterBtnPage = QtWidgets.QWidget()
        self.enterBtnPage.setObjectName("enterBtnPage")
        self.btn.addWidget(self.enterBtnPage)

        self.enterBtn = QtWidgets.QPushButton(self.enterBtnPage)
        self.enterBtn.setGeometry(QtCore.QRect(100, 10, 100, 20))
        self.enterBtn.setStyleSheet("background-color: rgb(191, 191, 191)")
        self.enterBtn.setObjectName("enterBtn")

#------------------------------------------------------------------------------
        #afterLogin의 세번째 페이지
        self.myInfoPage = QtWidgets.QWidget()
        self.myInfoPage.setObjectName("myInfoPage")
        self.afterLogin.addWidget(self.myInfoPage)

        self.mailForMyInfoLabel = QtWidgets.QLabel(self.myInfoPage)
        self.mailForMyInfoLabel.setGeometry(QtCore.QRect(39, 130, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.mailForMyInfoLabel.setFont(font)
        self.mailForMyInfoLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mailForMyInfoLabel.setObjectName("mailForMyInfoLabel")

        self.ageForMyInfoLabel = QtWidgets.QLabel(self.myInfoPage)
        self.ageForMyInfoLabel.setGeometry(QtCore.QRect(165, 100, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ageForMyInfoLabel.setFont(font)
        self.ageForMyInfoLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ageForMyInfoLabel.setObjectName("ageForMyInfoLabel")

        self.nameForMyInfoInput = QtWidgets.QLineEdit(self.myInfoPage)
        self.nameForMyInfoInput.setGeometry(QtCore.QRect(80, 100, 81, 20))
        self.nameForMyInfoInput.setEnabled(False)
        self.nameForMyInfoInput.setStyleSheet("background: rgb(235, 235, 235);")
        self.nameForMyInfoInput.setObjectName("nameForMyInfoInput")

        self.idForMyInfoLabel = QtWidgets.QLabel(self.myInfoPage)
        self.idForMyInfoLabel.setGeometry(QtCore.QRect(50, 70, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.idForMyInfoLabel.setFont(font)
        self.idForMyInfoLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.idForMyInfoLabel.setObjectName("idForMyInfoLabel")

        self.mailForMyInfoInput = QtWidgets.QLineEdit(self.myInfoPage)
        self.mailForMyInfoInput.setGeometry(QtCore.QRect(80, 130, 210, 20))
        self.mailForMyInfoInput.setEnabled(False)
        self.mailForMyInfoInput.setStyleSheet("background: rgb(235, 235, 235);")
        self.mailForMyInfoInput.setObjectName("mailForMyInfoInput")

        self.idForMyInfoInput = QtWidgets.QLineEdit(self.myInfoPage)
        self.idForMyInfoInput.setGeometry(QtCore.QRect(80, 70, 210, 20))
        self.idForMyInfoInput.setEnabled(False)
        self.idForMyInfoInput.setStyleSheet("background: rgb(235, 235, 235);")
        self.idForMyInfoInput.setObjectName("idForMyInfoInput")

        self.bestScoreForMyInfoInput = QtWidgets.QLineEdit(self.myInfoPage)
        self.bestScoreForMyInfoInput.setGeometry(QtCore.QRect(129, 160, 161, 20))
        self.bestScoreForMyInfoInput.setEnabled(False)
        self.bestScoreForMyInfoInput.setStyleSheet("background: rgb(235, 235, 235);")
        self.bestScoreForMyInfoInput.setObjectName("bestScoreForMyInfoInput")

        self.nameForMyInfoLabel = QtWidgets.QLabel(self.myInfoPage)
        self.nameForMyInfoLabel.setGeometry(QtCore.QRect(29, 100, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.nameForMyInfoLabel.setFont(font)
        self.nameForMyInfoLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nameForMyInfoLabel.setObjectName("nameForMyInfoLabel")

        self.myInfoLabel = QtWidgets.QLabel(self.myInfoPage)
        self.myInfoLabel.setEnabled(True)
        self.myInfoLabel.setGeometry(QtCore.QRect(0, 40, 300, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.myInfoLabel.setFont(font)
        self.myInfoLabel.setStyleSheet("")
        self.myInfoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.myInfoLabel.setObjectName("myInfoLabel")

        self.ageForMyInfoInput = QtWidgets.QLineEdit(self.myInfoPage)
        self.ageForMyInfoInput.setGeometry(QtCore.QRect(210, 100, 80, 20))
        self.ageForMyInfoInput.setEnabled(False)
        self.ageForMyInfoInput.setStyleSheet("background: rgb(235, 235, 235);")
        self.ageForMyInfoInput.setObjectName("ageForMyInfoInput")

        self.bestScoreForMyInfoLabel = QtWidgets.QLabel(self.myInfoPage)
        self.bestScoreForMyInfoLabel.setGeometry(QtCore.QRect(38, 160, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.bestScoreForMyInfoLabel.setFont(font)
        self.bestScoreForMyInfoLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bestScoreForMyInfoLabel.setObjectName("bestScoreForMyInfoLabel")

        self.playGamesForMyInfoLabel = QtWidgets.QLabel(self.myInfoPage)
        self.playGamesForMyInfoLabel.setGeometry(QtCore.QRect(39, 190, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.playGamesForMyInfoLabel.setFont(font)
        self.playGamesForMyInfoLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.playGamesForMyInfoLabel.setObjectName("playGamesForMyInfoLabel")

        self.playGamesForMyInfoInput = QtWidgets.QLineEdit(self.myInfoPage)
        self.playGamesForMyInfoInput.setGeometry(QtCore.QRect(130, 190, 161, 20))
        self.playGamesForMyInfoInput.setEnabled(False)
        self.playGamesForMyInfoInput.setStyleSheet("background: rgb(235, 235, 235);")
        self.playGamesForMyInfoInput.setText("")
        self.playGamesForMyInfoInput.setObjectName("playGamesForMyInfoInput")

#------------------------------------------------------------------------------
        #afterLogin의 네번째 페이지
        self.rankingPage = QtWidgets.QWidget()
        self.rankingPage.setObjectName("rankingPage")
        self.afterLogin.addWidget(self.rankingPage)

        self.rank1Input = QtWidgets.QLineEdit(self.rankingPage)
        self.rank1Input.setEnabled(False)
        self.rank1Input.setGeometry(QtCore.QRect(60, 40, 210, 20))
        self.rank1Input.setStyleSheet("background: rgb(235, 235, 235);")
        self.rank1Input.setObjectName("rank1Input")

        self.rank1Label = QtWidgets.QLabel(self.rankingPage)
        self.rank1Label.setGeometry(QtCore.QRect(20, 40, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.rank1Label.setFont(font)
        self.rank1Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rank1Label.setObjectName("rank1Label")

        self.rank2Input = QtWidgets.QLineEdit(self.rankingPage)
        self.rank2Input.setEnabled(False)
        self.rank2Input.setGeometry(QtCore.QRect(60, 60, 210, 20))
        self.rank2Input.setStyleSheet("background: rgb(235, 235, 235);")
        self.rank2Input.setObjectName("rank2Input")

        self.rank3Input = QtWidgets.QLineEdit(self.rankingPage)
        self.rank3Input.setEnabled(False)
        self.rank3Input.setGeometry(QtCore.QRect(60, 80, 210, 20))
        self.rank3Input.setStyleSheet("background: rgb(235, 235, 235);")
        self.rank3Input.setObjectName("rank3Input")

        self.rank4Input = QtWidgets.QLineEdit(self.rankingPage)
        self.rank4Input.setEnabled(False)
        self.rank4Input.setGeometry(QtCore.QRect(60, 100, 210, 20))
        self.rank4Input.setStyleSheet("background: rgb(235, 235, 235);")
        self.rank4Input.setObjectName("rank4Input")

        self.rank5Input = QtWidgets.QLineEdit(self.rankingPage)
        self.rank5Input.setEnabled(False)
        self.rank5Input.setGeometry(QtCore.QRect(60, 120, 210, 20))
        self.rank5Input.setStyleSheet("background: rgb(235, 235, 235);")
        self.rank5Input.setObjectName("rank5Input")

        self.rank6Input = QtWidgets.QLineEdit(self.rankingPage)
        self.rank6Input.setEnabled(False)
        self.rank6Input.setGeometry(QtCore.QRect(60, 140, 210, 20))
        self.rank6Input.setStyleSheet("background: rgb(235, 235, 235);")
        self.rank6Input.setObjectName("rank6Input")

        self.rank10Input = QtWidgets.QLineEdit(self.rankingPage)
        self.rank10Input.setEnabled(False)
        self.rank10Input.setGeometry(QtCore.QRect(60, 220, 210, 20))
        self.rank10Input.setStyleSheet("background: rgb(235, 235, 235);")
        self.rank10Input.setObjectName("rank10Input")

        self.rank9Input = QtWidgets.QLineEdit(self.rankingPage)
        self.rank9Input.setEnabled(False)
        self.rank9Input.setGeometry(QtCore.QRect(60, 200, 210, 20))
        self.rank9Input.setStyleSheet("background: rgb(235, 235, 235);")
        self.rank9Input.setObjectName("rank9Input")

        self.rank7Input = QtWidgets.QLineEdit(self.rankingPage)
        self.rank7Input.setEnabled(False)
        self.rank7Input.setGeometry(QtCore.QRect(60, 160, 210, 20))
        self.rank7Input.setStyleSheet("background: rgb(235, 235, 235);")
        self.rank7Input.setObjectName("rank7Input")

        self.rank8Input = QtWidgets.QLineEdit(self.rankingPage)
        self.rank8Input.setEnabled(False)
        self.rank8Input.setGeometry(QtCore.QRect(60, 180, 210, 20))
        self.rank8Input.setStyleSheet("background: rgb(235, 235, 235);")
        self.rank8Input.setObjectName("rank8Input")

        self.rankingLabel = QtWidgets.QLabel(self.rankingPage)
        self.rankingLabel.setEnabled(True)
        self.rankingLabel.setGeometry(QtCore.QRect(60, 15, 210, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rankingLabel.setFont(font)
        self.rankingLabel.setStyleSheet("")
        self.rankingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rankingLabel.setObjectName("rankingLabel")

        self.rank2Label = QtWidgets.QLabel(self.rankingPage)
        self.rank2Label.setGeometry(QtCore.QRect(20, 60, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.rank2Label.setFont(font)
        self.rank2Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rank2Label.setObjectName("rank2Label")

        self.rank3Label = QtWidgets.QLabel(self.rankingPage)
        self.rank3Label.setGeometry(QtCore.QRect(20, 80, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.rank3Label.setFont(font)
        self.rank3Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rank3Label.setObjectName("rank3Label")

        self.rank4Label = QtWidgets.QLabel(self.rankingPage)
        self.rank4Label.setGeometry(QtCore.QRect(20, 100, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.rank4Label.setFont(font)
        self.rank4Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rank4Label.setObjectName("rank4Label")

        self.rank6Label = QtWidgets.QLabel(self.rankingPage)
        self.rank6Label.setGeometry(QtCore.QRect(20, 140, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.rank6Label.setFont(font)
        self.rank6Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rank6Label.setObjectName("rank6Label")

        self.rank5Label = QtWidgets.QLabel(self.rankingPage)
        self.rank5Label.setGeometry(QtCore.QRect(20, 120, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.rank5Label.setFont(font)
        self.rank5Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rank5Label.setObjectName("rank5Label")

        self.rank7Label = QtWidgets.QLabel(self.rankingPage)
        self.rank7Label.setGeometry(QtCore.QRect(20, 160, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.rank7Label.setFont(font)
        self.rank7Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rank7Label.setObjectName("rank7Label")

        self.rank9Label = QtWidgets.QLabel(self.rankingPage)
        self.rank9Label.setGeometry(QtCore.QRect(20, 200, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.rank9Label.setFont(font)
        self.rank9Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rank9Label.setObjectName("rank9Label")

        self.rank8Label = QtWidgets.QLabel(self.rankingPage)
        self.rank8Label.setGeometry(QtCore.QRect(20, 180, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.rank8Label.setFont(font)
        self.rank8Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rank8Label.setObjectName("rank8Label")

        self.rank10Label = QtWidgets.QLabel(self.rankingPage)
        self.rank10Label.setGeometry(QtCore.QRect(20, 220, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.rank10Label.setFont(font)
        self.rank10Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rank10Label.setObjectName("rank10Label")

#------------------------------------------------------------------------------
        #afterLogin의 다섯번째 페이지
        self.logoutPage = QtWidgets.QWidget()
        self.logoutPage.setObjectName("logoutPage")
        self.afterLogin.addWidget(self.logoutPage)

        self.logoutLabel = QtWidgets.QLabel(self.logoutPage)
        self.logoutLabel.setGeometry(QtCore.QRect(0, 100, 300, 20))
        self.logoutLabel.setStyleSheet("")
        self.logoutLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.logoutLabel.setObjectName("logoutLabel")

        self.logoutBtn = QtWidgets.QPushButton(self.logoutPage)
        self.logoutBtn.setGeometry(QtCore.QRect(100, 140, 100, 20))
        self.logoutBtn.setStyleSheet("background-color: rgb(191, 191, 191)")
        self.logoutBtn.setObjectName("logoutBtn")

#==============================================================================

        self.mainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.mainWindow)
        self.mainWindow.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.mainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login.setText(_translate("MainWindow", "LOGIN"))
        self.join.setText(_translate("MainWindow", "JOIN"))
        self.findInfo.setText(_translate("MainWindow", "FIND INFO"))
        self.quit.setText(_translate("MainWindow", "QUIT"))
        self.nameOfGameLabel.setText(_translate("MainWindow", "UP AND DOWN"))
        self.idForLoginLabel.setText(_translate("MainWindow", "ID"))
        self.pwForLoginLabel.setText(_translate("MainWindow", "PW"))
        self.loginBtn.setText(_translate("MainWindow", "LOGIN"))
        self.idForJoinLabel.setText(_translate("MainWindow", "ID"))
        self.pwForJoinLabel.setText(_translate("MainWindow", "PW"))
        self.nameForJoinLabel.setText(_translate("MainWindow", "NAME"))
        self.ageForJoinLabel.setText(_translate("MainWindow", "AGE"))
        self.mailForJoinLabel.setText(_translate("MainWindow", "MAIL"))
        self.joinBtn.setText(_translate("MainWindow", "JOIN"))
        self.checkForIdBtn.setText(_translate("MainWindow", "CHECK"))
        self.checkForMailBtn.setText(_translate("MainWindow", "CHECK"))
        self.findIdBtn.setText(_translate("MainWindow", "FIND ID"))
        self.findPwBtn.setText(_translate("MainWindow", "FIND PW"))
        self.mailForFindIdLabel.setText(_translate("MainWindow", "MAIL"))
        self.findBtnForFindId.setText(_translate("MainWindow", "FIND"))
        self.idForFindPwLabel.setText(_translate("MainWindow", "ID"))
        self.mailForFindPwLabel.setText(_translate("MainWindow", "MAIL"))
        self.findBtnForFindPw.setText(_translate("MainWindow", "FIND"))
        self.quitLabel.setText(_translate("MainWindow", "QUIT TO CLOSE THE WINDOW."))
        self.quitBtn.setText(_translate("MainWindow", "QUIT"))
        self.logout.setText(_translate("MainWindow", "LOGOUT"))
        self.myInfo.setText(_translate("MainWindow", "MY INFO"))
        self.playGame.setText(_translate("MainWindow", "PLAY GAME"))
        self.ranking.setText(_translate("MainWindow", "RANKING"))
        self.explainGame.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">THE ANSWER</span> IS THE RANDOM NUMBER <span style=\" font-weight:600;\">BETWEEN 1 AND 50. </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PUT INTEGER BETWEEN 1 AND 50. </p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">IF THE NUMBER YOU ENTERED IS SMALLER THAN ANSWER, \'UP\' MESSAGE, IF NOT, \'DOWN\' MESSAGE WILL BE PRINDTED.</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">SCORE</span> IS THE NUMBER OF<span style=\" font-weight:600;\"> TRIAL.</span></p></body></html>"))
        self.playBtn.setText(_translate("MainWindow", "PLAY"))
        self.putAnswerLabel.setText(_translate("MainWindow", "PUT INTEGER BETWEEN 1 AND 50"))
        self.enterBtn.setText(_translate("MainWindow", "ENTER"))
        self.mailForMyInfoLabel.setText(_translate("MainWindow", "MAIL"))
        self.ageForMyInfoLabel.setText(_translate("MainWindow", "AGE"))
        self.idForMyInfoLabel.setText(_translate("MainWindow", "ID"))
        self.nameForMyInfoLabel.setText(_translate("MainWindow", "NAME"))
        self.bestScoreForMyInfoLabel.setText(_translate("MainWindow", "BEST SCORE"))
        self.playGamesForMyInfoLabel.setText(_translate("MainWindow", "PLAY GAMES"))
        self.rank1Label.setText(_translate("MainWindow", "1ST"))
        self.rankingLabel.setText(_translate("MainWindow", "TOP 10 SCORE"))
        self.rank2Label.setText(_translate("MainWindow", "2ND"))
        self.rank3Label.setText(_translate("MainWindow", "3RD"))
        self.rank4Label.setText(_translate("MainWindow", "4TH"))
        self.rank6Label.setText(_translate("MainWindow", "6TH"))
        self.rank5Label.setText(_translate("MainWindow", "5TH"))
        self.rank7Label.setText(_translate("MainWindow", "7TH"))
        self.rank9Label.setText(_translate("MainWindow", "9TH"))
        self.rank8Label.setText(_translate("MainWindow", "8TH"))
        self.rank10Label.setText(_translate("MainWindow", "10TH"))
        self.logoutLabel.setText(_translate("MainWindow", "LOGOUT TO RETURN TO BEFORE LOGIN PAGE."))
        self.logoutBtn.setText(_translate("MainWindow", "LOGOUT"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    ui = Ui_MainWindow()
    userInfo=User.UserInfo(ui)
    menu=Menu.Menu(ui)
    game=Game.Game(ui)

    sys.exit(app.exec_())

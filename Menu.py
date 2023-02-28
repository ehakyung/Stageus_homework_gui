import sqlite3

class Menu:
    def __init__(self, ui):
        self.connect=sqlite3.connect("database.db")
        self.cursor=self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS userInfo (id TEXT PRIMARY KEY, pw TEXT, name TEXT, age INTEGER, email TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS recordInfo (id TEXT REFERENCES userInfo(id), count INTEGER, dateTime TEXT)")

        self.ui=ui 
        self.ui.join.clicked.connect(self.joinEvent)
        self.ui.login.clicked.connect(self.loginEvent)
        self.ui.findInfo.clicked.connect(self.findInfoEvent)
        self.ui.quit.clicked.connect(self.quitEvent)
        self.ui.findIdBtn.clicked.connect(self.findIdBtnEvent)
        self.ui.findPwBtn.clicked.connect(self.findPwBtnEvent)
        self.ui.playGame.clicked.connect(self.playGameEvent)
        self.ui.playBtn.clicked.connect(self.playEvent)
        self.ui.myInfo.clicked.connect(self.myInfoEvent)
        self.ui.ranking.clicked.connect(self.rankingEvent)
        self.ui.logout.clicked.connect(self.logoutEvent)
        self.ui.logoutBtn.clicked.connect(self.logoutBtnEvent)
        self.ui.quitBtn.clicked.connect(self.ui.mainWindow.close)

    def joinEvent(self):
        self.ui.beforeLogin.setCurrentIndex(1)

    def loginEvent(self):
        self.ui.beforeLogin.setCurrentIndex(2)

    def findInfoEvent(self):
        self.ui.beforeLogin.setCurrentIndex(3)

    def quitEvent(self):
        self.ui.beforeLogin.setCurrentIndex(4)

    def findIdBtnEvent(self):
        self.ui.find.setCurrentIndex(0)

    def findPwBtnEvent(self):
        self.ui.find.setCurrentIndex(1)

    def changeMenu(self):
        self.ui.menu.setCurrentIndex(1)
        self.ui.afterLogin.setCurrentIndex(0)

    def playGameEvent(self):
        self.ui.afterLogin.setCurrentIndex(1)
        self.ui.game.setCurrentIndex(0)
        self.ui.btn.setCurrentIndex(0)

    def playEvent(self):
        self.ui.game.setCurrentIndex(1)
        self.ui.trialLabel.setText("THE NUMBER OF TRIAL: 1")
        self.ui.answerFailLabel.setText("")
        self.ui.btn.setCurrentIndex(1)

    def myInfoEvent(self):
        self.ui.afterLogin.setCurrentIndex(2)

    def rankingEvent(self):
        self.ui.afterLogin.setCurrentIndex(3)

    def logoutEvent(self):
        self.ui.afterLogin.setCurrentIndex(4)

    def logoutBtnEvent(self):
        self.ui.menu.setCurrentIndex(0)
        self.ui.beforeLogin.setCurrentIndex(0)
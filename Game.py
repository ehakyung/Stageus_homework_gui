import sqlite3, random, User

class Game:    
    def __init__(self, ui):
        self.connect=sqlite3.connect("database.db")
        self.cursor=self.connect.cursor()

        self.loggedId=None
        self.answer=None
        self.count=None
        self.score=[]

        self.user=None
        self.ui=ui

        self.ui.playBtn.clicked.connect(self.setAnswerEvent)
        self.ui.enterBtn.clicked.connect(self.enterBtnEvent)
        self.ui.answerInput.returnPressed.connect(self.enterBtnEvent)

    def setAnswerEvent(self):
        self.answer=random.randint(1,50)
        self.count=1

    def loadId(self, id):
        self.loggedId=id

    def enterBtnEvent(self):
        try:
            if int(self.ui.answerInput.text())==self.answer:
                self.user=User.UserInfo(self.ui)
                self.cursor.execute("INSERT INTO recordInfo VALUES (?, ?, datetime('now','localtime'))", [self.loggedId, self.count])
                self.connect.commit()
                self.ui.trialLabel.setText("SCORE: "+str(self.count)+"TRIAL")
                self.ui.answerFailLabel.setText("CORRECT ANSWER!")
                self.ui.btn.setCurrentIndex(0)
            elif int(self.ui.answerInput.text())>50 or int(self.ui.answerInput.text())<1:
                self.ui.answerFailLabel.setText("ONLY BETWEEN 1 AND 50 YOU CAN ENTER")
            elif int(self.ui.answerInput.text())>self.answer:
                self.ui.answerFailLabel.setText("DOWN")
                self.count+=1
                self.ui.trialLabel.setText("THE NUMBER OF TRIAL: "+str(self.count))
            elif int(self.ui.answerInput.text())<self.answer:
                self.ui.answerFailLabel.setText("UP")
                self.count+=1
                self.ui.trialLabel.setText("THE NUMBER OF TRIAL: "+str(self.count))
        except ValueError:
            self.ui.answerFailLabel.setText("ONLY INTEGER YOU CAN ENTER")

import sqlite3

class ShowInfo:
    def __init__(self, ui):
        self.connect=sqlite3.connect("database.db")
        self.cursor=self.connect.cursor()
        self.ui=ui
        self.loggedId=None
        self.ui.myInfo.clicked.connect(self.myInfoEvent)
        self.ui.ranking.clicked.connect(self.rankingEvent)

    def loadId(self, id):
        self.loggedId=id

    def myInfoEvent(self): 
        self.ui.myInfoLabel.setText(self.loggedId+"'S INFO")
        self.cursor.execute("SELECT name, age, email FROM userInfo WHERE id=?", [self.loggedId])
        result=self.cursor.fetchall() 
        self.ui.idForMyInfoInput.setText(self.loggedId)
        self.ui.nameForMyInfoInput.setText(result[0][0])
        self.ui.ageForMyInfoInput.setText(str(result[0][1]))
        self.ui.mailForMyInfoInput.setText(result[0][2])
        self.cursor.execute("SELECT count FROM recordInfo WHERE id=? ORDER BY count, dateTime", [self.loggedId])
        result=self.cursor.fetchall()
        if len(result)<1:
            self.ui.bestScoreForMyInfoInput.setText("NO SCORE")
            self.ui.playGamesForMyInfoInput.setText("NO PLAY")
        else:
            self.ui.bestScoreForMyInfoInput.setText(str(result[0][0]))
            self.ui.playGamesForMyInfoInput.setText(str(len(result)))

    def rankingEvent(self):
        self.cursor.execute("SELECT id, count, dateTime FROM recordInfo ORDER BY count, dateTime LIMIT 10")
        result=self.cursor.fetchall()
        if len(result)<10:
            for i in range (10-len(result)):
                result.append(["-","-","-"])
        self.ui.rank1Input.setText(result[0][0]+" / "+str(result[0][1])+" / "+result[0][2])
        self.ui.rank2Input.setText(result[1][0]+" / "+str(result[1][1])+" / "+result[1][2])
        self.ui.rank3Input.setText(result[2][0]+" / "+str(result[2][1])+" / "+result[2][2])
        self.ui.rank4Input.setText(result[3][0]+" / "+str(result[3][1])+" / "+result[3][2])
        self.ui.rank5Input.setText(result[4][0]+" / "+str(result[4][1])+" / "+result[4][2])
        self.ui.rank6Input.setText(result[5][0]+" / "+str(result[5][1])+" / "+result[5][2])
        self.ui.rank7Input.setText(result[6][0]+" / "+str(result[6][1])+" / "+result[6][2])
        self.ui.rank8Input.setText(result[7][0]+" / "+str(result[7][1])+" / "+result[7][2])
        self.ui.rank9Input.setText(result[8][0]+" / "+str(result[8][1])+" / "+result[8][2])
        self.ui.rank10Input.setText(result[9][0]+" / "+str(result[9][1])+" / "+result[9][2])
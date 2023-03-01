import sqlite3, Menu, Game, ShowInfo, re

class UserInfo:

    def __init__(self, ui):
        self.loggedId=None
        self.menu=Menu.Menu(ui)
        self.ui=ui
        self.game=None

        self.connect=sqlite3.connect("database.db")
        self.cursor=self.connect.cursor()
        self.ui.checkForIdBtn.clicked.connect(self.idForJoinCheck)
        self.ui.checkForMailBtn.clicked.connect(self.mailForJoinCheck)
        self.ui.joinBtn.clicked.connect(self.joinBtnEvent)
        self.ui.idForJoinInput.returnPressed.connect(self.idForJoinCheck)
        self.ui.mailForJoinInput.returnPressed.connect(self.mailForJoinCheck)

        self.ui.loginBtn.clicked.connect(self.loginBtnEvent)
        self.ui.pwForLoginInput.returnPressed.connect(self.loginBtnEvent)
        self.ui.findBtnForFindId.clicked.connect(self.findBtnForFindIdEvent)
        self.ui.mailForFindIdInput.returnPressed.connect(self.findBtnForFindIdEvent)
        self.ui.findBtnForFindPw.clicked.connect(self.findBtnForFindPwEvent)
        self.ui.mailForFindPwInput.returnPressed.connect(self.findBtnForFindPwEvent)

        self.ui.logoutBtn.clicked.connect(self.logoutBtnEvent)

    def idForJoinCheck(self):
        id=self.ui.idForJoinInput.text()
        self.cursor.execute("SELECT id FROM userInfo WHERE id=?", [id]) 
        result=self.cursor.fetchall() 
        if len(result)==0:
            self.ui.joinFailLabel.setText("YOU CAN USE THIS ID")
        else:
            self.ui.joinFailLabel.setText("ALREADY USED ID")

    def mailForJoinCheck(self):
        mail=self.ui.mailForJoinInput.text()
        REGEX_EMAIL = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        if not re.fullmatch(REGEX_EMAIL, mail):
            self.ui.joinFailLabel.setText("INVALID MAIL")
        else:
            self.cursor.execute("SELECT email FROM userInfo WHERE email=?", [mail]) 
            result=self.cursor.fetchall() 
            if len(result)==0:
                self.ui.joinFailLabel.setText("YOU CAN USE THIS MAIL")
            else:
                self.ui.joinFailLabel.setText("ALREADY USED MAIL")


    def joinBtnEvent(self): #이메일검증여부 추가해서 데이터베이스 저장여부 결정하게 함수 수정하기
        id=self.ui.idForJoinInput.text()
        pw=self.ui.pwForJoinInput.text()
        name=self.ui.nameForJoinInput.text()
        age=self.ui.ageForJoinInput.text()
        mail=self.ui.mailForJoinInput.text()

        if id=="" or pw=="" or name=="" or age=="" or mail=="": 
                self.ui.joinFailLabel.setText("PLEASE FILL IN ALL THE BLANKS")
        else:
            REGEX_EMAIL = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
            if not re.fullmatch(REGEX_EMAIL, mail):
                self.ui.joinFailLabel.setText("INVALID MAIL")
            else:
                self.cursor.execute("SELECT id, email FROM userInfo WHERE id=? OR email=?", [id, mail])
                result=self.cursor.fetchall() 
                if len(result)==0:
                    try:
                        age=self.ui.ageForJoinInput.text()
                        if int(age)>0:
                            pw=self.ui.pwForJoinInput.text()
                            name=self.ui.nameForJoinInput.text()
                            if pw!="" and name!="":
                                self.cursor.execute("INSERT INTO userInfo VALUES (?, ?, ?, ?, ?)", [id, pw, name, age, mail])
                                self.connect.commit()
                                self.ui.joinFailLabel.setText("WELCOME! PLEASE LOGIN FOR PLAYING GAME")
                        else:
                            self.ui.joinFailLabel.setText("AGE MUST BE LARGER THAN 0")
                    except ValueError:
                            self.ui.joinFailLabel.setText("AGE CAN BE ONLY INTEGER")
                else:
                    self.ui.joinFailLabel.setText("ALREADY USED ID OR MAIL")

    def loginBtnEvent(self):
        id=self.ui.idForLoginInput.text()
        pw=self.ui.pwForLoginInput.text()
        self.cursor.execute("SELECT id, pw FROM userInfo WHERE id=? AND pw=?", [id, pw])
        result=self.cursor.fetchall()
        if len(result)==0:
            self.ui.loginFailLabel.setText("INCORRECT ID OR PW")
        else:
            self.loggedId=id
            self.game=Game.Game(self.ui)
            self.showInfo=ShowInfo.ShowInfo(self.ui)
            self.game.loadId(id)
            self.showInfo.loadId(id)
            self.ui.idSmileLabel.setText(id+" :)")
            self.menu.changeMenu()

    def logoutBtnEvent(self):
        self.loggedId=None

    def findBtnForFindIdEvent(self):
        mail=self.ui.mailForFindIdInput.text()
        self.cursor.execute("SELECT id FROM userInfo WHERE email=?", [mail])
        result=self.cursor.fetchall()
        if len(result)==0:
            self.ui.findIdFailLabel.setText("THERE'S NO MAIL YOU ENTERED")
        else:
            self.ui.findIdFailLabel.setText("YOUR ID IS "+result[0][0])

    def findBtnForFindPwEvent(self):
        id=self.ui.idForFindPwInput.text()
        mail=self.ui.mailForFindPwInput.text()
        if id=="" or mail=="":
            self.ui.findPwFailLabel.setText("PLEASE FILL IN ALL THE BLANKS")
        else:
            self.cursor.execute("SELECT pw FROM userInfo WHERE id=? AND email=?", [id, mail])
            result=self.cursor.fetchall()
            if len(result)==0:
                self.ui.findPwFailLabel.setText("ID AND MAIL DON'T BE MATCHED")
            else:
                self.ui.findPwFailLabel.setText("YOUR PW IS "+result[0][0])
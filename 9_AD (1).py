import random
class IndianPoker():
    def __init__(self):
        self.resetGame()

    def nextRound(self):
        if len(self.numlist)==0 or self.P1chip<1 or self.P2chip<1:
            self.Result #???이건 무슨 코드지??
            answer=f"게임 종료\nPlayer1:{self.P1chip}개\tPlayer2:{self.P2chip}개\n"
            if self.P1chip>self.P2chip:
                answer+="Player1 승리"
            elif self.P1chip<self.P2chip:
                answer+="Player2 승리"
            else:
                answer+="무승부"
        else:
            self.P1card=random.choice(self.numlist) 
            self.numlist1.remove(self.P1card)
            self.P2card=random.choice(self.numlist)
            self.numlist2.remove(self.P2card)
            self.P1chip-=1; self.P2chip-=1
            self.P1bet=1; self.P2bet=1
            self.Chip1.setText(str(self.P1chip))
            self.Chip2.setText(str(self.P2chip))

    def resetGame(self):
        self.numlist1=[1,2,3,4,5,6,7,8,9,10]
        self.numlist2=[1,2,3,4,5,6,7,8,9,10]
        self.P1chip=30; self.P2chip=30
        self.P1bet=0; self.P2bet=0
        self.Chip1.setText("")#이 부분은 없어도 될듯
        self.Chip2.setText("")#이 부분은 없어도 될듯2
        self.nextRound()

    def buttonClicked(self):
        button=self.sender()
        key=button.text()
        if key=="Open1":
            self.Card1.setText(str(self.P2card))
        if key=="Close1":
            self.Card1.setText("")
        if key=="Open2":
            self.Card2.setText(str(self.P1card))
        if key=="Close2":
            self.Card2.setText("")
        if key=="Call1":
            self.P1chip-=(self.P2bet-self.P1bet)
            self.P1bet=self.P2bet
            self.roundResult()
            
        if key=="Call2":
            self.P2chip-=(self.P1bet-self.P2bet)
            self.P2bet=self.P1bet
            self.roundResult()
        if key=="Raise1":
            if int(self.Betting1.text())<=self.P1chip and int(self.Betting1.text())<=self.P2chip:
                self.P1bet+=int(self.Betting1.text())
                self.P1chip-=int(self.Betting1.text())
                self.Chip1.setText(str(self.P1chip))
                self.Betting1.setText("")
            else:
                "배팅액이 너무 많습니다. 다시 입력하시오."
                self.Betting1.setText("")
        if key=="Raise2":
            if int(self.Betting2.text())<=self.P1chip and int(self.Betting2.text())<=self.P2chip:
                self.P2bet+=int(self.Betting2.text())
                self.P2chip-=int(self.Betting2.text())
                self.Chip2.setText(str(self.P2chip))
                self.Betting2.setText("") #이 부분을 잘 모르겠음.
            else:
                "배팅액이 너무 많습니다. 다시 입력하시오."
                self.Betting2.setText("")
        if key=="Die1":
            self.P2chip+=(self.P1bet+self.P2bet)
            self.roundResult()
        if key=="Die2":
            self.P1chip+=(self.P1bet+self.P2bet)
            self.roundResult()
        if key=="Next":
            self.nextRound()
        if key=="Reset":
            self.resetGame()
        
       
        
    
    def roundResult(self):
        self.Chip1.setText(str(self.P1chip))
        self.Chip2.setText(str(self.P2chip))
        a=f"Player1의 카드:{self.P1card}\tPlayer2의 카드:{self.P2card}"
        if self.P1card>self.P2card:
            a+=f"\n라운드 승자:Player1\nPlayer1의 칩:{self.P1chip+self.P1bet}+{self.P1bet}={self.P1chip+self.P1bet*2}\tPlayer2의 칩:{self.P2chip+self.P2bet}-{self.P2bet}={self.P2chip}"
        elif self.P1card<self.P2card:
            a+=f"\n라운드 승자:Player2\nPlayer1의 칩:{self.P1chip+self.P1bet}-{self.P1bet}={self.P1chip}\tPlayer2의 칩:{self.P2chip+self.P2bet}+{self.P2bet}={self.P2chip+self.P2bet*2}"
        else:
            a+=f"\n라운드 승자:무승부\nPlayer1의 칩:{self.P1chip+self.P1bet}\tPlayer2의 칩:{self.P2chip+self.P2bet}"
    
    def P1die(self):
        a=f"라운드 승자:Player2\nPlayer1의 칩:{self.P1chip+self.P1bet}-{self.P1bet}={self.P1chip}\tPlayer2의 칩:{self.P2chip+self.P2bet}+{self.P2bet}={self.P2chip+self.P2bet+self.P1bet}"
    def P2die(self):
        a=f"\n라운드 승자:Player1\nPlayer1의 칩:{self.P1chip+self.P1bet}+{self.P1bet}={self.P1chip+self.P1bet+self.P2bet}\tPlayer2의 칩:{self.P2chip+self.P2bet}-{self.P2bet}={self.P2chip}" 

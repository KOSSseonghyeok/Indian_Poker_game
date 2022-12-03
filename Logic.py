import random




class IndianPoker():
    def __init__(self):
        try:
            self.status = False 
            self.resetGame()
        except Exception as e:
            print("__init__", e)
    
    
    def nextRound(self):
        try:
            if len(self.numlist1)==0  or len(self.numlist2) == 0 or self.P1chip<1 or self.P2chip<1:
                answer=f"게임 종료\nPlayer1:{self.P1chip}개\t\t                   Player2:{self.P2chip}개\n"
                if self.P1chip>self.P2chip:
                    answer+="Player1 승리"
                elif self.P1chip<self.P2chip:
                    answer+="Player2 승리"
                else:
                    answer+="무승부"
                self.status = False
                # self.Result.setText(answer)
                return answer
            else:
                if self.status == False: #게임 중에 next를 못누르게 하기 위해서
                    self.status = True  #게임 상태를 알려줌
                    self.P1card=random.choice(self.numlist1) 
                    self.numlist1.remove(self.P1card)
                    self.P2card=random.choice(self.numlist2)
                    self.numlist2.remove(self.P2card)
                    self.P1chip-=1; self.P2chip-=1
                    self.P1bet=1; self.P2bet=1
                    return self.Bettingresult()
                else:
                    return "게임 중입니다."
        except Exception as e:
            print("nextRound", e)
            
    def resetGame(self):
        try:
            self.numlist1=[1,2,3,4,5,6,7,8,9,10]
            self.numlist2=[1,2,3,4,5,6,7,8,9,10]
            self.P1chip=30; self.P2chip=30
            self.P1bet=0; self.P2bet=0
            self.status = False
            return self.nextRound()
        except Exception as e:
            print("resetGame", e)

    
    
    def roundResult(self):
        try:
            a=f"\n\n\n\n         Player1의 카드:{self.P1card}\t                Player2의 카드:{self.P2card}"
            if self.P1card>self.P2card:
                a+=f"\n\n\n\n\t\t      라운드 승자:Player1\n\n\n\n         Player1의 칩:{self.P1chip+self.P1bet}+{self.P1bet}={self.P1chip+self.P1bet*2}\t Player2의 칩:{self.P2chip+self.P2bet}-{self.P2bet}={self.P2chip}"
                self.P1chip += self.P1bet*2
            elif self.P1card<self.P2card:
                a+=f"\n\n\n\n\t\t      라운드 승자:Player2\n\n\n\n         Player1의 칩:{self.P1chip+self.P1bet}-{self.P1bet}={self.P1chip}\t Player2의 칩:{self.P2chip+self.P2bet}+{self.P2bet}={self.P2chip+self.P2bet*2}"
                self.P2chip += self.P2bet*2
            else:
                self.P1chip += self.P1bet
                self.P2chip += self.P2bet
                a+=f"\n\n\n\n\t\t      라운드 승자:무승부\n\n\n\n         Player1의 칩:{self.P1chip+self.P1bet}\t               Player2의 칩:{self.P2chip+self.P2bet}"
            self.status = False
            return a
        except Exception as e:
            print("roundResult", e)

    def P1die(self):
        try:
            miracle = 0
            if self.P1card == 10:
                miracle = 10
            self.P2chip+=(self.P1bet+self.P2bet+miracle)
            self.P1chip -= miracle
            self.status = False            
            return f"\n\n\n\n\t\t라운드 승자:Player2\n\n\n\n          Player1의 칩:{self.P1chip+miracle+self.P1bet}-{self.P1bet+miracle}={self.P1chip}\t Player2의 칩:{self.P2chip-miracle-self.P2bet}+{self.P2bet+miracle}={self.P2chip}"

        except Exception as e:
            print("p1die", e)
            
    def P2die(self):
        try:
            miracle = 0
            if self.P2card == 10:
                miracle = 10
            self.P1chip+=(self.P1bet+self.P2bet+miracle)
            self.P2chip -= miracle
            self.status = False
            return f"\n\n\n\n\t\t라운드 승자:Player1\n\n\n\n          Player1의 칩:{self.P1chip-miracle-self.P2bet}+{self.P2bet+miracle}={self.P1chip}\t Player2의 칩:{self.P2chip+miracle+self.P2bet}-{self.P2bet+miracle}={self.P2chip}" 

        except Exception as e:
            print("p2die", e)
            
    def Bettingresult(self):
        try:
            return f"Plater1 베팅:{self.P1bet}개\t\t                   Player2 베팅:{self.P2bet}개"
        except Exception as e:
            print("Bettingresult", e)
            
    def getCard(self, n):
        if n==1:
            return self.P1card
        else:
            return self.P2card
    def getChip(self, n):
        if n==1:
            return self.P1chip
        else:
            return self.P2chip
    def getBet(self, n):
        if n==1:
            return self.P1bet
        else:
            return self.P2bet
    def Call(self, n):
        if n==1:
            self.P1chip-=(self.P2bet-self.P1bet)
            self.P1bet=self.P2bet
        else:
            self.P2chip-=(self.P1bet-self.P2bet)
            self.P2bet=self.P1bet
    def Raise(self, n, a):
        if(a.isdigit() == False): #숫자가 아닌 글자가 입력될 경우 예외 처리
            return "다시 입력해주세요"
        
        if n==1:
            if self.P1bet+int(a)<=self.P2bet: #raise 조건에 부합하지 않을 경우 두가지
                return "low"
            elif int(a)>self.P1chip or int(a)>self.P2chip:
                return "high"
            self.P1bet+=int(a)
            self.P1chip-=int(a)
        else:
            if self.P2bet+int(a)<=self.P1bet:
                return "low"
            elif int(a)>self.P1chip or int(a)>self.P2chip:
                return "high"
            self.P2bet+=int(a)
            self.P2chip-=int(a)

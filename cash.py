# 은행 프로그램
import os

# 파일 입출력 방식
# file = "C:/Users/박준형/Desktop/은행계좌만들기/bank.txt"
file = "C:/Users/coke/Desktop/항공대/멋사/계좌 만들기/bank.txt"
#f = open(file,"r")
all_id = list() 


#한 사람의 계좌정보를 담아서 관리할 목적으로 구현되는 클래스
class Account:
    def __init__(self, userid= "", name = "", balance=0):        # 생성자
        if(userid == ""):
            self.userid = input("계좌번호 : ")
            self.name = input("이름 : ")
            self.balance = int(input("예금 : "))
            print("##계좌개설을 완료하였습니다##")
        else:
            self.userid = userid
            self.name = name
            self.balance = balance
            
    # 출력함수
    def disp(self):            
        print("계좌번호:{0}\t이름: {1}\t잔액: {2}".format(self.userid, self.name, self.balance))
    
    # 데이터 호출 함수
    def info(self):
        return "{0}:{1}:{2}\n".format(self.userid, self.name, self.balance)
    
    # 
    def getid(self):
        return self.userid
    
    # 입금
    def deposit(self, money):
        self.balance += money
        return self.balance
    
    # 출금
    def withdraw(self, money):
        self.balance -= money
        return self.balance
    
    # 잔액 조회
    def getBalance(self):     
        return self.balance

###########################
# 저장된 계좌 파일 호출                 
try:
    f = open(file,"r")
    
    while True:
        line = f.readline()
        if not line:
            break

        a,b,c = line.split(":")
        all_id.append(Account(a,b,int(c)))
    f.close()
except Exception as ex:
    print("파일 없습니다")
    print(ex)

    
###########################
# 계좌정보를 이용하여 구현될 기능을 담고 있는 클래스 멤버필드 
# 멤버메서드 : makeAccount() - 계좌개설을 담당할 메서드
class BankManager:
    # 출금처리를 담당할 메서드
    def withdraw(self,userid):    
        for i in all_id:
            if i.getid() == userid:
                print("계좌이름 : ",i.name)
                print("계좌잔고 : ",i.balance)
                money = int(input("출금하실 금액을 입력해주세요 : "))
                if money < i.balance:
                    bal = i.withdraw(money)
                    print("\n##계좌잔고 : {0} 원##".format(bal))
                    print("##출금이 완료되었습니다##")
                else:
                    print("잔액 부족")
                return 0
        print("일치하는 계좌번호가 존재하지 않습니다")

        
    # 입금처리를 담당할 메서드
    def deposit(self,userid):     
        for i in all_id:
            if i.getid() == userid:
                print("계좌이름 : ",i.name)
                print("계좌잔고 : ",i.balance)
                money = int(input("입금하실 금액을 입력해주세요 : "))
                if money >= 0:
                    bal = i.deposit(money)
                    print("\n##계좌잔고 : {0} 원##".format(bal))
                    print("##입금이 완료되었습니다##")
                else:
                    print("금액 입력이 올바르지 않습니다.")
                return 0
        print("일치하는 계좌번호가 존재하지 않습니다")

    
    # 계좌번호의 중복여부를 판단할 메서드
    def new_id(self,user):             
        for i in all_id:
            if i.getid() == user.getid():
                return "입력하신 계좌번호는 이미 존재하는 계좌번호 입니다."
            
        all_id.append(user)
        return "계좌 개설이 완료되었습니다."   
    
    # 전체고객의 계좌정보를 출력할 메서드
    def showAccount(self):      
        for i in all_id: 
          print("계좌번호:{0}\t이름: {1}\t잔액: {2}".format(i.userid, i.name,  i.balance))
                
    # 파일 저장 메서드
    def save(self):
        f = open(file,"w")
        for i in all_id:
            f.write(i.info())
            
        f.close()


    # 계좌 이체 메서드
    def send(self,userid):
        money = int(input("송금할 금액을 입력해주세요 : "))
        sendid = input("{0}원을 받을 분의 계좌를 입력해주세요 : ".format(money))      # (money ,"원을 받을 분의 계좌를 입력해주세요 :") 를 Format 연산자로 변경 220502 14:49)
        SendOK = False
        for i in all_id:
            if money > 0 :
            # bal = i.deposit(money)
                if i.getid()==userid:                   # 송금계좌 확인
                    i.withdraw(money)                   # 출금
                if i.getid()==sendid:
                    i.deposit(money)                    # 입금
                    SendOK = False
            else:
                print("금액 입력이 올바르지 않습니다.")
                return 0
        if SendOK:
            print("송금에 실패하였습니다.")
        else:
            print("계좌번호 {0}로 {1}원이 송금 되었습니다.".format(sendid,money))

            
############################
# 사용자와의 인터페이스를 담당할 목적의 클래스
class BanckingSystem: 
    def run():
        while True:
            print("======Bank Menu======")
            print("1. 계좌개설")
            print("2. 입금하기")
            print("3. 출금하기")
            print("4. 전체조회")
            print("5. 계좌이체")
            print("6. 프로그램 종료")
            print("=====================")
            ch = input("입력 : ")
            if ch == "1":       # 계좌개설
                print("=======계좌개설=======")
                print(BankManager().new_id(Account()))
                print("=====================")
                
            elif ch == "2":     # 입금
                print("=======입금하기=======")
                userid = input("입금하실 계좌번호를 입력해주세요 : ")
                BankManager().deposit(userid)
                print("=====================")
                 
            elif ch == "3":    # 출금
                print("========출 금========")
                userid = input("출금하실 계좌번호를 입력해주세요 : ")
                a = BankManager().withdraw(userid)
                if a == None:
                    print("{0}원 출금하셨습니다.".format(a))
                print("=====================")
            
            elif ch == "4":     # 조회
                print("========조 회========")
                BankManager().showAccount()
                print("=====================")

            elif ch == "5":     # 추가기능
                print("=======계좌이체=======")
                userid = input("송금하실 계좌번호를 입력해주세요 : ")
                BankManager().send(userid)
                print("=====================")
                
                
            elif ch == "6":     # 종료
                BankManager().save()
                print("종료")
                break

##############################
if __name__ =='__main__':
    BanckingSystem.run()
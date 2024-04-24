from datetime import date as d           #to get current date
from pandas import DataFrame             #to convert dictionary into row and coloms so,that only import DataFrame
class bank:
    b_name='SBI'
    branch='VADA'
    ifsc='SBIN000234'
    manager='Shahith'
    def __init__(self,name,ac,mob,bal):
        self.name=name
        self.ac=ac
        self.mob=mob
        self.bal=bal
        self.st={'Date':[d.today()],'CR':['_'],'DR':['_'],'Balance':[self.bal]}
    def details(self):
        print(f'{"="*8} BANK DETAILS {"="*8}\n'
              f'Bank_name:{self.b_name}\n'
              f'IFSC:{self.ifsc}\n'
              f'Manager:{self.manager}\n'
              f'{"="*8} CUSTOMER DETAILS {"="*8}\n'
              f'Name:{self.name}\n'
              f'Account:{self.ac}\n'
              f'Mobile_no:{self.mob}\n'
              f'Balance:{self.bal}\n'
              f'{"-"*30}\n')
    def deposit(self,amt):
        if amt > 0:
            self.bal += amt
            print(f'{amt}Rs got Credited to your account\n'
                  f'Total Balance:{self.bal}\n'
                  f'{"_"*30}\n')
            self.st['Date'] += [d.today()]
            self.st['CR'] += [amt]
            self.st['DR'] += ['_']
            self.st['Balance'] += [self.bal]
        else:
            print('Enter Valid Amount')
    def deposit(self,amt):
        if amt <= self.bal:
            if amt%100==0:
                self.bal-=amt
                print(f'{amt} RS debited from your account\n'
                      f'Total Balance:{self.bal}\n'
                      f'{"_"*30}\n')
                self.st['Date'] += [d.today()]
                self.st['CR'] += ['_']
                self.st['DR'] += [amt]
                self.st['Balance'] += [self.bal]
            else:
                print('Enter valid amount \n either 100rs,200rs or 500rs')
        else:
            print('Insufficient Balance')
    def transfer(self,cus,amt):
        if amt <= self.bal:
            self.bal-=amt
            cus.bal += amt
            print(f'{amt}RS transfered successfully to {cus.name}')
            self.st['Date'] += [d.today()]
            self.st['CR'] += ['_']
            self.st['DR'] += [amt]
            self.st['Balance'] += [self.bal]
            cus.st['Date'] += [d.today()]
            cus.st['CR'] += [amt]
            cus.st['DR'] += ['_']
            cus.st['Balance'] += [cus.bal]
        else:
            print("Insufficient Balance")
    def interest(self,rate=5.4):
        iamt = self.bal*(rate/100)
        self.bal += iamt
        print(f' your account got credited {iamt}RS as interest \n'
              f'Total Balance:{self.bal}')
    def statement(self):
        df=(self.st)
        print(df)
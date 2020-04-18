'''
Created on 18-Apr-2020

@author: ila roy
'''
#OOPR-Prac-9
#Start writing you code here
class SmartCard:
    def __init__(self,card_no):
        self.__card_no = card_no
        self.__account_balance = None
    
    def get_card_no(self):
        return self.__card_no
    def get_account_balance(self):
        return self.__account_balance
    
    def set_account_balance(self,account_balance):
        self.__account_balance=account_balance

class Transaction:
    def __init__(self):
        self.__transaction_id=None
    
    def get_transaction_id(self):
        return self.__transaction_id
    
    def top_up_card(self,employee, amount):
        if amount>= 500 and amount <=10000:
            if employee.validate_employee_id() and employee.validate_card_no():
                new_amount=employee.smart_card.get_account_balance()
                if new_amount == None:
                    employee.smart_card.set_account_balance(amount)
                else:
                    new_amount+=amount 
                    employee.smart_card.set_account_balance(new_amount)
            else:
                return -1
        else:
            return -1 
    
    def make_payment(self,employee, amount):
        if employee.smart_card.get_account_balance() > amount:
            if employee.smart_card.get_account_balance() and employee.validate_employee_id():
                debit_amount= employee.smart_card.get_account_balance() - amount
                if debit_amount >= 500:
                    y=str(employee.get_employee_id())
                    self.__transaction_id= "T" + y[0] + str(employee.smart_card.get_card_no()[3:5])
                    employee.smart_card.set_account_balance(debit_amount)
                else:
                    return -1 
            else:
                return -1
        else:
            return -1

class Employee:
    def __init__(self,employee_id, employee_name, smart_card):
        self.__employee_id=employee_id
        self.__employee_name=employee_name
        self.smart_card = smart_card
    
    def get_employee_id(self):
        return self.__employee_id
    def get_employee_name(self):
        return self.__employee_name
        
    def validate_employee_id(self):
        if self.__employee_id >1000 and self.__employee_id <= 700000:
            return True
        else:
            return False
            
    def validate_card_no(self):
        x=self.smart_card.get_card_no()
        if len(x) == 9 :
            if x.startswith("INF"):
                if x[3:].isdigit():
                    return True 
                else:
                    return False 
            else:
                return False 
        else:
            return False 
            
s=SmartCard("INF453722")
e1=Employee(1005,"Sam",s)
t1=Transaction()
print(e1.validate_card_no())
print(e1.validate_employee_id())
t1.top_up_card(e1,1000)
print(t1.make_payment(e1,500))
x=s.get_account_balance()
print(x)
t=t1.get_transaction_id()
print(t)
print(s.get_card_no())
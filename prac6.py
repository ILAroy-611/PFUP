'''
Created on 17-Apr-2020

@author: ila roy
'''
#OOPR-Prac-6
#Note: Verification is not available for this problem, however you can submit your code

#Start writing you code here

class Loan:
    __loan_counter = 1001
    def __init__(self):
        self.__loan_id=None
        self.__loan_amount=None
        self.__interest_rate=None
        
    def generate_loan_id(self):
        Loan.__loan_counter+=1 
        self.__loan_id=Loan.__loan_counter
        
      
    def calculate_amount_interest_rate(self,monthly_salary):
        pass 
    def set_loan_amount(self,loan_amount):
        self.__loan_amount=loan_amount
    def set_interest_rate(self,interest_rate):
        self.__interest_rate=interest_rate
    def get_loan_id(self):
        return self.__loan_id
    def get_loan_amount(self):
        return self.__loan_amount
    def get_interest_rate(self):
        return self.__interest_rate
        
class HomeLoan(Loan):
    def __init__(self):
        super().__init__()
        self.__points=5
        
    def get_points(self):
        return self.__points
        
    def calculate_amount_interest_rate(self,monthly_salary):
        if monthly_salary>=20000:
            amount=15*monthly_salary
            self.set_loan_amount(amount)
            self.set_interest_rate(15)
            self.generate_loan_id()
        else:
            return -1 
            
class PersonalLoan(Loan):
    def __init__(self):
        super().__init__()
        self.__gift_voucher=500
        
    def get_gift_voucher(self):
        return self.__gift_voucher
        
    def calculate_amount_interest_rate(self,monthly_salary):
        if monthly_salary>=7000:
            amount=5*monthly_salary
            self.set_loan_amount(amount)
            self.set_interest_rate(12)
            self.generate_loan_id()
        else:
            return -1 

class Customer:
    __customer_id_list=[1,2,3,4,5]
    def __init__(self,loan_type, monthly_salary):
        self.__customer_id=Customer.__customer_id_list[-1]+1
        Customer.__customer_id_list.append(self.__customer_id)
        self.__loan_type=loan_type
        self.__monthly_salary=monthly_salary
        self.__loan=None
        
    def apply_loan(self):
        if self.__loan_type=="Home" or self.__loan_type=="Personal":
            if self.__loan_type=="Home":
                loan_obj=HomeLoan()
                loan_obj.calculate_amount_interest_rate(self.__monthly_salary)
                self.__loan=loan_obj
            
            else:
                loan_obj=PersonalLoan()
                loan_obj.calculate_amount_interest_rate(self.__monthly_salary)
                self.__loan=loan_obj
            
                
    def get_customer_id(self):
        return self.__customer_id
    def get_loan_type(self):
        return self.__loan_type
    def get_monthly_salary(self):
        return self.__monthly_salary
    def get_loan(self):
        return self.__loan

c=Customer("Home",25000)
c.apply_loan()
x=c.get_loan().get_loan_amount()
print(x)
x=c.get_loan().get_interest_rate()
print(x)
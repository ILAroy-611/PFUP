'''
Created on 16-Apr-2020

@author: ila roy
'''
#OOPR-Prac-10
#Start writing you code here
class Laptop:
    def __init__(self,grcode, expiry):
        self.__grcode=grcode
        self.__expiry=expiry
    def get_grcode(self):
        return self.__qrcode
    def get_expiry(self):
        return self.__allocation_expiry_date
    

class Scanner:
    def __init__(self,emp_laptop_dict):
        self.__emp_laptop_dict=emp_laptop_dict
    
    def validate_emp_laptop(self,emp_id,laptop):
        for key,value in self.__emp_laptop_dict.items():
            if emp_id==key:
                if laptop==self.__emp_laptop_dict[key]:
                    return True
                else:
                    return False
            else:
                return False
    
    def validate_expiry(self,laptop):
        for key,value in self.__emp_laptop_dict.items():
            if value==laptop:
                if self.__emp_laptop_dict[key].get_expiry==True:
                    return True
                else:
                    return False
            else:
                flag=0 
        if flag==0 :
            return True
        
    def scan(self,empid,laptop):
        for key,value in self.__emp_laptop_dict.items():
            if self.validate_expiry(value):
                if self.validate_emp_laptop(key,validate_emp_laptop):
                    return True
                else:
                    return False
            else:
                return False
    def get_emp_laptop_dict(self):
        return self.__emp_laptop_dict
    
   

l1=Laptop("UAL1",True)
l2=Laptop("CSK2",False)
l3=Laptop("DD12",False)
emp_laptop_dict={101:l1,102:l2,103:l3}
'''
 
'''
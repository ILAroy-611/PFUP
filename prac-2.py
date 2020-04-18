'''
Created on 14-Apr-2020

@author: ila roy
'''
#OOPR-Prac-2
#Start writing you code here
class Dog:
    counter=100 
    dog_breed_dict={"Labrador Retriever":5,"German Shepherd":12,"Beagle":0}
    def __init__(self,breed_list,accessories_required):
        self.__dog_id_list=[]
        self.__breed_list=breed_list
        self.__price=0
        self.__accessories_required=accessories_required
        
    def get_dog_id_list(self):
        return self.__dog_id_list
    def get_breed_list(self):
        return self.__breed_list
    def get_price(self):
        return self.__price
    def get_accessories_required(self):
        return self.__accessories_required
        
    def get_dog_price(self,breed):
        price=0 
        if breed=="Labrador Retriever":
            price=800
        elif breed=="German Shepherd":
            price=1230
        elif breed=="Beagle":
            price=650 
        return price
        
    def generate_dog_id(self,breed):
        Dog.counter+=1 
        dog_id=breed[0]+str(Dog.counter)
        return dog_id
        
    def validate_breed(self):
        for i in self.__breed_list:
            if i in Dog.dog_breed_dict:
                flag=1 
            else:
                flag=0 
                break 
        if flag==0:
            return False
        else:
            return True
            
    def validate_quantity(self):
        for i in self.__breed_list:
            if i in Dog.dog_breed_dict:
                if Dog.dog_breed_dict[i]>=1 :
                    flag=1 
                else:
                    flag=0 
                    break 
            else:
                flag=0 
                break 
        if flag==0:
            return False
        else:
            return True
            
    def calculate_total_price(self):
        if self.validate_quantity():
            if self.validate_breed():
                for i in self.__breed_list:
                    Dog.dog_breed_dict[i]-=1 
                    word=self.generate_dog_id(i)
                    self.__dog_id_list.append(word)
                    self.__price+=self.get_dog_price(i)
                if self.__accessories_required:
                    self.__price+=350
                if self.__price>1500:
                    self.__price=0.95*self.__price
            else:
                return -1 
        else:
            return -2 
d=Dog(["Labrador Retriever", "beaGLE"],True)
x=d.calculate_total_price()
print(x)
x=d.get_price()
print(x)
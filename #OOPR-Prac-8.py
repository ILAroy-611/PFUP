'''
Created on 18-Apr-2020

@author: ila roy
'''
#OOPR-Prac-8
#Start writing you code here
class CabRepository:
    cab_type_list = ['Sedan', 'SUV', 'Hatch Back']
    charge_per_km = [17, 15, 13]
    no_of_cars = [5, 4, 0]

class CabService:
    __counter = 1000
    def __init__(self,cab_type, distance_in_kms):
        self.__cab_type=cab_type
        self.__distance_in_kms=distance_in_kms
        self.__service_id= None

    def get_cab_type(self):
        return self.__cab_type
    def get_distance_in_kms(self):
        return self.__distance_in_kms
    def get_service_id(self):
        return self.__service_id
    def get_cab_charge(self):
        pass 
        
    def calculate_waiting_charge(self,waiting_time_mins):
        if waiting_time_mins <=30 :
            waiting_amount=0 
        else:
            waiting_amount= (waiting_time_mins-30)*5 
        return waiting_amount
            
    def get_cab_charge(self,index):
        return CabRepository.charge_per_km[index]
        
    def booking(self,waiting_time_mins):
        total_amount=0 
        charge=0 
        index=self.check_availability()
        if index!=-1 :
            waiting_amount=self.calculate_waiting_charge(waiting_time_mins)
            charge_per_km=self.get_cab_charge(index)
            charge= charge_per_km*self.__distance_in_kms
            CabRepository.no_of_cars[index]=CabRepository.no_of_cars[index]-1 
            CabService.__counter+=1 
            self.__service_id=CabService.__counter
            total_amount+=waiting_amount+charge
            return total_amount
        else:
            return -1 
            
    def check_availability(self):
        if self.__cab_type in CabRepository.cab_type_list:
            index=CabRepository.cab_type_list.index(self.__cab_type)
            if CabRepository.no_of_cars[index]>0:
                return index 
            else:
                return -1
        else:
            return -1 
c1=CabService("Sedan",10)
print(c1.booking(30))

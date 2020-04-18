'''
Created on 18-Apr-2020

@author: ila roy
'''
#OOPR-Prac-7
#Start writing you code here
class Project:
    def __init__(self,project_id,number_of_employees):
        self.__project_id=project_id
        self.__number_of_employees=number_of_employees

    def get_project__id(self):
        return self.__project_id
    def get_number_of_employees(self):
        return self.__number_of_employees
        
    def update_number_of_employees(self):
        self.__number_of_employees+=1 

class Employee:
    __employee_count=1000
    def __init__(self):
        self.__employee_id=None
        
    def generate_employee_id(self):
        Employee.__employee_count+=1
        self.__employee_id= "E" + str(Employee.__employee_count)
        
    def get_employee_id(self):
        return self.__employee_id
        
class Department:
    __dep_project_list=[]
    __employee_dict={}
    @staticmethod
    def add_project(project_list) :
        x=len(project_list)+len(Department.__dep_project_list)
        if x <= 5 :
            for i in project_list:
                Department.__dep_project_list.append(i)
        else:
            return -1 
            
    @staticmethod
    def add_employee(employee, project_id):
        flag=1 
        for i in Department.__dep_project_list:
            if project_id ==i.get_project__id():
                if i.get_number_of_employees()<10:
                    employee.generate_employee_id()
                    Department.__employee_dict.update({employee.get_employee_id():project_id})
                    i.update_number_of_employees()
                    flag=1 
                    break 
                else:
                    print("project can not have more than 10 employees")
                    return -2 
            else:
                flag=0 
        if flag==0 :
            print("project not found")
            return -1
                
e1=Employee()
p1=Project(20,1)
p2=Project(30,1)
p3=Project(40,1)
p4=Project(50,1)
project_list=[p1,p2,p3,p4]
Department.add_project(project_list)
Department.add_employee(e1,30)
print(e1.get_employee_id())

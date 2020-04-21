'''
Created on 21-Apr-2020

@author: ila roy
'''
#DSA-Assgn-25

def find_number_of_platforms(arrival_time_list,departure_time_list):
    #Remove pass and test your program
    count = 0
    low = 0 
    arrival_time_list.sort()
    departure_time_list.sort()
    for i in departure_time_list :
        for j in arrival_time_list :
            if arrival_time_list[low] < i:
                count+=1 
                low+=1 
                
        if count>=len(arrival_time_list)-low:
            break 
         
    return count

#Pass different values to the function and test your program
arrival_time_list = [800,810]
departure_time_list = [2300,2000]
print("The arrival time of the trains:", arrival_time_list)
print("The departure time of the trains:",departure_time_list)
print("Minimum number of platforms required :",find_number_of_platforms(arrival_time_list,departure_time_list))
arrival_time_list = [800, 810, 900, 740, 1200, 1400]
departure_time_list=[2300, 2000, 1200, 1349, 1500, 2120]
print("The arrival time of the trains:", arrival_time_list)
print("The departure time of the trains:",departure_time_list)
print("Minimum number of platforms required :",find_number_of_platforms(arrival_time_list,departure_time_list))
print("The arrival time of the trains:", arrival_time_list)
print("The departure time of the trains:",departure_time_list)
arrival_time_list=[940, 1010, 300, 830, 720, 1400]
departure_time_list= [1000, 1500, 440, 840, 930, 1540]
print("The arrival time of the trains:", arrival_time_list)
print("The departure time of the trains:",departure_time_list)
print("Minimum number of platforms required :",find_number_of_platforms(arrival_time_list,departure_time_list))
print("The arrival time of the trains:", arrival_time_list)
print("The departure time of the trains:",departure_time_list)
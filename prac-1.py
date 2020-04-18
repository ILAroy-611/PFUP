'''
Created on 14-Apr-2020

@author: ila roy
'''
#OOPR-Prac-1
#Start writing you code here
class Purchase:
    list_of_items=['Apple', 'Biscuits', 'Chocolates', 'Jam', 'Butter', 'Milk', 'Soap', 'Hand Sanitizer']
    list_of_count_of_each_item_sold=[0]*len(list_of_items)
    def __init__(self):
        self.__items_purchased=[]
        self.__item_on_offer=None
    def get_items_purchased(self):
        return self.__items_purchased
    def get_item_on_offer(self):
        return self.__item_on_offer
    def sell_items(self,list_of_items_to_be_purchased):
        count=0 
        for i in list_of_items_to_be_purchased:
            for j in range(0,len(Purchase.list_of_items)):
                if i.lower()==Purchase.list_of_items[j].lower():
                    count+=1 
                    Purchase.list_of_count_of_each_item_sold[j]=count 
                    count=0 
                    self.__items_purchased.append(i.lower())
                    if i.lower()=="soap":
                        self.provide_offer()
                    break 
                    
    def provide_offer(self):
        self.__item_on_offer="HAND SANITIZER"
        count=0 
        for i in range(0,len(Purchase.list_of_items)):
            if "hand sanitizer" == Purchase.list_of_items[i].lower():
                count+=1 
                Purchase.list_of_count_of_each_item_sold[i]=count 
                count=0 

    @staticmethod   
    def find_total_items_sold():
        sum=0 
        for i in Purchase.list_of_count_of_each_item_sold:
            sum+=i 
        return sum 
s= Purchase()
s.sell_items(['JAM', 'CHOcolates', 'Ghee', 'Soap'])
x=s.get_items_purchased()
print(x)
x=s.get_item_on_offer()
print(x)
x=Purchase.find_total_items_sold()
print(x)
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 11:44:51 2018

@author: RPS
"""
"""
data=[45,65,"D","true","False",4e5]
print(data)

for _ in data:
    if(type(_) is int):
        print(_)
        
        
import random
idlist=[]
for _ in range(1,50):
    idlist.append(random.randint(1,1000))
    
print(idlist)    

idlist.sort();
print(idlist)
idlist.reverse()
print(idlist)

names=["CITI","POL","GOOGLE"]
names.sort()
print(names)
print(names[0:])

"""
"""
emplist=[[1,"Anoop","Chennai"],[2,"Gayathri","Mumbai"],[3,"Dev","Kolkatta"]]
for row in emplist:
    print(row[0])
    for _ in row:
        if(_ is "Chennai"):
            print(row[1])
            
"""            
            
list1=["Chennai","Bangalore","Pune"]            
list2=["TN","KN","MH"]
idlist=[]

for(x,y) in zip(list1,list2):
    print(x,y)
    print(x+y)
idlist.append(x+y)    

print(idlist)
    
#join operations

print(("->").join(list1+list2))    


    
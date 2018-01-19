# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 14:20:10 2018

@author: RPS
"""
import datetime
print(datetime.datetime.now().hour)

def cutoff(amount):
    currtime=datetime.datetime.now().hour;
    if(currtime > 17):
        print ("tomorrow")
    else:
        print ("ok")
        
cutoff(56)        




   # for (key,value) in datelist.items():
   # print(("->").join(str(key)+str(value))
   # print(key,"=",value) 
   

   
       
       
#holidaydates()  

#import holidays
#from datetime import date
#holidays(date.today().strftime("%d/%m/%Y"));
#holidays('1/1/2018')
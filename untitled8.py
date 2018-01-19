# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 14:13:36 2018

@author: RPS
"""

def holidaydates():

    datelist={"20180101":{"reason":"New Year"},
                "20180126":{"reason":"Republic Day"}}


    for (key,value) in datelist.items():
   # print(("->").join(str(key)+str(value))
       print(key,"=",value) 
       
       
holidaydates()       
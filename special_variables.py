# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 13:48:37 2018

@author: RPS
"""

#if __name__ == "__main__":
#        print("in main module")
#else:
#    print("not in main module")    

def dictionarymemo():

    productInfo={"productid":356,"productname":"laptop","price":45000,"brand":"acer"}
    print(productInfo.keys())
    print(productInfo.values())


    for (key,value) in productInfo.items():
   # print(("->").join(str(key)+str(value))
       print(key,"=",value)   
   
   
dictionarymemo()
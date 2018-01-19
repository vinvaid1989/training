# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 12:25:00 2018

@author: RPS
"""
"""
data=(56,"Max",True)
print(data)


custData=[(1,"Suman","Chennai"),(2,"Anand","Bangalore"),(3,"Arup","Mumbai")]

print(custData[0])
custData.append((4,"Raja","Pune"))

print(custData)

"""
"""
#Dictionary

productInfo={"productid":356,"productname":"laptop","price":45000,"brand":"acer"}
print(productInfo.keys())
print(productInfo.values())


for (key,value) in productInfo.items():
   # print(("->").join(str(key)+str(value))
   print(key,"=",value)

"""

#Dictionary and list

productinfo = {"123":{"productname":"mobile","brand":"samsung",
                      "features":["bluetooth","wifi","frontcam"]},
                "425":{"productname":"mobile","brand":"apple",
                       "features":["bluetooth","wifi","frontcam"]}

}
                
                
for (key,value) in productinfo.items():
    print(key,"->",value)
    
for _ in productinfo.keys():
    for inner in productinfo[_].keys():
        if(inner is "brand"):
            print(productinfo[_][inner])
































# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 10:48:20 2018

@author: RPS
"""
"""
name="String Functions"
print(name.center(len(name)+20,'*'));
print(name.ljust(len(name)+20,'*'));
print(name.rjust(len(name)+20,'*'));

amt=str(6565)
print(amt.center(len(amt)+20,'*'));
"""

#convert to base 64 data
import base64
sqno=456
base64Data=base64.b64encode(str(sqno).encode(encoding='utf-8',errors='strict'))
print(base64Data)

#for loop
coursename="Python"
for _ in coursename[0:]:
    print(chr(int(_)),end="")

 
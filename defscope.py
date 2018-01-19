# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 14:40:07 2018

@author: RPS
"""

amount=4567

def testscope():
    global amount
    amount=100
    print(amount)
    
testscope()
print(amount)    
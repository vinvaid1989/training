# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 14:48:37 2018

@author: RPS
"""

import os;
path="C:/Users/RPS/Desktop/python";
for (dirpath,dirnames,filenames) in os.walk(path):
    
    print(filenames);
    
    for file in filenames:
        (shortname, extension) = os.path.splitext(file)
        print(shortname,extension)
        if(extension=='.py'):
            contents=open(path+"/"+file,'r')
            for line in contents:
                print(line)
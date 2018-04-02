# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 17:07:16 2018

@author: SAMEERGO
"""

cnt = 0
f = open('CV.txt','r')
lines = f.readlines()
lines = [x.strip() for x in lines]
print(lines)
for word in lines:
    if word == "Correct":
        cnt = cnt+1
print("Classification accuracy =",cnt*100/len(lines))
f.close()
f = open('CV.txt','w')
f.close()


#%%
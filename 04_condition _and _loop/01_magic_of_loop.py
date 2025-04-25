# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n = int(input(""))
x = int(input("")) 
for i in range(1, n+1):
    print(i)
    if(x % 2 == 0):
        x = x / 2
    else:
        x = x * 2 - 1
print(int(x))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 18:34:50 2019

@author: twang
"""

with open('northwind.txt', 'r') as f:
    wholefile = f.read()
    wholefile = wholefile.split()
    d={}
    for word in wholefile:
        if word not in d:
            d[word]=0
        d[word]+=1
        print(d.items())
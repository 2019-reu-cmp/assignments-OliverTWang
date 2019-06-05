#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 04:36:08 2019

@author: twang
"""
import statistics
day = []
nspot = []

with open('sunspots.txt', 'r') as f:
    for line in f:
        l = line.split()
        day.append(l[0])
        nspot.append(float(l[1]))
    average = statistics.mean(nspot)
    print('average number of sunspots per day is:', average)


    low = input("What is the lowest daily sunspot that counts?")
    high = input("What is the highest daily sunspot that counts?")
    if (low > high):
        print('Range minimum cannot be higher than range maximum')
    else:
        total = 0
        for d in nspot:
            if (float(d) < float(high)) and (float(d) > float(low)):
                total += 1
        print('Total number of days within range is:', total)
                
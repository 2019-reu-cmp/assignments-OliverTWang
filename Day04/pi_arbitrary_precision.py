#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:02:16 2019

@author: twang
"""

from mpmath import mp
mp.dps = 50 #set prescision to 50 digits (decimal)
pi = mp.mpf( mp.pi )
pi_2 = mp.fdiv(pi, 2) 

mp.fsub(2, 2E-5) #bad
mp.fsub(2, '2E-5') #good 

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:28:20 2019

@author: twang
"""

import numpy as np
import matplotlib.pyplot as plt
filename = 'sunspots.tsv'
num,spot = np.loadtxt(filename, unpack=True)
plt.plot(num,spot, 'x', markersize=1)

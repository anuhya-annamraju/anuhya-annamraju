# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 16:52:21 2022

This file shows the difference between scatter plots and line plots

@author: AA
"""

from matplotlib import pyplot as plt

#Close previous figures if any is open
plt.close('all')

#Line Plots and Scatter Plots
fig, axes = plt.subplots(2,2)
# axes is a multidimensional numpy array
axes[0][0].plot([1,2,3,4,5,6,7,8,9],[1,23,32,43,47,58,6,77,28],marker = 'x')
axes[0][0].set_title("Plot with Marker x")
axes[0][1].scatter([1,2,3,4,5,6,7,8,9],[11,3,100,53,49,82,16,107,128])
axes[0][1].set_title("Scatter without Marker")
axes[1][0].scatter([1,2,3,4,5,6,7,8,9],[156,38,12,93,37,48,86,27,238], marker = 'x')
axes[1][0].set_title("Scatter with Marker x")
axes[1][1].plot([1,2,3,4,5,6,7,8,9],[14,243,322,413,57,89,49,71,98])
axes[1][1].set_title("Plot without Marker")

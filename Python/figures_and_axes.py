# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 16:31:03 2022

This file shows the different methods used to create 
matplotlib figures and subplots inside figures.

@author: Anuhya Annamraju
"""

from matplotlib import pyplot as plt

#Close previous figures if any is open
plt.close('all')

#Single Figure with No Axis
fig = plt.figure()
plt.plot([1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9])
plt.title("Single Figure Without Axes")

#Add Axis to Single Figure with No Axis
fig = plt.figure()
ax = plt.subplot()
ax.plot([1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9])
plt.title("Adding Axis to Single Figure Without Axes")

#Single figure with single axis
fig, ax = plt.subplots()
ax.plot([1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9])
plt.title("Single Figure With Single Axis")


#Single figure with single axis and multiple plots
fig, ax = plt.subplots()
ax.plot([1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9])
ax.plot([1,2,3,4,5,6,7,8,9],[1,23,32,43,47,58,6,77,28])
ax.plot([1,2,3,4,5,6,7,8,9],[11,3,100,53,49,82,16,107,128])
plt.title("Single Figure With Single Axis And Multiple Plots")


#Single figure with multiple axes
fig, axes = plt.subplots(2,2)
# axes is a multidimensional numpy array
axes[0][0].plot([1,2,3,4,5,6,7,8,9],[1,23,32,43,47,58,6,77,28])
axes[0][0].set_title("Title of Axes[0][0]")
axes[0][1].plot([1,2,3,4,5,6,7,8,9],[11,3,100,53,49,82,16,107,128])
axes[0][1].set_title("Title of Axes[0][1]")
axes[1][0].plot([1,2,3,4,5,6,7,8,9],[156,38,12,93,37,48,86,27,238])
axes[1][0].set_title("Title of Axes[1][0]")
axes[1][1].plot([1,2,3,4,5,6,7,8,9],[14,243,322,413,57,89,49,71,98])
axes[1][1].set_title("Title of Axes[1][1]")

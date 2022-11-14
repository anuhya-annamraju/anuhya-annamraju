# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 16:31:03 2022

This file shows the different methods used to create 
matplotlib figures and subplots inside figures.

@author: Anuhya Annamraju
"""

from matplotlib import pyplot as plt

data_x = [1,2,3,4,5,6,7,8,9]
data_y = [1,2,3,4,5,6,7,8,9]

#Close previous figures if any is open
plt.close('all')

#Single Figure with No Axis
fig = plt.figure()
plt.plot(data_x,data_y)
plt.title("Single Figure Without Axes")

#Add Axis to Single Figure with No Axis
fig = plt.figure()
ax = plt.subplot()
ax.plot(data_x,data_y)
plt.title("Adding Axis to Single Figure Without Axes")

#Single figure with single axis
fig, ax = plt.subplots()
ax.plot(data_x,data_y)
plt.title("Single Figure With Single Axis")


#Single figure with single axis and multiple plots
fig, ax = plt.subplots()
ax.plot(data_x,data_y)
data_y = [1,23,32,43,47,58,6,77,28]
ax.plot(data_x,data_y)
data_y = [11,3,100,53,49,82,16,107,128]
ax.plot(data_x,data_y)
plt.title("Single Figure With Single Axis And Multiple Plots")


#Single figure with multiple axes
fig, axes = plt.subplots(2,2)
# axes is a multidimensional numpy array
data_y = [1,23,32,43,47,58,6,77,28]
ax = axes[0][0]
ax.plot(data_x,data_y)
ax.set_title("Title of Axes[0][0]")

data_y = [11,3,100,53,49,82,16,107,128]
ax = axes[0][1]
ax.plot(data_x,)
ax.set_title("Title of Axes[0][1]")

data_y = [156,38,12,93,37,48,86,27,238]
ax = axes[1][0]
ax.plot(data_x,data_y)
ax.set_title("Title of Axes[1][0]")

data_y = [14,243,322,413,57,89,49,71,98]
ax = axes[1][1]
ax.plot(data_x,data_y)
ax.set_title("Title of Axes[1][1]")

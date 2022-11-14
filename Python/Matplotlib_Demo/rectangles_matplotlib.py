# -*- coding: utf-8 -*-
"""
Created on Thu May 19 11:55:07 2022

Info: Demonstartion of matplotib.patches API to draw 2D rectangles

@author: Anuhya Annamraju

"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

#No. of rectangles desired
rectangle_count = 10 

#Length of the edge of the rectangle desired
edge =1

#Clear the axis if a figure already exists
plt.cla()

#Create a new Figure object
fig = plt.figure()

#Add axis to the created Figure object
ax = fig.add_subplot(111)

for i in range(rectangle_count):

    #Select the x coordinate of the anchor point in the range 0-5    
    bottom_left_x = random.uniform(0,5)
    
    #Select the y coordinate of the anchor point in the range 0-10
    bottom_left_y = random.uniform(0,10)
    
    # Create a Rectangle patch
    # Param1 - Tuple (anchor_x,anchor_y)
    # Param2 - Width of the rectangle
    # Param3 - Height of the rectangle
    rect = patches.Rectangle((bottom_left_x,bottom_left_y), edge,edge, linewidth=1, edgecolor='g', facecolor='r')
    
    # Add the patch to the Axes
    ax.add_patch(rect)

#Set x-Limit of the axis
ax.set_xlim(0,10)

#Set y-Limit of the axis
ax.set_ylim(0,10)

#Show Plot
plt.show()



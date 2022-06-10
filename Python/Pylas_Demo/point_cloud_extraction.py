# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 11:47:15 2022

Info: This data package been produced by and downloaded from the National Ecological Observatory Network (NEON).
NEON is funded by the National Science Foundation (Awards 0653461, 0752017, 1029808, 1138160, 1246537, 1638695,
1638696, 1724433) and managed cooperatively by Battelle. 

These data are provided under the terms of the NEON data policy at https://www.neonscience.org/data-policy.

For more information please refer to the text file in the parent folder of this project.

@author: Anuhya Annamraju

Copyright (C): AirRobot GmbH & Co. KG. All Rights Reserved.
"""


import pylas
import plotly.io as pio
from random import randint
import plotly.graph_objects as go
import numpy as np

pio.renderers.default='browser'

with pylas.open('NEON_D06_KONZ_DP1_704000_4324000_classified_point_cloud_colorized.laz') as fh : 
    
    print('Points from Header:', fh.header.point_count)
    las = fh.read()
    print(las)
    print('Points from data:', len(las.points))

    l = len(las.points)
    index = 0
    data_x = []
    data_y = []
    data_z = []
    intensities =[]
    downsampling_factor = 25
    
    while index < int(l/downsampling_factor):
        
        data_x.append(las.points.item(index*downsampling_factor)[0])
        data_y.append(las.points.item(index*downsampling_factor)[1])
        data_z.append(las.points.item(index*downsampling_factor)[2])
        intensities.append(las.points.item(index*downsampling_factor)[3])
        index +=1 
                
    
    max_intensity = max(intensities)
    
    intensities_pc = np.ones(len(intensities))
    
    if max_intensity != 0:
        intensities_pc = [(max_intensity-i)/max_intensity for i in intensities]
    else:
        intensities_pc = [('#%06X' % randint(0, 0xFF0F00)) for i in intensities]
    
    
    fig = go.Figure(data=go.Scatter3d(
        x = data_x,
        y = data_y,
        z = data_z,
        mode='markers',
        marker=dict(size=1,color=np.array(intensities_pc)
        )
    ))
    
    fig.show()
    


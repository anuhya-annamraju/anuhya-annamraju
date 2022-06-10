# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 11:47:15 2022

Info: This data package been produced by and downloaded from the National Ecological Observatory Network (NEON).
NEON is funded by the National Science Foundation (Awards 0653461, 0752017, 1029808, 1138160, 1246537, 1638695,
1638696, 1724433) and managed cooperatively by Battelle. 

These data are provided under the terms of the NEON data policy at https://www.neonscience.org/data-policy.

For more information please refer to the text file in the parent folder of this project.

@author: Anuhya Annamraju

"""


import pylas
import plotly.io as pio
from random import randint
import plotly.graph_objects as go
import numpy as np

# Choose Browser as the 3D Plot renderer
pio.renderers.default='browser'

with pylas.open('NEON_D06_KONZ_DP1_704000_4324000_classified_point_cloud_colorized.laz') as data : 
    
    #Extracted data contains
    # 1.Header
    # 2. VLR - Variable Length Record
    # 3. Point Records - Point cloud data
    
    # Method Read() returns point cloud data
    las = data.read()
    l = las.points.size
    point_cloud_data = las.points
    index = 0
    data_x = []
    data_y = []
    data_z = []
    intensities =[]
    downsampling_factor = 25
    downsampled_len = int(l/downsampling_factor)
    
    
    #Reducing the sample size of the data for visualization
    while index < downsampled_len:
        
        row = point_cloud_data[index*downsampling_factor]
        
        #row contains 13 values in the following order
        # [X', 'Y', 'Z', 'intensity', 'bit_fields', 'raw_classification', 'scan_angle_rank', 'user_data', 'point_source_id', 'gps_time', 'red', 'green', 'blue']
        
        data_x.append(row[0])
        data_y.append(row[1])
        data_z.append(row[2])
        intensities.append(row[3])
        index +=1 
                
    
    max_intensity = max(intensities)
    
    intensities_pc = np.ones(len(intensities))
    
    # If intensity of the recorded points is zero, create a new array of colors to visulaize data
    if max_intensity != 0:
        intensities_pc = [(max_intensity-i)/max_intensity for i in intensities]
    else:
        intensities_pc = [('#%06X' % randint(0, 0xFF0F00)) for i in intensities]
    
    #Visualize the point cloud in 3D plot
    fig = go.Figure(data=go.Scatter3d(
        x = data_x,
        y = data_y,
        z = data_z,
        mode='markers',
        marker=dict(size=1,color=np.array(intensities_pc)
        )
    ))
    
    fig.show()
    


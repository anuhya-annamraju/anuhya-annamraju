# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 15:46:39 2022

@author: AA
"""

import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.pyplot as plt
import matplotlib as mpl
import application_classes


root=tk.Tk()
root.title("Sample Based Path Planning Algorithms")

root_height = root.winfo_height()
root_width = root.winfo_width()

frame_controls = tk.Frame(root)
frame_controls.pack(padx=5,pady=5)

simulate = tk.Button(frame_controls,text="Simulate",command=lambda:simulate_algorithms(gui_instance))
simulate.pack(padx=5,pady=5)

frame_rrt = tk.Frame(root,width = root_width/2 - 20 ,height = root_height/2-20)
frame_rrt.pack(side = tk.LEFT,fill=tk.BOTH,expand=True)

print(plt.__file__)
style.use("ggplot")

mpl.rcParams['lines.linewidth'] = 0.7

#Frame for the left half 
frame_plot_rrt=tk.Frame(master=frame_rrt,padx=5,pady=5,borderwidth=1,relief="solid")
frame_plot_rrt.pack(side=tk.LEFT,padx=1,pady=1,fill=tk.BOTH,expand=True)

fig_rrt=Figure(dpi=100)
axes_rrt=fig_rrt.add_subplot()

fig_rrt.subplots_adjust(left=0.06,bottom=0.08,right=0.97,top=0.94,wspace=None,hspace=None)
canvas_rrt = FigureCanvasTkAgg(fig_rrt, master=frame_plot_rrt)  # A tk.DrawingArea.
canvas_rrt.draw()
canvas_rrt.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
NavigationToolbar2Tk(canvas_rrt, frame_plot_rrt)

frame_rrt_star = tk.Frame(root,width = root_width/2 - 20 ,height = root_height/2-20)
frame_rrt_star.pack(side = tk.LEFT,fill=tk.BOTH,expand=True)

#Frame for the left half 
frame_plot_rrtstar=tk.Frame(master=frame_rrt_star,padx=5,pady=5,borderwidth=1,relief="solid")
frame_plot_rrtstar.pack(side=tk.LEFT,padx=1,pady=1,fill=tk.BOTH,expand=True)

fig_rrt_star=Figure(dpi=100)
axes_rrt_star=fig_rrt_star.add_subplot()

fig_rrt_star.subplots_adjust(left=0.06,bottom=0.08,right=0.97,top=0.94,wspace=None,hspace=None)
canvas_rrt_star = FigureCanvasTkAgg(fig_rrt_star, master=frame_plot_rrtstar)  # A tk.DrawingArea.
canvas_rrt_star.draw()
canvas_rrt_star.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
NavigationToolbar2Tk(canvas_rrt_star, frame_plot_rrtstar)


axes_rrt.set_title( "RRT  Algorithm")
axes_rrt_star.set_title("RRT Star Algorithm")

gui_instance = application_classes.GUI(fig_rrt,fig_rrt_star,canvas_rrt,canvas_rrt_star,axes_rrt,axes_rrt_star)

def simulate_algorithms(gui_instance):
    
    print("Nothing")

root.mainloop()


    



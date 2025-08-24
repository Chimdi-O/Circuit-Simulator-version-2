import tkinter as tk
import math 
import numpy  


class Wire(): 
    def __init__(self,master):
        #start and end pos are updated in the event handler in main.py 
        self.start_pos = None 
        self.end_pos = None
        self.geometry = []     
        self.circle_size = 4

    def draw_wire(self,master): 
        self.geometry = [master.canvas.create_line( self.start_pos[0],  self.start_pos[1], self.end_pos[0], self.end_pos[1], fill="black", width=3),
               master.canvas.create_oval( self.start_pos[0] - self.circle_size  ,  self.start_pos[1] - self.circle_size,  self.start_pos[0] + self.circle_size,  self.start_pos[1] + self.circle_size  ,fill="white"),
              master.canvas.create_oval( self.end_pos[0] - self.circle_size  ,  self.end_pos[1] - self.circle_size,  self.end_pos[0] + self.circle_size,  self.end_pos[1] + self.circle_size  ,fill="white")]    
    
    def move_line(self,master):  
        master.canvas.coords(self.geometry[0], self.start_pos, self.end_pos)
        master.canvas.coords(self.geometry[1], self.start_pos[0] - self.circle_size  ,  self.start_pos[1] - self.circle_size,  self.start_pos[0] + self.circle_size,  self.start_pos[1] + self.circle_size)
        master.canvas.coords(self.geometry[2], self.end_pos[0] - self.circle_size  ,  self.end_pos[1] - self.circle_size,  self.end_pos[0] + self.circle_size,  self.end_pos[1] + self.circle_size)

#Draw the resistor symbol within tkinter instead of using an image
class Resistor(Wire): 
     def __init__(self,master): 
          super().__init__(master)
          self.top_left =[]
          self.top_right =[]
          self.bottom_left =[]
          self.bottom_right=[]
          self.resistance = 0
          self.gap_start = [] 
          self.gap_end = []
    
     def draw_wire(self,master): 
        self.top_left = self.start_pos
        self.top_right = self.start_pos
        self.bottom_left = self.start_pos
        self.bottom_right= self.start_pos
        self.gap_start = self.start_pos
        self.gap_end = self.start_pos

        self.geometry = [master.canvas.create_line( self.start_pos[0],self.start_pos[1], self.gap_start[0], self.gap_start[1], fill="black", width=3),
               master.canvas.create_line(self.gap_end[0],self.gap_end[1],self.end_pos[0],self.end_pos[1], fill="black", width=3),
               master.canvas.create_oval( self.start_pos[0] - self.circle_size  ,  self.start_pos[1] - self.circle_size,  self.start_pos[0] + self.circle_size,  self.start_pos[1] + self.circle_size  ,fill="white"),
               master.canvas.create_oval( self.end_pos[0] - self.circle_size  ,  self.end_pos[1] - self.circle_size,  self.end_pos[0] + self.circle_size,  self.end_pos[1] + self.circle_size  ,fill="white"),

               master.canvas.create_polygon(self.bottom_left[0],self.bottom_left[1],
                                   self.bottom_right[0],self.bottom_right[1],
                                   self.top_right[0],self.top_right[1],
                                   self.top_right[0],self.top_right[1],
                                   self.top_left[0],self.top_left[1],
                                   fill="",outline= "black",width=3) ] 
        # self.geometry.append(master.canvas.create_line(100,100,200,100, fill="black", width=3)) # ruler
        
    
     def move_line(self,master):  
        self.calc_shape()
    
        
        master.canvas.coords(self.geometry[0], self.start_pos[0],self.start_pos[1],self.gap_start[0],self.gap_start[1])
        master.canvas.coords(self.geometry[1], self.gap_end[0], self.gap_end[1], self.end_pos[0], self.end_pos[1])
        master.canvas.coords(self.geometry[2], self.start_pos[0] - self.circle_size  ,  self.start_pos[1] - self.circle_size,  self.start_pos[0] + self.circle_size,  self.start_pos[1] + self.circle_size)
        master.canvas.coords(self.geometry[3], self.end_pos[0] - self.circle_size  ,  self.end_pos[1] - self.circle_size,  self.end_pos[0] + self.circle_size,  self.end_pos[1] + self.circle_size)

        master.canvas.coords(self.geometry[4],self.bottom_left[0],self.bottom_left[1],
                                   self.bottom_right[0],self.bottom_right[1],
                                   self.top_right[0],self.top_right[1],
                                   self.top_right[0],self.top_right[1],
                                   self.top_left[0],self.top_left[1])
        


     # use the equation of the line to find the x line what ever you call it 
     def calc_shape(self): 
         if self.start_pos == self.end_pos: 
            self.top_left = self.start_pos
            self.top_right = self.start_pos
            self.bottom_left = self.start_pos
            self.bottom_right= self.start_pos
            self.gap_start = self.start_pos
            self.gap_end = self.start_pos
            return
     
         #calculates the vector starting at start pos 
         dx = self.end_pos[0] - self.start_pos[0]
         dy = self.end_pos[1] - self.start_pos[1]

         length = math.sqrt(dx**2 + dy**2)

         #normalised vectors 
         norm_dx = dx/length
         norm_dy = dy/length 

         #normalised perpendicular vectors 
         norm_px = -norm_dy
         norm_py = norm_dx

         #scaled normalised vectors, how far along the line + how thick the resistor should be 
         scale = 25
         perp_scale = 12

         scaled_norm_dx = norm_dx*scale 
         scaled_norm_dy = norm_dy*scale 

         scaled_norm_px = norm_px*perp_scale
         scaled_norm_py = norm_py*perp_scale

         #middle 
         midx = (self.end_pos[0] + self.start_pos[0])/2
         midy = (self.end_pos[1] + self.start_pos[1])/2

         mid_right = [midx - scaled_norm_dx, midy - scaled_norm_dy]
         mid_left = [midx + scaled_norm_dx, midy + scaled_norm_dy]

         self.gap_end = mid_left
         self.gap_start = mid_right

         self.top_right = [mid_right[0] + scaled_norm_px, mid_right[1] + scaled_norm_py]
         self.bottom_right = [mid_right[0] - scaled_norm_px, mid_right[1] - scaled_norm_py]

         self.top_left = [mid_left[0] + scaled_norm_px, mid_left[1] + scaled_norm_py]
         self.bottom_left = [mid_left[0] - scaled_norm_px, mid_left[1] - scaled_norm_py]







  
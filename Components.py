import tkinter as tk


class Wire(): 
    def __init__(self,master):
        self.start_pos = None 
        self.end_pos = None
        self.geometry = [] 
        self.symbol = False      

    def draw_wire(self,master,start_pos,end_pos): 
        self.geometry = [master.canvas.create_line( start_pos[0],  start_pos[1], end_pos[0], end_pos[1], fill="black", width=3),
                master.canvas.create_oval( start_pos[0] - 10  ,  start_pos[1] - 10,  start_pos[0] + 10,  start_pos[1] + 10  ,fill="blue"),
                master.canvas.create_oval( end_pos[0] - 10  ,  end_pos[1] - 10,  end_pos[0] + 10,  end_pos[1] + 10  ,fill="blue")]
        if self.symbol: 
                self.geometry.append(master.canvas.create_image(( start_pos[0] +  end_pos[0])/2 ,( start_pos[1] +  end_pos[1])/2, anchor=tk.CENTER, image=self.symbol))
    
    def move_line(self,master,start_pos,end_pos):  
          master.canvas.coords(self.geometry[0], start_pos[0],  start_pos[1], end_pos[0], end_pos[1])
          master.canvas.coords(self.geometry[1], start_pos[0] - 10  ,  start_pos[1] - 10,  start_pos[0] + 10,  start_pos[1] + 10)
          master.canvas.coords(self.geometry[2], end_pos[0] - 10  ,  end_pos[1] - 10,  end_pos[0] + 10,  end_pos[1] + 10)
          
          if self.symbol: 
               master.canvas.coords(self.geometry[3],( start_pos[0] +  end_pos[0])/2 ,( start_pos[1] +  end_pos[1])/2)

import customtkinter as ctk
from CTkMenuBar import *
import tkinter as tk

class App(tk.Tk): 
    def __init__(self): 
        super().__init__()        

        self.title("Circuit simulator")
        self.geometry("800x600")
        
        self.create_menubar()
        
        self.mouse_position = [0,self.menu_bar.winfo_height()]
        self.mode = "none" 
    
    def create_menubar(self): 
        self.menu_bar = tk.Menu(self,tearoff=False)
         
        self.component_menu = tk.Menu(self,tearoff = False) 
        self.component_menu.add_cascade(label="Resistor")
        self.component_menu.add_cascade(label="Wire")
        self.component_menu.add_cascade(label="Battery")
        self.component_menu.add_cascade(label="Capacitor")
        self.component_menu.add_cascade(label="LED")

        self.file_menu = tk.Menu(self,tearoff=False)
        self.file_menu.add_cascade(label="Save As")  
        self.file_menu.add_cascade(label="Save")
        self.file_menu.add_cascade(label="Load") 


        self.menu_bar.add_cascade(label="File",menu=self.file_menu)
        self.menu_bar.add_cascade(label="Edit",font=("comic sans",5))
        self.menu_bar.add_cascade(label="Components",menu=self.component_menu)     
        self.menu_bar.add_cascade(label="Scope")

        self.config(menu=self.menu_bar)
        
    def create_canvas(self): 
        pass 
    
    def locate_mouse(self,event): 
        self.mouse_position = [event.x,event.y]
        if event.y>self.menu_bar.winfo_height():
            print(self.mouse_position)

    def update(self): 
        pass
        #if self.mode == "drawing": 
        
app = App() 
app.option_add("*Menu.Font", "utopia 205")
app.bind('<Motion>',app.locate_mouse)
app.mainloop() 


#pastakudasai
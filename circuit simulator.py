import customtkinter as ctk
from CTkMenuBar import *
import tkinter as tk


class MenuBar(tk.Menu): 
    def __init__(self, master): 
        super().__init__(master)
        
        self.components_menu = tk.Menu(self,tearoff = False) 
        self.components_menu.add_cascade(label="Resistor")
        self.components_menu.add_cascade(label="Wire")
        self.components_menu.add_cascade(label="Battery")
        self.components_menu.add_cascade(label="Capacitor")
        self.components_menu.add_cascade(label="LED")

        self.file_menu = tk.Menu(self,tearoff=False)
        self.file_menu.add_cascade(label="Save As")  
        self.file_menu.add_cascade(label="Save")
        self.file_menu.add_cascade(label="Load") 


        self.add_cascade(label="File",menu=self.file_menu)
        self.add_cascade(label="Edit",font=("comic sans",5))
        self.add_cascade(label="Components",menu=self.components_menu)     
        self.add_cascade(label="Scope")
          


class Canvas(tk.Canvas): 
    def __init(self,master): 
        super.__init__(master,fg_color="white") 


class App(tk.Tk): 
    def __init__(self): 
        super().__init__()

        self.title("Circuit simulator")
        self.geometry("800x600")
        self.menu_bar = MenuBar(master=self)
        self.config(menu=self.menu_bar)
        
        self.Canvas = Canvas(master=self)
        self.Canvas.pack(expand=True,fill="both") 
        self.mouse_position = [0,self.menu_bar.winfo_height()]
        

    def locate_mouse(self,event): 
        self.mouse_position = [event.x,event.y]
        if event.y>self.menu_bar.winfo_height():
            print(self.mouse_position)

app = App() 
app.option_add("*Menu.Font", "utopia 205")
app.bind('<Motion>',app.locate_mouse)
app.mainloop() 


#pastakudasai
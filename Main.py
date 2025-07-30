import tkinter as tk
from Components import *

#save save save!!!! current

class EventHandler(): 
    def __init__(self,master): 
        #Motion 
        self.locate_mouse = True 
        self.move_line = False

        #Button1 
        self.start_drawing = False 

        #Button1 release 
        self.stop_drawing = False 

        #Misc 
        self.current_component = None 

        master.canvas.bind('<Motion>',lambda event, master=master: self.Motion_handler(event,master))
        master.canvas.bind('<Button-1>', lambda event, master=master: self.Button1_handler(event,master))
        master.canvas.bind('<ButtonRelease-1>',lambda event, master=master: self.Button1_release_handler(event,master))

    def Motion_handler(self,event,master):
        
        if self.locate_mouse: 
            master.mouse_position = [(round(event.x/50))*50,(round(event.y/50))*50]
            print(master.mouse_position)
        
        if self.move_line: 
            self.current_component.end_pos = master.mouse_position
            self.current_component.move_line(master,self.current_component.start_pos,self.current_component.end_pos)

    def Button1_handler(self,event,master): 
        print("Button 1 pressed")
        if self.start_drawing:
             
             self.current_component.start_pos = [master.mouse_position[0],master.mouse_position[1]]
             self.current_component.end_pos = self.current_component.start_pos
             self.current_component.draw_wire(master,self.current_component.start_pos,self.current_component.end_pos)

             self.move_line = True 
             self.stop_drawing = True 
             
    def Button1_release_handler(self,event,master): 
        print("button 1 released")
        if self.stop_drawing: 
            master.components.append(self.current_component)
            self.move_line = False
            self.stop_drawing = False 
            self.start_drawing = False

            self.select_component(self.current_component.__class__.__name__,master)

            
             
    
    def select_component(self,component,master): 
        component_dict = {"Wire":Wire(master)}#,"Resistor", }
        self.current_component = component_dict[component]
        self.start_drawing = True
         


class App(tk.Tk): 

    def __init__(self): 
        super().__init__()        

        self.title("Circuit simulator")
        self.geometry("800x600")
        
        self.create_menubar()
        self.create_canvas()
        self.EventHandler = EventHandler(master=self) 
        
        self.mouse_position = [0,self.menu_bar.winfo_height()]
        self.mode = "none" 
        self.components = []
    
    def create_menubar(self): 
        self.menu_bar = tk.Menu(self,tearoff=False)  
        self.component_menu = tk.Menu(self,tearoff = False) 
        self.component_menu.add_cascade(label="Wire",command=lambda Component="Wire" ,master=self : self.EventHandler.select_component(Component,master))
        self.component_menu.add_cascade(label="Resistor")
        self.component_menu.add_cascade(label="Battery")
        self.component_menu.add_cascade(label="Capacitor")
        self.component_menu.add_cascade(label="LED")

        self.file_menu = tk.Menu(self,tearoff=False)
        self.file_menu.add_cascade(label="Save As")  
        self.file_menu.add_cascade(label="Save")
        self.file_menu.add_cascade(label="Load") 

        self.menu_bar.add_cascade(label="File",menu=self.file_menu)
        self.menu_bar.add_cascade(label="Edit")
        self.menu_bar.add_cascade(label="Components",menu=self.component_menu)     
        self.menu_bar.add_cascade(label="Scope")

        self.config(menu=self.menu_bar)
        
    def create_canvas(self): 
        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill="both",expand=1)  

    

    def update(self): 
        pass    
        
app = App() 

app.mainloop() 
#pastakudasai
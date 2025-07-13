import customtkinter as ctk
from CTkMenuBar import * 

class MenuBar(CTkMenuBar): 
    def __init__(self, master): 
        super().__init__(master)

        self.add_cascade(text="File")
        self.add_cascade(text="Edit")
        self.add_cascade(text="Draw")
        self.option_add(option="Draw", text= "Draw_submenu")
        
                                             
        self.add_cascade(text="Scope")
       
        


class Canvas(ctk.CTkCanvas): 
    def __init(self,master): 
        super.__init__(master,fg_color="white") 



class App(ctk.CTk): 
    def __init__(self): 
        super().__init__()

        self.title("Circuit simulator")
        self.geometry("800x600")
        self.button_frame = MenuBar(master=self)
        self.button_frame.pack(fill='x')
        self.Canvas = Canvas(master=self)
        self.Canvas.pack(expand=True,fill="both") 
        self.mouse_position = [0,self.button_frame.winfo_height()]
    
    def locate_mouse(self,event): 
        self.mouse_position = [event.x,event.y]
        if event.y>self.button_frame.winfo_height():
            print(self.mouse_position)
    

app = App() 

app.bind('<Motion>',app.locate_mouse)
app.mainloop() 


#pastakudasai
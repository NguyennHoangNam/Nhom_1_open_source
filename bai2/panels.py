import customtkinter as ctk

class Panel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master= parent,fg_color='#4a4a4a')
        self.pack(fill = 'x', pady= 4, ipady = 8)

class SliderPanel(Panel):
    def __init__(self,parent,text,params_data,min_value,max_value):
        super().__init__(parent= parent)
        self.rowconfigure((0,1), weight=1)
        self.columnconfigure((0,1),weight=1)
        ctk.CTkLabel(self,text=text).grid(column = 0 ,row = 0, sticky = 'w',padx = 5)
        self.num_label = ctk.CTkLabel(self,text = params_data.get(),)
        self.num_label.grid(column = 1 ,row = 0, sticky = 'e',padx = 5)
        ctk.CTkSlider(self,variable=params_data,
                      from_=min_value,to = max_value,command = self.update_text).grid(row = 1, column = 0, columnspan = 2, sticky = 'ew',padx = 5,pady=5)
    def update_text(self,value):
        self.num_label.configure(text = f'{round(value,2)}')

class SwitchPanel(Panel):
    def __init__(self,parent,*args):
        super().__init__(parent= parent)

        for var,text in args:
            switch = ctk.CTkSwitch(self,text= text,variable= var,button_color="#3078c9" ,fg_color="#4a4a4a")
            switch.pack(side = 'left',expand = True,fill = 'both', padx = 5, pady =5)

class ButtonPanel(Panel):
    def __init__(self,parent,text,func):
        super().__init__(parent= parent)
        self.btn = ctk.CTkButton(self,text=text,command=func,fg_color='#3078c9')
        self.btn.pack(padx = 5, pady =5)

        

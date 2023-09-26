import customtkinter as ctk
from tkinter import filedialog

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

class FileNamePanel(Panel):
    def __init__(self, parent,name_string,file_string):
        super().__init__(parent = parent)
        self.name_string = name_string
        self.name_string.trace('w',self.update_text)
        self.file_string = file_string
        ctk.CTkEntry(self,textvariable=self.name_string).pack(fill = 'x',padx = '20',pady= 5)

        frame = ctk.CTkFrame(self,fg_color='transparent')
        jpg_check = ctk.CTkCheckBox(frame,text = 'jpg',command= lambda: self.click('jpg'),  variable= self.file_string, onvalue= 'jpg',offvalue = 'png')
        jpg_check.pack(side = 'left',fill = 'x',expand =True)
        png_check = ctk.CTkCheckBox(frame,text = 'png',command= lambda: self.click('png'),  variable= self.file_string, onvalue= 'png', offvalue= 'jpg')
        png_check.pack(side = 'left',fill = 'x',expand =True)
        frame.pack(expand = True,fill = 'x',padx= 20)

        self.output = ctk.CTkLabel(self, text = '')
        self.output.pack()

    def click(self,value):
        self.file_string.set(value)
        self.update_text()

    def update_text(self,*args):
        if self.name_string.get():
            text = self.name_string.get().replace(' ','_') +'.'+ self.file_string.get()
            self.output.configure(text = text)

class FilePathPanel(Panel):
    def __init__(self,parent,path_string):
        super().__init__(parent = parent)
        self.path_string = path_string

        ctk.CTkButton(self,text= ' Open ',command=self.open_file_dialog).pack(pady =5)
        ctk.CTkEntry(self,textvariable=self.path_string).pack(expand= True,fill = 'both',padx = 5,pady = 5)

    def open_file_dialog(self):
        self.path_string.set(filedialog.askdirectory())

class SaveButton(ctk.CTkButton):
    def __init__(self,parent,export_image,name_string,file_string,path_string):
        super().__init__(master=parent,text='save',command= self.save)
        self.pack(side = 'bottom',pady = 10)
        self.export_image = export_image
        self.name_string = name_string
        self.file_string = file_string
        self.path_string = path_string

    def save(self):
        self.export_image(
            self.name_string.get(),
            self.file_string.get(),
            self.path_string.get()
        )
import customtkinter as ctk
from tkinter import filedialog,Canvas
from menu import Menu


class Import_Frame(ctk.CTkFrame):

    def __init__(self, parent,open_workplace,import_image_func):
        super().__init__(master=parent)
        self.grid(column = 0, row = 0,sticky = "nsew")
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.open_func = open_workplace
        self.import_image_func = import_image_func
        self.open_button = ctk.CTkButton(self, text='open image', command=self.open_dialog).pack(expand = True)

    def open_dialog(self):
        self.path = filedialog.askopenfile().name
        self.import_image_func(self.path)
        self.open_func()
        


class Workplace_Frame(ctk.CTkFrame):
    def __init__(self, parent,close_func,resized_image,resize_image_func,position_vars,color_vars):
        super().__init__(master=parent,bg_color="#242424")
        self.grid(column = 0, row = 0,sticky = "nsew")
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=2, uniform='a')
        self.columnconfigure(1,weight=6, uniform='a')
        self.menu = Menu(self,position_vars,color_vars)
        self.canvas = Canvas_area(self,resized_image,resize_image_func)
        self.close_button = ctk.CTkButton(master=parent,
                         text='x',
                         text_color='#fff' ,
                         fg_color='transparent',
                         width= 40,
                         height= 40,
                         corner_radius= 0,
                         hover_color='#8a0606',
                         command=close_func)
        self.close_button.place(relx = 0.99, rely = 0.01, anchor ='ne')
    

class Canvas_area(Canvas):
    def __init__(self,parent,resized_image,resize_image_func):
        super().__init__(master= parent,background='#242424',bd=0,highlightthickness=0,relief='ridge')
        self.grid(row=0,column=1,sticky="nsew")
        self.resized_image= resized_image
        self.create_image(self.winfo_width() / 2,self.winfo_height()/2,image = self.resized_image)
        self.bind('<Configure>',resize_image_func)
          



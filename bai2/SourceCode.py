import customtkinter as ctk
import numpy as np
from frame_widgets import *
from PIL import ImageTk,Image

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.geometry('1300x700+150+50')
        self.title('photo')
        self.minsize(800,500)
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.create_para()
        self.import_frame = Import_Frame(self,self.open_workplace,self.import_image)
        rotation = ctk.DoubleVar()
            
        self.mainloop()

    def create_para(self):
        self.position_vars = {
            'rotation' : ctk.DoubleVar(value=0),
        }
        self.color_vars = {
            'red' : ctk.DoubleVar(value=0),
            'green' : ctk.DoubleVar(value=0),
            'blue' : ctk.DoubleVar(value=0),
            'gamma' : ctk.DoubleVar(value=1),
            'grey_scale':ctk.BooleanVar(value=False),
            'invert':ctk.BooleanVar(value=False),
        }
        for var in list(self.position_vars.values()) + list(self.color_vars.values()):
            var.trace('w',self.manipulate_image)

    def manipulate_image(self,*args):
        self.image_array = np.array(self.origin_image, dtype=np.int16)
        self.gamma()
        self.rgb_slide()
        self.grey_scale()
        self.invert()


        self.image = Image.fromarray(np.clip(self.image_array,0,255).astype(np.uint8))
        

        self.show_image()

    def open_workplace(self):
        self.import_frame.grid_forget()
        self.workplace_frame = Workplace_Frame(self,self.close_workplace,self.imagetk,self.resize_image,self.position_vars,self.color_vars)
    
    def close_workplace(self):
        self.workplace_frame.grid_forget()
        self.import_frame.grid()
        
    def import_image(self,path):
        self.origin_image = Image.open(path)
        self.image = self.origin_image
        self.image_array = np.array(self.image)
        self.image_ratio = self.image.size[0] / self.image.size[1]
        self.imagetk = ImageTk.PhotoImage(self.image)
        
        
    def resize_image(self,event):
        self.Canvas_ratio = event.width/event.height

        self.canvas_width = event.width
        self.canvas_height = event.height
        if self.Canvas_ratio > self.image_ratio:
            self.image_height = int(event.height)
            self.image_width = int(self.image_height * self.image_ratio)
        else:
            self.image_width = int(event.width)
            self.image_height = int(self.image_width / self.image_ratio)
        self.show_image()

    def show_image(self):
        self.workplace_frame.canvas.delete('all')
        self.resized_image = self.image.resize((self.image_width,self.image_height))
        self.imagetk = ImageTk.PhotoImage(self.resized_image)
        self.workplace_frame.canvas.create_image(self.canvas_width / 2,self.canvas_height/2,image = self.imagetk)
    
    def rgb_slide(self):
        for i,color in enumerate(['red','green','blue']):
            if self.color_vars[color].get()>0:
                self.image_array[:, :, i] = (self.image_array[:, :, i].astype(np.int16) +
                                                 (255-self.image_array[:, :, i].astype(np.int16))*((self.color_vars[color].get())/100))
            elif self.color_vars[color].get()<0:
                self.image_array[:, :, i] = (self.image_array[:, :, i].astype(np.int16) -
                                                 (self.image_array[:, :, i].astype(np.int16))*((self.color_vars[color].get())/-100))
    def grey_scale(self):
        if self.color_vars['grey_scale'].get():
            self.image_array = np.dot(self.image_array[...,:3],[0.2989, 0.5870, 0.1140])
    
    def invert(self):
        if self.color_vars['invert'].get():
            self.image_array = 255-self.image_array[...,:3]
    
    def gamma(self):
        normalized_image = self.image_array / 255.0
        adjusted_image = np.power(normalized_image, self.color_vars['gamma'].get())
        scaled_image = adjusted_image * 255.0
        self.image_array = scaled_image
App()



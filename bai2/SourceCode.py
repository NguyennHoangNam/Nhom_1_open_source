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
        self.import_frame = Import_Frame(self,self.open_workplace,self.import_image)
            
        self.mainloop()

    def create_params(self):
        self.position_vars = {
            'rotation' : ctk.DoubleVar(value=0)
        }
        self.color_vars = {
            'red' : ctk.DoubleVar(value=0),
            'green' : ctk.DoubleVar(value=0),
            'blue' : ctk.DoubleVar(value=0),
            'gamma' : ctk.DoubleVar(value=1),
            'grey_scale':ctk.BooleanVar(value=False),
            'invert':ctk.BooleanVar(value=False),
        }
        self.funtions = {
            'crop': self.image_crop,
            'resize': self.resize_image
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
        self.create_params()
        self.workplace_frame = Workplace_Frame(self,self.close_workplace,self.imagetk,self.funtions,self.position_vars,self.color_vars)
    
    def close_workplace(self):
        self.workplace_frame.grid_forget()
        self.import_frame.grid()
        
    def import_image(self,path):
        self.origin_image = Image.open(path)
        self.image = self.origin_image
        self.image_array = np.array(self.image)
        self.imagetk = ImageTk.PhotoImage(self.image)
        
        
    def resize_image(self,event):
        self.image_ratio = self.image.size[0] / self.image.size[1]
        self.canvas_width = self.workplace_frame.canvas.winfo_width()
        self.canvas_height = self.workplace_frame.canvas.winfo_height()
        self.Canvas_ratio = self.canvas_width /self.canvas_height
        if self.Canvas_ratio > self.image_ratio:
            self.image_height = int(self.canvas_height)
            self.image_width = int(self.image_height * self.image_ratio)
        else:
            self.image_width = int(self.canvas_width)
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
                self.image_array[:, :, i] = (self.image_array[:, :, i] +
                                                 (255-self.image_array[:, :, i])*((self.color_vars[color].get())/100))
            elif self.color_vars[color].get()<0:
                self.image_array[:, :, i] = (self.image_array[:, :, i] -
                                                 (self.image_array[:, :, i])*((self.color_vars[color].get())/-100))
    def grey_scale(self):
        if self.color_vars['grey_scale'].get():
            self.image_array = np.dot(self.image_array[...,:3],[0.2989, 0.5870, 0.1140])
    
    def invert(self):
        if self.color_vars['invert'].get():
            self.image_array = 255-self.image_array[...,:3]
    
    def gamma(self):
        if self.color_vars['gamma'].get() != 1:
            normalized_image = np.round(self.image_array[...] / 255.0,3)
            adjusted_image = np.power(normalized_image, round(self.color_vars['gamma'].get(),2))
            scaled_image = adjusted_image * 255.0
            self.image_array = scaled_image

    def image_crop(self):
        self.selection_rectangle = self.workplace_frame.canvas.create_rectangle(0, 0, 0, 0, outline="red", width=2, dash=(4, 4))
        self.workplace_frame.canvas.bind("<ButtonPress-1>", self.start_selection)
        self.workplace_frame.canvas.bind("<B1-Motion>", self.update_selection)
        self.workplace_frame.canvas.bind("<ButtonRelease-1>", self.end_selection)
        self.workplace_frame.menu.position_tab.crop_btn.btn.configure(fg_color="#192f70")
    def start_selection(self,event):
    # Record the starting coordinates of the selection
        self.x_offset = int((self.canvas_width - self.resized_image.size[0])/2)
        self.y_offset = int((self.canvas_height -self.resized_image.size[1])/2)
        self.selection_start_x = event.x 
        self.selection_start_y = event.y 
        
    def update_selection(self,event):
        # Update the coordinates of the selection rectangle as the mouse moves
        self.workplace_frame.canvas.coords(self.selection_rectangle, self.selection_start_x, self.selection_start_y, event.x, event.y)

    def end_selection(self,event):
        # Perform the crop operation based on the selection coordinates
        try:
            if self.selection_start_x < self.x_offset: self.selection_start_x = self.x_offset
            if self.selection_start_y < self.y_offset: self.selection_start_y = self.y_offset
            x1, y1, x2, y2 = self.selection_start_x- self.x_offset, self.selection_start_y-self.y_offset, event.x- self.x_offset, event.y- self.y_offset

            self.croped_image = np.array(self.resized_image)[y1: y2, x1: x2,:]
            self.image = Image.fromarray(self.croped_image.astype(np.uint8))
            self.origin_image = self.image
            self.resize_image(event)
            self.workplace_frame.canvas.unbind("<ButtonPress-1>")
            self.workplace_frame.canvas.unbind("<B1-Motion>")
            self.workplace_frame.canvas.unbind("<ButtonRelease-1>")
            self.workplace_frame.menu.position_tab.crop_btn.btn.configure(fg_color="#3078c9")
        except:
            self.workplace_frame.canvas.delete(self.selection_rectangle)
            self.workplace_frame.canvas.unbind("<ButtonPress-1>")
            self.workplace_frame.canvas.unbind("<B1-Motion>")
            self.workplace_frame.canvas.unbind("<ButtonRelease-1>")
            self.workplace_frame.menu.position_tab.crop_btn.btn.configure(fg_color="#3078c9")
App()



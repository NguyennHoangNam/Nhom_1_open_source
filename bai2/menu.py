import customtkinter as ctk
from panels import *

class Menu(ctk.CTkTabview):
    def __init__(self,parent,position_vars,color_vars):
        super().__init__(master=parent)
        self.grid(row = 0,column = 0 ,sticky = 'nsew',padx = 10, pady = 10)

        self.add('Posistion')
        self.add('Color')
        self.add('Effect')
        self.add('Export')

        PositionFrame(self.tab('Posistion'),position_vars)
        ColorFrame(self.tab('Color'),color_vars)

class PositionFrame(ctk.CTkFrame):
    def __init__(self,parent,position_vars):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand = True,fill = 'both')
        SliderPanel(self,"rotation",position_vars['rotation'],min_value=-255,max_value=255)

class ColorFrame(ctk.CTkFrame):
    def __init__(self,parent,color_vars):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand = True,fill = 'both')
        SwitchPanel(self,(color_vars['grey_scale'], "B/W"),(color_vars['invert'],'Invert'))
        SliderPanel(self,"Gamma",color_vars['gamma'],min_value=2,max_value=0)
        SliderPanel(self,"Red",color_vars['red'],min_value=-100,max_value=100)
        SliderPanel(self,"Green",color_vars['green'],min_value=-100,max_value=100)
        SliderPanel(self,"Blue",color_vars['blue'],min_value=-100,max_value=100)
import customtkinter as ctk
import numpy as np
import pandas as pd
from table import *

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.geometry('1400x700+150+50')
        self.title('Faketoshop')
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.get_data()
        self.table = Table(self,self.np_data)


        self.mainloop()

    def get_data(self):
        self.csv_data =pd.read_csv('diemPython.csv',index_col=0,header = 0)
        self.np_data =  np.array(self.csv_data.iloc[:,:])
        row_sum = np.sum(self.np_data,axis = 0)
        self.np_data = np.vstack((self.np_data,row_sum))
        self.np_data[9,0] = 'total'
App()

print("test")
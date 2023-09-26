import customtkinter as ctk

class Table(ctk.CTkFrame):
    def __init__(self,parent,data):
        super().__init__(master=parent)
        header = 'Mã lớp,Số SV,Loại A+,Loại A,Loại B+,Loại B,Loại C+,Loại C,Loại D+,Loại D,Loại F,L1,L2,TX1,TX2,Cuối kỳ'.split(',')
        for j in range(data.shape[0]):    
            for i in range(data.shape[1]):
                self.text = ctk.CTkLabel(self,text=data[j,i])
                self.text.grid(column = i,row = j,padx = 5,pady = 5)
        self.grid(column = 0, row = 0, sticky = 'nsew',padx = 20, pady = 20)
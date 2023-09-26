from tkinter import ttk

class Table(ttk.Treeview):
    def __init__(self,parent,data):
        super().__init__(master=parent)
        header = 'Mã lớp,Số SV,Loại A+,Loại A,Loại B+,Loại B,Loại C+,Loại C,Loại D+,Loại D,Loại F,L1,L2,TX1,TX2,Cuối kỳ'.split(',')
        self.data_columns = data.shape[1]
        self["columns"] = tuple(range(self.data_columns))
        for i in range(self.data_columns):
            self.heading(i, text=header[i])  
            if i == 0:
                self.column(i, width=100) 
            else:
                self.column(i, width=50) 
        for row in data:
            self.insert("", "end", values=tuple(row))
        self.grid(column=0,row=0,sticky = 'snew')

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="#2a2d2e",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#343638",
                        bordercolor="#343638",
                        borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])
        style.configure("Treeview.Heading",
                        background="#565b5e",
                        foreground="white",
                        relief="flat")
        style.map("Treeview.Heading",
                    background=[('active', '#3484F0')])
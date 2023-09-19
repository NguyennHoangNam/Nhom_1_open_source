#bài này giải hệ phương trình x+2y=5 và 3x+4y =6
# Yêu cầu hoàn chỉnh lại đoạn code
#để có 1 app giải hệ phương trình có n phương trình n ẩn
import numpy as np

import tkinter as tk


window = tk.Tk()
window.geometry('600x400')
window.title("Input Form")

# Create labels
label1 = tk.Label(window, text="Puong trinh 1:")
label1.grid(column=0,row=0)


label4 = tk.Label(window, text="Puong trinh 2:")
label4.grid(column=0,row=1)

# Create entry fields
input1 = tk.Entry(window)
input1.grid(column=1,row=0)

input2 = tk.Entry(window)
input2.grid(column=2,row=0)

input3 = tk.Entry(window)
input3.grid(column=1,row=1)

input4 = tk.Entry(window)
input4.grid(column=2,row=1)

input5 = tk.Entry(window)
input5.grid(column=3,row=0)

input6 = tk.Entry(window)
input6.grid(column=3,row=1)
def tinh_toan():
    try:
        x1 = int(input1.get())
        y1 = int(input2.get())
        x2 = int(input3.get())
        y2 = int(input4.get())
        b1 = int(input3.get())
        b2 = int(input4.get())
        A = np.array([(x1,y1),(x2,y2)])
        B = np.array([b1,b2])
        A1  = np.linalg.inv(A) # tạo ma trận nghich đảo

        X = np.dot(A1,B)
        kq.set(f'Nghiem cua he:{X}')
    except:
        kq.set('error')   
# Create button
submit_btn = tk.Button(window, text="tinh", command= tinh_toan)
submit_btn.grid(column=0,row=3)

kq = tk.StringVar()
kq_label = tk.Label(window, textvariable=kq)
kq_label.grid(column=0,row=4,columnspan=4)

# Run the event loop
window.mainloop()
print("test")
# Retrieve the input values




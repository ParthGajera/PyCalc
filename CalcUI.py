from tkinter import *
'''

from tkinter import messagebox
messagebox.showinfo("test" , "hoi, dit is een test als je dit leest is het gelukt")#

'''
top = Tk()

def helloCallBack():
    print(AddObj)
    return "   +    "

AddObj = Button(top, text ="+", command = helloCallBack)
print("5")
AddObj.pack()
top.mainloop()
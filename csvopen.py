# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 16:01:30 2022

@author: Pushkar bansal
"""


# importing tkinter and tkinter.ttk
# and all their functions and classes
from tkinter import Tk


  
# importing askopenfile function
# from class filedialog
from tkinter.filedialog import askopenfile

file="hello"

def selectfile():
    root = Tk()
    root.geometry('200x100')
    root.withdraw()
   # root.after(1000,lambda:root.destroy())
    file = askopenfile()
    filename=file
    #print(filename.readlines())
    i=0
    lst1=[]
    for line in filename.readlines():
        if (i==0):
            i=1
            continue
        line.replace("\n","")
        lst1.append(line.replace("\n","").split(","))
        
    print(lst1) 
    
    return lst1




  


#print(text)
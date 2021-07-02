from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk
import cv2
from tfpred import tfpreduh
from torchpred import torchpreduh
def getdet():
    global ws1
    global wb1
    root = Tk()
    root.geometry("400x150")
    root.title("Glaucomo Classification")
    root['background']='#99643A'
    
    def browsefunc():
    
        #filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        #(("","*.xlsx"),("all files","*.*")) )
        filez = filedialog.askopenfilenames(parent=root,title='Choose a file',multiple=True)

        var=root.tk.splitlist(filez)
        #print(var[0])
        imageuh=cv2.imread(var[0])
        cv2.namedWindow('image', cv2.WINDOW_KEEPRATIO)
        cv2.resizeWindow('image', 200, 200)
        cv2.imshow('image', imageuh)
        #cv2.resizeWindow('custom window', 200, 200)
        temp=torchpreduh(var[0])
        temp2=tfpreduh(var[0])
        if(temp==0 and temp2==0):
            mylabel2=Label(root,text="Glaucoma -ve with high accuracy for the image selected")
            mylabel2.grid(row=25,column=0,columnspan=3,padx=10,pady=10)

        elif(temp==1 and temp2==1):
            mylabel2=Label(root,text="Glaucoma +ve with high accuracy for the image selected")
            mylabel2.grid(row=25,column=0,columnspan=3,padx=10,pady=10)
            
        elif(temp2==0 and temp==1):
            mylabel2=Label(root,text="Glaucoma -ve for the image selected")
            mylabel2.grid(row=25,column=0,columnspan=3,padx=10,pady=10)

        elif(temp2==1 and temp==0):
            mylabel2=Label(root,text="Glaucoma +ve for the image selected")
            mylabel2.grid(row=25,column=0,columnspan=3,padx=10,pady=10)
        
        
        
        
    def button2_click():
        root.destroy()



    mylabel1=Label(root,text="Glaucoma Classification")
    mylabel1.grid(row=1,column=0,columnspan=3,padx=10,pady=10)


    button_2 = Button(root, text="exit", padx=20, pady=10, command=button2_click)
    button_2.grid(row=10, column=2)


    browsebutton = Button(root, text="Browse",padx=20,pady=10 ,command=browsefunc)
    browsebutton.grid(row=10, column=1)



    root.mainloop()

getdet()


from tkinter import Tk
from tkinter import *
root = Tk()
root.title("Neural Networks With Health")
root.geometry("1000x800")


# #Adding Background image
from tkinter import ttk
#img = PhotoImage(file="D:\\images\\neural network2.png")
#img=img.zoom(2,2)
#lbl = Label(root,image = img).place(x=0,y=0)

#Adding The title of the app
title = Label(root, text="Dr:Robot",font=("Times New Roman",50),fg="white",bg='#00614c',pady=20)
title.pack()

#Applying different models on the passed image
#In this block of code we will define our libraries
import numpy as np
# this library is used to convert the images into numbers or matrices of numbers
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
# this library is used to draw graphs or plots
import os
# this library is used to read extensions from drivers inside operating system
import cv2
# this library is used to be able to import the dataset that you will use
from tqdm import tqdm
# this library is used to see the progress of reading data from your data set
import tensorflow as tf
from tensorflow import keras
#import h5py
#h2o.init()
size=100
def head():
    #glioma(2)
      out['text']=path
      y_img = []
      image1 = cv2.imread(p)
      image_array1 = cv2.resize(image1,(size,size))
      y_img.append(list(image_array1))
      y_img = np.array(y_img)
      y_result =  model1.predict(y_img)
      out['text']=get_code(np.argmax(y_result))
def eyes():
      out['text']=path
      y_img = []
      image1 = cv2.imread(p)
      image_array1 = cv2.resize(image1,(size,size))
      y_img.append(list(image_array1))
      y_img = np.array(y_img)
      y_result =  model2.predict(y_img)
      out['text']=get_code(np.argmax(y_result))
#Adding the label and the entry that will holds our dataset path
#first adding label for descriping the entry
descrip= Label(root,text="Enter your image path here",font=("Arial",18),fg='white',bg='#008879')
descrip.place(x=20,y=200)
#second adding entry
path=StringVar()
path.set("Brain Tumor project\\1.meningioma\\meningioma1.png")
entr=Entry(root,font=("Arial",18),width=40,textvariable=path)
path=path.get()
entr.place(x=400,y=200)
#Third displaying the predicated output
pred=Label(root,text="The predicated output is: ",font=("Arial",25),fg='#e89eb0',bg='#3f5256')
pred.place(x=20,y=450)
out=Label(root,text="",font=("Arial",50),fg='#e89eb0',bg='#3f5256')
out.place(x=400,y=450)

#Partioning our app to 3 splits
eyedis= Button(root,text="Eye diagnosis",font=("Arial",25),fg='white',bg='#2c908b',command=head)
eyedis.place(x=10,y=600)

headdis= Button(root,text="Head diagnosis",font=("Arial",25),fg='white',bg='#2c908b',command=eyes)
headdis.place(x=235,y=600)

root.mainloop()
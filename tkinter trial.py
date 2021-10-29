#!/usr/bin/env python
# coding: utf-8

# In[3]:


from tkinter import *

project = Tk()

project.title("my first tkinter trial")
project.geometry("400x500")
mylabel1=Label(project, text="USERNAME",fg="green",bg="aqua",font=("Arial",12,"bold")).place(x=50, y=50)
username= Entry(project,bg = "white",width = 25).place(x=160,y=50)
mylabel2=Label(project, text="PASSWORD",fg="green",bg="aqua",font=("Arial",12,"bold")).place(x=50, y=110)
password= Entry(project,bg = "white",width = 25,show='*').place(x=160,y=110)
myButton1=Button(project,text="LOG IN",fg="black",bg="cadetblue1",width=10).place(x=170, y=180)
myButton2=Button(project,text="REGISTER",bg="red",width=10).place(x=170, y=210)
mylabel3=Label(project,text="terms and conditions apply, read our privacy policy to see",bg="aqua",font=("Times New Roman",10,"bold")).place(x=40,y=400)
        
project.mainloop()


# In[ ]:





# In[ ]:





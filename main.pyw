# -*- coding: utf-8 -*-  
import tkinter
import os
root=tkinter.Tk()
root.title('CDNDrive GUI')
root['height']=100
root['width']=400

labelName=tkinter.Label(root,
                        text='链接:',
                        justify=tkinter.RIGHT,
                        anchor='e',
                        width=80)
labelName.place(x=5,y=5,width=40,height=20)
varName=tkinter.StringVar(root,value='')
entryName=tkinter.Entry(root,
                         width=80,
                         textvariable=varName)
entryName.place(x=50,y=5,width=300,height=20)

rememberMe=tkinter.IntVar(root,value=1)
def loign():
    name=entryName.get()
    com="CDNDrive download "+name
    os.system(com)
buttonOk=tkinter.Button(root,
                        text='下载',
                        command=loign)
buttonOk.place(x=30,y=50,width=50,height=20)
def pip():
    os.system("pip install CDNDrive")
buttonpip=tkinter.Button(root,
                        text='初始化',
                        command=pip)
buttonpip.place(x=80,y=50,width=50,height=20)

root.mainloop()
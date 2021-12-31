# -*- coding: utf-8 -*-
import tkinter
from tkinter import ttk
from tkinter import filedialog
import os

root = tkinter.Tk()
root.title('CDNDrive GUI')
root['height'] = 200
root['width'] = 400

label1 = tkinter.Label(root,
                       text='链接:',
                       justify=tkinter.RIGHT,
                       anchor='e',
                       width=80)
label1.place(x=5, y=5, width=50, height=20)
varLink = tkinter.StringVar(root, value='')
entryLink = tkinter.Entry(root,
                          width=80,
                          textvariable=varLink)
entryLink.place(x=60, y=5, width=300, height=20)

label2 = tkinter.Label(root,
                       text='Cookie:',
                       justify=tkinter.RIGHT,
                       anchor='e',
                       width=80)
label2.place(x=5, y=35, width=50, height=20)
varCookie = tkinter.StringVar(root, value='')
entryCookie = tkinter.Entry(root,
                            width=80,
                            textvariable=varCookie)
entryCookie.place(x=60, y=35, width=300, height=20)
label3 = tkinter.Label(root,
                       text='网站:',
                       justify=tkinter.RIGHT,
                       anchor='e',
                       width=80)
label3.place(x=5, y=65, width=50, height=20)
addr = tkinter.StringVar(value='4')
tre = tkinter.Label(root,
                    text='线程:',
                    justify=tkinter.RIGHT,
                    anchor='e',
                    width=80)
tre.place(x=145, y=65, width=50, height=20)
entrytre = tkinter.Entry(root,
                         width=80,
                         textvariable=addr)
entrytre.place(x=200, y=65, width=60, height=20)

comboSite = ttk.Combobox(root,
                         values=["bili", "baijia", "csdn", "sohu",
                                 "jian", "weibo", "ali", "163", "osc", "sogou"],
                         state="readonly")
comboSite.place(x=60, y=65, width=100, height=20)
comboSite.current(1)
label4 = tkinter.Label(root,
                       text='用户名:',
                       justify=tkinter.RIGHT,
                       anchor='e',
                       width=80)
label4.place(x=5, y=95, width=50, height=20)
varuser = tkinter.StringVar(root, value='')
entryuser = tkinter.Entry(root,
                          width=80,
                          textvariable=varuser)
entryuser.place(x=60, y=95, width=300, height=20)
label5 = tkinter.Label(root,
                       text='密码:',
                       justify=tkinter.RIGHT,
                       anchor='e',
                       width=80)
label5.place(x=5, y=125, width=50, height=20)
varpsw = tkinter.StringVar(root, value='')
entrypsw = tkinter.Entry(root,
                         width=80,
                         textvariable=varpsw)
entrypsw.place(x=60, y=125, width=300, height=20)


def download():
    name = entryLink.get()
    tre = entrytre.get()
    com = "cdrive download "+"-t "+tre+" "+name
    os.system(com)


buttonDL = tkinter.Button(root,
                          text='下载',
                          command=download)
buttonDL.place(x=30, y=170, width=50, height=20)


def loign():
    usr = entryuser.get()
    psw = entrypsw.get()
    site = comboSite.get()
    com = "cdrive login "+site+" "+usr+" "+psw
    os.system(com)


buttonlogin = tkinter.Button(root,
                             text='登陆',
                             command=loign)
buttonlogin.place(x=130, y=170, width=50, height=20)


def pip():
    os.system("pip install cdrive")


def upload():
    site = comboSite.get()
    tre = entrytre.get()
    file = filedialog.askopenfilename(initialdir=os.getcwd())
    com = "cdrive upload "+site+" -t "+tre+" "+"\""+file+"\""
    os.system(com)


buttonDL = tkinter.Button(root,
                          text='上传',
                          command=upload)
buttonDL.place(x=180, y=170, width=50, height=20)
buttonpip = tkinter.Button(root,
                           text='初始化',
                           command=pip)
buttonpip.place(x=80, y=170, width=50, height=20)


def loignc():
    cookies = entryCookie.get()
    site = comboSite.get()
    com = "cdrive cookies "+site+" SESSDATA="+cookies
    os.system(com)


buttonloginc = tkinter.Button(root,
                              text='登陆cookies',
                              command=loignc)
buttonloginc.place(x=230, y=170, width=80, height=20)
root.mainloop()

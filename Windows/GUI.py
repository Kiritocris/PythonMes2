import tkinter as tk
import sys

sys.path.append("../PythonMes2")
from Windows.Fonts import Fonts as nkf
import tkinter.messagebox as tkMessageBox

from Windows.Fonts.Fonts import header2, header3

sizex=1200
sizey=900

class Interfaz:
    def __init__(self,sizex,sizey):
        self.sizex=sizex
        self.sizey=sizey

    def window(self,title,sizex=None,sizey=None,bgcolor=None):
        if (not (sizex)):
            sizex=self.sizex
        if (not (sizey)):
            sizey=self.sizey
        window=tk.Tk()
        window.title(title)
        if(bgcolor):
            window.config(background=bgcolor)
        sizefull=str(sizex)+'x'+str(sizey)+'+'+'400'+'+'+'100'        
        window.geometry(sizefull)
        window.resizable(True,True)
        
        return window

    def btn(self,frame,text,colora,colorb,hovera,hoverb,padx,pady,command):
        newbtn=tk.Button(
            frame,
            text=text,
            activebackground=hovera,
            activeforeground=hoverb,
            bg=colora,
            fg=colorb,
            padx=str(padx),
            pady=str(pady),
            font=nkf.defaultfont(),
            command=command
        )
        return newbtn

    def entry(self,frame,colora,colorb,width,typetext=''):
        newentry=tk.Entry(
            frame,
            bg=colora,
            fg=colorb,
            width=width,
            show=typetext,
            font=header3()
        )
        return newentry

    def lbl(self,frame,colorb,padx,pady,text,font='default',family=None,bgcolor=None):

        if(not family):
            if(font=='default'):
                font=nkf.defaultfont()
            elif(font=='header1'):
                font=nkf.header1()
            elif(font=='header2'):
                font=nkf.header2()
            elif(font=='header3'):
                font=nkf.header3()
        else:
            if(font=='default'):
                font=nkf.defaultfont(family)
            elif(font=='header1'):
                font=nkf.header1(family)
            elif(font=='header2'):
                font=nkf.header2(family)
            elif(font=='header3'):
                font=nkf.header3(family)

        label=tk.Label(
            frame,
            fg=colorb,
            padx=padx,
            pady=pady,
            text=text,
            font=font
        )
        if(bgcolor):
            label.config(background=bgcolor)
        return label

    def lblframe(self,window,border=0,width=None,height=None):
        if(not width):
            width=self.sizex
        if(not height):
            height=self.sizey
        frame=tk.LabelFrame(
            window,
            width=width,
            height=height,
            bd=border
        )
        return frame

    def warning(self):
        tkMessageBox.showerror('Credenciales incorrectas','Usuario o contraseña incorrecto')
    
    def warningpage(self):
        tkMessageBox.showinfo('indice inferior a 0','Estas buscando en un indice que no existe')
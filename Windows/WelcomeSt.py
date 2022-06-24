from tkinter import LEFT, RIGHT, TOP
import sys
sys.path.append("../PythonMes2")

from Clases import List
from Windows import GUI

def open(st):
    btnpadx=5
    btnpady=2
    ntk=GUI.Interfaz(GUI.sizex,GUI.sizey+20)
    ntl=List.List()
    ntl.readdir()
    name=st

    Welcomestudent=ntk.window('Sign in')

    mainmessage=ntk.lblframe(Welcomestudent)
    mainmessage.pack()

    greeting='W e l c o m e  s t  '+name

    message=ntk.lbl(mainmessage,'#37123C',5,10,greeting,'header1')
    message.pack(expand=True)

    submessage=ntk.lbl(mainmessage,'#37123C',5,4,'Revisa tus calificaciones c:','header3')
    submessage.pack()

    content=ntk.lblframe(Welcomestudent)
    content.pack(fill='x')

    btnreturn=ntk.btn(content,'Salir','#37123C','#FFFFFF','#71677C','#A99F96',btnpadx,btnpady,Welcomestudent.destroy)
    btnreturn.pack(side=LEFT,padx=(50,0))

    framegrid=ntk.lblframe(Welcomestudent)
    framegrid.pack(fill='both')

    Welcomestudent.mainloop()
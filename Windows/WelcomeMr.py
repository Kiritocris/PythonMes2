from tkinter import LEFT, RIGHT, TOP
import sys

sys.path.append("../PythonMes2")

from Clases import List
from Windows import GUI

def open(mr):
    btnpadx=5
    btnpady=2
    externalpad=100
    ntk=GUI.Interfaz(GUI.sizex,GUI.sizey+20)
    ntl=List.List()
    ntl.readdir()
    name=mr
    Welcomemr=ntk.window('Sign in')

    mainmessage=ntk.lblframe(Welcomemr)
    mainmessage.pack()

    greeting='W e l c o m e  m r  '+name

    message=ntk.lbl(mainmessage,'#37123C',5,10,greeting,'header1')
    message.pack(expand=True)

    submessage=ntk.lbl(mainmessage,'#37123C',5,4,'Es tiempo de evaluar alumnos','header3')
    submessage.pack()

    content=ntk.lblframe(Welcomemr)
    content.pack(fill='x')

    listframe=ntl.createlist(Welcomemr)

    btnprevious=ntk.btn(content,'Anterior','#37123C','#FFFFFF','#71677C','#A99F96',btnpadx,btnpady,lambda :ntl.previous(Welcomemr))
    btnprevious.pack(side=LEFT,padx=externalpad)

    btnreturn=ntk.btn(content,'Salir','#37123C','#FFFFFF','#71677C','#A99F96',btnpadx,btnpady,Welcomemr.destroy)
    btnreturn.pack(side=LEFT,padx=(300,0))

    btnnext=ntk.btn(content,'Siguiente','#37123C','#FFFFFF','#71677C','#A99F96',btnpadx,btnpady,lambda :ntl.next(listframe,Welcomemr))
    btnnext.pack(side=RIGHT,padx=externalpad)

    Welcomemr.mainloop()


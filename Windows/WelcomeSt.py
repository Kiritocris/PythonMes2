from tkinter import LEFT, RIGHT, TOP
import sys
import pandas as pd
sys.path.append("../PythonMes2")

from Windows import GUI

def open(st):
    btnpadx=5
    btnpady=2
    ntk=GUI.Interfaz(GUI.sizex,GUI.sizey+20)
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

    file=pd.read_csv('Test/Test.csv',header=0)

    index=file.index[file['# Nombre'] == st].to_list()
    print(index)
    row=file.loc[ index[0] , : ]
    
    labels=[]
    tags=['Nombre','Matricula','Materia 1','Materia 2','Materia 3','Final']
    for i in range(len(tags)):
        tag=ntk.lbl(framegrid,'#37123C',30,40,tags[i],'header3')
        labels.append(tag)
        labels[i].grid(row=i,column=0,padx=(300,0),pady=(5,0))
    values=[]
    for i in range(len(tags)):
        tag=ntk.lbl(framegrid,'#37123C',30,40,row[i],'header3')
        values.append(tag)
        values[i].grid(row=i,column=1,padx=(250,0),pady=(5,0))


    Welcomestudent.mainloop()
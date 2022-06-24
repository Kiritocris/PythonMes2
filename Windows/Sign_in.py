import sys
import GUI

sys.path.append("../PythonMes2")
from Clases import Verify

def signinwindow():
    check=Verify.Verify()
    ntk=GUI.Interfaz(GUI.sizex,GUI.sizey)
    signin=ntk.window('Sign in',None,None,'#71677C')

    btnpadx=25
    btnpady=5
    mr='Bienvenido docente \n por favor ingrese sus credenciales'
    student='Bienvenido alumno \n por favor ingrese sus credenciales'
    font='Simsun'

    framegrid=ntk.lblframe(signin)
    framegrid.columnconfigure(0, weight=1)
    framegrid.columnconfigure(1,weight=1)
    framegrid.pack()
    #Script for label
    labelmr=ntk.lbl(framegrid,'#37123C',30,40,mr,'header2')
    labelmr.grid(row=0,column=0)
   
    labelst=ntk.lbl(framegrid,'#37123C',35,40,student,'header2')
    labelst.grid(row=0,column=1)
    
    labelmruser=ntk.lbl(framegrid,'#37123C',30,40,'Username','header3',font)
    labelmruser.grid(row=1,column=0)
    
    labelmrusers=ntk.lbl(framegrid,'#37123C',30,40,'Username','header3',font)
    labelmrusers.grid(row=1,column=1)

    entradamr=ntk.entry(framegrid,'#A99F96','#000000',30)
    entradamr.grid(row=2,column=0)

    entradamrpass=ntk.entry(framegrid,'#A99F96','#000000',30)
    entradamrpass.grid(row=4,column=0)

    entradast=ntk.entry(framegrid,'#A99F96','#000000',30)
    entradast.grid(row=2,column=1)

    entradastpass=ntk.entry(framegrid,'#A99F96','#000000',30)
    entradastpass.grid(row=4,column=1)

    labelmrpass=ntk.lbl(framegrid,'#37123C',30,40,'Passsword','header3',font)
    labelmrpass.grid(row=3,column=0)
    
    labelspass=ntk.lbl(framegrid,'#37123C',30,40,'Passsword','header3',font)
    labelspass.grid(row=3,column=1)

    btnentrymr=ntk.btn(framegrid,'Log in','#37123C','#FFFFFF','#71677C','#A99F96',btnpadx,btnpady,lambda:check.findcredentials(entradamrpass.get(),entradamr.get(),0,signin))
    btnentrymr.grid(row=5,column=0,pady=60)

    btnentrys=ntk.btn(framegrid,'Log in','#37123C','#FFFFFF','#71677C','#A99F96',btnpadx,btnpady,lambda:check.findcredentials(entradastpass.get(),entradast.get(),1,signin))
    btnentrys.grid(row=5,column=1,pady=60)

    btnreg=ntk.btn(framegrid,'Register','#37123C','#FFFFFF','#71677C','#A99F96',btnpadx,btnpady,lambda:check.addstudent())
    btnreg.grid(row=6,column=1,pady=60)
    
    signin.mainloop()

signinwindow()


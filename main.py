from Windows import GUI


ntk=GUI.Interfaz(1200, 800)

btnpadx=40
btnpady=5


mainwindow=ntk.window('Sign in')

signbtn=ntk.btn(mainwindow,'Sign in','#37123C','#FFFFFF','#71677C','#A99F96',btnpadx,btnpady,ntk.warning)
signbtn.pack()
labeluser=ntk.lbl(mainwindow,'#37123C',5,4,'Username')
labeluser.pack()
usermr=ntk.entry(mainwindow,'#A99F96','#37123C',8,'*')
usermr.pack()

mainwindow.mainloop()
import pandas as pd
import sys

sys.path.append("../PythonMes2")
from Windows import WelcomeMr
from Windows import WelcomeSt
from Windows import GUI

ntk=GUI.Interfaz(GUI.sizex,GUI.sizey)

class Verify():
    def __init__(self):
        self.__dirmr='Test\Testmr.csv'
        self.__dirst='Test\Test.csv'
        

    def findcredentials(self,dpass,duser,id,mainframe=None):
        if(id==1):
            file=pd.read_csv(self.__dirst,header=0)
        elif(id==0):
            file=pd.read_csv(self.__dirmr,header=0)
        passwords=file['Password']
        usernames=file['Username']
        names=file['# Nombre']
        self.indexpass=None
        self.indexuser=None
        name=None
        value=False
        indexpass=passwords.index.tolist()
        indexuser=usernames.index.tolist()
        for i in range(len(indexpass)):
            if(passwords[i]==dpass):
                self.indexpass=indexpass[i]
            if(usernames[i]==duser):
                self.indexuser=indexuser[i]
            if(not(isinstance(self.indexpass,type(None)) or isinstance(self.indexuser,type(None)))):
                if(self.indexpass==self.indexuser):
                    name=names[i]
                    value=True
                    break
        if(value):
            mainframe.destroy()
            if(id==1):
                WelcomeSt.open(name)
            else:
                WelcomeMr.open(name)
        else:
            ntk.warning()
    
    def addstudent(self):
        add=ntk.window('Agregar Estudiante',GUI.sizex,600)
        frametitle=ntk.lblframe(add)
        frametitle.pack(fill='x')
        
        framegrid=ntk.lblframe(add)
        framegrid.pack(fill='both')

        labeltitle=ntk.lbl(frametitle,'#37123C',5,10,'Bienvenido al registro','header1')
        labeltitle.pack()

        labels=[]
        tags=['Nombre','Matricula','Username','Password']
        for i in range(len(tags)):
            tag=ntk.lbl(framegrid,'#37123C',30,40,tags[i],'header3')
            labels.append(tag)
            labels[i].grid(row=i,column=0,padx=(30,0),pady=(5,0))
        btns=[]
        for i in range(len(tags)):
            tag=ntk.entry(framegrid,'#A99F96','#000000',30)
            btns.append(tag)  
            btns[i].grid(row=i,column=1,padx=(30,0),pady=(5,0))
        
        def iter(btns):
            data=[]
            for btn in btns:
                data.append(btn.get())
            return data


        save=ntk.btn(framegrid,'Save data','#37123C','#FFFFFF','#71677C','#A99F96',20,5,lambda: self.writestudent(iter(btns),add))
        save.grid(row=1,column=4,padx=(200,0),pady=(5,0))

        discard=ntk.btn(framegrid,'Discard data','#37123C','#FFFFFF','#71677C','#A99F96',20,5,add.destroy)
        discard.grid(row=2,column=4,padx=(200,0),pady=(5,0))


        add.mainloop()

    def writestudent(self,data,frame):
        from csv import writer
        
        datas=[data[0],data[1],0,0,0,0,data[2],data[3]]
        with open('./Test/Test.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(datas) 
            f_object.close()
        frame.destroy()
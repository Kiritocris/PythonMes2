import pandas as pd
import numpy as np
import sys 
sys.path.append(r'C:\Users\Kirito\Documents\Curso de programacion\Bootcamp\Proyectos\PythonMes2')
from Clases import Student
from Windows import GUI

ntk=GUI.Interfaz(GUI.sizex,GUI.sizey)

class List():

    def __init__(self):
        self.__dir='./Test/Test.csv'
        self.__list=[]
        self.indexi=0
        self.indexf=9
        self.listframe=None

    def readdir(self):
        file=pd.read_csv(self.__dir,header=0)
        self.__list=[]
        nombres=file['# Nombre'][self.indexi:self.indexf].to_list()
        matriculas=file['Matricula'][self.indexi:self.indexf].to_list()
        mat1s=file['Materia 1'][self.indexi:self.indexf].to_list()
        mat2s=file['Materia 2'][self.indexi:self.indexf].to_list()
        mat3s=file['Materia 3'][self.indexi:self.indexf].to_list()
        finals=file['Final'].to_list()
        print(nombres)
        print(self.indexi,self.indexf)
        size=len(nombres)
        for i in range(size):
            profilestudent=Student.Student(nombres[i],matriculas[i],mat1s[i],mat2s[i],mat3s[i],finals[i])
            self.__list.append(profilestudent)
        return size

    def previous(self,mainframe):
        if(self.indexi==0):
            ntk.warningpage()
        else:
            print('Entro en el else')
            self.indexi-=9
            self.indexf-=10
            self.readdir()
            self.listframe.destroy()
            self.createlist(mainframe)

    def next(self,frame,mainframe):
            self.indexi+=9
            self.indexf+=10
            frame.destroy()
            if(self.readdir()==0):
                ntk.warningpage()
                self.indexi-=9
                self.indexf-=10
            else:
                self.listframe.destroy()
                self.createlist(mainframe)

    def getlist(self):
        return self.__list
    
    def createlist(self,frame):
        print('Usando createlist')
        self.listframe=ntk.lblframe(frame)
        self.listframe.pack()

        nametag=ntk.lbl(self.listframe,'#37123C',6,20,'Nombre','header3','Helvetica')
        nametag.grid(row=0,column=0)

        nametag1=ntk.lbl(self.listframe,'#37123C',6,0,'Matricula','header3','Helvetica')
        nametag1.grid(row=0,column=1)

        nametag2=ntk.lbl(self.listframe,'#37123C',6,4,'Matematicas','header3','Helvetica')
        nametag2.grid(row=0,column=2)

        nametag3=ntk.lbl(self.listframe,'#37123C',6,4,'Programacion','header3','Helvetica')
        nametag3.grid(row=0,column=3)

        nametag4=ntk.lbl(self.listframe,'#37123C',6,4,'Calculo','header3','Helvetica')
        nametag4.grid(row=0,column=4)

        nametag6=ntk.lbl(self.listframe,'#37123C',6,4,'Modificar','header3','Helvetica')
        nametag6.grid(row=0,column=6)

        students=self.getlist()
        size=len(students)
        for i in range(size):
            data=students[i].getdata()
            print(data)
            i+=1
            for j in range(5):
                studentvalue=ntk.lbl(self.listframe,'#37123C',6,20,data[j],'header3','Helvetica')
                studentvalue.grid(row=i,column=j)
        try:
            btns=self.btns(students,0,students[0])
            btns=self.btns(students,1,students[1])
            btns=self.btns(students,2,students[2])
            btns=self.btns(students,3,students[3])
            btns=self.btns(students,4,students[4])
            btns=self.btns(students,5,students[5])
            btns=self.btns(students,6,students[6])
            btns=self.btns(students,7,students[7])
            btns=self.btns(students,8,students[8])
        except:
            print('No existe algun indice')
        
        return self.listframe

    def btns(self,value,i,student):
        if(isinstance(value[i],Student.Student)):
            btn=ntk.btn(self.listframe,'Modificar','#37123C','#FFFFFF','#71677C','#A99F96',10,5,lambda :self.changevalue(student.getdata()))
            btn.grid(row=i+1,column=6)
        return btn

    def changevalue(self,value):
        openvalu=ntk.window("Modificar calificacion")
        submessage=ntk.lbl(openvalu,'#37123C',5,4,'Revisa tus calificaciones c:','header3')
        submessage.pack()

        framegrid=ntk.lblframe(openvalu)
        framegrid.pack(fill='both')

        file=pd.read_csv('Test/Test.csv',header=0)

        index=file.index[file['# Nombre'] == value[0]].to_list()

        row=file.loc[ index[0] , : ]
        
        labels=[]
        tags=['Nombre','Matricula','Materia 1','Materia 2','Materia 3','Final']
        for i in range(len(tags)):
            tag=ntk.lbl(framegrid,'#37123C',30,40,tags[i],'header3')
            labels.append(tag)
            labels[i].grid(row=i,column=0,padx=(100,0),pady=(5,0))

        values=[]
        for i in range(len(tags)):
            tag=ntk.lbl(framegrid,'#37123C',30,40,row[i],'header3')
            values.append(tag)
            values[i].grid(row=i,column=1,padx=(100,0),pady=(5,0))

        entrys=[]
        for i in range(3):
            tag=ntk.entry(framegrid,'#A99F96','#000000',30)
            entrys.append(tag)
            entrys[i].grid(row=i+2,column=2,padx=(250,0),pady=(5,0))

        tagnew=ntk.lbl(framegrid,'#37123C',30,40,'Ingrese calificaciones nuevas','header3')
        tagnew.grid(row=1,column=2,padx=(250,0),pady=(5,0))

        submit=ntk.btn(framegrid,'Guardar cambios','#37123C','#FFFFFF','#71677C','#A99F96',5,2,lambda: self.savedata(openvalu,index[0],entrys[0].get(),entrys[1].get(),entrys[2].get()))
        submit.grid(row=5,column=2,padx=(250,0),pady=(5,0),)

        cancelsubmit=ntk.btn(framegrid,'Cancelar','#37123C','#FFFFFF','#71677C','#A99F96',5,2,openvalu.destroy)
        cancelsubmit.grid(row=6,column=2,padx=(250,0),pady=(5,0),)

        openvalu.mainloop()
    
    def savedata(self,frame,index,*args):
        data_p = pd.read_csv('./Test/Test.csv')
        data = np.array(data_p.values)

        newvalues=[]
        for i in range(3):
            newvalues.append(int(args[i]))
            data[index][i+2] = newvalues[i]
        prom=sum(newvalues)/len(newvalues)
        data[index][5]=int(prom)
        np.savetxt('./Test/Test.csv',data, delimiter=",",fmt="%s",header="Nombre,Matricula,Materia 1,Materia 2,Materia 3,Final,Username,Password")
        
        frame.destroy()

    
    

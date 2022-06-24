import pandas as pd

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

        nametag5=ntk.lbl(self.listframe,'#37123C',6,4,'Final','header3','Helvetica')
        nametag5.grid(row=0,column=5)

        nametag6=ntk.lbl(self.listframe,'#37123C',6,4,'Modificar','header3','Helvetica')
        nametag6.grid(row=0,column=6)

        students=self.getlist()
        size=len(students)
        for i in range(size):
            data=students[i].getdata()
            print(data)
            i+=1
            for j in range(6):
                studentvalue=ntk.lbl(self.listframe,'#37123C',6,20,data[j],'header3','Helvetica')
                studentvalue.grid(row=i,column=j)
        
        return self.listframe

    def changevalues(self,nombre):
        changewindow=ntk.window('Cambio de notas')
        print(nombre)

        changewindow.mainloop()
    
    

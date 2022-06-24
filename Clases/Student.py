class Student():
    def __init__(self,nombre,matricula,mat1,mat2,mat3,final=0):
        self.__nombre=nombre
        self.__matricula=matricula
        self.__final=final
        self.__mat1=mat1
        self.__mat2=mat2
        self.__mat3=mat3

    def getdata(self):
        return [self.__nombre,self.__matricula,self.__mat1,self.__mat2,self.__mat3,self.__final]

    def personaldata(self,user,password):
        self.__user=user
        self.__password=password
        return [self.__user,self.__password]
    

    


    
        
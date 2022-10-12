from tkinter import Entry, Place, Tk, Label, Button, messagebox
from turtle import width
import numpy as np

class app(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.label1 = Label(self, text="Ingrese un nùmero");self.label1.place(x=10,y=10)
        self.encasillas = Entry(self);self.encasillas.place(x=10,y=50)
        self.b1 = Button(self,text="Crear matriz", command=self.crear_matriz);self.b1.place(x=10,y=80)


    def crear_matriz(self):
        self.tamanio = int(self.encasillas.get())
        self.ncolumnas = self.tamanio
        self.nfilas = self.tamanio
        ncasillas = self.tamanio*self.tamanio
        global ncolumnas, nfilas
        ncolumnas = self.ncolumnas
        nfilas = self.nfilas
        #messagebox.showinfo("Si","Funciona el boton")
        self.v2 = Tk()
        #self.v2.geometry("1000x1000")
        #self.mm = [[""]*self.tamanio for y in range(self.tamanio )] #Otra forma de crear la matriz

        #----------------------------
        self.bcalcular = Button(self.v2,text="Resolver",command=self.CCdeterminante);self.bcalcular.place(x=10,y=10)
        #-----------------------------
        self.bborrar = Button(self.v2,text="Borrar",command=self.obtenerDeterminante2x2);self.bborrar.place(x=100,y=10)
        self.mm = []
        for fila in range(self.nfilas):
            self.mm.append([])
            for columna in range(self.ncolumnas):
                self.mm[fila].append(0)

        

        print(self.mm)


    
        #Agregar datos
        contador = 0
        for fila in range(0,self.nfilas):
            for columna in range(0,self.ncolumnas):
                valor = contador#str(fila)+","+str(self.ncolumnas)
                print(str(contador)+": "+str(valor))
                casilla = Entry(self.v2,width=4);casilla.place(x=(columna*30),y=((fila*30)+50))
                casilla.insert(0,valor)
                self.mm[fila][columna] = casilla
                valor = ""
                contador+=1


        """for fila in range(0,self.nfilas):
            for columna in range(0,self.ncolumnas):
                print(self.mm[fila][columna].get())"""

      




    def MObjeto_MNumero(self):

        for fila in range(0,self.nfilas):
            for columna in range(0,self.ncolumnas):
                print(self.mm[fila][columna].get())

        matrizObjeto = self.mm


        MNumero = []
        for fila in range(self.nfilas):
            MNumero.append([])
            for columna in range(self.ncolumnas):
                valor = int(self.mm[fila][columna].get())
                MNumero[fila].append(valor)


        self.matriz = np.array(MNumero)
        print("Numpt: ")
        print(self.matriz)
        return self.matriz


    def CCdeterminante(self):
        matriz1 =  self.MObjeto_MNumero()
        respuesta = "D: "
        # respuesta = respuesta+str(np.linalg.det(matriz1))
        #respuesta = respuesta+str(determinanteDeMatriz(matriz1))
        print(self.obtenerDeterminante2x2(matriz1))

        self.labelR = Label(self.v2,text=respuesta);self.labelR.place(x=150,y=10)   
        #self.labelR.config(textvariable=respuesta)     
                
        """
        self.matriz = np.arange(ncasillas, dtype=np.int64).reshape(self.tamanio, self.tamanio)
        print(matriz)
        for i in range(0,self.tamanio):
            for j in range(0,self.tamanio):
                casilla = Entry(self.v2, text="0",width=1);casilla.place(x=(i+5),y=(j+5))
                resultado = self.matriz.clip(array, )"""
    
    def determinanteDeMatriz(matriz):
        pass

    def obtenerSubMatriz2x2(matriz): # Brandon
        
        #array de sub matrices 2x2
        pass
    def obtenerDeterminante2x2(self,matriz): # Brandon
        # la forma de la matriz debe ser [[1,2],[3,4]]
        matriz = matriz# solo obtiene el vvalor de la matriz
        n00 = matriz[0][0]# obtiene la posicion de arriba izquierda
        n01 = matriz[0][1]#obtiene la posicion arriba derecha
        n10 = matriz[1][0]# obtiene la posicion abajo izquierda0
        n11 = matriz[1][1]#obtiene la posición derecha abajo

        print("n00: "+str(n00))# immprime valor para verificar
        print("n01: "+str(n01))# immprime valor para verificar
        print("n10: "+str(n10))# immprime valor para verificar
        print("n11: "+str   (n11))# immprime valor para verificar

        determinate = (n00*n11)-(n01*n10)# hace la resta de valores para la determinate
        print(determinate)# imprime la determinante
        return determinate#retrona la determinante

a = app()
a.mainloop()
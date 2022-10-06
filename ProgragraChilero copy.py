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
        ncolumnas = self.tamanio
        nfilas = self.tamanio
        ncasillas = self.tamanio*self.tamanio
        #messagebox.showinfo("Si","Funciona el boton")
        v2 = Tk()
        v2.geometry("1000x1000")
        #mm = [[""]*self.tamanio for y in range(self.tamanio )]
        mm = []
        for fila in range(nfilas):
            mm.append([])
            for columna in range(ncolumnas):
                mm[fila].append(0)

        

        print(mm)
        #Agregar datos
        contador = 0
        for fila in range(0,nfilas):
            for columna in range(0,ncolumnas):
                valor = contador#str(fila)+","+str(ncolumnas)
                print(str(contador)+": "+str(valor))
                casilla = Entry(v2,width=4);casilla.place(x=(fila*30),y=(columna*30))
                casilla.insert(0,valor)
                mm[fila][columna] = casilla
                valor = ""
                contador+=1

        for fila in range(0,nfilas):
            for columna in range(0,ncolumnas):
                print(mm[fila][columna].get())

        matriz = np.array(mm)
        print("Numpt: ")
        print(matriz)
            



    

                
        """
        self.matriz = np.arange(ncasillas, dtype=np.int64).reshape(self.tamanio, self.tamanio)
        print(matriz)
        for i in range(0,self.tamanio):
            for j in range(0,self.tamanio):
                casilla = Entry(v2, text="0",width=1);casilla.place(x=(i+5),y=(j+5))
                resultado = self.matriz.clip(array, )"""

a = app()
a.mainloop()
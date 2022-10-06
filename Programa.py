from tkinter import Entry, Place, Tk, Label, Button, messagebox
from turtle import width
import numpy as np


def determinanteDeMatriz(matriz):
    largo = len(matriz[0]);
    if largo == 1:
        return matriz[0][1];
    
    anterior = [[1 for x in range(0, largo+1)] for x in range(0, largo+1)]
    return determinante_Matriz(matriz, anterior)

def determinante_Matriz(matriz, anterior):
    largo = len(matriz[0]);
    if largo == 2:
        return obtenerDeterminante2x2(matriz)

    # Crea una matriz de (n-1)x(n-1) de tamaño llena de 0's
    # Los 0's serán cambiados por los valores obtenidos de las determinantes mas abajo.
    reducida = [[0 for x in range(0, largo -1)] for x in range(0, largo - 1)]
    renglonesConCeroEnMedio = []
    renglonSinCeroEnMedio = []
    subMatrices = obtenerSubMatrices2x2(matriz);
    intAnterior = obtenerIntDe(anterior);
    for i in largo - 1:
        for j in largo - 1:
            reducida[i][j] = obtenerDeterminante2x2(subMatrices[i][j]) / intAnterior[i][j]
            esCero = reducida[i][j] == 0
            perteneceARenglonesExtremos = i == 1 or i == largo - 1
            perteneceAColumnasExtremas = j == 1 or j == largo - 1
            if esCero and not perteneceARenglonesExtremos and not perteneceAColumnasExtremas:
                renglonesConCeroEnMedio.append(i)
        if renglonesConCeroEnMedio.count(i) == 0:
            renglonSinCeroEnMedio = reducida[i]

    # Si todos tienen un cero en medio, la determinante no puede ser obtenida, pues no se puede dividir entre 0.
    if len(renglonesConCeroEnMedio) == largo - 1:
        return None
    # Los renglones con 0's en medio, deben ser sumados con otros renglones para eliminar el 0.
    if len(renglonesConCeroEnMedio) != 0:
        for i in renglonesConCeroEnMedio:
            for j in len(reducida[i]):
                reducida[i][j] += renglonSinCeroEnMedio[j]
    
    return determinante_Matriz(reducida, matriz)


    

def obtenerSubMatrices2x2(matriz): # Nicolle
    # Obtiene una lista de todas las matrices de 2x2 dentro de la matriz especificada
    # Una matriz es una lista de renglones y un renglon es una lista de números.
    pass
def obtenerIntDe(matriz): # José Ángel
    # Obtiene la matriz int() de la matriz especificada.
    # Una matriz es una lista de renglones y un renglon es una lista de números.
    pass
def obtenerDeterminante2x2(matriz): # Brandon
    # Obtiene la determinante de una matriz 2x2 especificada.
    # Una matriz es una lista de renglones y un renglon es una lista de números.
    pass
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
        #messagebox.showinfo("Si","Funciona el boton")
        self.v2 = Tk()
        #self.v2.geometry("1000x1000")
        #self.mm = [[""]*self.tamanio for y in range(self.tamanio )] #Otra forma de crear la matriz

        #----------------------------
        self.bcalcular = Button(self.v2,text="Resolver",command=self.CCdeterminante);self.bcalcular.place(x=10,y=10)
        #-----------------------------
        self.bborrar = Button(self.v2,text="Borrar");self.bborrar.place(x=100,y=10)
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
        respuesta = respuesta+str(determinanteDeMatriz(self.mm))
        

        self.labelR = Label(self.v2,text=respuesta);self.labelR.place(x=150,y=10)   
        #self.labelR.config(textvariable=respuesta)     
                
        """
        self.matriz = np.arange(ncasillas, dtype=np.int64).reshape(self.tamanio, self.tamanio)
        print(matriz)
        for i in range(0,self.tamanio):
            for j in range(0,self.tamanio):
                casilla = Entry(self.v2, text="0",width=1);casilla.place(x=(i+5),y=(j+5))
                resultado = self.matriz.clip(array, )"""

a = app()
a.mainloop()
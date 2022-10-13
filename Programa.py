from tkinter import Entry, Place, Tk, Label, Button, messagebox
from turtle import width
import numpy as np


def determinanteDeMatriz(matriz):
    largo = len(matriz[0])
    if largo == 1:
        return matriz[0][1]

    anterior = [[1 for x in range(0, largo+1)] for x in range(0, largo+1)]
    return determinante_Matriz(matriz, anterior)


def determinante_Matriz(matriz, anterior):
    print("Anterior:\n", np.matrix(anterior))
    print("Matriz:\n", np.matrix(matriz))

    largo = len(matriz[0])
    largoReducida = largo - 1
    transpuestaMatriz = obtenerTranspuestaDe(matriz)
    if determinanteSera0(matriz) or determinanteSera0(transpuestaMatriz):
        return 0
    if largo == 2:
        return obtenerDeterminante2x2(matriz) / obtenerIntDe(anterior)[0][0]

    while tieneCeros(obtenerIntDe(matriz)):
        eliminarCerosDeIntDe(matriz)

    # Crea una matriz de (n-1)x(n-1) de tamaño llena de 0's
    # Los 0's serán cambiados por los valores obtenidos de las determinantes mas abajo.
    reducida = [[0 for x in range(0, largo - 1)] for x in range(0, largo - 1)]
    subMatrices = obtenerSubMatrices2x2(matriz)
    intAnterior = obtenerIntDe(anterior)
    for i in range(largoReducida):
        for j in range(largoReducida):
            reducida[i][j] = obtenerDeterminante2x2(
                subMatrices[i*largoReducida + j]) / intAnterior[i][j]

    print("Reducida:\n", np.matrix(reducida))
    # Si todos tienen un cero en medio, la determinante no puede ser obtenida, pues no se puede dividir entre 0.
    if determinanteSera0(reducida) or determinanteSera0(obtenerTranspuestaDe(reducida)):
        return 0
    # Los renglones con 0's en medio, deben ser sumados con otros renglones para eliminar el 0.
    while tieneCeros(obtenerIntDe(reducida)):
        eliminarCerosDeIntDe(reducida)

    return determinante_Matriz(reducida, matriz)


def determinanteSera0(matriz) -> bool:
    for renglon in matriz:
        renglonEn0 = True
        for celda in matriz:
            if celda != 0:
                renglonEn0 = False
        if renglonEn0:
            return True

    for renglon in matriz:
        if matriz.count(renglon) > 1:
            return True


def obtenerTranspuestaDe(matriz):
    transpuesta = []
    rango = range(len(matriz))

    for celda in rango:
        renglonTranspuesto = []
        for fila in rango:
            renglonTranspuesto.append(matriz[fila][celda])
        transpuesta.append(renglonTranspuesto)
    return transpuesta


def eliminarCerosDeIntDe(matriz):
    largo = len(matriz[0])
    rango = range(1, largo - 1)

    simplificada = []
    for iFila in rango:
        for jCelda in rango:
            esCero = matriz[iFila][jCelda] == 0
            if not esCero:
                continue
            renglonesSinCeroEnCelda = obtenerRenglonesSinCeroEnCelda(
                matriz, jCelda)
            print("Renglón ", iFila + 1, "+", renglonesSinCeroEnCelda[0] + 1)
            sumarRenglonARenglonB(matriz, iFila, renglonesSinCeroEnCelda[0])


def obtenerRenglonesSinCeroEnCelda(matriz: [[float]], celda: int) -> [int]:
    renglones = []
    for renglon in range(len(matriz)):
        if matriz[renglon][celda] != 0:
            renglones.append(renglon)
    return renglones


def sumarRenglonARenglonB(matriz, renglonA, renglonB):
    matriz[renglonA] = sumarRenglones(matriz[renglonA], matriz[renglonB])


def sumarRenglones(renglonA, renglonB) -> [float]:
    renglonC = []
    for i in range(len(renglonA)):
        renglonC.append(renglonA[i] + renglonB[i])
    return renglonC


def tieneCeros(matriz) -> bool:
    for renglon in matriz:
        for celda in renglon:
            if celda == 0:
                return True
    return False


def obtenerSubMatrices2x2(matriz):  # Nicolle
    # Obtiene una lista de todas las matrices de 2x2 dentro de la matriz especificada
    # Una matriz es una lista de renglones y un renglon es una lista de números.
    lista = []
    matricitas = []
    ren = []
    ren2 = []
    i = 0
    j = 0
    n = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz)-1:
            ren = matriz[i][j:j+2]
            ren2.append(ren)
            while n < len(ren2)-1 and n <= (len(ren2)-len(matriz)):
                matricitas = [ren2[n], ren2[n+len(matriz)-1]]
                lista.append(matricitas)
                n = n+1
            j = j+1
        i = i+1
    return lista  # lista con las matrices 2x2


def obtenerIntDe(matriz):  # José Ángel
    # Obtiene la matriz int() de la matriz especificada.
    # Una matriz es una lista de renglones y un renglon es una lista de números.
    intde = [[i for i in renglon] for renglon in matriz]
    largo = len(intde[0])
    alto = len(intde)
    # Quita la ultima fila
    intde[alto-1] = None
    intde.remove(None)

    # Quita la primera fila
    intde.remove(intde[0])

    # Quita la primera y la ultima entrada de las filas restantes
    for ren in intde:
        ren[largo-1] = None
        ren.remove(None)
        ren.remove(ren[0])
    return intde


def obtenerDeterminante2x2(matriz):  # Brandon
    # Obtiene la determinante de una matriz 2x2 especificada.
    # Una matriz es una lista de renglones y un renglon es una lista de números.
    # la forma de la matriz debe ser [[1,2],[3,4]]
    matriz = matriz  # solo obtiene el vvalor de la matriz
    n00 = matriz[0][0]  # obtiene la posicion de arriba izquierda
    n01 = matriz[0][1]  # obtiene la posicion arriba derecha
    n10 = matriz[1][0]  # obtiene la posicion abajo izquierda
    n11 = matriz[1][1]  # obtiene la posición derecha abajo

    # hace la resta de valores para la determinate
    determinate = (n00*n11)-(n01*n10)

    return determinate  # retrona la determinante


class app(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.label1 = Label(self, text="Ingrese un nùmero")
        self.label1.place(x=10, y=10)
        self.encasillas = Entry(self)
        self.encasillas.place(x=10, y=50)
        self.b1 = Button(self, text="Crear matriz", command=self.crear_matriz)
        self.b1.place(x=10, y=80)

    def crear_matriz(self):
        self.tamanio = int(self.encasillas.get())
        self.ncolumnas = self.tamanio
        self.nfilas = self.tamanio
        ncasillas = self.tamanio*self.tamanio
        global ncolumnas, nfilas
        ncolumnas = self.ncolumnas
        nfilas = self.nfilas
        self.v2 = Tk()
        # self.v2.geometry("1000x1000")
        # self.mm = [[""]*self.tamanio for y in range(self.tamanio )] #Otra forma de crear la matriz

        # ----------------------------
        self.bcalcular = Button(self.v2, text="Resolver",
                                command=self.CCdeterminante)
        self.bcalcular.place(x=10, y=10)
        # -----------------------------
        # self.bborrar = Button(self.v2,text="Borrar",command=obtenerDeterminante2x2);self.bborrar.place(x=100,y=10)
        self.mm = []
        for fila in range(self.nfilas):
            self.mm.append([])
            for columna in range(self.ncolumnas):
                self.mm[fila].append(0)

        # Agregar datos
        contador = 0
        for fila in range(0, self.nfilas):
            for columna in range(0, self.ncolumnas):
                valor = 1  # str(fila)+","+str(self.ncolumnas)
                if fila == columna:
                    valor = 0

                casilla = Entry(self.v2, width=4)
                casilla.place(x=(columna*30), y=((fila*30)+50))
                casilla.insert(0, valor)
                self.mm[fila][columna] = casilla
                valor = ""
                contador += 1

    def MObjeto_MNumero(self):
        matrizObjeto = self.mm

        MNumero = []
        for fila in range(self.nfilas):
            MNumero.append([])
            for columna in range(self.ncolumnas):
                valor = int(self.mm[fila][columna].get())
                MNumero[fila].append(valor)

        return MNumero

    def CCdeterminante(self):
        matriz1 = self.MObjeto_MNumero()
        respuesta = "D: "
        # respuesta = respuesta+str(np.linalg.det(matriz1))
        respuesta = respuesta+str(determinanteDeMatriz(matriz1))

        self.labelR = Label(self.v2, text=respuesta)
        self.labelR.place(x=150, y=10)
        # self.labelR.config(textvariable=respuesta)


a = app()
a.mainloop()

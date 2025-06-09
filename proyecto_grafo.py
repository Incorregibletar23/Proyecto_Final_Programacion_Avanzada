# 1.- ---------- Encabezado ----------

'''
Programa: Proyecto Grafo - proyecto_grafo.py
Autores:
- Ramírez Vásquez Eduardo
- Rosas López Renata
Fecha de creación: 14/05/2025
Fechas de modificación:
    Eduardo:
        - 31/05/2025 2:30 pm(v2.1: Se empezará a hacer la interfaz gráfica del proyecto)
        - 01/06/2025 2:13 pm(v2.2: Se hace el lobby de la aplicación)
        - 02/06/2025 1:32 pm(v2.2: Prueba 7)
        - 02/06/2025 1:52 pm(v2.2: Prueba 8)
        - 02/06/2025 2:40 pm(v2.2: Pruebas de github finalizadas, se empezará a trabajar en conjunto ahora)
        - 02/06/2025 2:40 pm(v2.3: Agregue las especificaciones de bordes)
        - 02/06/2025 1:24 pm(v2.4: Empecé a hacer la interfaz gráfica de administrador)
        - 07/06/2025 5:30 pm(v2.5: Se agregó el grafo y se empezó a hacer el botón de agregar salas)
        - 08/06/2025 1:48 pm(v2.6: Se agregó la funcion de agregar salas al botón)
        - 08/06/2025 1:48 pm(v2.7: Se agregaron las salas iniciales al abrir el código)
        - 08/06/2025 2:48 pm(v2.8: Se agregó la funcion de eliminar salas al botón)
        - 08/06/2025 3:48 pm(v2.9: Se agregó la funcion de agregar caminos al botón)
        - 08/06/2025 4:41 pm(v2.10: Se agregó la funcion de eliminar caminos al botón)
        - 08/06/2025 9:46 pm(v2.11: Se hizo las funciones de  el botón de mostrar y el subbotón salas)
        - 09/06/2025 3:07 pm(v2.12: Se hizo el mapa)

    Renata:
        - 02/06/2025 1:32 pm(v2.2: Se empieza a probar el github)
        - 02/06/2025 1:32 pm(v2.2: Prueba 6)
        - 02/06/2025 1:55 pm(v2.2: Prueba 9)
        - 02/06/2025 1:32 pm(v2.2: Prueba 10)
        - 08/06/2025 9:48 pm(v2.3: Empece a modificar la ventana usuario)
'''

# 2.- ---------- Importación de módulos y bibliotecas ----------

#           IMPORTACIONES PARA TERMINAL

import os
import networkx as nx
import matplotlib.pyplot as plt
import tracemalloc
import time

#           FIN DE IMPORTACIONES PARA TERMINAL

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 3.- ---------- Definición de funciones o clases ----------

#-----------CLASES PARA USO EN LA TERMINAL:----------

'''
class NodoDoble:
    def __init__(self, destino, peso):
        self.destino = destino
        self.peso = peso
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    def __init__(self):
        self.inicio = None
    def insertarFinal(self, destino, peso):
        nuevo_nodo = NodoDoble(destino, peso)
        if not self.inicio:
            self.inicio = nuevo_nodo
            return
        actual = self.inicio
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo
        nuevo_nodo.anterior = actual
    def eliminar(self, destino):
        actual = self.inicio
        while actual:
            if actual.destino == destino:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                if actual == self.inicio:
                    self.inicio = actual.siguiente
                return True
            actual = actual.siguiente
        return False
    def mostrar(self):
        actual = self.inicio
        while actual:
            print(f"{actual.destino}--{actual.peso}--", end=" -> ")
            actual = actual.siguiente
        print("None")
    def lista_de_aristas(self):
        aristas = []
        actual = self.inicio
        while actual:
            aristas.append((actual.destino, actual.peso))
            actual = actual.siguiente
        return aristas

class Grafo:
    def __init__(self):
        self.grafo = {}
    def agregar_vertice(self):
        while True:
            try:
                rango = int(input('¿Cuántas salas vas a ingresar? '))
                break
            except ValueError:
                print("Por favor, ingresa un número entero.")
        for i in range(rango):
            vertice = input(f'Ingresa sala {i+1}: ')
            if vertice in self.grafo:
                print(f"La sala '{vertice}' ya existe.")
                time.sleep(2.2)
            else:
                self.grafo[vertice] = ListaDobleEnlazada()
                print(f"Sala '{vertice}' agregada.")
                time.sleep(2.2)
    def agregar_arista(self):
        while True:
            try:
                rango = int(input('¿Cuántos caminos vas a ingresar? '))
                break
            except ValueError:
                print("Por favor, ingresa un número entero válido para los caminos.")
        for _ in range(rango):
            nodo_1 = input('Ingresa sala de origen: ')
            nodo_2 = input('Ingresa Sala de destino: ')
            while True:
                try:
                    peso = int(input('Ingresa distancia entre salas: '))
                    break
                except ValueError:
                    print("Por favor, ingresa un entero para las distancias.")
            if nodo_1 in self.grafo:
                if nodo_2 in self.grafo:
                    self.grafo[nodo_1].insertarFinal(nodo_2, peso)
                    print(f'Sala de {nodo_1} a {nodo_2} agregada con {peso} metros de separación')
                    time.sleep(3)
                else:
                    print(f'{nodo_2} no existe.')
                    time.sleep(2.2)
            else:
                print(f'{nodo_1} no existe.')
                time.sleep(2.2)
    def eliminar_arista(self):
        origen = input('Ingresa sala de origen: ')
        destino = input('Ingresa sala de destino: ')
        try:
            if origen in self.grafo:
              if destino in self.grafo:
                  eliminado = self.grafo[origen].eliminar(destino)

                  if not eliminado:
                      raise ValueError(f"No existe un camino de {origen} a {destino}.")
                      time.sleep(2.2)
                  else:
                      print(f"Sala de {origen} a {destino} eliminada.")
                      time.sleep(2.2)
              else:
                  raise KeyError(f"La sala: {destino} no existe.")
                  time.sleep(2.2)
            else:
                raise KeyError(f"La sala: {origen} no existe.")
                time.sleep(2.2)
        except (KeyError, ValueError) as e:
            print(e)
            time.sleep(2.5)
    def eliminar_vertice(self):
        vertice = input('Ingresa la sala que quieres eliminar: ')
        try:
            if vertice in self.grafo:
                del self.grafo[vertice]
                for lista in self.grafo.values():
                    lista.eliminar(vertice)
                print(f"Sala '{vertice}' eliminado.")
                time.sleep(2.2)
            else:
                raise KeyError(f"La sala '{vertice}' no existe.")
                time.sleep(2.2)
        except KeyError as e:
            print(e)
            time.sleep(2.2)
    def encontrar(self):
        vertice = input('Ingresa sala a buscar: ')
        if vertice in self.grafo:
            print(f"Caminos desde '{vertice}':")
            self.grafo[vertice].mostrar()
            time.sleep(5)
        else:
            print(f"La sala: '{vertice}' no existe.")
            time.sleep(2.2)
    def ver_grafo(self):
        print("Mostrando salas en lista:")
        for vertice, lista in self.grafo.items():
            print(f"{vertice} -> ", end="")
            lista.mostrar()
        time.sleep(7)
    def matriz_de_adyacencia(self):
        vertices = list(self.grafo.keys())
        n = len(vertices)
        indices = {nodo: i for i, nodo in enumerate(vertices)}
        matriz = [[0] * n for _ in range(n)]
        for vertice, lista in self.grafo.items():
            origen_idx = indices[vertice]
            aristas = lista.lista_de_aristas()
            for destino, peso in aristas:
                destino_idx = indices[destino]
                matriz[origen_idx][destino_idx] = int(peso)
        print('MATRIZ DE ADYACENCIA')
        for fila in matriz:
            print(fila)
        return matriz
    def visualizar(self):
        G = nx.DiGraph()
        for origen, lista in self.grafo.items():
            for destino, peso in lista.lista_de_aristas():
                G.add_edge(origen, destino, weight=peso)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, arrows=True)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.title("Mapa de salas")
        plt.show()


    def menu(self):
        print()
        while True:
            print("--- Bienvenido administrador ---")
            print("1. Agregar salas")
            print("2. Agregar caminos")
            print("3. Mostrar lista de salas")
            print("4. Ver mapa")
            print("5. Eliminar sala")
            print("6. Eliminar camino")
            print("7. Buscar caminos de una sala")
            print('8. Ver matriz de adyacencia de salas')
            print("9. Ver uso de memoria")
            print("10. Salir")
            print()
            try:
                opcion = input("Selecciona una opción: ")
                if opcion == '1':
                    self.agregar_vertice()
                elif opcion == '2':
                    self.agregar_arista()
                elif opcion == '3':
                    self.ver_grafo()
                elif opcion == '4':
                    self.visualizar()
                    time.sleep(10)
                elif opcion == '5':
                    self.eliminar_vertice()
                elif opcion == '6':
                    self.eliminar_arista()
                elif opcion == '7':
                    self.encontrar()
                elif opcion == '8':
                    self.matriz_de_adyacencia()
                    time.sleep(10)
                elif opcion == '9':
                    usoMemoria()
                    time.sleep(4)
                elif opcion == '10':
                    break
                else:
                    raise ValueError("Opción no válida.")
            except ValueError as e:
                print(e)

class BusquedaDeCamino:
    def __init__(self, matriz, origen, destino):
        self.matriz = matriz
        self.origen = origen
        self.destino = destino
        self.caminos = []
    def recursividad(self, actual, camino, distancia):
        if actual == self.destino:
            self.caminos.append((camino, distancia))
            return

        for s, d in enumerate(self.matriz[actual]):
            if d != 0 and s not in camino:
                self.recursividad(s, camino + [s], distancia + d)
    def dfs(self):
        self.recursividad(self.origen, [self.origen], 0)

        if not self.caminos:
            return None, []
        else:
            distanciaminima = self.caminos[0][1]
            for _, d in self.caminos[1:]:
                if d < distanciaminima:
                    distanciaminima = d

            caminosminimos = [i for i, d in self.caminos if d == distanciaminima]
            return distanciaminima, caminosminimos

def usoMemoria():
    current, peak = tracemalloc.get_traced_memory()
    print(f"Memoria utilizada: {current / (1024 ** 2):.2f} MB")
    print(f"Memoria máxima utilizada: {peak / (1024 ** 2):.2f} MB")

def menu_usuario(grafo):
    print()
    while True:
        print("--- Bienvenido usuario ---")
        print("1. Mostrar mapa")
        print("2. Calcular el camino más corto entre dos salas")
        print("3. Salir")
        print()

        try:
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                grafo.visualizar()
                time.sleep(10)
            elif opcion == '2':
                grafo.visualizar()
                time.sleep(1)
                origen = input("Ingresa el vértice de origen: ")
                destino = input("Ingresa el vértice de destino: ")
                if origen in grafo.grafo and destino in grafo.grafo:
                    vertices = list(grafo.grafo.keys())
                    indices = {nodo: i for i, nodo in enumerate(vertices)}
                    matriz = grafo.matriz_de_adyacencia()
                    origen_idx = indices[origen]
                    destino_idx = indices[destino]
                    busqueda = BusquedaDeCamino(matriz, origen_idx, destino_idx)
                    distancia, caminos = busqueda.dfs()
                    if distancia is None:
                        print(f"No hay camino entre {origen} y {destino}.")
                        time.sleep(2.2)
                    else:
                        print(f"La distancia más corta es: {distancia}")
                        print("Posibles caminos:")
                        for camino in caminos:
                            print(" -> ".join([list(grafo.grafo.keys())[i] for i in camino]))
                        time.sleep(10)
                else:
                    print(f"Uno o ambas salas '{origen}' y '{destino}' no existen.")
                    time.sleep(2.2)
            elif opcion == '3':
                break
            else:
                raise ValueError("Opción no válida.")
        except ValueError as e:
            print(e)

def menu()
    grafo = Grafo()
    for i in range(12):
        grafo.grafo[str(i)] = ListaDobleEnlazada()

    conexiones = [
        [0, 4, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    for i in range(len(conexiones)):
        for j in range(len(conexiones[i])):
            peso = conexiones[i][j]
            if peso != 0:
                grafo.grafo[str(i)].insertarFinal(str(j), peso)
    while True:
        print("--- Bienvenido ---")
        print("1. Entrar como Administrador")
        print("2. Entrar como Usuario")
        print("3. Salir")
        try:
            opcion = input("Selecciona una opción: ")
            if opcion == '1':
                grafo.menu()
            elif opcion == '2':
                menu_usuario(grafo)
            elif opcion == '3':
                break
            elif opcion == '4':

                matriz = [
                    [0, 4, 3, 0],
                    [4, 0, 0, 1],
                    [3, 0, 0, 1],
                    [0, 1, 1, 0]
                ]


                busqueda = BusquedaDeCamino(matriz, 0, 3)
                distancia, caminos = busqueda.dfs()
                print(distancia)
                print(caminos)
                time.sleep(7)


            else:
                raise ValueError("Opción no válida.")
        except ValueError as e:
            print(e)
'''
#-----------FIN DE LAS CLASES DE TERMINAL----------

#-----------CLASES DEL GRAFO----------

class NodoDoble:
    def __init__(self, destino, peso):
        self.destino = destino
        self.peso = peso
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    def __init__(self):
        self.inicio = None
    def insertarFinal(self, destino, peso):
        nuevo_nodo = NodoDoble(destino, peso)
        if not self.inicio:
            self.inicio = nuevo_nodo
            return
        actual = self.inicio
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo
        nuevo_nodo.anterior = actual
    def eliminar(self, destino):
        actual = self.inicio
        while actual:
            if actual.destino == destino:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                if actual == self.inicio:
                    self.inicio = actual.siguiente
                return True
            actual = actual.siguiente
        return False
    def mostrar(self):
        actual = self.inicio
        while actual:
            print(f"{actual.destino}--{actual.peso}--", end=" -> ")
            actual = actual.siguiente
        print("None")
    def lista_de_aristas(self):
        aristas = []
        actual = self.inicio
        while actual:
            aristas.append((actual.destino, actual.peso))
            actual = actual.siguiente
        return aristas
    def mostrarNuevo(self, origen, ventana):
        actual = self.inicio
        salas = []
        texto1 = origen + '   ' 
        salas.append(texto1)
        while actual:
            texto = '   ' + str(actual.destino) + ', distancia: ' + str(actual.peso) + 'm' + '   '
            salas.append(texto)
            actual = actual.siguiente
        salida = '-->'.join(salas)
        
        self.etiquetaSalSal = tk.Label(
            ventana,
            text=salida,                        # Texto que muestra la etiqueta
            font=("Century Gothic", 12, "bold"),# Fuente, tamaño y estilo (negrita)
            fg="black",                         # Color del texto
            bg="#f0f0f0",                       # Color del fondo de la etiqueta
            width=80,                           # Ancho de la etiqueta (en caracteres aprox.)
            anchor="center",                    # Posición del texto dentro de la etiqueta
            relief="flat",                      # Tipo de borde (puede ser flat, raised, sunken, ridge, groove, solid)
            bd=2,                               # Grosor del borde
            padx=10,                            # Espacio interno horizontal
            pady=5                              # Espacio interno vertical
        )
        self.etiquetaSalSal.pack(pady=10)

class Grafo:
    def __init__(self):
        self.grafo = {}
    def agregarSal(self, rango, ventana):
        # Establecer rango y ventana para poder ser usados durante las funciones
        self.rango = int(rango)
        self.ventana = ventana
        # Contador
        self.contador = 0
        # Cosas de agregar salas (Para poder agregar salas y que se creen y destruyan los objetos)
        self.objetos = []
        self.accAgrSalSal()
    def accAgrSalSal(self):
        #          ROMPER EL BUCLE
        if self.contador >= self.rango:
            messagebox.showinfo('Completado', f'Se han agregado TODAS las salas correctamente')
            return
            # NOTA: el return no retorna nada, ya que solo sirve para terminar el bucle
        # Eliminar los objetos de la sala que se está escribiendo para insertar los de la siguiente sala
        for objeto in self.objetos:
            objeto.destroy()
        self.objetos.clear()
        # Etiqueta de agregar sala
        self.etiquetaAgrSal = tk.Label(
            self.ventana,
            text=f"Ingresa el nombre de la Sala {self.contador + 1}",# Texto que muestra la etiqueta
            font=("Century Gothic", 12, "bold"),# Fuente, tamaño y estilo (negrita)
            fg="black",                         # Color del texto
            bg="#f0f0f0",                       # Color del fondo de la etiqueta
            width=30,                           # Ancho de la etiqueta (en caracteres aprox.)
            anchor="center",                    # Posición del texto dentro de la etiqueta
            relief="flat",                      # Tipo de borde (puede ser flat, raised, sunken, ridge, groove, solid)
            bd=2,                               # Grosor del borde
            padx=10,                            # Espacio interno horizontal
            pady=5                              # Espacio interno vertical
        )
        # Entrada de nombre de sala
        self.entradaNomSal = tk.Entry(
            self.ventana,
            font=("Century Gothic", 12),
            bg="#ffffff",           # Fondo 
            fg="#333333",           # Texto 
            bd=2,                   # Grosor del borde
            relief="groove",        # Estilo del borde
            width=30,               # Ancho en caracteres
            justify="center",       # Texto centrado
            insertbackground="black"# Color del cursor
        )
        # Boton ingresar el nombre de la sala
        self.botonNomSal = tk.Button(
            self.ventana,
            text='Ingresar',
            font=("Century Gothic", 10),
            bg="#abaeb8",              # Fondo
            fg="black",                # Color del texto
            activebackground="#4b5572",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=23,                   # Espacio horizontal interno
            pady=3,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=lambda: self.ingNomSal(self.entradaNomSal)
        )
        # Posiciones
        self.etiquetaAgrSal.pack(pady=10)
        self.entradaNomSal.pack(pady=10)
        self.botonNomSal.pack(pady=10)
        # Colocar cada objeto en la lista objetos
        self.objetos.append(self.etiquetaAgrSal)
        self.objetos.append(self.entradaNomSal)
        self.objetos.append(self.botonNomSal)
    def ingNomSal(self, entradaSala):
        sala = str(entradaSala.get())
        if sala in self.grafo:
            messagebox.showinfo('Sala existente', f'La sala {sala} ya existe')
        else:
            self.grafo[sala] = ListaDobleEnlazada()
            messagebox.showinfo('Sala Ingresada', f'La sala {sala} se insertó correctamente')
            self.contador += 1
            # Volver a ejecutar acción agregar sala por sala:
            self.accAgrSalSal()
    def eliminarSal(self, rango, ventana):
        # Establecer rango y ventana para poder ser usados durante las funciones
        self.rango = int(rango)
        self.ventana = ventana
        # Contador
        self.contador = 0
        # Cosas de eliminar salas (Para poder eliminar salas y que se creen y destruyan los objetos)
        self.objetos = []
        self.accEliSalSal()
    def accEliSalSal(self):
        #          ROMPER EL BUCLE
        if self.contador >= self.rango:
            messagebox.showinfo('Completado', f'Se han eliminado TODAS las salas correctamente')
            return
            # NOTA: el return no retorna nada, ya que solo sirve para terminar el bucle
        # Eliminar los objetos de la sala que se está escribiendo para insertar los de la siguiente sala
        for objeto in self.objetos:
            objeto.destroy()
        self.objetos.clear()
        # Etiqueta de eliminar sala
        self.etiquetaEliSal = tk.Label(
            self.ventana,
            text=f"Ingresa el nombre de la Sala {self.contador + 1} a eliminar",# Texto que muestra la etiqueta
            font=("Century Gothic", 12, "bold"),# Fuente, tamaño y estilo (negrita)
            fg="black",                         # Color del texto
            bg="#f0f0f0",                       # Color del fondo de la etiqueta
            width=30,                           # Ancho de la etiqueta (en caracteres aprox.)
            anchor="center",                    # Posición del texto dentro de la etiqueta
            relief="flat",                      # Tipo de borde (puede ser flat, raised, sunken, ridge, groove, solid)
            bd=2,                               # Grosor del borde
            padx=10,                            # Espacio interno horizontal
            pady=5                              # Espacio interno vertical
        )
        # Entrada de nombre de sala
        self.entradaNomSal = tk.Entry(
            self.ventana,
            font=("Century Gothic", 12),
            bg="#ffffff",           # Fondo 
            fg="#333333",           # Texto 
            bd=2,                   # Grosor del borde
            relief="groove",        # Estilo del borde
            width=30,               # Ancho en caracteres
            justify="center",       # Texto centrado
            insertbackground="black"# Color del cursor
        )
        # Boton ingresar el nombre de la sala
        self.botonNomSal = tk.Button(
            self.ventana,
            text='Ingresar',
            font=("Century Gothic", 10),
            bg="#abaeb8",              # Fondo
            fg="black",                # Color del texto
            activebackground="#4b5572",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=23,                   # Espacio horizontal interno
            pady=3,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=lambda: self.eliIngNomSal(self.entradaNomSal)
        )
        # Posiciones
        self.etiquetaEliSal.pack(pady=10)
        self.entradaNomSal.pack(pady=10)
        self.botonNomSal.pack(pady=10)
        # Colocar cada objeto en la lista objetos
        self.objetos.append(self.etiquetaEliSal)
        self.objetos.append(self.entradaNomSal)
        self.objetos.append(self.botonNomSal)
    def eliIngNomSal(self, entradaSala):
        sala = str(entradaSala.get())
        if sala not in self.grafo:
            messagebox.showinfo('Sala inexistente', f'¡La sala {sala} NO existe!, quizas escribiste mal')
            self.contador += 1
            # Volver a ejecutar acción agregar sala por sala:
            self.accEliSalSal()
        else:
            del self.grafo[sala]
            for lista in self.grafo.values():
                lista.eliminar(sala)
            messagebox.showinfo('Sala Eliminada', f'La sala {sala}, {self.contador + 1} se eliminó correctamente')
            self.contador += 1
            # Volver a ejecutar acción agregar sala por sala:
            self.accEliSalSal()
    def agregarCam(self, rango, ventana):
        # Establecer rango y ventana para poder ser usados durante las funciones
        self.rango = int(rango)
        self.ventana = ventana
        # Contador
        self.contador = 0
        # Cosas de agregar caminos (para poder agregar caminos y que se creen y destruyan los objetos)
        self.objetos = []
        self.accAgrCam()
    def accAgrCam(self):
        #          ROMPER EL BUCLE
        if self.contador >= self.rango:
            messagebox.showinfo('Completado', f'Se han agregado TODOS los caminos correctamente')
            return
            # NOTA: el return no retorna nada, ya que solo sirve para terminar el bucle
        # Eliminar los objetos del camino que esta escribiendo para insertar los del nuevo camino
        for objeto in self.objetos:
            objeto.destroy()
        self.objetos.clear()
        # Etiqueta de agregar camino
        self.etiquetaAgrCamOri = tk.Label(
            self.ventana,
            text=f"Ingresa el nombre de la sala de Origen del camino {self.contador + 1}",# Texto que muestra la etiqueta
            font=("Century Gothic", 12, "bold"),# Fuente, tamaño y estilo (negrita)
            fg="black",                         # Color del texto
            bg="#f0f0f0",                       # Color del fondo de la etiqueta
            width=45,                           # Ancho de la etiqueta (en caracteres aprox.)
            anchor="center",                    # Posición del texto dentro de la etiqueta
            relief="flat",                      # Tipo de borde (puede ser flat, raised, sunken, ridge, groove, solid)
            bd=2,                               # Grosor del borde
            padx=10,                            # Espacio interno horizontal
            pady=5                              # Espacio interno vertical
        )
        self.etiquetaAgrCamDes = tk.Label(
            self.ventana,
            text=f"Ingresa el nombre de la sala de Destino del camino {self.contador + 1}",# Texto que muestra la etiqueta
            font=("Century Gothic", 12, "bold"),# Fuente, tamaño y estilo (negrita)
            fg="black",                         # Color del texto
            bg="#f0f0f0",                       # Color del fondo de la etiqueta
            width=45,                           # Ancho de la etiqueta (en caracteres aprox.)
            anchor="center",                    # Posición del texto dentro de la etiqueta
            relief="flat",                      # Tipo de borde (puede ser flat, raised, sunken, ridge, groove, solid)
            bd=2,                               # Grosor del borde
            padx=10,                            # Espacio interno horizontal
            pady=5                              # Espacio interno vertical
        )
        self.etiquetaAgrDisCam = tk.Label(
            self.ventana,
            text=f"Ingresa la distancia {self.contador + 1} entre los caminos",# Texto que muestra la etiqueta
            font=("Century Gothic", 12, "bold"),# Fuente, tamaño y estilo (negrita)
            fg="black",                         # Color del texto
            bg="#f0f0f0",                       # Color del fondo de la etiqueta
            width=0,                            # Ancho de la etiqueta (en caracteres aprox.)
            anchor="center",                    # Posición del texto dentro de la etiqueta
            relief="flat",                      # Tipo de borde (puede ser flat, raised, sunken, ridge, groove, solid)
            bd=2,                               # Grosor del borde
            padx=10,                            # Espacio interno horizontal
            pady=5                              # Espacio interno vertical
        )
        # Entrada de nombre de sala
        self.entradaNomCamOri = tk.Entry(
            self.ventana,
            font=("Century Gothic", 12),
            bg="#ffffff",           # Fondo 
            fg="#333333",           # Texto 
            bd=2,                   # Grosor del borde
            relief="groove",        # Estilo del borde
            width=30,               # Ancho en caracteres
            justify="center",       # Texto centrado
            insertbackground="black"# Color del cursor
        )
        self.entradaNomCamDes = tk.Entry(
            self.ventana,
            font=("Century Gothic", 12),
            bg="#ffffff",           # Fondo 
            fg="#333333",           # Texto 
            bd=2,                   # Grosor del borde
            relief="groove",        # Estilo del borde
            width=30,               # Ancho en caracteres
            justify="center",       # Texto centrado
            insertbackground="black"# Color del cursor
        )
        self.entradaDisCam = tk.Entry(
            self.ventana,
            font=("Century Gothic", 12),
            bg="#ffffff",           # Fondo 
            fg="#333333",           # Texto 
            bd=2,                   # Grosor del borde
            relief="groove",        # Estilo del borde
            width=30,               # Ancho en caracteres
            justify="center",       # Texto centrado
            insertbackground="black"# Color del cursor
        )
        # Boton ingresar el camino
        self.botonNomCam = tk.Button(
            self.ventana,
            text='Ingresar',
            font=("Century Gothic", 10),
            bg="#abaeb8",              # Fondo
            fg="black",                # Color del texto
            activebackground="#4b5572",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=23,                   # Espacio horizontal interno
            pady=3,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=lambda: self.ingNomCam(self.entradaNomCamOri, self.entradaNomCamDes, self.entradaDisCam)
        )
        # Posiciones
        self.etiquetaAgrCamOri.pack(pady=10)
        self.entradaNomCamOri.pack(pady=10)
        self.etiquetaAgrCamDes.pack(pady=10)
        self.entradaNomCamDes.pack(pady=10)
        self.etiquetaAgrDisCam.pack(pady=10)
        self.entradaDisCam.pack(pady=10)
        self.botonNomCam.pack(pady=10)
        # Colocar cada objeto en la lista objetos
        self.objetos.append(self.etiquetaAgrCamOri)
        self.objetos.append(self.entradaNomCamOri)
        self.objetos.append(self.etiquetaAgrCamDes)
        self.objetos.append(self.entradaNomCamDes)
        self.objetos.append(self.etiquetaAgrDisCam)
        self.objetos.append(self.entradaDisCam)
        self.objetos.append(self.botonNomCam)
    def ingNomCam(self, salaOrigen, salaDestino, Distancia):
        Origen = str(salaOrigen.get())
        Destino = str(salaDestino.get())
        Dist = int(Distancia.get())
        if Origen not in self.grafo:
            messagebox.showinfo('Sala inexistente', f'¡La sala {Origen} NO existe!, quizas escribiste mal')
            return
        if Destino not in self.grafo:
            messagebox.showinfo('Sala inexistente', f'¡La sala {Destino} NO existe!, quizas escribiste mal')
            return
        else:
            self.grafo[Origen].insertarFinal(Destino, Dist)
            self.contador += 1
            messagebox.showinfo('Ingresado Correctamente', f'El camino de {Origen} a {Destino} con {Dist}m se ingresó correctamente')
            # Volver a ejecutar acción agregar sala por sala:
            self.accAgrCam()
    def eliminarCam(self, rango, ventana):
        # Establecer rango y ventana para poder ser usados durante las funciones
        self.rango = int(rango)
        self.ventana = ventana
        # Contador
        self.contador = 0
        # Cosas de eliminar caminos (para poder eliminar caminos y que se creen y destruyan los objetos)
        self.objetos = []
        self.accEliCam()
    def accEliCam(self):
        #          ROMPER EL BUCLE
        if self.contador >= self.rango:
            messagebox.showinfo('Completado', f'Se han eliminado TODOS los caminos correctamente')
            return
            # NOTA: el return no retorna nada, ya que solo sirve para terminar el bucle
        # Eliminar los objetos del camino que esta escribiendo para insertar los de la nueva accion
        for objeto in self.objetos:
            objeto.destroy()
        self.objetos.clear()
        # Etiqueta de eliminar camino
        self.etiquetaEliCamOri = tk.Label(
            self.ventana,
            text=f"Ingresa el nombre de la sala de Origen del camino\na eliminar numero {self.contador + 1}",# Texto que muestra la etiqueta
            font=("Century Gothic", 12, "bold"),# Fuente, tamaño y estilo (negrita)
            fg="black",                         # Color del texto
            bg="#f0f0f0",                       # Color del fondo de la etiqueta
            width=45,                           # Ancho de la etiqueta (en caracteres aprox.)
            anchor="center",                    # Posición del texto dentro de la etiqueta
            relief="flat",                      # Tipo de borde (puede ser flat, raised, sunken, ridge, groove, solid)
            bd=2,                               # Grosor del borde
            padx=10,                            # Espacio interno horizontal
            pady=5                              # Espacio interno vertical
        )
        self.etiquetaEliCamDes = tk.Label(
            self.ventana,
            text=f"Ingresa el nombre de la sala de Destino del camino\na eliminar numero {self.contador + 1}",# Texto que muestra la etiqueta
            font=("Century Gothic", 12, "bold"),# Fuente, tamaño y estilo (negrita)
            fg="black",                         # Color del texto
            bg="#f0f0f0",                       # Color del fondo de la etiqueta
            width=45,                           # Ancho de la etiqueta (en caracteres aprox.)
            anchor="center",                    # Posición del texto dentro de la etiqueta
            relief="flat",                      # Tipo de borde (puede ser flat, raised, sunken, ridge, groove, solid)
            bd=2,                               # Grosor del borde
            padx=10,                            # Espacio interno horizontal
            pady=5                              # Espacio interno vertical
        )
        # Entrada de nombre de sala
        self.entradaNomCamOri = tk.Entry(
            self.ventana,
            font=("Century Gothic", 12),
            bg="#ffffff",           # Fondo 
            fg="#333333",           # Texto 
            bd=2,                   # Grosor del borde
            relief="groove",        # Estilo del borde
            width=30,               # Ancho en caracteres
            justify="center",       # Texto centrado
            insertbackground="black"# Color del cursor
        )
        self.entradaNomCamDes = tk.Entry(
            self.ventana,
            font=("Century Gothic", 12),
            bg="#ffffff",           # Fondo 
            fg="#333333",           # Texto 
            bd=2,                   # Grosor del borde
            relief="groove",        # Estilo del borde
            width=30,               # Ancho en caracteres
            justify="center",       # Texto centrado
            insertbackground="black"# Color del cursor
        )
        # Boton ingresar el camino
        self.botonNomCam = tk.Button(
            self.ventana,
            text='Ingresar',
            font=("Century Gothic", 10),
            bg="#abaeb8",              # Fondo
            fg="black",                # Color del texto
            activebackground="#4b5572",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=23,                   # Espacio horizontal interno
            pady=3,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=lambda: self.eliIngNomCam(self.entradaNomCamOri, self.entradaNomCamDes)
        )
        # Posiciones
        self.etiquetaEliCamOri.pack(pady=10)
        self.entradaNomCamOri.pack(pady=10)
        self.etiquetaEliCamDes.pack(pady=10)
        self.entradaNomCamDes.pack(pady=10)
        self.botonNomCam.pack(pady=10)
        # Colocar cada objeto en la lista objetos
        self.objetos.append(self.etiquetaEliCamOri)
        self.objetos.append(self.entradaNomCamOri)
        self.objetos.append(self.etiquetaEliCamDes)
        self.objetos.append(self.entradaNomCamDes)
        self.objetos.append(self.botonNomCam)
    def eliIngNomCam(self, salaOrigen, salaDestino):
        Origen = str(salaOrigen.get())
        Destino = str(salaDestino.get())
        if Origen not in self.grafo:
            messagebox.showinfo('Sala inexistente', f'¡La sala {Origen} NO existe!, quizas escribiste mal')
            return
        if Destino not in self.grafo:
            messagebox.showinfo('Sala inexistente', f'¡La sala {Destino} NO existe!, quizas escribiste mal')
            return
        else:
            eliminacion = self.grafo[Origen].eliminar(Destino)
            if not eliminacion:
                messagebox.showinfo('Camino inexistente', f'¡El camino de {Origen} a {Destino} NO existe!\nquizas escribiste mal')
                return
            else:
                messagebox.showinfo('Eliminado Correctamente', f'El camino de {Origen} a {Destino} se eliminó correctamente')
                self.contador += 1
                self.accEliCam()
    def mostrarSal(self, ventana):
        self.vent = ventana
        # Etiqueta de Ingresar Sala
        self.etiquetaIngSal = tk.Label(
            self.vent,
            text=f"Ingresa el nombre de la sala a buscar",# Texto que muestra la etiqueta
            font=("Century Gothic", 12, "bold"),# Fuente, tamaño y estilo (negrita)
            fg="black",                         # Color del texto
            bg="#f0f0f0",                       # Color del fondo de la etiqueta
            width=45,                           # Ancho de la etiqueta (en caracteres aprox.)
            anchor="center",                    # Posición del texto dentro de la etiqueta
            relief="flat",                      # Tipo de borde (puede ser flat, raised, sunken, ridge, groove, solid)
            bd=2,                               # Grosor del borde
            padx=10,                            # Espacio interno horizontal
            pady=5                              # Espacio interno vertical
        )
        # Entrada de Ingresar Sala
        self.entradaIngSal = tk.Entry(
            self.vent,
            font=("Century Gothic", 12),
            bg="#ffffff",           # Fondo 
            fg="#333333",           # Texto 
            bd=2,                   # Grosor del borde
            relief="groove",        # Estilo del borde
            width=30,               # Ancho en caracteres
            justify="center",       # Texto centrado
            insertbackground="black"# Color del cursor
        )
        # Botón Ingresar Sala
        self.botonNomCam = tk.Button(
            self.vent,
            text='Ingresar',
            font=("Century Gothic", 10),
            bg="#abaeb8",              # Fondo
            fg="black",                # Color del texto
            activebackground="#4b5572",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=23,                   # Espacio horizontal interno
            pady=3,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command= self.ingMosSal
        )
        # Posiciones
        self.etiquetaIngSal.pack(pady=10)
        self.entradaIngSal.pack(pady=10)
        self.botonNomCam.pack(pady=10)
    def ingMosSal(self):
        sala = self.entradaIngSal.get()
        if sala in self.grafo:
            # Etiqueta caminos desde
            self.etiquetaCamDes = tk.Label(
                self.vent,
                text=f"Caminos desde {sala}:",# Texto que muestra la etiqueta
                font=("Century Gothic", 12, "bold"),# Fuente, tamaño y estilo (negrita)
                fg="black",                         # Color del texto
                bg="#f0f0f0",                       # Color del fondo de la etiqueta
                width=45,                           # Ancho de la etiqueta (en caracteres aprox.)
                anchor="center",                    # Posición del texto dentro de la etiqueta
                relief="flat",                      # Tipo de borde (puede ser flat, raised, sunken, ridge, groove, solid)
                bd=2,                               # Grosor del borde
                padx=10,                            # Espacio interno horizontal
                pady=5                              # Espacio interno vertical
            )
            # Posiciones
            self.etiquetaCamDes.pack(pady=10)
            self.grafo[sala].mostrarNuevo(sala, self.vent)
        else:
            messagebox.showinfo('Sala inexistente', f'¡La sala {sala} NO existe!, quizas escribiste mal')
    def mostrarMapa(self, ventana):
        # Grafo
        G = nx.DiGraph()
        # Crear Caminos
        for origen, lista in self.grafo.items():
            for destino, peso in lista.lista_de_aristas():
                G.add_edge(origen, destino, weight=peso)
        # Figura
        ima = plt.Figure()
        # Tamaño
        area = ima.add_subplot(1, 1, 1)
        # Titulo
        area.set_title('Mapa del Museo')
        pos = nx.spring_layout(G)
        # Modificar el formato de las cosas
        nx.draw(
            G, pos,
            with_labels=True,
            ax=area,
            node_color='#b7bedb',    # Color de los nodos
            node_shape='s',          # Nodos cuadrados
            font_color='#212b6a',    # Color de letra nodos
            edge_color='gray',       # Color de las aristas
            node_size=800,           # Tamaño de los nodos
            font_size=6              # Tamaño de letra de etiquetas
        )
        nx.draw_networkx_edge_labels(
            G, pos,
            edge_labels=nx.get_edge_attributes(G, 'weight'),
            ax=area,
            font_size=8                                  # Tamaño de letra de etiquetas de aristas
        )
            # Agregar la imagen a la ventana
        canvas = FigureCanvasTkAgg(ima, master=ventana)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill="both")
    
#-----------CLASES DE LA INTERFAZ----------

class VentanaPrincipal:
    def __init__(self):
        self.ventanaPrincipal = tk.Tk()
        self.ventanaPrincipal.title('RutaFacil')
        self.ventanaPrincipal.geometry('800x600+300+0')
        self.fondoDividido()
        # Icono de la ventana
        self.ventanaPrincipal.iconbitmap('Iconochicografo.ico')
    def fondoDividido(self):
        # Tamaños de la ventana
        alto = 600
        ancho = 800
        # Color crema:
        self.colorArriba = tk.Frame(self.ventanaPrincipal, bg='#f0f0f0', width=ancho, height=alto//2)
        self.colorArriba.pack(side='top', fill='x')
        # Color naranja
        self.colorAbajo = tk.Frame(self.ventanaPrincipal, bg='#fb8a49', width=ancho, height=alto//2)
        self.colorAbajo.pack(side='bottom', fill='x')

        #-----------COSAS DE LA VENTANA PRINCIPAL----------

        # Texto de espacio
        self.etiquetaEspacio1 = tk.Label(self.colorArriba, text="    ", font=("Arial", 12))
        self.etiquetaEspacio2 = tk.Label(self.colorArriba, text="    ", font=("Arial", 12))
        self.etiquetaEspacio3 = tk.Label(self.colorArriba, text="    ", font=("Arial", 12))
        # Texto Titulo y Slogan de la aplicación
        self.etiquetaTitulo = tk.Label(
            self.colorArriba,
            text="RutaFacil",                   # Texto que muestra la etiqueta
            font=("Century Gothic", 45, "bold"),# Fuente, tamaño y estilo (negrita)
            fg="black",                         # Color del texto
            bg="#f0f0f0",                       # Color del fondo de la etiqueta
            width=30,                           # Ancho de la etiqueta (en caracteres aprox.)
            anchor="center",                    # Posición del texto dentro de la etiqueta
            relief="flat",                      # Tipo de borde (puede ser flat, raised, sunken, ridge, groove, solid)
            bd=2,                               # Grosor del borde
            padx=10,                            # Espacio interno horizontal
            pady=5                              # Espacio interno vertical
        )
        self.etiquetaSlogan = tk.Label(self.colorArriba, text="¡Llega a tus destinos sin preocuparte!", font=("Century Gothic", 18))
        # Boton Iniciar Sesion como usuario y administrador
        self.botonISAdmin = tk.Button(
            self.colorArriba,
            text='Iniciar Sesión como Administrador',
            font=("Century Gothic", 10),
            bg="#abaeb8",              # Fondo
            fg="black",                # Color del texto
            activebackground="#4b5572",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=5,                    # Espacio horizontal interno
            pady=2,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.abrirAdmin
        )
        self.botonISUs = tk.Button(
            self.colorArriba,
            text='Iniciar Sesión como Usuario',
            font=("Century Gothic", 10),
            bg="#abaeb8",              # Fondo
            fg="black",                # Color del texto
            activebackground="#4b5572",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=23,                    # Espacio horizontal interno
            pady=3,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=lambda: IniciarSesioncomoUsuario()
        )
        # Posiciones
        self.etiquetaEspacio1.pack(pady = 35)
        self.etiquetaTitulo.pack(pady = 8)
        self.etiquetaSlogan.pack(pady = 5)
        self.etiquetaEspacio2.pack(pady = 3)
        self.botonISAdmin.pack(pady = 5)
        self.botonISUs.pack(pady = 5)
        self.etiquetaEspacio3.pack(pady = 1)
    def abrirAdmin(self):
        self.ventanaPrincipal.destroy()
        IniciarSesioncomoAdministrador()

class IniciarSesioncomoUsuario:
    def __init__(self):
        self.ventUs = tk.Tk()
        self.ventUs.title('Usuario')
        self.ventUs.geometry('800x600+300+0')
        # Icono de la ventana
        self.ventUs.iconbitmap('Logous.ico')
        self.divisiones_colores_ventUs()
    # Botones de acciones para usuario --------------------------------------------------------------
        # 
        self.boton_camino_corto = tk.Button(
            self.div_izq,
            text = " Mostrar mapa  ",
            font=("Comic Sans MS", 10),
            bg='#99a3a4',              # Fondo
            fg="black",                # Color del texto
            activebackground="#f8f9f9",# Fondo al presionar
            activeforeground="black",  # Color del texto al presionar
            padx=15,                    # Espacio horizontal interno
            pady=2,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.comandoTemporal_1
        )
        
        self.boton_camino_corto.pack(pady=50)
        #
        self.boton_calcular_camino = tk.Button(
            self.div_izq,
            text = "Calcular camino",
            font=("Comic Sans MS", 10),
            bg='#99a3a4',              # Fondo
            fg="black",                # Color del texto
            activebackground="#f8f9f9",# Fondo al presionar
            activeforeground="black",  # Color del texto al presionar
            padx=16,                    # Espacio horizontal interno
            pady=2,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.comandoTemporal_2
        )
        
        self.boton_calcular_camino.pack(pady=50)

        self.salir= tk.Button(
            self.div_izq,
            text = "Salir",
            font=("Comic Sans MS", 10),
            bg='#99a3a4',              # Fondo
            fg="black",                # Color del texto
            activebackground="#f8f9f9",# Fondo al presionar
            activeforeground="black",  # Color del texto al presionar
            padx=17,                   # Espacio horizontal interno
            pady=2,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=lambda: self.salir_ventUs()
        )
        
        self.salir.pack(pady=50)

    def salir_ventUs(self):
        self.ventUs.destroy()
        
    def regresar(self):
        self.ventus.destroy()
        Ventanaprincipal()

    def comandoTemporal_1(self):
        print('funcion')
        
    def comandoTemporal_2(self):
        print('funcion')
        
    def divisiones_colores_ventUs(self):
        
        # #717d7e
        self.color_arriba = tk.Frame(self.ventUs, bg='#2c3e50', width=800, height=40)
        self.color_arriba.pack(side='top', fill='x')

        # Color crema (resto: 560px)
        self.color_fondo= tk.Frame(self.ventUs, bg='#f4f6f7', width=800)
        self.color_fondo.pack(side='top', fill='both', expand = True)
        self.division_izquierda()

    def division_izquierda(self):
        
        self.div_izq = tk.Frame(self.color_fondo, bg='#ccd1d1', width=180, height=560)
        self.div_izq.pack(side='left', fill='y', anchor = 'nw')
        self.div_izq.pack_propagate(False)
    
        self.fondo = tk.Frame(self.color_fondo, bg='#fbfcfc', width=300, height=560)
        self.fondo.pack(side='right', fill='both', expand = True)
        
class IniciarSesioncomoAdministrador:
    def __init__(self):
        self.contrasena = '1234'
        self.ventAdmin = tk.Tk()
        self.ventAdmin.title('Contraseña')
        self.ventAdmin.geometry('800x600+300+0')
        # Icono de la ventana
        self.ventAdmin.iconbitmap('Contrasena.ico')

        #-----------COSAS DE LA VENTANA CONTRASEÑA----------

        # Texto de espacio
        self.etiquetaEspacio1 = tk.Label(self.ventAdmin, text="    ", font=("Arial", 12))
        self.etiquetaEspacio2 = tk.Label(self.ventAdmin, text="    ", font=("Arial", 12))
        # Texto Contraseña
        self.etiquetaContrasena = tk.Label(self.ventAdmin, text="Ingresa la contraseña", font=("Century Gothic", 12))
        # Entrada de la contraseña
        self.entradaCont = tk.Entry(
            self.ventAdmin,
            font=("Century Gothic", 12),
            bg="#ffffff",           # Fondo 
            fg="#333333",           # Texto 
            bd=2,                   # Grosor del borde
            relief="groove",        # Estilo del borde
            width=30,               # Ancho en caracteres
            justify="center",       # Texto centrado
            insertbackground="black"# Color del cursor
        )
        # Botones Ingresar Contraseña y Regresar
        self.botonIngresar = tk.Button(
            self.ventAdmin,
            text='Ingresar',
            font=("Century Gothic", 10),
            bg="#abaeb8",              # Fondo
            fg="black",                # Color del texto
            activebackground="#4b5572",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=8,                    # Espacio horizontal interno
            pady=2,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.pruebadeContrasena
        )
        self.botonRegresar = tk.Button(
            self.ventAdmin,
            text='Regresar',
            font=("Century Gothic", 10),
            bg="red",                  # Fondo
            fg="white",                # Color del texto
            activebackground="#900303",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=6,                    # Espacio horizontal interno
            pady=2,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.regresar
        )
        # Posiciones
        self.etiquetaEspacio1.pack(pady = 50)
        self.etiquetaContrasena.pack(pady = 8)
        self.entradaCont.pack(pady = 8)
        self.botonIngresar.pack(pady = 8)
        self.botonRegresar.pack(pady = 1)
        self.etiquetaEspacio2.pack(pady = 3)
    def pruebadeContrasena(self):
        contrasenaIngresada = self.entradaCont.get()
        if contrasenaIngresada == self.contrasena:
            self.entrarControl()
        else:
            messagebox.showinfo('Contraseña incorrecta', 'Ingresa de nuevo')
    def regresar(self):
        self.ventAdmin.destroy()
        VentanaPrincipal()
    def entrarControl(self):
        self.ventAdmin.destroy()
        self.contrasenaCorrecta()
    def contrasenaCorrecta(self):
        self.ventControl = tk.Tk()
        self.ventControl.title('Administrador')
        self.ventControl.geometry('800x600+300+0')
        # Icono de la ventana
        self.ventControl.iconbitmap('Logoadmin.ico')
        self.lineadeFondoAdmin()
    def lineadeFondoAdmin(self):
        # Tamaños de la ventana
        ancho = 800
        # Color naranja (40px)
        self.colorArriba = tk.Frame(self.ventControl, bg='#fb8a49', width=ancho, height=40)
        self.colorArriba.pack(side='top', fill='x')

        # Color crema (resto: 560px)
        self.colorAbajo = tk.Frame(self.ventControl, bg='#f0f0f0', width=ancho)
        self.colorAbajo.pack(side='top', fill='both', expand = True)
        self.divisionBeige()
    def divisionBeige(self):
        # Color del Menú de acciones
        self.menu = tk.Frame(self.colorAbajo, bg='#fcc1a0', width=180, height=560)
        self.menu.pack(side='left', fill='y', anchor = 'nw')
        self.menu.pack_propagate(False)
    
        # Color de la Imagen resultado
        self.imagen = tk.Frame(self.colorAbajo, bg='#f0f0f0', width=300, height=560)
        self.imagen.pack(side='right', fill='both', expand = True)

        #-----------COSAS DE LA SUBVENTANA ADMINISTRADOR(MENÚ)----------
        
        # Etiqueta Espacio
        self.etiquetaEspacio7 = tk.Label(
            self.menu,
            text="   ",  # Texto que muestra la etiqueta
            font=("Century Gothic", 12, "bold"),# Fuente, tamaño y estilo (negrita)
            fg="black",                         # Color del texto
            bg="#fcc1a0",                       # Color del fondo de la etiqueta
            width=8,                            # Ancho de la etiqueta (en caracteres aprox.)
            anchor="center",                    # Posición del texto dentro de la etiqueta
            relief="flat",                      # Tipo de borde (puede ser flat, raised, sunken, ridge, groove, solid)
            bd=2,                               # Grosor del borde
            padx=1,                             # Espacio interno horizontal
            pady=5                              # Espacio interno vertical
        )
        # Botones
        self.botonAgregarSal = tk.Button(
            self.menu,
            text='Agregar Salas',
            font=("Century Gothic", 10),
            bg="#abaeb8",              # Fondo
            fg="black",                # Color del texto
            activebackground="#4b5572",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=15,                   # Espacio horizontal interno
            pady=2,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.agrSal
        )
        self.botonAgregarCam = tk.Button(
            self.menu,
            text='Agregar Caminos',
            font=("Century Gothic", 10),
            bg="#abaeb8",              # Fondo
            fg="black",                # Color del texto
            activebackground="#4b5572",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=6,                    # Espacio horizontal interno
            pady=2,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.agrCam
        )
        self.botonEliminarSal = tk.Button(
            self.menu,
            text='Eliminar Salas',
            font=("Century Gothic", 10),
            bg="#abaeb8",              # Fondo
            fg="black",                # Color del texto
            activebackground="#4b5572",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=14,                   # Espacio horizontal interno
            pady=2,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.eliSal
        )
        self.botonEliminarCam = tk.Button(
            self.menu,
            text='Eliminar Caminos',
            font=("Century Gothic", 10),
            bg="#abaeb8",              # Fondo
            fg="black",                # Color del texto
            activebackground="#4b5572",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=5,                    # Espacio horizontal interno
            pady=2,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.eliCam
        )
        self.botonMostrar = tk.Button(
            self.menu,
            text='Mostrar',
            font=("Century Gothic", 10),
            bg="#abaeb8",              # Fondo
            fg="black",                # Color del texto
            activebackground="#4b5572",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=34,                   # Espacio horizontal interno
            pady=2,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.mostrar
        )
        self.botonBuscar = tk.Button(
            self.menu,
            text='Buscar',
            font=("Century Gothic", 10),
            bg="#abaeb8",              # Fondo
            fg="black",                # Color del texto
            activebackground="#4b5572",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=36,                   # Espacio horizontal interno
            pady=2,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.regresar
        )
        self.botonReg = tk.Button(
            self.menu,
            text='Regresar',
            font=("Century Gothic", 10),
            bg="red",                  # Fondo
            fg="white",                # Color del texto
            activebackground="#900303",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=30,                   # Espacio horizontal interno
            pady=2,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.regresar
        )
        # Posiciones
        self.etiquetaEspacio7.pack(pady = 26)
        self.botonAgregarSal.pack(pady = 10)
        self.botonAgregarCam.pack(pady = 10)
        self.botonEliminarSal.pack(pady = 10)
        self.botonEliminarCam.pack(pady = 10)
        self.botonMostrar.pack(pady = 10)
        self.botonBuscar.pack(pady = 10)
        self.botonReg.pack(pady = 10)

        #-----------COSAS DE LA SUBVENTANA ADMINISTRADOR(IMAGEN)----------

        # Etiqueta de espacio
        self.etiquetaEspacio4 = tk.Label(self.imagen, text="    ", font=("Arial", 12))
        # Textos
        self.etiquetaBienAdmin = tk.Label(
            self.imagen,
            text="¡Bienvenido Administrador!",  # Texto que muestra la etiqueta
            font=("Century Gothic", 30, "bold"),# Fuente, tamaño y estilo (negrita)
            fg="black",                         # Color del texto
            bg="#f0f0f0",                       # Color del fondo de la etiqueta
            width=23,                           # Ancho de la etiqueta (en caracteres aprox.)
            anchor="center",                    # Posición del texto dentro de la etiqueta
            relief="flat",                      # Tipo de borde (puede ser flat, raised, sunken, ridge, groove, solid)
            bd=2,                               # Grosor del borde
            padx=1,                             # Espacio interno horizontal
            pady=5                              # Espacio interno vertical
        )
        self.etiquetaAccion = tk.Label(self.imagen, text="Seleccione cualquier acción de la barra de menú", font=("Century Gothic", 12))
        # Posiciones
        self.etiquetaEspacio4.pack(pady = 90)
        self.etiquetaBienAdmin.pack(pady = 10)
        self.etiquetaAccion.pack(pady = 8)
    def limpiarImagen(self):
        if hasattr(self, 'etiquetaEspacio4'):
            self.etiquetaEspacio4.destroy()
            self.etiquetaBienAdmin.destroy()
            self.etiquetaAccion.destroy()
        if hasattr(self, 'marAcc'):
            self.marAcc.destroy()
            del self.marAcc
    def agrSal(self):
        self.limpiarImagen()

        #-----------MARCO DE ACCION PARA MANIPULAR EL GRAFO----------

        self.marAcc = tk.Frame(self.imagen, bg="#f0f0f0")
        self.marAcc.pack(expand=True)

        #-----------COSAS DE LA SUBVENTANA MARCOFORMULARIO----------

        # Etiquetas
        self.etiquetaCuaSal = tk.Label(
            self.marAcc,
            text="Escribe cuántas salas quieres agregar",  # Texto que muestra la etiqueta
            font=("Century Gothic", 12, "bold"),# Fuente, tamaño y estilo (negrita)
            fg="black",                         # Color del texto
            bg="#f0f0f0",                       # Color del fondo de la etiqueta
            width=30,                           # Ancho de la etiqueta (en caracteres aprox.)
            anchor="center",                    # Posición del texto dentro de la etiqueta
            relief="flat",                      # Tipo de borde (puede ser flat, raised, sunken, ridge, groove, solid)
            bd=2,                               # Grosor del borde
            padx=1,                             # Espacio interno horizontal
            pady=5                              # Espacio interno vertical
        )
        # Entradas
        self.entradaNumSal = tk.Entry(
            self.marAcc,
            font=("Century Gothic", 12),
            bg="#ffffff",           # Fondo 
            fg="#333333",           # Texto 
            bd=2,                   # Grosor del borde
            relief="groove",        # Estilo del borde
            width=30,               # Ancho en caracteres
            justify="center",       # Texto centrado
            insertbackground="black"# Color del cursor
        )
        # Botones
        self.botonNumSal = tk.Button(
            self.marAcc,
            text='Ingresar',
            font=("Century Gothic", 10),
            bg="#abaeb8",              # Fondo
            fg="white",                # Color del texto
            activebackground="#4b5572",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=30,                   # Espacio horizontal interno
            pady=2,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.ingNumSal
        )
        # Posiciones
        self.etiquetaCuaSal.pack(pady = 10)
        self.entradaNumSal.pack(pady=10)
        self.botonNumSal.pack(pady=10)
    def ingNumSal(self):
        numSal = self.entradaNumSal.get()
        self.etiquetaCuaSal.destroy()
        self.entradaNumSal.destroy()
        self.botonNumSal.destroy()
        grafo.agregarSal(numSal, self.marAcc)
    def eliSal(self):
        self.limpiarImagen()

        #-----------MARCO DE ACCION PARA MANIPULAR EL GRAFO----------

        self.marAcc = tk.Frame(self.imagen, bg="#f0f0f0")
        self.marAcc.pack(expand=True)

        #-----------COSAS DE LA SUBVENTANA MARCOFORMULARIO----------

        # Etiquetas
        self.etiquetaCuaSal = tk.Label(
            self.marAcc,
            text="Escribe cuántas salas quieres eliminar",  # Texto que muestra la etiqueta
            font=("Century Gothic", 12, "bold"),# Fuente, tamaño y estilo (negrita)
            fg="black",                         # Color del texto
            bg="#f0f0f0",                       # Color del fondo de la etiqueta
            width=30,                           # Ancho de la etiqueta (en caracteres aprox.)
            anchor="center",                    # Posición del texto dentro de la etiqueta
            relief="flat",                      # Tipo de borde (puede ser flat, raised, sunken, ridge, groove, solid)
            bd=2,                               # Grosor del borde
            padx=1,                             # Espacio interno horizontal
            pady=5                              # Espacio interno vertical
        )
        # Entradas
        self.entradaNumSal = tk.Entry(
            self.marAcc,
            font=("Century Gothic", 12),
            bg="#ffffff",           # Fondo 
            fg="#333333",           # Texto 
            bd=2,                   # Grosor del borde
            relief="groove",        # Estilo del borde
            width=30,               # Ancho en caracteres
            justify="center",       # Texto centrado
            insertbackground="black"# Color del cursor
        )
        # Botones
        self.botonNumSal = tk.Button(
            self.marAcc,
            text='Ingresar',
            font=("Century Gothic", 10),
            bg="#abaeb8",              # Fondo
            fg="white",                # Color del texto
            activebackground="#4b5572",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=30,                   # Espacio horizontal interno
            pady=2,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.eliIngNumSal
        )
        # Posiciones
        self.etiquetaCuaSal.pack(pady = 10)
        self.entradaNumSal.pack(pady=10)
        self.botonNumSal.pack(pady=10)
    def eliIngNumSal(self):
        numSal = self.entradaNumSal.get()
        self.etiquetaCuaSal.destroy()
        self.entradaNumSal.destroy()
        self.botonNumSal.destroy()
        grafo.eliminarSal(numSal, self.marAcc)
    def agrCam(self):
        self.limpiarImagen()

        #-----------MARCO DE ACCION PARA MANIPULAR EL GRAFO----------

        self.marAcc = tk.Frame(self.imagen, bg="#f0f0f0")
        self.marAcc.pack(expand=True)

        #-----------COSAS DE LA SUBVENTANA MARCOFORMULARIO----------

        # Etiquetas
        self.etiquetaCuaCam = tk.Label(
            self.marAcc,
            text="Escribe cuantos caminos quieres agregar",  # Texto que muestra la etiqueta
            font=("Century Gothic", 12, "bold"),# Fuente, tamaño y estilo (negrita)
            fg="black",                         # Color del texto
            bg="#f0f0f0",                       # Color del fondo de la etiqueta
            width=38,                           # Ancho de la etiqueta (en caracteres aprox.)
            anchor="center",                    # Posición del texto dentro de la etiqueta
            relief="flat",                      # Tipo de borde (puede ser flat, raised, sunken, ridge, groove, solid)
            bd=2,                               # Grosor del borde
            padx=1,                             # Espacio interno horizontal
            pady=5                              # Espacio interno vertical
        )
        # Entradas
        self.entradaNumCam = tk.Entry(
            self.marAcc,
            font=("Century Gothic", 12),
            bg="#ffffff",           # Fondo 
            fg="#333333",           # Texto 
            bd=2,                   # Grosor del borde
            relief="groove",        # Estilo del borde
            width=30,               # Ancho en caracteres
            justify="center",       # Texto centrado
            insertbackground="black"# Color del cursor
        )
        # Botones
        self.botonNumCam = tk.Button(
            self.marAcc,
            text='Ingresar',
            font=("Century Gothic", 10),
            bg="#abaeb8",              # Fondo
            fg="white",                # Color del texto
            activebackground="#4b5572",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=30,                   # Espacio horizontal interno
            pady=2,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.agrNumCam
        )
        # Posiciones
        self.etiquetaCuaCam.pack(pady = 10)
        self.entradaNumCam.pack(pady=10)
        self.botonNumCam.pack(pady=10)
    def agrNumCam(self):
        numCam = self.entradaNumCam.get()
        self.etiquetaCuaCam.destroy()
        self.entradaNumCam.destroy()
        self.botonNumCam.destroy()
        grafo.agregarCam(numCam, self.marAcc)
    def eliCam(self):
        self.limpiarImagen()

        #-----------MARCO DE ACCION PARA MANIPULAR EL GRAFO----------

        self.marAcc = tk.Frame(self.imagen, bg="#f0f0f0")
        self.marAcc.pack(expand=True)

        #-----------COSAS DE LA SUBVENTANA MARCOFORMULARIO----------

        # Etiquetas
        self.etiquetaCuaCam = tk.Label(
            self.marAcc,
            text="Escribe cuantos caminos quieres eliminar",  # Texto que muestra la etiqueta
            font=("Century Gothic", 12, "bold"),# Fuente, tamaño y estilo (negrita)
            fg="black",                         # Color del texto
            bg="#f0f0f0",                       # Color del fondo de la etiqueta
            width=38,                           # Ancho de la etiqueta (en caracteres aprox.)
            anchor="center",                    # Posición del texto dentro de la etiqueta
            relief="flat",                      # Tipo de borde (puede ser flat, raised, sunken, ridge, groove, solid)
            bd=2,                               # Grosor del borde
            padx=1,                             # Espacio interno horizontal
            pady=5                              # Espacio interno vertical
        )
        # Entradas
        self.entradaNumCam = tk.Entry(
            self.marAcc,
            font=("Century Gothic", 12),
            bg="#ffffff",           # Fondo 
            fg="#333333",           # Texto 
            bd=2,                   # Grosor del borde
            relief="groove",        # Estilo del borde
            width=30,               # Ancho en caracteres
            justify="center",       # Texto centrado
            insertbackground="black"# Color del cursor
        )
        # Botones
        self.botonNumCam = tk.Button(
            self.marAcc,
            text='Ingresar',
            font=("Century Gothic", 10),
            bg="#abaeb8",              # Fondo
            fg="white",                # Color del texto
            activebackground="#4b5572",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=30,                   # Espacio horizontal interno
            pady=2,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.eliNumCam
        )
        # Posiciones
        self.etiquetaCuaCam.pack(pady = 10)
        self.entradaNumCam.pack(pady=10)
        self.botonNumCam.pack(pady=10)
    def eliNumCam(self):
        numCam = self.entradaNumCam.get()
        self.etiquetaCuaCam.destroy()
        self.entradaNumCam.destroy()
        self.botonNumCam.destroy()
        grafo.eliminarCam(numCam, self.marAcc)
    def mostrar(self):
        self.limpiarImagen()
        
        #-----------MARCO DE ACCION PARA MANIPULAR EL GRAFO----------

        self.marAcc = tk.Frame(self.imagen, bg="#f0f0f0")
        self.marAcc.pack(expand=True)

        #-----------COSAS DE LA SUBVENTANA MARCOFORMULARIO----------

        # Etiquetas
        self.etiquetaMostrar = tk.Label(
            self.marAcc,
            text="Mostrar:",  # Texto que muestra la etiqueta
            font=("Century Gothic", 30, "bold"),# Fuente, tamaño y estilo (negrita)
            fg="black",                         # Color del texto
            bg="#f0f0f0",                       # Color del fondo de la etiqueta
            width=38,                           # Ancho de la etiqueta (en caracteres aprox.)
            anchor="center",                    # Posición del texto dentro de la etiqueta
            relief="flat",                      # Tipo de borde (puede ser flat, raised, sunken, ridge, groove, solid)
            bd=2,                               # Grosor del borde
            padx=1,                             # Espacio interno horizontal
            pady=5                              # Espacio interno vertical
        )
        # Botones
        self.botonMosSal = tk.Button(
            self.marAcc,
            text='Sala',
            font=("Century Gothic", 10),
            bg="#abaeb8",              # Fondo
            fg="black",                # Color del texto
            activebackground="#4b5572",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=55,                   # Espacio horizontal interno
            pady=2,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.mostrarSal
        )
        self.botonMosLisSal = tk.Button(
            self.marAcc,
            text='Lista de Salas',
            font=("Century Gothic", 10),
            bg="#abaeb8",              # Fondo
            fg="black",                # Color del texto
            activebackground="#4b5572",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=27,                   # Espacio horizontal interno
            pady=2,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.mosLisSal
        )
        self.botonMosMatAdy = tk.Button(
            self.marAcc,
            text='Matriz de Adyacencia',
            font=("Century Gothic", 10),
            bg="#abaeb8",              # Fondo
            fg="black",                # Color del texto
            activebackground="#4b5572",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=5,                    # Espacio horizontal interno
            pady=2,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.regresar
        )
        self.botonMosMap = tk.Button(
            self.marAcc,
            text='Mapa',
            font=("Century Gothic", 10),
            bg="#abaeb8",              # Fondo
            fg="black",                # Color del texto
            activebackground="#4b5572",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=52,                   # Espacio horizontal interno
            pady=2,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.mosMap
        )
        # Posiciones
        self.etiquetaMostrar.pack(pady = 10)
        self.botonMosSal.pack(pady = 10)
        self.botonMosLisSal.pack(pady = 10)
        self.botonMosMatAdy.pack(pady = 10)
        self.botonMosMap.pack(pady = 10)
    def mostrarSal(self):
        self.limpiarImagen()
        # Hacer de nuevo el contenedor temporal
        self.marAcc = tk.Frame(self.imagen, bg="#f0f0f0")
        self.marAcc.pack(expand=True)
        # Funcion
        grafo.mostrarSal(self.marAcc)
    def mosLisSal(self):
        self.limpiarImagen()
        # Hacer de nuevo el contenedor temporal
        self.marAcc = tk.Frame(self.imagen, bg="#f0f0f0")
        self.marAcc.pack(expand=True)
        # Funcion
        grafo.mosLisSal(self.marAcc)
    def mosMap(self):
        self.limpiarImagen()
        # Hacer de nuevo el contenedor temporal
        self.marAcc = tk.Frame(self.imagen, bg="#f0f0f0")
        self.marAcc.pack(expand=True)
        # Funcion
        grafo.mostrarMapa(self.marAcc)

# 4.- ---------- Variables u objetos globales ----------

# Grafo
grafo = Grafo()
#-----------Agregar las salas iniciales al empezar el código----------
salasIniciales = ['Arte Prehispánico', 'Arte Contemporáneo', 'Escultura', 'Pintura Europea', 'Fotografía', 'Arte Moderno', 'Arte Oriental', 'Arte Popular Mexicano', 'Historia Natural', 'Virreinato', 'Revolución', 'Ciencias y Tecnología']
for sala in salasIniciales:
    grafo.grafo[sala] = ListaDobleEnlazada()
conexiones = [
    [0, 4, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 0, 0, 5, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0],
    [0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 0, 0, 4, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
for conexion in range(len(conexiones)):
    for conexionj in range(len(conexiones[conexion])):
        distancia = conexiones[conexion][conexionj]
        if distancia != 0:
            origen = salasIniciales[conexion]
            destino = salasIniciales[conexionj]
            grafo.grafo[origen].insertarFinal(destino, distancia)

# 5.- ---------- Bloque Principal ----------
if __name__ == '__main__':
    aplicacionGrafo = VentanaPrincipal()
    aplicacionGrafo.ventanaPrincipal.mainloop()
    
# 6.- ---------- Documentación y comentarios ----------
'''
Búsqueda de información:
    - Chatgpt:
        + Como modificar el boton
        + Bold en la letra significa negritas
        + lambda: es para los botones, para que se ejecute toda la clase al dar click al boton
        + Es mejor usar funciones para abrir nuevas ventanas y poder utilizarlas, ya que con una funcion cierras
        la ventana
        + Como modificar las etiquetas
        + En donde va el texto (posición) es con anchor, este puede ser:
            ~ center: al centro
            ~ w: a la izquierda
            ~ e: a la cerecha
            ~ n: arriba
            ~ s: abajo
            ~ nw: arriba e izquierda
            ~ se: abajo derecha
        + Los tipos de borde para el boton son:
            ~ flat: sin borde
            ~ raised: efecto 3D
            ~ sunken: hundido
            ~ groove: con ranura
            ~ ridge: con relieve
        + fill en pack controla la manera en que se expande un witget (en este caso la barra naranjarosa) en el
        contenedor, sus opciones son:
            ~ none: mantiene su tamaño mínimo
            ~ x: se expande horizontalmente para llenar todo lo ancho posible
            ~ y: se expande verticalmente para llenar todo el alto posible
            ~ both: se expande en ambas direcciones para llenar todo el espacio posible
        + Para agregar la ventana en dos partes es necesario usar tk.Frame, y en width es la anchura y height es
        altura en frames
        + Para hacer que el texto de la subventana de abajo se ponga hasta arriba de la etiqueta, hay que agre-
        gar anchor='n'
        + Al usar pack, esta función puede hacer que la ventana lateral del menú sea lo más estrecha posible pa-
        ra ajustarse lo más posible a los botones
        + Para destruir objetos, ".destroy" funciona para ventanas y etiquetas (lo usamos en la ventana de admi-
        nistrador para que se eliminen las etiquetas de bienvenido y selecciona accion)
        + Fue necesario hacer contenedores extra en la ventana imagen para poder manupilar facilmente esta ven-
        tana
        + expand=True sirve para hacer que el marco de accion rellene toda la subventana imagen
        + En accAgrSalSal, objeto.destroy elimina los objetos de la pantalla, y self.objetos.clear() sirve para
        eliminarlos de la lista
        + hasattr(objeto, "atributo") sirve para ver si un objeto tiene un atributo y devuelve True, si no tiene
        el atributo, devuelve False (en este caso el objeto es self, y el atribut es marco de acción o etiqueta
        espacio 4)
        + "separador".join(lista) sirve para combinar los elementos de una lista mas un separador
        + plt.figure() es la imágen del mapa del grafo
        + .add_subplot(1,1,1) es el área de donde se pone el grafo networkx
        + Se utilizó Matplottlib porque es una función que funciona con entornos gráficos
        + Se utiliza FigureCanvasTkAgg ya que su función es integrar la imágen de matplotlib a la interfaz de
        tkinter
    - Código del profesor y clasroom de la materia:
        + Esqueleto del código
        + Menú
'''

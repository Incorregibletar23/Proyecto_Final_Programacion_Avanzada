# 1.- ---------- Encabezado ----------

'''
Programa: Proyecto Grafo - proyecto_grafo.py
Autor: Ramírez Vásquez Eduardo
Fecha de creación: 14/05/2025
Fechas de modificación:
    - 31/05/2025 2:30 pm(v2.1: Se empezará a hacer la interfaz gráfica del proyecto)
    - 01/06/2025 2:13 pm(v2.2: Se hace el lobby de la aplicación)
'''

# 2.- ---------- Importación de módulos y bibliotecas ----------

#           IMPORTACIONES PARA TERMINAL
'''
import os
import networkx as nx
import matplotlib.pyplot as plt
import tracemalloc
import time
'''
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import messagebox

# 3.- ---------- Definición de funciones o clases ----------

#           CLASES PARA USO EN LA TERMINAL
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
                rango = int(input('¿Cuántos salas vas a ingresar? '))
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
#           FIN DE LAS CLASES DE TERMINAL

#           CLASES DE LOS MÉTODOS GRAFICOS

class VentanaPrincipal:
    def __init__(self):
        self.ventanaPrincipal = tk.Tk()
        self.ventanaPrincipal.title('RutaFacil')
        self.ventanaPrincipal.geometry('800x600+600+100')
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
        self.etiquetaTitulo = tk.Label(self.colorArriba, text="RutaFacil", font=("Century Gothic", 45))
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
            padx=6,                   # Espacio horizontal interno
            pady=2,                   # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",           # Cambia a manita
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
            padx=7,                   # Espacio horizontal interno
            pady=3,                   # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",           # Cambia a manita
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
        self.ventUs.geometry('800x600+600+100')
        # Icono de la ventana
        self.ventUs.iconbitmap('Logous.ico')
        
class IniciarSesioncomoAdministrador:
    def __init__(self):
        self.contrasena = 'Admin'
        self.ventAdmin = tk.Tk()
        self.ventAdmin.title('Contraseña')
        self.ventAdmin.geometry('800x600+600+100')
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
            insertbackground="black" # Color del cursor
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
            padx=6,                   # Espacio horizontal interno
            pady=2,                   # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",           # Cambia a manita
            command=self.pruebadeContrasena
        )
        self.botonRegresar = tk.Button(
            self.ventAdmin,
            text='Regresar',
            font=("Century Gothic", 10),
            bg="#707380",              # Fondo
            fg="black",                # Color del texto
            activebackground="#4b5572",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=6,                   # Espacio horizontal interno
            pady=2,                   # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",           # Cambia a manita
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
        self.ventControl.geometry('800x600+600+100')
        # Icono de la ventana
        self.ventControl.iconbitmap('Logoadmin.ico')

# 4.- ---------- Variables u objetos globales ----------
# 5.- ---------- Bloque Principal ----------
if __name__ == '__main__':
    aplicacionGrafo = VentanaPrincipal()
    aplicacionGrafo.ventana.mainloop()
    
# 6.- ---------- Documentación y comentarios ----------
'''
Búsqueda de información:
    - Chatgpt:
        + Como modificar el boton
        + Bold en la letra significa negritas
        + lambda: es para los botones, para que se ejecute toda la clase al dar click al boton
        + Es mejor usar funciones para abrir nuevas ventanas y poder utilizarlas, ya que con una funcion cierras la ventana
'''

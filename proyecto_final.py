# 1.- ---------- Encabezado ----------

'''
Programa: Proyecto Grafo - proyecto_grafo.py
Autores:
- Ramírez Vásquez Eduardo
- Rosas López Renata
Fecha de creación: 15/06/2025
Fechas de modificación:
    Eduardo:
        - 12/06/2025 10:13 am(v3.1: Se empezó a hacer el proyecto final incluyendo todos los temas vistos)

    Renata:
'''

# 2.- ---------- Importación de módulos y bibliotecas ----------

import os
import networkx as nx
import matplotlib.pyplot as plt
import tracemalloc
import time
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 3.- ---------- Definición de funciones o clases ----------

#-----------CLASES DEL ARBOL----------

class Nodo:
  def __init__(self, dato):
    self.dato = dato
    self.izquierda = None
    self.derecha = None

class ABB:
  def __init__(self):
    self.raiz = None
  def insertar(self, dato):
    nuevo_nodo = Nodo(dato)
    if self.raiz is None:
      self.raiz = nuevo_nodo
    else:
      self._insertar_recursivo(dato, self.raiz)
  def _insertar_recursivo(self, dato, nodo_actual):
    if dato < nodo_actual.dato:
      if nodo_actual.izquierda is None:
        nodo_actual.izquierda = Nodo(dato)
      else:
        self._insertar_recursivo(dato, nodo_actual.izquierda)
    if dato > nodo_actual.dato:
      if nodo_actual.derecha is None:
        nodo_actual.derecha = Nodo(dato)
      else:
        self._insertar_recursivo(dato, nodo_actual.derecha)
  def _imprimir(self):
    self._imprimir_recursivo(self.raiz,0)
  def _imprimir_recursivo(self, nodo_actual, nivel):
    if nodo_actual is not None:
      self._imprimir_recursivo(nodo_actual.derecha, nivel + 1)
      print("      "  * nivel + f'-> {nodo_actual.dato}')
      self._imprimir_recursivo(nodo_actual.izquierda, nivel + 1)
  def verimagen(self, nombre="arbol_binario"):
    punto = Digraph()
    punto.attr('node', shape='circle')
    if self.raiz is not None:
      self.verimagen_recursivo(self.raiz, punto)
    return punto
  def verimagen_recursivo(self, nodo_actual, punto):
    punto.node(str(nodo_actual.dato))
    if nodo_actual.izquierda is not None:
      punto.edge(str(nodo_actual.dato), str(nodo_actual.izquierda.dato))
      self.verimagen_recursivo(nodo_actual.izquierda, punto)
    if nodo_actual.derecha is not None:
      punto.edge(str(nodo_actual.dato), str(nodo_actual.derecha.dato))
      self.verimagen_recursivo(nodo_actual.derecha, punto)
  def inorden(self):
    print('Inorden', end=' ')
    self.inorden_recursivo(self.raiz)
    print()
  def inorden_recursivo(self, nodo_actual):
    if nodo_actual is not None:
      self.inorden_recursivo(nodo_actual.izquierda)
      print(nodo_actual.dato, end=' ')
      self.inorden_recursivo(nodo_actual.derecha)
  def preorden(self):
    print('Preorden', end=' ')
    self.preorden_recursivo(self.raiz)
    print()
  def preorden_recursivo(self, nodo_actual):
    if nodo_actual is not None:
      print(nodo_actual.dato, end=' ')
      self.preorden_recursivo(nodo_actual.izquierda)
      self.preorden_recursivo(nodo_actual.derecha)
  def postorden(self):
    print('Postorden', end=' ')
    self.postorden_recursivo(self.raiz)
    print()
  def postorden_recursivo(self, nodo_actual):
    if nodo_actual is not None:

      self.postorden_recursivo(nodo_actual.izquierda)

      self.postorden_recursivo(nodo_actual.derecha)
      print(nodo_actual.dato, end=' ')
  def eliminar(self, dato):
    self.raiz = self._eliminar_recursivo(dato, self.raiz)
  def _eliminar_recursivo(self, dato, nodo_actual):
    if nodo_actual is None:
      return nodo_actual
    if dato < nodo_actual.dato:
      nodo_actual.izquierda = self._eliminar_recursivo(dato, nodo_actual.izquierda)
    elif dato > nodo_actual.dato:
      nodo_actual.derecha = self._eliminar_recursivo(dato, nodo_actual.derecha)
    else:
      if nodo_actual.izquierda is None:
        return nodo_actual.derecha
      elif nodo_actual.derecha is None:
        return nodo_actual.izquierda
      temp = self._encontrar_minimo(nodo_actual.derecha)
      nodo_actual.dato = temp.dato
      nodo_actual.derecha = self._eliminar_recursivo(temp.dato, nodo_actual.derecha)
    return nodo_actual
  def _encontrar_minimo(self, nodo_actual):
    while nodo_actual.izquierda is not None:
      nodo_actual = nodo_actual.izquierda
    return nodo_actual
  def display(self):
    display(self.verimagen())

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
    def mostnomnue(self):
        actual = self.inicio
        almacenar = []
        while actual:
            mostrar = str(actual.destino) + " - distancia: " + str(actual.peso) + "m"
            almacenar.append(mostrar)
            actual = actual.siguiente
        salida = " -- ".join(almacenar)
        return salida

    def listnommat(self, caso):
        match caso:
            case "imprimir":
                almacenar = []
                actual = self.inicio
                while actual:
                    almacenar.append((actual.destino, actual.peso))  
                    actual = actual.siguiente
                return almacenar
            case "DFS":
                almacenar = []
                actual = self.inicio
                while actual:
                    almacenar.append((actual.destino, int(actual.peso)))
                    actual = actual.siguiente
                return almacenar

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
    def mostrar_lista_salas(self, contenedor):
        # Etiqueta caminos desde
        self.eti_de_salas = tk.Label(
            contenedor,
            text=f"Lista de salas ",            # Texto que muestra la etiqueta
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
        self.eti_de_salas.pack(pady=10)
        # Crear contenedor
        self.texto_mostrar = tk.Text(contenedor,                 # En donde se coloca el contenedor
                                     width=160,                  # Ancho de la etiqueta
                                     height=30,                  # Define cuantas líneas de texto se pueden mostrar                 
                                     font=("Century Gothic", 10),# Fuente, tamaño y estilo
                                     fg="black",                 # Color del texto
                                     bg="#f0f0f0"                # Color de fondo de la etiqueta
                                     )
        self.texto_mostrar.pack(fill="both", expand=True, pady=10)
        lista_de_salas = []
        for sala, caminos in self.grafo.items():
            lista_de_salas.append(f"{sala} -- {caminos.mostnomnue()}")
        texto = "\n\n".join(lista_de_salas)
        self.texto_mostrar.insert(tk.END, texto)
        self.texto_mostrar.config(state="disabled")
    def most_mat_ady(self, contenedor):
        # Etiqueta 
        self.Etiqueta_titmat = tk.Label(
                contenedor,
                text=f"Matriz de adyacencia ",      # Texto que muestra la etiqueta
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
        self.Etiqueta_titmat.pack(pady=10)
        # Crear contenedor
        self.mostrar_matriz = tk.Text(
                contenedor,
                font=("Century Gothic", 10),        # Fuente, tamaño y estilo (negrita)
                fg="black",                         # Color del texto
                bg="#f0f0f0",                       # Color del fondo de la etiqueta
                width=160,                          # Ancho de la etiqueta (en caracteres aprox.)
                height=30                           # Define cuantas líneas de texto puede mostrar
        )
        self.mostrar_matriz.pack(fill="both", expand=True, pady=10)
        # Hacer matriz
        nodos = list(self.grafo.keys())
        n = len(nodos)
        posicion = {nodo: indice for indice, nodo in enumerate(nodos)}
        matriz_most = [[0] * n for _ in range(n)]
        for clave, valor in self.grafo.items():
            origen = posicion[clave]
            nombres = valor.listnommat("imprimir")
            for final, peso in nombres:
                destino = posicion[final]
                matriz_most[origen][destino] = peso
        # convertir a cadena
        texto = "\n \n\n\n"
        for lista, listas in enumerate(matriz_most):
            texto_lista = " ".join(str(elemento) for elemento in listas)
            texto += f"\t\t{nodos[lista]}\t\t\t\t{texto_lista}\n"
        self.mostrar_matriz.insert(tk.END, texto)
        self.mostrar_matriz.config(state="disabled")

                
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
            command=self.abrirUsu
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
    def abrirUsu(self):
        self.ventanaPrincipal.destroy()
        ChecarID()

class ChecarID:
    def __init__(self):
        self.venChe = tk.Tk()
        self.venChe.title('ID')
        self.venChe.geometry('800x600+300+0')
        # Icono de la ventana
        self.venChe.iconbitmap('Logous.ico')
        self.checarID()
    def checarID(self):
        # Cosas de la ventana ID
        self.etiquetaEspacio10 = tk.Label(self.venChe, text="   ", font=("Century Gothic", 12))
        self.etiquetaEspacio11 = tk.Label(self.venChe, text="   ", font=("Century Gothic", 12))
        self.etiquetaID = tk.Label(self.venChe, text="Escribe tu ID de Usuario", font=("Century Gothic", 12))
        self.entradaID = tk.Entry(
            self.venChe,
            font=("Century Gothic", 12),
            bg="#ffffff",           # Fondo 
            fg="black",             # Texto 
            bd=2,                   # Grosor del borde
            relief="groove",        # Estilo del borde
            width=23,               # Ancho en caracteres
            justify="center",       # Texto centrado
            insertbackground="black"# Color del cursor
        )
        self.botonIngID = tk.Button(
            self.venChe,
            text='Ingresar',
            font=("Century Gothic", 10),
            bg="#abaeb8",              # Fondo
            fg="black",                # Color del texto
            activebackground="#4b5572",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=76,                   # Espacio horizontal interno
            pady=3,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.cP
        )
        self.etiquetaTitulo = tk.Label(
            self.venChe,
            text="¿No tienes id aun? ¡Crea uno!",# Texto que muestra la etiqueta
            font=("Century Gothic", 12),# Fuente, tamaño y estilo (negrita)
            fg="black",                         # Color del texto
            bg="#f0f0f0",                       # Color del fondo de la etiqueta
            width=30,                           # Ancho de la etiqueta (en caracteres aprox.)
            anchor="center",                    # Posición del texto dentro de la etiqueta
            relief="flat",                      # Tipo de borde (puede ser flat, raised, sunken, ridge, groove, solid)
            bd=2,                               # Grosor del borde
            padx=10,                            # Espacio interno horizontal
            pady=5                              # Espacio interno vertical
        )
        self.botonCreID = tk.Button(
            self.venChe,
            text='Crear ID',
            font=("Century Gothic", 10),
            bg="#abaeb8",              # Fondo
            fg="black",                # Color del texto
            activebackground="#4b5572",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=76,                    # Espacio horizontal interno
            pady=3,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.cP
        )
        # Posiciones
        self.etiquetaEspacio10.pack(pady=45)
        self.etiquetaID.pack(pady=5)
        self.entradaID.pack(pady=5)
        self.botonIngID.pack(pady=5)
        self.etiquetaEspacio11.pack(pady=7)
        self.etiquetaTitulo.pack(pady=5)
        self.botonCreID.pack(pady=5)
    def cP(self):
        print(1)

class IniciarSesioncomoUsuario:
    def __init__(self):
        self.ventUs = tk.Tk()
        self.ventUs.title('Usuario')
        self.ventUs.geometry('800x600+300+0')
        # Icono de la ventana
        self.ventUs.iconbitmap('Logous.ico')
        self.divisiones_colores_ventUs()
    # Botones de acciones para usuario --------------------------------------------------------------
        self.etiquetaEspacio8 = tk.Label(
            self.div_izq,
            text="   ",  # Texto que muestra la etiqueta
            font=("Century Gothic", 12, "bold"),# Fuente, tamaño y estilo (negrita)
            fg="black",                         # Color del texto
            bg="#ccd1d1",                       # Color del fondo de la etiqueta
            width=8,                            # Ancho de la etiqueta (en caracteres aprox.)
            anchor="center",                    # Posición del texto dentro de la etiqueta
            relief="flat",                      # Tipo de borde (puede ser flat, raised, sunken, ridge, groove, solid)
            bd=2,                               # Grosor del borde
            padx=1,                             # Espacio interno horizontal
            pady=5                              # Espacio interno vertical
        )
        self.botonLisSal = tk.Button(
            self.div_izq,
            text = "Lista de Salas",
            font=("Comic Sans MS", 10),
            bg='#99a3a4',              # Fondo
            fg="black",                # Color del texto
            activebackground="#f8f9f9",# Fondo al presionar
            activeforeground="black",  # Color del texto al presionar
            padx=14,                   # Espacio horizontal interno
            pady=2,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.lisSalUsu
        )
        self.boton_camino_corto = tk.Button(
            self.div_izq,
            text = " Mostrar mapa  ",
            font=("Comic Sans MS", 10),
            bg='#99a3a4',              # Fondo
            fg="black",                # Color del texto
            activebackground="#f8f9f9",# Fondo al presionar
            activeforeground="black",  # Color del texto al presionar
            padx=9,                    # Espacio horizontal interno
            pady=2,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.mosMapUsu
        )
        self.boton_calcular_camino = tk.Button(
            self.div_izq,
            text = "Buscar camino",
            font=("Comic Sans MS", 10),
            bg='#99a3a4',              # Fondo
            fg="black",                # Color del texto
            activebackground="#f8f9f9",# Fondo al presionar
            activeforeground="black",  # Color del texto al presionar
            padx=13,                   # Espacio horizontal interno
            pady=2,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.comandoTemporal_3
        )
        self.botonRegresar = tk.Button(
            self.div_izq,
            text='Regresar',
            font=("Century Gothic", 10),
            bg="red",                  # Fondo
            fg="white",                # Color del texto
            activebackground="#900303",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=30,                    # Espacio horizontal interno
            pady=2,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.regresar
        )
        self.etiquetaEspacio8.pack(pady=58)
        self.botonLisSal.pack(pady=10)
        self.boton_camino_corto.pack(pady=10)
        self.boton_calcular_camino.pack(pady=10)
        self.botonRegresar.pack(pady=10)

        #-----------COSAS DE LA SUBVENTANA USUARIO(fondo)----------

        # Etiqueta de espacio
        self.etiquetaEspacio9 = tk.Label(self.fondo, text="    ", bg="#f0f0f0", font=("Arial", 12))
        # Textos
        self.etiquetaBienUsu = tk.Label(
            self.fondo,
            text="¡Bienvenido Usuario!",  # Texto que muestra la etiqueta
            font=("Century Gothic", 30, "bold"),# Fuente, tamaño y estilo (negrita)
            fg="black",                         # Color del texto
            bg="#f0f0f0",                         # Color del fondo de la etiqueta
            width=23,                           # Ancho de la etiqueta (en caracteres aprox.)
            anchor="center",                    # Posición del texto dentro de la etiqueta
            relief="flat",                      # Tipo de borde (puede ser flat, raised, sunken, ridge, groove, solid)
            bd=2,                               # Grosor del borde
            padx=1,                             # Espacio interno horizontal
            pady=5                              # Espacio interno vertical
        )
        self.etiquetaAccionUsu = tk.Label(self.fondo, text="Seleccione cualquier acción de la barra de menú", bg="#f0f0f0", font=("Century Gothic", 12))
        # Posiciones
        self.etiquetaEspacio9.pack(pady = 90)
        self.etiquetaBienUsu.pack(pady = 10)
        self.etiquetaAccionUsu.pack(pady = 8)
        
    def limpiar(self):
        if hasattr(self, 'etiquetaEspacio9'):
            self.etiquetaEspacio9.destroy()
            self.etiquetaBienUsu.destroy()
            self.etiquetaAccionUsu.destroy()
        if hasattr(self, 'marAccUsu'):
            self.marAccUsu.destroy()
    def lisSalUsu(self):
        self.limpiar()
        self.marAccUsu = tk.Frame(self.fondo, bg="#f0f0f0")
        self.marAccUsu.pack(expand=True)
        grafo.mostrar_lista_salas(self.marAccUsu)
    def mosMapUsu(self):
        self.limpiar()
        # Hacer de nuevo el contenedor temporal
        self.marAccUsu = tk.Frame(self.fondo, bg="#f0f0f0")
        self.marAccUsu.pack(expand=True)
        # Funcion
        grafo.mostrarMapa(self.marAccUsu)
    def regresar(self):
        self.ventUs.destroy()
        VentanaPrincipal()

    def comandoTemporal_3(self):
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
    
        self.fondo = tk.Frame(self.color_fondo, bg='#f0f0f0', width=300, height=560)
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
            command=lambda:self.regresar_vent_prin()
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
            command=self.mostrar_salas
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
            command=self.mostrar_matriz_
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
    def mostrar_salas(self):
        self.limpiarImagen()
        # Hacer de nuevo el contenedor temporal
        self.marAcc = tk.Frame(self.imagen, bg="#f0f0f0")
        self.marAcc.pack(expand=True)
        # Funcion
        grafo.mostrar_lista_salas(self.marAcc)
    def regresar_vent_prin(self):
        self.ventControl.destroy()
        VentanaPrincipal()
    def mostrar_matriz_(self):
        self.limpiarImagen()
        # Hacer de nuevo el contenedor temporal
        self.marAcc = tk.Frame(self.imagen, bg="#f0f0f0")
        self.marAcc.pack(expand=True)
        # Funcion
        grafo.most_mat_ady(self.marAcc)

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
# Arbol
arbolID = ABB()
arbolID.insertar("202501")
arbolID.insertar("202502")
arbolID.insertar("202503")
arbolID.insertar("202504")

# 5.- ---------- Bloque Principal ----------
if __name__ == '__main__':
    aplicacionGrafo = VentanaPrincipal()
    aplicacionGrafo.ventanaPrincipal.mainloop()
    
# 6.- ---------- Documentación y comentarios ----------
'''
Búsqueda de información:
    - Chatgpt:
    - Código del profesor y clasroom de la materia:
        + Esqueleto del código
        + Menú
    - Formado a partir del proyecto de grafo
'''

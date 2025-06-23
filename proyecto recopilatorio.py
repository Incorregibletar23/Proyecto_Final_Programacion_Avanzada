# ---------- IMPORTACION DE MODULOS Y BIBLIOTECAS ----------

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import networkx as nx
import matplotlib.pyplot as plt
import tracemalloc
import time
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import random
import queue
from proyecto_final import Nodo
from proyecto_final import ABB
from proyecto_final import NodoDoble
from proyecto_final import ListaDobleEnlazada
from proyecto_final import Grafo
from proyecto_final import VentanaPrincipal
from proyecto_final import ChecarID
from proyecto_final import IniciarSesioncomoUsuario
from proyecto_final import IniciarSesioncomoAdministrador
from proyecto_final import PruebaPersonas
from proyecto_final import BusquedaDeCamino

# ---------- CLASES Y FUNCIONES ----------
class Operaciones:
    def __init__(self, padre):
        self.padre = padre
        self.ventana = tk.Toplevel(padre)
        self.ventana.title("Sumar dos números")
        self.ventana.geometry("400x300")
        self._crear_interfaz()

    def _crear_interfaz(self):
        # Etiquetas y campos de entrada
        tk.Label(self.ventana, text="Número 1:", font=("Arial", 12)).pack(pady=5)
        self.entrada_num1 = tk.Entry(self.ventana, font=("Arial", 12))
        self.entrada_num1.pack(pady=5)

        tk.Label(self.ventana, text="Número 2:", font=("Arial", 12)).pack(pady=5)
        self.entrada_num2 = tk.Entry(self.ventana, font=("Arial", 12))
        self.entrada_num2.pack(pady=5)

        # Botón para calcular
        boton_sumar = tk.Button(self.ventana, text="Sumar",
                                command=self._calcular_suma,
                                font=("Arial", 12))
        boton_sumar.pack(pady=10)

        # Etiqueta para mostrar el resultado
        self.etiqueta_resultado = tk.Label(self.ventana, text="", font=("Arial", 12))
        self.etiqueta_resultado.pack(pady=10)

    def _calcular_suma(self):
        try:
            numero1 = int(self.entrada_num1.get())
            numero2 = int(self.entrada_num2.get())
            suma = numero1 + numero2
            self.etiqueta_resultado.config(text=f"Resultado: {suma}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números enteros válidos")


class MenuEduardo:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Academia de Computación")
        self.ventana.geometry("800x600+600+100")
        self.crear_menu()

        #---------COSAS DE LA VENTANA PRINCIPAL----------

        # Icono de la ventana
        self.ventana.iconbitmap('iconopythonchico.ico')
        # Texto de espacio
        self.etiqueta_espacio1 = tk.Label(self.ventana, text="    ", font=("Arial", 12))
        # Imagen icono python
        self.imagen_icono = Image.open('iconopython.png')
        self.imagen_icono = self.imagen_icono.resize((200, 200))
        self.imagen_icono_tk = ImageTk.PhotoImage(self.imagen_icono)
        self.label_imagen_icono = tk.Label(self.ventana, image=self.imagen_icono_tk)
        # Texto Eduardo Ramírez
        self.etiqueta_nombre = tk.Label(self.ventana, text="Ramírez Vásquez Eduardo", font=("Time New Roman", 23))
        # Posiciones
        self.etiqueta_espacio1.pack(pady = 25)
        self.label_imagen_icono.pack(pady=30)
        self.etiqueta_nombre.pack()
    

    def crear_menu(self):
        barra_menu = tk.Menu(self.ventana)

        # Estructura de menús jerárquicos
        estructura_menus = {
            "Principal": {
                "Salir": self._salir,
            },
            "Programación Avanzada": {
                "Contenedores": {
                    "Tuplas": {
                        "Practica 1 T": None,
                        "Practica 2 T": None
                    },
                    "Estructuras y Contenedores": {
                        "Documento EC": None,
                        "Actividad 1 EC": None,
                        "Actividad 2 EC": None
                    },
                    "Listas": None,
                    "Conjuntos": {
                        "Documento C": None,
                        "Codigo C": None
                    },
                    "Diccionarios" : None
                },
                "Pilas y Colas": {
                    "Pilas": {
                        "Pilas Normal" : {
                            "Documento PN" : None,
                            "Codigo PN" : None
                        },
                        "Pilas Micropython" : None
                    },
                    "Colas": {
                        "Colas Normal" : None,
                        "Colas Micropython" : {
                            "Codigo CM" : None,
                            "UML CM" : None
                        }
                    }
                },
                "Estructuras y Algoritmos Avanzados" : {
                    "Recursividad" : None,
                    "Grafos y Algoritmos de Busqueda" : None
                },
                "Arboles" : {
                    "Practica 1 ABB" : None,
                    "Practica 2 ABB" : None,
                    "Practica 3 ABB" : None
                },
                "Programación Concurrente" : {
                    "Practica 1 CC" : None,
                    "Practica 2 CC" : None
                }
            },
            "Proyectos": {
                "Proyecto Unidad 1" : None,
                "Proyecto Unidad 2" : None,
                "Proyecto Unidad 3" : {
                    "Codigo PU3" : None,
                    "Presentacion PU3" : None
                }
            },
            "Ayuda": {
                "Acerca de": None
            }
        }

        # Función recursiva para crear menús y submenús
        def crear_submenu(padre, estructura):
            for etiqueta, contenido in estructura.items():
                if callable(contenido):
                    padre.add_command(label=etiqueta, command=contenido)
                elif contenido is None:
                    padre.add_command(label=etiqueta, command=lambda s=etiqueta: self._accion(s))
                else:
                    submenu = tk.Menu(padre, tearoff=0)
                    crear_submenu(submenu, contenido)
                    padre.add_cascade(label=etiqueta, menu=submenu)

        crear_submenu(barra_menu, estructura_menus)
        self.ventana.config(menu=barra_menu)

    def _salir(self):
        self.ventana.quit()
        self.ventana.destroy()
        MenuPrincipal()

    def _abrir_operaciones(self):
        Operaciones(self.ventana)

    def _accion(self, nombre):
        match nombre:
            case "Presentacion PU3":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "URL del canva:\n \nhttps://www.canva.com/design/DAGq1AvEGzU/NFeT-2fxMIGX4L5MPhnDFw/edit?utm_content=DAGq1AvEGzU&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton\nVideo:\n\nhttps://drive.google.com/file/d/1uwnV77hsIA6vj49XcKbSwEYFj8M9mxR7/view?usp=sharing \n \n Esp32: \n\nhttps://wokwi.com/projects/434491088861818881"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Acerca de":
                messagebox.showinfo("Acerca de", "Programa de Programación Avanzada\nVersión 1.0\npor Jorge Anzaldo")
            case "Proyecto Unidad 1":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://docs.google.com/document/d/18jtN_xtKsdO3vkkzGQc6ViPAdSvPL19_Em2RSnCWWtc/edit?usp=sharing"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Proyecto Unidad 2":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "¡Tienes que abrirlo desde el archivo de esta carpeta!\n \n El primer código es: \n https://colab.research.google.com/drive/1IvIiUYVhTv7WrJa431VXXJVODehNMqMy?usp=sharing"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Codigo PU3":
                aplicacionGrafo = VentanaPrincipal()
                aplicacionGrafo.ventanaPrincipal.mainloop()
            case "Practica 2 CC":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://colab.research.google.com/drive/1N0Ghm4-bPv3vo_84MpL9c6xTG7Y0QKoY?usp=sharing&authuser=0"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Practica 1 CC":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://docs.google.com/document/d/1lt204IGdS-VHmpEVl_y0-JkG1QezlqfoF5uDl4Ni8vc/edit?usp=classroom_web&authuser=0"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Practica 2 ABB":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://colab.research.google.com/drive/1ajVKJE6KI9foPRSprqcwIZH9H2sgiPi1?usp=sharing"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Practica 1 ABB":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://colab.research.google.com/drive/1xXbIJWsSh5RYsw4mA2dQ6vYxwgmbuhZz?usp=sharing"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Practica 3 ABB":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://colab.research.google.com/drive/17qW0rm4p72hotkOL2j2y8CBTIY3B9NZR?usp=sharing"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Grafos y Algoritmos de busqueda":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://colab.research.google.com/drive/1IvIiUYVhTv7WrJa431VXXJVODehNMqMy?usp=sharing"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Recursividad":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://www.onlinegdb.com/fYFa536Ym"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "UML CM":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://drive.google.com/file/d/1y9wNKJqSDMV9B6PxqkLWafx6DoTQiqnt/view?usp=classroom_web&authuser=0"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Codigo CM":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://wokwi.com/projects/425792494558552065"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Colas Normal":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://www.onlinegdb.com/d9QQNQB-l"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Pilas Micropython":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://wokwi.com/projects/424801011248966657"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Documento PN":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://docs.google.com/document/d/1lMm6tN0C7AQycKvIcosFfEp-0dkfsGRM9eaU8_OhbNw/edit?tab=t.0"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Codigo PN":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://onlinegdb.com/gm3LoAUdv"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Practica 1 T":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://wokwi.com/projects/423748612474006529"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Practica 2 T":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://wokwi.com/projects/423735788136664065"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Documento EC":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://docs.google.com/document/d/1Y3ICKeA9lWZEsxRTvRRCm6_9HZThgPTXLTCC_J2VYBw/edit?tab=t.0"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Actividad 1 EC":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://www.onlinegdb.com/9MSaNyZGA4"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Actividad 2 EC":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://www.onlinegdb.com/zu8eS_HIA"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Listas":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://www.onlinegdb.com/bsnOrtPMj"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Documento C":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://docs.google.com/document/d/1Zd7BQoO-TuxfyPFy2rDIsdwuoNtW2XMdgueBMAuUZPg/edit?tab=t.0"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Codigo C":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://www.onlinegdb.com/8xKIEE9Aw"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Diccionarios":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://www.onlinegdb.com/EQpQCLZIJ"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case _:
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                etiqueta = tk.Label(nueva_ventana, text=f"Esta es la ventana para: {nombre}", font=("Arial", 14))
                etiqueta.pack(pady=20)

class MenuRenata:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Academia de Computación")
        self.ventana.geometry("800x600+600+100")
        self.crear_menu()

        #---------COSAS DE LA VENTANA PRINCIPAL----------

        # Icono de la ventana
        self.ventana.iconbitmap('iconopythonchico.ico')
        # Texto de espacio
        self.etiqueta_espacio1 = tk.Label(self.ventana, text="    ", font=("Arial", 12))
        # Imagen icono python
        self.imagen_icono = Image.open('iconopython.png')
        self.imagen_icono = self.imagen_icono.resize((200, 200))
        self.imagen_icono_tk = ImageTk.PhotoImage(self.imagen_icono)
        self.label_imagen_icono = tk.Label(self.ventana, image=self.imagen_icono_tk)
        # Texto Eduardo Ramírez
        self.etiqueta_nombre = tk.Label(self.ventana, text="Rosas López Renata", font=("Time New Roman", 23))
        # Posiciones
        self.etiqueta_espacio1.pack(pady = 25)
        self.label_imagen_icono.pack(pady=30)
        self.etiqueta_nombre.pack()
    

    def crear_menu(self):
        barra_menu = tk.Menu(self.ventana)

        # Estructura de menús jerárquicos
        estructura_menus = {
            "Principal": {
                "Salir": self._salir,
            },
            "Programación Avanzada": {
                "ESP 32": {
                    "Manejo de LEDs con Tuplas en MicroPython (ESP32)": None,
                    "Manejo de LEDs con Listas en MicroPython (ESP32)": None,
                    "Manejo de LEDs con Pilas en MicroPython (ESP32)": None,
                    "Manejo de LEDs con Colas en MicroPython (ESP32)": None
                },
                "Contenedores": {
                    "Práctica 1 Estructuras de Datos y Contenedores": None,
                    "Práctica 2 Listas": None,
                    "Práctica 3 Conjuntos": None,
                    "Práctica 4 Diccionarios": None
                },
                "Pilas y Colas": None,
                "Recursividad y Grafos": {
                    "Recursividad 2CV13": None,
                    "Grafos 2CV13": None
                },
                "Arboles Binarios": {
                    "Arboles Binarios 2CV13": None,
                    "Recorridos de Arboles Binarios 2CV13": None
                },
                "Concurrencia": None
            },
            "Proyectos": {
                "Proyecto Unidad 1": None,
                "Proyecto Unidad 2": None,
                "Proyecto Unidad 3": {
                    "Codigo PU3" : None,
                    "Presentacion PU3" : None
                }
            },
            "Ayuda": {
                "Acerca de": None
            }
        }

        # Función recursiva para crear menús y submenús
        def crear_submenu(padre, estructura):
            for etiqueta, contenido in estructura.items():
                if callable(contenido):
                    padre.add_command(label=etiqueta, command=contenido)
                elif contenido is None:
                    padre.add_command(label=etiqueta, command=lambda s=etiqueta: self._accion(s))
                else:
                    submenu = tk.Menu(padre, tearoff=0)
                    crear_submenu(submenu, contenido)
                    padre.add_cascade(label=etiqueta, menu=submenu)

        crear_submenu(barra_menu, estructura_menus)
        self.ventana.config(menu=barra_menu)

    def _salir(self):
        self.ventana.quit()
        self.ventana.destroy()
        MenuPrincipal()

    def _abrir_operaciones(self):
        Operaciones(self.ventana)

    def _accion(self, nombre):
        match nombre:
            case "Presentacion PU3":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "URL del canva:\n \nhttps://www.canva.com/design/DAGq1AvEGzU/NFeT-2fxMIGX4L5MPhnDFw/edit?utm_content=DAGq1AvEGzU&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton\nVideo:\n\nhttps://drive.google.com/file/d/1uwnV77hsIA6vj49XcKbSwEYFj8M9mxR7/view?usp=sharing \n \n Esp32: \n\nhttps://wokwi.com/projects/434491088861818881"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Acerca de":
                messagebox.showinfo("Acerca de", "Programa de Programación Avanzada\nVersión 1.0\npor Jorge Anzaldo")
            case "Proyecto Unidad 1":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://colab.research.google.com/drive/1dCGWvaOxwdQiw07UTONpzfAr5S3zrpNo?usp=sharing"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Proyecto Unidad 2":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "¡Tienes que abrirlo desde el archivo de esta carpeta!\n \n El primer código es: \n https://colab.research.google.com/drive/1IvIiUYVhTv7WrJa431VXXJVODehNMqMy?usp=sharing"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Codigo PU3":
                aplicacionGrafo = VentanaPrincipal()
                aplicacionGrafo.ventanaPrincipal.mainloop()
            case "Practica 2 CC":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://colab.research.google.com/drive/1N0Ghm4-bPv3vo_84MpL9c6xTG7Y0QKoY?usp=sharing&authuser=0"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Diccionarios":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://www.onlinegdb.com/EQpQCLZIJ"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Concurrencia":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://colab.research.google.com/drive/1pOZ7SgkHYq-14I5iMOOcrYPIBN_y_1PI?usp=sharing&authuser=0"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Recorridos de Arboles Binarios 2CV13":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://colab.research.google.com/drive/1SsXwuqizwCTr8xPw9D1xhAtVhpij7Syn?usp=sharing&authuser=0"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Arboles Binarios 2CV13":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://colab.research.google.com/drive/1Z80XYWjC9LadiFUzjftPYl9fqDRZPSeO?usp=sharing&authuser=0"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Grafos 2CV13":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://colab.research.google.com/drive/1NcPC9VpXfNoJGlELtnmZgfrDTQAhqf6-?usp=sharing"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Recursividad 2CV13":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://colab.research.google.com/drive/1RXeM3oR_eBGOfsWGHi490A3LlNQ598yz?usp=sharing&authuser=0"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Pilas y Colas":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://colab.research.google.com/drive/14vz5zv3_njnbK1SxoL5y1QhUn-VREqeN?usp=sharing&authuser=0"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Práctica 4 Diccionarios":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://colab.research.google.com/drive/1d-5p8RIlUp_-RZA_wu8RmLnko5JGLCyb?usp=sharing&authuser=0"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Práctica 3 Conjuntos":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://colab.research.google.com/drive/1Rk-OY0YGot9FPQvOzRz3AheC3k1gqGvj?usp=sharing&authuser=0"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Práctica 2 Listas":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://colab.research.google.com/drive/1LpmPIp8xarR5x6Bj95uaU7r_mnH4W8LV?usp=sharing&authuser=0"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Práctica 1 Estructuras de Datos y Contenedores":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://colab.research.google.com/drive/1rCthSGg8B595JqiN_Q-eWSYuuv6q45TW?usp=sharing&authuser=0"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Manejo de LEDs con Colas en MicroPython (ESP32)":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://wokwi.com/projects/425795263602714625?authuser=0"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Manejo de LEDs con Pilas en MicroPython (ESP32)":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://wokwi.com/projects/425795004647394305?authuser=0"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Manejo de LEDs con Listas en MicroPython (ESP32)":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://wokwi.com/projects/424700386727105537?authuser=0"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case "Manejo de LEDs con Tuplas en MicroPython (ESP32)":
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                text = "Código de la práctica:\n \nhttps://wokwi.com/projects/424196070327742465?authuser=0"
                texto = tk.Text(nueva_ventana,# En donde se coloca el contenedor
                    width=160,                  # Ancho de la etiqueta
                    height=30,                  # Define cuantas líneas de texto se pueden mostrar
                    font=("Century Gothic", 10),# Fuente, tamaño y estilo
                    fg="black",                 # Color del texto
                    bg="#f0f0f0"                # Color de fondo de la etiqueta
                )
                texto.pack(fill="both", expand=True, pady=10)
                texto.insert(tk.END, text)
                texto.config(state="disabled")
            case _:
                nueva_ventana = tk.Toplevel(self.ventana)
                nueva_ventana.title(nombre)
                nueva_ventana.geometry("400x300")
                nueva_ventana.iconbitmap('iconopythonchico.ico')
                etiqueta = tk.Label(nueva_ventana, text=f"Esta es la ventana para: {nombre}", font=("Arial", 14))
                etiqueta.pack(pady=20)

class MenuPrincipal:
    def __init__(self):
        self.ventanaPrincipal = tk.Tk()
        self.ventanaPrincipal.title('Iniciar Sesion')
        self.ventanaPrincipal.geometry('800x600+300+0')
        self.ventanaPrincipal.iconbitmap('iconopythonchico.ico')
        self.fondoDividido()
    def fondoDividido(self):
        # Tamaños de la ventana
        alto = 600
        ancho = 800
        # Color crema:
        self.colorArriba = tk.Frame(self.ventanaPrincipal, bg='#f0f0f0', width=ancho, height=alto//2)
        self.colorArriba.pack(side='top', fill='x')
        # Color naranja
        self.colorAbajo = tk.Frame(self.ventanaPrincipal, bg='#4c94cc', width=ancho, height=alto//2)
        self.colorAbajo.pack(side='bottom', fill='x')

        #-----------COSAS DE LA VENTANA PRINCIPAL----------

        # Texto de espacio
        self.etiquetaEspacio1 = tk.Label(self.colorArriba, text="    ", font=("Arial", 12))
        self.etiquetaEspacio2 = tk.Label(self.colorArriba, text="    ", font=("Arial", 12))
        self.etiquetaEspacio3 = tk.Label(self.colorArriba, text="    ", font=("Arial", 12))
        # Texto Titulo y Slogan de la aplicación
        self.etiquetaTitulo = tk.Label(
            self.colorArriba,
            text="Proyecto Recopilatorio",                   # Texto que muestra la etiqueta
            font=("Century Gothic", 35, "bold"),# Fuente, tamaño y estilo (negrita)
            fg="black",                         # Color del texto
            bg="#f0f0f0",                       # Color del fondo de la etiqueta
            width=30,                           # Ancho de la etiqueta (en caracteres aprox.)
            anchor="center",                    # Posición del texto dentro de la etiqueta
            relief="flat",                      # Tipo de borde (puede ser flat, raised, sunken, ridge, groove, solid)
            bd=2,                               # Grosor del borde
            padx=10,                            # Espacio interno horizontal
            pady=5                              # Espacio interno vertical
        )
        self.etiquetaSlogan = tk.Label(self.colorArriba, text="Programación Avanzada", font=("Century Gothic", 18))
        # Boton Iniciar Sesion como usuario y administrador
        self.botonISAdmin = tk.Button(
            self.colorArriba,
            text='Ingresar como Renata',
            font=("Century Gothic", 10),
            bg="#abaeb8",              # Fondo
            fg="black",                # Color del texto
            activebackground="#4b5572",# Fondo al presionar
            activeforeground="white",  # Color del texto al presionar
            padx=27,                    # Espacio horizontal interno
            pady=2,                    # Espacio vertical interno
            relief="raised",           # Estilo de borde
            bd=3,                      # Grosor del borde
            cursor="hand2",            # Cambia a manita
            command=self.abrirAdmin
        )
        self.botonISUs = tk.Button(
            self.colorArriba,
            text='Ingresar como Eduardo',
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
        MenuRenata()
    def abrirUsu(self):
        self.ventanaPrincipal.destroy()
        MenuEduardo()
# ---------- VARIABLES U OBJETOS GLOBALES ---------

# ---------- MAIN ----------
if __name__ == "__main__":
    aplicacion = MenuPrincipal()
    aplicacion.ventanaPrincipal.mainloop()

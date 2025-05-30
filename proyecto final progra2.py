import tkinter as tk
from tkinter import messagebox
from proyecto_grafo import NodoDoble

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


class MenuPrincipal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Academia de Computación")
        self.ventana.geometry("800x600")
        self.crear_menu()

    def crear_menu(self):
        barra_menu = tk.Menu(self.ventana)

        # Estructura de menús jerárquicos
        estructura_menus = {
            "Principal": {
                "Salir": self._salir,
            },
            "Fundamentos POO": {
                "Unidad I": None,
                "Unidad II": {
                    "IPO": {
                        "Entrada": self._abrir_operaciones,
                        "Salida": None
                    },
                    "SubUnidad II": None
                },
                "Unidad III": None
            },
            "Programación Avanzada": {
                "Contenedores": {
                    "Tuplas": None,
                    "Lista": None,
                    "Conjuntos": None
                },
                "Pilas y Colas": {
                    "Pilas": None,
                    "Colas": None
                }
            },
            "Proyecto": {
                "Análisis": None,
                "Diseño": None,
                "Desarrollo": None
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

    def _abrir_operaciones(self):
        Operaciones(self.ventana)

    def _accion(self, nombre):
        if nombre == "Acerca de":
            messagebox.showinfo("Acerca de", "Programa de Programación Avanzada\nVersión 1.0\npor Jorge Anzaldo")
        else:
            nueva_ventana = tk.Toplevel(self.ventana)
            nueva_ventana.title(nombre)
            nueva_ventana.geometry("400x300")
            etiqueta = tk.Label(nueva_ventana, text=f"Esta es la ventana para: {nombre}", font=("Arial", 14))
            etiqueta.pack(pady=20)


if __name__ == "__main__":
    aplicacion = MenuPrincipal()
    aplicacion.ventana.mainloop()

from tkinter import *
import math

def crear_ventana():
    bg_color = "#d42bf0"
    fg_color = "#333"
    font = ("Arial", 12)
    vent = Tk()
    vent.title("Calculadora Simple")
    vent.geometry("750x400")
    vent.configure(bg=bg_color)
    def formato_resultado(r):
        return int(r) if r % 1 == 0 else r
    def suma():
        n1 = txt1.get()
        n2 = txt2.get()
        try:
            r = float(n1) + float(n2)
            r = formato_resultado(r)
            txt3.delete(0, 'end')
            txt3.insert(0, r)
        except ValueError:
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")
    def resta():
        n1 = txt1.get()
        n2 = txt2.get()
        try:
            r = float(n1) - float(n2)
            r = formato_resultado(r)
            txt3.delete(0, 'end')
            txt3.insert(0, r)
        except ValueError:
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")
    def multiplicacion():
        n1 = txt1.get()
        n2 = txt2.get()
        try:
            r = float(n1) * float(n2)
            r = formato_resultado(r)
            txt3.delete(0, 'end')
            txt3.insert(0, r)
        except ValueError:
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")
    def division():
        n1 = txt1.get()
        n2 = txt2.get()
        try:
            r = float(n1) / float(n2)
            r = formato_resultado(r)
            txt3.delete(0, 'end')
            txt3.insert(0, r)
        except ValueError:
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")
        except ZeroDivisionError:
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")
    def valor_absoluto():
        n1 = txt1.get()
        try:
            r = abs(float(n1))
            r = formato_resultado(r)
            txt3.delete(0, 'end')
            txt3.insert(0, r)
        except ValueError:
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")
    def mcm():
        def calcular_mcm(a, b):
            return abs(a * b) // math.gcd(a, b)

        n1 = txt1.get()
        n2 = txt2.get()
        try:
            r = calcular_mcm(int(n1), int(n2))
            txt3.delete(0, 'end')
            txt3.insert(0, r)
        except ValueError:
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")
    def mcd():
        n1 = txt1.get()
        n2 = txt2.get()
        try:
            r = math.gcd(int(n1), int(n2))
            txt3.delete(0, 'end')
            txt3.insert(0, r)
        except ValueError:
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")
    def salir():
        vent.destroy()

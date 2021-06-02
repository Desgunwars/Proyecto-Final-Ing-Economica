import tkinter as tk
import math 
from alerta import Alert


class NumeroPeriodos(object):
    def __init__(self):
        super().__init__()
        self.newWindow = tk.Toplevel()
        self.newWindow.title = "Numero de Periodos"
        self.newWindow.geometry('500x230')
        self.newWindow.resizable(0, 0)        

        self.wrapper = tk.LabelFrame(self.newWindow, text="Numero de Periodos")

        # Variables
        self.n = tk.StringVar()
        self.vp = tk.StringVar()
        self.i = tk.StringVar()
        self.vf = tk.StringVar()

        # Label and entry point
        self.labelValorFinal = tk.Label(self.wrapper, text="Ingrese Valor Final: ")
        self.entryValorFinal = tk.Entry(self.wrapper, width=35, bd=5, textvariable=self.vf)

        self.labelTasaInteres = tk.Label(self.wrapper, text="Ingrese Valor Presente: ")
        self.entryTasaInteres = tk.Entry(self.wrapper, width=35, bd=5, textvariable=self.vp)

        self.labelNperiodos = tk.Label(self.wrapper, text="Ingrese la tasa de Ineteres: ")
        self.entryNperiodos = tk.Entry(self.wrapper, width=35, bd=5, textvariable=self.i)

        self.mensajeLabelRuslt = tk.Label(self.wrapper, text="El Valor Final es: ")
        self.mensajeReult = tk.Label(self.wrapper, textvariable = self.n, font=("Time New Roman", 10, "bold"))
        
        # Buttons
        self.calcularValorFInal = tk.Button(self.wrapper, text="Calcular Periodos", width=25, command=self.CalcularPeriodos)
        self.atras = tk.Button(self.wrapper, text="Atras",width=10, command=self.Cerrar)

        # Add Pack Wrapper
        self.wrapper.pack(padx=10, pady=5, fill="both", expand="yes")

        # Grid Label and Entry
        self.labelValorFinal.grid(column=0, row=0, padx=5, pady=5)
        self.entryValorFinal.grid(column=1, row=0, padx=5, pady=5)
        self.labelTasaInteres.grid(column=0, row=1, padx=5, pady=5)
        self.entryTasaInteres.grid(column=1, row=1, padx=5, pady=5)
        self.labelNperiodos.grid(column=0, row=2, padx=5, pady=5)
        self.entryNperiodos.grid(column=1, row=2, padx=5, pady=5)
        self.mensajeLabelRuslt.grid(column=0, row=4, padx=5, pady=5)
        self.mensajeReult.grid(column=1, row=4, padx=5, pady=5)
        # Butons Grid
        self.calcularValorFInal.grid(column=0, row=3, padx=5, pady=5)
        self.atras.grid(column=1, row=3, padx=5, pady=5)

    def CalcularPeriodos(self):
        if self.vf.get() == "" or self.vp.get() == "" or self.i.get() == "" :
            alerta = Alert()
        else:
            valorFinal = float(self.vf.get())
            valorPresente = float(self.vp.get())
            tasaInteres = float(self.i.get())
            pagaron = 0
            multi = math.log(valorFinal/valorPresente)/math.log(1 + tasaInteres) 
            self.n.set(str(round(multi)) + "Meses")

    def Cerrar(self):
        self.newWindow.destroy()

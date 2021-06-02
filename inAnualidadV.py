import tkinter as tk
from alerta import Alert


class InAnualidadV(object):
    def __init__(self):
        super().__init__()
        self.newWindow = tk.Toplevel()
        self.newWindow.title = "Anualidad Vencida Con Interes Global"
        self.newWindow.geometry('500x230')
        self.newWindow.resizable(0, 0)        

        self.wrapper = tk.LabelFrame(self.newWindow, text="Anualidad Vencida Con Interes Global")

        # Variables
        self.A = tk.StringVar()
        self.vp = tk.StringVar()
        self.n = tk.StringVar()
        self.i = tk.StringVar()

        # Label and entry point
        self.labelValorFinal = tk.Label(self.wrapper, text="Ingrese Valor Presente: ")
        self.entryValorFinal = tk.Entry(self.wrapper, width=35, bd=5, textvariable=self.vp)

        self.labelTasaInteres = tk.Label(self.wrapper, text="Ingrese la Tasa Efectiva: ")
        self.entryTasaInteres = tk.Entry(self.wrapper, width=35, bd=5, textvariable=self.i)

        self.labelNperiodos = tk.Label(self.wrapper, text="Ingrese Numero de Periodos: ")
        self.entryNperiodos = tk.Entry(self.wrapper, width=35, bd=5, textvariable=self.n)

        self.mensajeLabelRuslt = tk.Label(self.wrapper, text="La Anualidad Vencida Con Interes Global: ")
        self.mensajeReult = tk.Label(self.wrapper, textvariable = self.A, font=("Time New Roman", 10, "bold"))
        
        # Buttons
        self.calcularValorFInal = tk.Button(self.wrapper, text="Calcular Anualidad Vencida", width=25, command=self.CalcularAnualidadVA)
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

    def CalcularAnualidadVA(self):
        if self.vp.get() == "" or self.i.get() == "" or self.n.get() == "" :
            alerta = Alert()
        else:
            valorPresente = float(self.vp.get())
            tasaEfectivaAnual = float(self.i.get())
            nperiodos = float(self.n.get())
            multi = ((valorPresente/nperiodos) + valorPresente * tasaEfectivaAnual)
            self.A.set(str(multi) + "$")

    def Cerrar(self):
        self.newWindow.destroy()

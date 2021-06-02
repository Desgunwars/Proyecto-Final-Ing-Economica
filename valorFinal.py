import tkinter as tk
from alerta import Alert


class ValorFinal(object):
    def __init__(self):
        super().__init__()
        self.newWindow = tk.Toplevel()
        self.newWindow.title = "Valor Final"
        self.newWindow.geometry('500x230')
        self.newWindow.resizable(0, 0)        

        self.wrapper = tk.LabelFrame(self.newWindow, text="Valor Final")

        # Variables
        self.vp = tk.StringVar()
        self.i = tk.StringVar()
        self.n = tk.StringVar()
        self.vf = tk.StringVar()

        # Label and entry point
        self.labelValorFinal = tk.Label(self.wrapper, text="Ingrese Valor Presente: ")
        self.entryValorFinal = tk.Entry(self.wrapper, width=35, bd=5, textvariable=self.vp)

        self.labelTasaInteres = tk.Label(self.wrapper, text="Ingrese Tasa de Interes: ")
        self.entryTasaInteres = tk.Entry(self.wrapper, width=35, bd=5, textvariable=self.i)

        self.labelNperiodos = tk.Label(
            self.wrapper, text="Ingrese el numero de periodos: ")
        self.entryNperiodos = tk.Entry(self.wrapper, width=35, bd=5, textvariable=self.n)

        self.mensajeLabelRuslt = tk.Label(self.wrapper, text="El Valor Final es: ")
        self.mensajeReult = tk.Label(self.wrapper, textvariable=self.vf, font=("Time New Roman", 10, "bold"))

        # Buttons
        self.calcularValorFInal = tk.Button(self.wrapper, text="Calcular Valor Final", width=25, command=self.CalcularVf)
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

    def CalcularVf(self):
        if self.vp.get() == "" or self.i.get() == "" or self.n.get() == "" :
            alerta = Alert()
        else:
            valorPresente = float(self.vp.get())
            tasainteres = float(self.i.get())
            nperiodos = float(self.n.get())
            pagaron = 0
            multi = (1 + tasainteres * nperiodos) 
            self.vf.set(str(multi) + "$")

    def Cerrar(self):
        self.newWindow.destroy()

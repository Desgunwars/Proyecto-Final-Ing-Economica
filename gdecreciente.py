import tkinter as tk
from alerta import Alert
import math

class GradienteDecreciente(object):
    def __init__(self):
        super().__init__()
        self.newWindow = tk.Toplevel()
        self.newWindow.title = "Gradiente Decreciente"
        self.newWindow.geometry('500x290')
        self.newWindow.resizable(0, 0)


        self.wrapper = tk.LabelFrame(self.newWindow, text="Gradiente Creciente")
        

        # Variables
        self.vf = tk.StringVar()
        self.i = tk.StringVar()
        self.n = tk.StringVar()
        self.vp = tk.StringVar()
        self.a = tk.StringVar()
        self.g = tk.StringVar()

        self.labelValueStart = tk.Label(self.wrapper, text = "Seleccione una Opcion")        
        self.list = ["Valor Presente", "Valor Final", "Cuota"]
        self.Cliketd = tk.StringVar()
        self.Cliketd.set(self.list[0])
        self.menuoption = tk.OptionMenu(self.wrapper, self.Cliketd, *self.list, command = self.opcionMenu)


        # Label and entry point
        self.labelCuota= tk.Label(
            self.wrapper, text="Ingrese la cuota: ")
        self.entryCuota = tk.Entry(
            self.wrapper, width=35, bd=5, textvariable=self.a)

        self.labelTasaInteres = tk.Label(
            self.wrapper, text="Ingrese Tasa de Interes: ")
        self.entryTasaInteres = tk.Entry(
            self.wrapper, width=35, bd=5, textvariable=self.i)

        self.labelNperiodos = tk.Label(
            self.wrapper, text="Ingrese el numero de periodos (Meses): ")
        self.entryNperiodos = tk.Entry(
            self.wrapper, width=35, bd=5, textvariable=self.n)

        self.labelGradiente = tk.Label(
            self.wrapper, text="Ingrese el gradiente: ")
        self.entryGradiente = tk.Entry(
            self.wrapper, width=35, bd=5, textvariable=self.g)

        self.mensajeLabelRuslt = tk.Label(
            self.wrapper, text="El Valor Presente es: ")
        self.mensajeReult = tk.Label(
            self.wrapper, textvariable=self.vp, font=("Time New Roman", 10, "bold"))


        # Buttons
        self.calcularValorFInal = tk.Button(
            self.wrapper, text="Calcular Valor Presente", width=25)

        self.atras = tk.Button(self.wrapper, text="Atras",
                                width=10, command=self.Cerrar)
        

        self.wrapper.pack(padx = 10, pady = 5, fill = "both")

        self.labelValueStart.grid(column = 0, row = 0)
        self.menuoption.grid(column = 1, row = 0, padx = 10, pady = 5 )

        self.labelCuota.grid(column=0, row=1, padx=5, pady=5)
        self.entryCuota.grid(column=1, row=1, padx=5, pady=5)
        self.labelTasaInteres.grid(column=0, row=2, padx=5, pady=5)
        self.entryTasaInteres.grid(column=1, row=2, padx=5, pady=5)
        self.labelNperiodos.grid(column=0, row=3, padx=5, pady=5)
        self.entryNperiodos.grid(column=1, row=3, padx=5, pady=5)
        self.labelGradiente.grid(column=0, row=4, padx=5, pady=5)
        self.entryGradiente.grid(column=1, row=4, padx=5, pady=5)

        self.calcularValorFInal.grid(column=0, row=5, padx=5, pady=5)
        self.atras.grid(column=1, row=5, padx=6, pady=5)

        self.mensajeLabelRuslt.grid(column=0, row=6, padx=5, pady=5)
        self.mensajeReult.grid(column=1, row=6, padx=5, pady=5)

        

    def opcionMenu(self,*args):
        if self.Cliketd.get() == "Valor Presente":
            self.labelCuota['text'] = "Ingrese la cuota: "
            self.mensajeLabelRuslt['text'] = "El Valor presente es de: "
            self.calcularValorFInal.config(text="Calcular Valor Presente",command=self.CalcularVp)

        elif self.Cliketd.get() == "Cuota":
            self.labelCuota['text'] = "Ingrese el Valor Final: "
            self.mensajeLabelRuslt['text'] = "El Cuota es de: "
            self.calcularValorFInal.config(text="Calcular Cuota",command=self.CalcularC)

        elif self.Cliketd.get() == "Valor Final":
            self.labelCuota['text'] = "Ingrese la Cuota: "
            self.mensajeLabelRuslt['text'] = "El Valor Final es de: "
            self.calcularValorFInal.config(text="Calcular Valor Final",command=self.CalcularVF)
    
    def CalcularVp(self):
        if self.a.get() == "" or self.i.get() == "":
            alerta = Alert()
        else:
            cuota = float(self.a.get())
            tasainteres = float(self.i.get())
            nperiodos = float(self.n.get())
            gradiente = float(self.g.get())

            valorentreparentesis = math.pow((1+tasainteres), nperiodos)
            calculo = cuota*((valorentreparentesis-1)/(tasainteres*valorentreparentesis))-(gradiente/tasainteres)*(((valorentreparentesis-1)/(valorentreparentesis*tasainteres))-(nperiodos/valorentreparentesis))
            self.vp.set("$"+str(calculo))

    def CalcularVF(self):
        if self.a.get() == "" or self.i.get() == "":
            alerta = Alert()
        else:
            cuota = float(self.a.get())
            tasainteres = float(self.i.get())
            nperiodos = float(self.n.get())
            gradiente = float(self.g.get())

            valorentreparentesis = math.pow((1+tasainteres), nperiodos)
            calculo = cuota*((valorentreparentesis-1)/tasainteres)-(gradiente/tasainteres)*(((valorentreparentesis-1)/tasainteres)-nperiodos)
            self.vp.set("$"+str(calculo))
    
    def CalcularC(self):
        if self.a.get() == "" or self.i.get() == "":
            alerta = Alert()
        else:
            valorfinal = float(self.a.get())
            tasainteres = float(self.i.get())
            nperiodos = float(self.n.get())
            gradiente = float(self.g.get())

            valorentreparentesis = math.pow((1+tasainteres), nperiodos)
            calculo = valorfinal+(gradiente/tasainteres)*(((valorentreparentesis-1)/tasainteres)-nperiodos)/((valorentreparentesis-1)/tasainteres)
            self.vp.set("$"+str(calculo))
            

    def Cerrar(self):
        self.newWindow.destroy()
                

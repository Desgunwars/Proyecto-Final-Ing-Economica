import tkinter as tk
from tkinter import ttk

class Aplication:
    def __init__(self):
        # Config Main Window GUI
        self.window1 = tk.Tk()
        self.window1.title("Ingenieria economica")
        self.window1.geometry('500x500')
        self.window1.resizable(0,0)
        self.window1.eval('tk::PlaceWindow . center')
        
        self.wrapper = tk.LabelFrame(self.window1, text = "Opciones de Simulacion")
        self.wrapper1 = tk.LabelFrame(self.window1, text = "Simulacion")
        self.wrapper2 = tk.LabelFrame(self.window1, text = "Ver Valores")
        
        self.labelValueStart = tk.Label(self.wrapper, text = "Seleccione Opcion de Simualacion")
        optionSimulation = ("Seleccione la Opcion de Simualacion", "Simulacion por Amortizacion", "Simulacion por Capitalizacion")
        self.listOptions = ttk.Combobox(self.wrapper, width = 33, values = optionSimulation)
        self.listOptions.current(0)
        
        #Formulas para la creacion de interfaz Grafica
        # Label and Entry form N periodos
        self.Nperiodos = tk.Label(self.wrapper, text = "Ingrese el numero de Periodos: ")
        self.EntryNperiodos = tk.Entry(self.wrapper, width = 35, bd = 5)
        
        # Label and entry form Value Cuota
        self.valorCuota = tk.Label(self.wrapper, text = "Ingrese el Valor de la Cuota: ")
        self.EntryvalorCuota = tk.Entry(self.wrapper, width = 35, bd = 5)
        
        # Label and entry form Value present
        self.valorPresnete = tk.Label(self.wrapper, text = "Ingrese el Valor presente: ")
        self.EntryValorPresente = tk.Entry(self.wrapper, width = 35, bd = 5)
        
        # Label and entry form Tasa Interes
        self.tasaInteres = tk.Label(self.wrapper, text = "Ingrese el valor de la tasa de Interes: ")
        self.EntryTasaInteres = tk.Entry(self.wrapper, width = 35, bd = 5)
        
        # Button  Simulation
        self.calcular = tk.Button(self.wrapper, text = "Generar Simulacion")
        self.atras = tk.Button(self.wrapper, text = "Cerrar")
        # Posicition and Config dimension LabelFrame
        self.wrapper.pack(padx = 10, pady = 5, fill = "both")
        self.wrapper1.pack(padx = 10, pady = 10, fill = "both", expand = "yes")
        self.wrapper2.pack(padx = 10, pady = 5, fill = "both", expand = "yes")
        
        # Grid Defination 
        
        # Grid Position label for form 
        self.labelValueStart.grid(column = 0, row = 0)
        self.Nperiodos.grid(column = 0 , row = 1)
        self.valorCuota.grid(column = 0 , row = 2)
        self.valorPresnete.grid(column = 0, row = 3)
        self.tasaInteres.grid(column = 0, row = 4)
        
        # Grid Position Entry for form
        self.listOptions.grid(column = 1, row = 0, padx = 10, pady = 5)
        self.EntryNperiodos.grid(column = 1, row = 1 , padx = 3, pady = 5)
        self.EntryvalorCuota.grid(column = 1, row = 2, padx = 3, pady = 5)
        self.EntryValorPresente.grid(column = 1, row = 3, padx = 3, pady = 5)
        self.EntryTasaInteres.grid(column = 1, row = 4, padx = 3, pady = 5)
        
        # Grid position button
        self.calcular.grid(column = 0, row = 5 ,padx = 3, pady = 5)
        self.atras.grid(column = 1, row = 5, padx = 3, pady = 5)
        
        self.window1.mainloop()
        
        
aplication = Aplication()


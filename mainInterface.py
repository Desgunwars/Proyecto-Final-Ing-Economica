import tkinter as tk
from tkinter import ttk

from alerta import Alert
from LogicaAmortizacion import TableAmortizacion
from LogicaCapitalizacion import TablaCapitalizacion
from valorPresente import ValorPresente
from valorFinal import ValorFinal
from tasaInteres import TasaInteres
from numeroPeriodos import NumeroPeriodos
from vpAnualidadV import VpAnualidadV
from vfAnualidadV import VfAnualidadV
from inAnualidadV import InAnualidadV
from gcreciente import GradienteCreciente
from gdecreciente import GradienteDecreciente

class Aplication():

    def __init__(self):
        super().__init__()
        # Config Main Window GUI
        self.window1 = tk.Tk()
        self.window1.title("Ingenieria economica")
        self.window1.geometry('680x615')
        self.window1.resizable(0,0) 
        self.window1.eval('tk::PlaceWindow . center')
        
        self.wrapper = tk.LabelFrame(self.window1, text = "Opciones de Simulacion")
        self.wrapper1 = tk.LabelFrame(self.window1, text = "Simulacion")
        self.wrapper2 = tk.LabelFrame(self.window1, text = "Calculos Adicionales")
        
        # Combobox 
        self.labelValueStart = tk.Label(self.wrapper, text = "Seleccione Opcion de Simualacion")        
        self.list = ["Seleccione la Opcion de Simualacion", "Simulacion por Amortizacion", "Simulacion por Capitalizacion"]
        self.Cliketd = tk.StringVar()
        self.Cliketd.set(self.list[0])
        self.menuoption = tk.OptionMenu(self.wrapper, self.Cliketd, *self.list, command = self.opcionMenu)
        
        
        self.plazo = tk.StringVar()
        self.cuota = tk.StringVar()
        self.tasa = tk.StringVar()
        
        #Formulas para la creacion de interfaz Grafica
        # Label and Entry form N periodos
        self.Nperiodos = tk.Label(self.wrapper, text = "Ingrese el numero de Periodos: ")
        self.EntryNperiodos = tk.Entry(self.wrapper, width = 35, bd = 5, state = "disabled", textvariable = self.plazo)
        
        # Label and entry form Value Cuota
        self.valorCuota = tk.Label(self.wrapper, text = "Ingrese el Valor de la Cuota: ")
        self.EntryvalorCuota = tk.Entry(self.wrapper, width = 35, bd = 5, state = "disabled", textvariable = self.cuota)
        
        # Label and entry form Tasa Interes
        self.tasaInteres = tk.Label(self.wrapper, text = "Ingrese el valor de la tasa de Interes: ")
        self.EntryTasaInteres = tk.Entry(self.wrapper, width = 35, bd = 5, state = "disabled", textvariable = self.tasa)
        
        # Button  Simulation
        self.calcular = tk.Button(self.wrapper, text = "Generar Simulacion", state = "disabled" ,command = self.decidir)
        self.atras = tk.Button(self.wrapper, text = "Cerrar" ,command = self.cancelar)
        
        # Format tabl
        self.tableColumn = ["n", "Cuota", "Interes", "Acumulado", "Saldo"]
        self.table = ttk.Treeview(self.wrapper1, columns = self.tableColumn, show = "headings", height =10)
        self.table.heading("n", text = "n", anchor = "center")
        self.table.heading("Cuota", text = "Cuota", anchor = "center")
        self.table.heading("Interes", text = "Interes", anchor = "center")
        self.table.heading("Acumulado", text = "Acumulado", anchor = "center")
        self.table.heading("Saldo", text = "Saldo", anchor = "center")
        
        # Tamaño de las columnas
        self.table.column("n", width = "100", stretch = False)
        self.table.column("Cuota", width = "130",  stretch = False)
        self.table.column("Interes", width = "130",  stretch = False)
        self.table.column("Acumulado", width = "130",  stretch = False)
        self.table.column("Saldo", width = "130", stretch = False)
        
        # Ver Valores Finales
        self.valorPresente = tk.Button(self.wrapper2, text = "> Calcular Valor Presente" , width = 20, command = self.callValorPresente)
        self.valorFinal = tk.Button(self.wrapper2, text = "> Calcular Valor Final", width = 20, command = self.callValorFinal)
        self.Caltasa = tk.Button(self.wrapper2, text = "> Calcular Tasa de Interes", width = 20, command = self.callTasaInteres)
        self.numeroPeriodos = tk.Button(self.wrapper2, text = "> Calcular Numero de Periodos", width = 25, command = self.callNperiodos)
        self.vpresenteAnualidadV = tk.Button(self.wrapper2, text = "> Calcular Valor Presente Anualidad Vencida", width = 35, justify = "center", command = self.callVpAnualidadV)
        self.vfinalAnualidadV = tk.Button(self.wrapper2, text = "> Calcular Valor Final Anualidad Vencida", width = 35,  justify = "left", command = self.callVfAnualidadV)
        self.interesGAnualidad = tk.Button(self.wrapper2, text = "> Calcular Anualidad Vencida Interes Global", width = 35, command = self.callAnualidadVIn)
        self.GCreciente = tk.Button(self.wrapper2, text = "> Calcular con Gradiente Creciente", width = 30, command = self.callGCreciente)
        self.GDecreciente = tk.Button(self.wrapper2, text = "> Calcular con Gradiente Decreciente", width = 30, command = self.callGDecreciente)

        # Posicition and Config dimension LabelFrame
        self.wrapper.pack(padx = 10, pady = 5, fill = "both")
        self.wrapper1.pack(padx = 10, pady = 5, fill = "both")
        self.wrapper2.pack(padx = 10, pady = 3, fill = "both")
        
        # Grid Defination 
        # Grid Position label for form 
        self.labelValueStart.grid(column = 0, row = 0)
        self.Nperiodos.grid(column = 0 , row = 1)
        self.valorCuota.grid(column = 0 , row = 2)
        self.tasaInteres.grid(column = 0, row = 4)
        
        # Grid Position Entry for form
        self.menuoption.grid(column = 1, row = 0, padx = 10, pady = 5 )
        self.EntryNperiodos.grid(column = 1, row = 1 , padx = 3, pady = 5)
        self.EntryvalorCuota.grid(column = 1, row = 2, padx = 3, pady = 5)
        self.EntryTasaInteres.grid(column = 1, row = 4, padx = 3, pady = 5)
        
        # Grid position button
        self.calcular.grid(column = 0, row = 5 ,padx = 3, pady = 5)
        self.atras.grid(column = 1, row = 5, padx = 3, pady = 5)
        self.valorPresente.grid(column = 0, row =6, padx = 5, pady = 5)
        self.valorFinal.grid(column = 0, row = 7, padx = 5, pady = 5)
        self.Caltasa.grid(column = 0, row = 8, padx = 5, pady = 5)
        self.numeroPeriodos.grid(column = 2, row = 6, padx = 5, pady = 5)
        self.vpresenteAnualidadV.grid(column = 1, row = 8, padx = 5, pady = 5)
        self.vfinalAnualidadV.grid(column = 1, row = 7, padx = 5, pady = 5)
        self.interesGAnualidad.grid(column = 1, row = 6, padx = 5, pady = 5)
        self.GCreciente.grid(column = 2, row = 7, padx = 5, pady = 5)
        self.GDecreciente.grid(column = 2, row = 8, padx = 5, pady = 5)
        
        # Grid Position Formad table
        self.table.grid(column =0 , columnspan = 2,row = 6, padx = 5, pady = 5)
        
        self.window1.mainloop()
    # Valida que la persona seleccionara alguna de las opciones de capitalizacio    
    def opcionMenu(self,*args):
        if self.Cliketd.get() == "Seleccione la Opcion de Simualacion":
            self.EntryNperiodos.config(state = 'disabled')
            self.EntryvalorCuota.config(state = 'disabled')
            self.EntryTasaInteres.config(state = 'disabled')
            self.calcular.config(state = 'disabled')
        else:
            self.EntryNperiodos.config(state = 'normal')
            self.EntryvalorCuota.config(state = 'normal')
            self.EntryTasaInteres.config(state = 'normal')
            self.calcular.config(state = 'normal')
            # Valia la Opcion de Simulacion, para cambiar el contanido del label
            if self.Cliketd.get() == "Simulacion por Capitalizacion":
                self.valorCuota['text'] = "Ingrese el Valor Final: "
            else:
                self.valorCuota['text'] = "Ingrese el Valor de la Cuota: "
                
    
    # Redirecciona cual de la opciones de mulacion para llamar la funcion
    def decidir(self):
        if self.Cliketd.get() == "Simulacion por Amortizacion":
            self.generarSimulacionAmortizacion()
        elif self.Cliketd.get() == "Simulacion por Capitalizacion":
            self.generarSimulacionCapitalizacion()
    
    def cancelar(self):
        self.window1.destroy()
    
    def generarSimulacionAmortizacion(self):
        if self.EntryNperiodos.get() == "" or self.EntryvalorCuota.get() == "" or self.EntryTasaInteres == "":
            alerta = Alert()
        else:
            calculo = TableAmortizacion(self.cuota.get(), self.tasa.get(), self.plazo.get())
            lista = calculo.calcular()
            cantidad = len(lista)
            for i in range(0,cantidad):
                self.table.insert("", 'end', values = (lista[i][0], lista[i][1], lista[i][2], lista[i][3], lista[i][4]))
    
    def generarSimulacionCapitalizacion(self): 
        if self.EntryNperiodos.get() == "" or self.EntryvalorCuota.get() == "" or self.EntryTasaInteres == "":
            alerta = Alert()
        else:
            capitalizacion = TablaCapitalizacion(self.cuota.get(), self.tasa.get(), self.plazo.get())
            lista = capitalizacion.calcularCapitalizacion()
            cantidad = len(lista)
            for i in range(0,cantidad):
                self.table.insert("", 'end', values = (lista[i][0], lista[i][1], lista[i][2], lista[i][3], lista[i][4]))
    
    def callValorPresente(self):
        window = ValorPresente()
        
    
    def callValorFinal(self):
        window = ValorFinal()
        
    
    def callTasaInteres(self):
        window = TasaInteres()
        
    
    def callNperiodos(self):
        window = NumeroPeriodos()

    def callAnualidadVIn(self):
        window = InAnualidadV()

    def callVfAnualidadV(self):
        window = VfAnualidadV()
    
    def callVpAnualidadV(self):
        window = VpAnualidadV()
    
    def callGCreciente(self):
        window = GradienteCreciente()

    def callGDecreciente(self):
        window = GradienteDecreciente()

# Terminar de Programar 

    # Tiempo
    # Interes
    # Tasa de Interes
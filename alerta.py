import tkinter as tk

class Alert(object):
    def __init__(self):
        self.alert = tk.Toplevel()
        self.alert.title = "Formulario Mal Ingresado"
        self.alert.geometry("200x65")
        self.alert.resizable(0,0) 
        
        self.TextAlert = tk.Label(self.alert, text = "No deje Campos Vacios", font = ("Time New Roman", 12,"bold"))
        self.buttonAceptar = tk.Button(self.alert, text = "Aceptar" , width = 10, command = self.Cerrar)
        
        self.TextAlert.grid(column = 0, row = 0)
        self.buttonAceptar.grid(column = 0, row = 1)
        
    def Cerrar(self):
        self.alert.destroy()
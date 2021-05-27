from tkinter import *
from tkinter.ttk import Combobox
import math

ventana = Tk()


seleccionAVP = IntVar()
seleccionAVF = IntVar()



#entrys y labels para anualidad de valor presente

#calcular valor presente
txtAVPvpi = Entry(ventana)
txtAVPvpc = Entry(ventana)
txtAVPvpn = Entry(ventana)

lblAVPvpi = Label(ventana, text="Tasa")
lblAVPvpc = Label(ventana, text="Cuota")
lblAVPvpn = Label(ventana, text="Periodo")

lblresultadoAVPvp = Label(ventana)
lblresultadoAVPc = Label(ventana)
lblresultadoAVPn = Label(ventana)

#calcular cuota
txtAVPcvp = Entry(ventana)
txtAVPci = Entry(ventana)
txtAVPcn = Entry(ventana)

lblAVPcvp = Label(ventana, text="Valor Presente")
lblAVPci = Label(ventana, text="Tasa")
lblAVPcn = Label(ventana, text="Periodo")

#calcular periodo
txtAVPnvp = Entry(ventana)
txtAVPni = Entry(ventana)
txtAVPnc = Entry(ventana)

lblAVPnvp = Label(ventana, text="Valor Presente")
lblAVPni = Label(ventana, text="Tasa")
lblAVPnc = Label(ventana, text="Cuota")










#entrys y labels para anualidad de valor final

#calcular valor final
txtAVFvfi = Entry(ventana)
txtAVFvfc = Entry(ventana)
txtAVFvfn = Entry(ventana)

lblAVFvfi = Label(ventana, text="Tasa")
lblAVFvfc = Label(ventana, text="Cuota")
lblAVFvfn = Label(ventana, text="Periodo")

#calcular cuota
txtAVFcvf = Entry(ventana)
txtAVFci = Entry(ventana)
txtAVFcn = Entry(ventana)

lblAVFcvf = Label(ventana, text="Valor Final")
lblAVFci = Label(ventana, text="Tasa")
lblAVFcn = Label(ventana, text="Periodo")

#calcular periodo
txtAVFnvf = Entry(ventana)
txtAVFni = Entry(ventana)
txtAVFnc = Entry(ventana)

lblAVFnvf = Label(ventana, text="Valor Final")
lblAVFni = Label(ventana, text="Tasa")
lblAVFnc = Label(ventana, text="Cuota")


#labels readultados AVF
lblresultadoAVFvf = Label(ventana)
lblresultadoAVFc = Label(ventana)
lblresultadoAVFn = Label(ventana)


#eleccion en los radio button

def seleccionadoAVP():
    if seleccionAVP.get() == 1:
        mostrarldbtxtAVPvp()
        eliminarldbtxtAVPc()
        eliminarldbtxtAVPn()

    elif seleccionAVP.get() == 2:
        mostrarldbtxtAVPc()
        eliminarldbtxtAVPvp()
        eliminarldbtxtAVPn()

    elif seleccionAVP.get() == 3:
        mostrarldbtxtAVPn()
        eliminarldbtxtAVPvp()
        eliminarldbtxtAVPc()

def seleccionadoAVF():
    if seleccionAVF.get() == 1:
        mostrarldbtxtAVFvf()
        eliminarldbtxtAVFc()
        eliminarldbtxtAVFn()

    elif seleccionAVF.get() == 2:
        mostrarldbtxtAVFc()
        eliminarldbtxtAVFvf()
        eliminarldbtxtAVFn()

    elif seleccionAVF.get() == 3:
        mostrarldbtxtAVFn()
        eliminarldbtxtAVFvf()
        eliminarldbtxtAVFc()



def eliminarSELRBAVP():
    RbAVPSel.pack_forget()
    RbAVPvp.pack_forget()
    RbAVPc.pack_forget()
    RbAVPn.pack_forget()

def eliminarSELRBAVF():
    RbAVFSel.pack_forget()
    RbAVFvF.pack_forget()
    RbAVFc.pack_forget()
    RbAVFn.pack_forget()


#funciones entry y labels de anualidada valor presente

#valor presente
def mostrarldbtxtAVPvp():
    
    lblAVPvpi.pack()
    txtAVPvpi.pack()

    lblAVPvpc.pack()
    txtAVPvpc.pack()

    lblAVPvpn.pack()
    txtAVPvpn.pack()

    btncalcularAVPvp.pack()

    
def calcularAVPvp():
    txtAVPvpiD = float(txtAVPvpi.get())
    txtAVPvpcD = int(txtAVPvpc.get())
    txtAVPvpnD = int(txtAVPvpn.get())
    valorentreparentesis = math.pow((1+txtAVPvpiD),txtAVPvpnD)
    resultadoAVPvp = round(txtAVPvpcD*((valorentreparentesis-1)/(txtAVPvpiD*valorentreparentesis)), 2)
    lblresultadoAVPvp.config(text="El valor presente es de: $"+ str(resultadoAVPvp))
    lblresultadoAVPvp.pack()

def eliminarldbtxtAVPvp():
    
    lblAVPvpi.pack_forget()
    txtAVPvpi.pack_forget()

    lblAVPvpc.pack_forget()
    txtAVPvpc.pack_forget()

    lblAVPvpn.pack_forget()
    txtAVPvpn.pack_forget()

    txtAVPvpi.delete(0, END)
    txtAVPvpc.delete(0, END)
    txtAVPvpn.delete(0, END)
    btncalcularAVPvp.pack_forget()
    lblresultadoAVPvp.pack_forget()
    


#cuota
def mostrarldbtxtAVPc():
    
    lblAVPcvp.pack()
    txtAVPcvp.pack()

    lblAVPci.pack()
    txtAVPci.pack()

    lblAVPcn.pack()
    txtAVPcn.pack()

    btncalcularAVPc.pack()

def calcularAVPc():
    txtAVPcvpD = int(txtAVPcvp.get())
    txtAVPciD = float(txtAVPci.get())
    txtAVPcnD = int(txtAVPcn.get())
    valorentreparentesis = math.pow((1+txtAVPciD),txtAVPcnD)
    resultadoAVPc = round(txtAVPcvpD*((txtAVPciD*valorentreparentesis)/(valorentreparentesis-1)), 2)
    lblresultadoAVPc.config(text="La cuota es de: $"+ str(resultadoAVPc))
    lblresultadoAVPc.pack()

def eliminarldbtxtAVPc():
    
    lblAVPcvp.pack_forget()
    txtAVPcvp.pack_forget()

    lblAVPci.pack_forget()
    txtAVPci.pack_forget()

    lblAVPcn.pack_forget()
    txtAVPcn.pack_forget()

    btncalcularAVPc.pack_forget()
    lblresultadoAVPc.pack_forget()


#periodo

def mostrarldbtxtAVPn():
    
    lblAVPnvp.pack()
    txtAVPnvp.pack()

    lblAVPni.pack()
    txtAVPni.pack()

    lblAVPnc.pack()
    txtAVPnc.pack()

    btncalcularAVPn.pack()

def calcularAVPn():
    txtAVPnvpD = int(txtAVPnvp.get())
    txtAVPniD = float(txtAVPni.get())
    txtAVPncD = int(txtAVPnc.get())
    resultadoAVPn = round((math.log(txtAVPncD)-math.log(txtAVPncD-(txtAVPniD*txtAVPnvpD)))/math.log(1+txtAVPniD), 2)
    lblresultadoAVPn.config(text="El perido es de: "+ str(resultadoAVPn))
    lblresultadoAVPn.pack()

def eliminarldbtxtAVPn():
    
    lblAVPnvp.pack_forget()
    txtAVPnvp.pack_forget()

    lblAVPni.pack_forget()
    txtAVPni.pack_forget()

    lblAVPnc.pack_forget()
    txtAVPnc.pack_forget()

    btncalcularAVPn.pack_forget()
    lblresultadoAVPn.pack_forget()





#funciones entry y labels de anualidada valor final

#valor final
def mostrarldbtxtAVFvf():
    
    lblAVFvfi.pack()
    txtAVFvfi.pack()

    lblAVFvfc.pack()
    txtAVFvfc.pack()

    lblAVFvfn.pack()
    txtAVFvfn.pack()

    btncalcularAVFvf.pack()

def calcularAVFvf():
    txtAVFvfiD = float(txtAVFvfi.get())
    txtAVFvfcD = int(txtAVFvfc.get())
    txtAVFvfnD = int(txtAVFvfn.get())
    valorentreparentesis = math.pow((1+txtAVFvfiD),txtAVFvfnD)
    resultadoAVFvf = round(txtAVFvfcD*((valorentreparentesis-1)/txtAVFvfiD), 2)
    lblresultadoAVFvf.config(text="El valor final es de: $"+ str(resultadoAVFvf))
    lblresultadoAVFvf.pack()

def eliminarldbtxtAVFvf():
    
    lblAVFvfi.pack_forget()
    txtAVFvfi.pack_forget()

    lblAVFvfc.pack_forget()
    txtAVFvfc.pack_forget()

    lblAVFvfn.pack_forget()
    txtAVFvfn.pack_forget()

    btncalcularAVFvf.pack_forget()
    lblresultadoAVFvf.pack_forget()


#cuota
def mostrarldbtxtAVFc():
    
    lblAVFcvf.pack()
    txtAVFcvf.pack()

    lblAVFci.pack()
    txtAVFci.pack()

    lblAVFcn.pack()
    txtAVFcn.pack()

    btncalcularAVFc.pack()


def calcularAVFc():
    txtAVFcvfD = int(txtAVFcvf.get())
    txtAVFciD = float(txtAVFci.get())
    txtAVFcnD = int(txtAVFcn.get())
    valorentreparentesis = math.pow((1+txtAVFciD),txtAVFcnD )
    resultadoAVFc = round(txtAVFcvfD*txtAVFciD/(valorentreparentesis-1), 2)
    lblresultadoAVFc.config(text="La cuota es de: $"+ str(resultadoAVFc))
    lblresultadoAVFc.pack()

def eliminarldbtxtAVFc():
    
    lblAVFcvf.pack_forget()
    txtAVFcvf.pack_forget()

    lblAVFci.pack_forget()
    txtAVFci.pack_forget()

    lblAVFcn.pack_forget()
    txtAVFcn.pack_forget()

    lblresultadoAVFc.pack_forget()
    btncalcularAVFc.pack_forget()

#periodo

def mostrarldbtxtAVFn():
    
    lblAVFnvf.pack()
    txtAVFnvf.pack()

    lblAVFni.pack()
    txtAVFni.pack()

    lblAVFnc.pack()
    txtAVFnc.pack()

    btncalcularAVFn.pack()

def calcularAVFn():
    txtAVFnvfD = int(txtAVFnvf.get())
    txtAVFniD = float(txtAVFni.get())
    txtAVFncD = int(txtAVFnc.get())
    resultadoAVFn = round((math.log(txtAVFnvfD*txtAVFniD+txtAVFncD)-math.log(txtAVFncD))/math.log(1+txtAVFniD), 2)
    lblresultadoAVFn.config(text="El periodo es de: $"+ str(resultadoAVFn))
    lblresultadoAVFn.pack()

def eliminarldbtxtAVFn():
    
    lblAVFnvf.pack_forget()
    txtAVFnvf.pack_forget()

    lblAVFni.pack_forget()
    txtAVFni.pack_forget()

    lblAVFnc.pack_forget()
    txtAVFnc.pack_forget()

    lblresultadoAVFn.pack_forget()
    btncalcularAVFn.pack_forget()










#eleccion del usuario en el combobox

def escoger():
    if combo.get() == "Anualidad Valor Presente":
        RbAVPSel.pack()
        RbAVPvp.pack()
        RbAVPc.pack()
        RbAVPn.pack()

        eliminarSELRBAVF()
        eliminarldbtxtAVFvf()
        eliminarldbtxtAVFc()
        eliminarldbtxtAVFn()


    elif combo.get() == "Anualidad Valor Final":

        RbAVFSel.pack()
        RbAVFvF.pack()
        RbAVFc.pack()
        RbAVFn.pack()

        eliminarSELRBAVP()
        eliminarldbtxtAVPvp()
        eliminarldbtxtAVPc()
        eliminarldbtxtAVPn()



            
#combobo que me eligira las opciones de calculo

opciones=["Seleccione una opcion", "Anualidad Valor Presente", "Anualidad Valor Final", "Gradiente Creciente", "Gradiente Decreciente"]
lblescogercalculo=Label(ventana,text="Escoge que desea calcular")

combo=Combobox(ventana,values=opciones)
botonescogercalculo = Button(ventana, text="Escoger", command=escoger)

lblescogercalculo.pack()
combo.pack()
botonescogercalculo.pack()

#Radios button para anualidad de valor presente
RbAVPSel = Radiobutton(ventana, text="Seleccione Una opcion", variable=seleccionAVP, value=0, command=seleccionadoAVP)
RbAVPvp = Radiobutton(ventana, text="Valor Presente", variable=seleccionAVP, value=1, command=seleccionadoAVP)
RbAVPc = Radiobutton(ventana, text="Cuota", variable=seleccionAVP, value=2, command=seleccionadoAVP)
RbAVPn = Radiobutton(ventana, text="Periodo", variable=seleccionAVP, value=3, command=seleccionadoAVP)

#Radios button para anualidad de valor final
RbAVFSel = Radiobutton(ventana, text="Seleccione Una opcion", variable=seleccionAVF, value=0, command=seleccionadoAVF)
RbAVFvF = Radiobutton(ventana, text="Valor Final", variable=seleccionAVF, value=1, command=seleccionadoAVF)
RbAVFc = Radiobutton(ventana, text="Cuota", variable=seleccionAVF, value=2, command=seleccionadoAVF)
RbAVFn = Radiobutton(ventana, text="Periodo", variable=seleccionAVF, value=3, command=seleccionadoAVF)

#botones para calcular AVP
btncalcularAVPvp = Button(ventana, text="calcular", command=calcularAVPvp)
btncalcularAVPc = Button(ventana, text="calcular", command=calcularAVPc)
btncalcularAVPn= Button(ventana, text="calcular", command=calcularAVPn)

#botones para calcular AVF
btncalcularAVFvf = Button(ventana, text="calcular", command=calcularAVFvf)
btncalcularAVFc = Button(ventana, text="calcular", command=calcularAVFc)
btncalcularAVFn= Button(ventana, text="calcular", command=calcularAVFn)


ventana.geometry("800x500")
ventana.mainloop()
import numpy_financial as npf
import tabulate as tab




class TablaCapitalizacion:
    
    def __init__(self, vf, tasa, plazo):
        self.valorFinal = float(vf)
        self.tasaInteres = float(tasa)
        self.plazo = int(plazo)
        
    def calcularCapitalizacion(self):
        cuota = round(npf.pmt(self.tasaInteres/100, self.plazo, 0, -self.valorFinal), 0)
        datos = []
        saldo = 0
        
        for i in range(1, self.plazo + 1):
            pago_capital = npf.ppmt(self.tasaInteres/100, i, self.plazo, 0, -self.valorFinal)
            pago_int = cuota - pago_capital
            pago_int2 = -pago_int
            saldo += pago_capital
            linea = [i,  format(cuota, '0,.0f'), format(pago_capital, '0,.0f'), format(pago_int2, '0,.0f'),format(saldo, '0,.0f')]
            datos.append(linea)
        return datos
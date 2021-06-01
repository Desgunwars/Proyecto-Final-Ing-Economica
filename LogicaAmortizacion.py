import numpy_financial as npf
import tabulate as tab
class TableAmortizacion:
    
    def __init__(self, capital, tasa, plazo):
        self.capital =  int(capital)
        self.tasa = float(tasa)
        self.plazo = int(plazo)
        self.calcular()
    
    def calcular(self):
        cuota = round(npf.pmt(self.tasa, self.plazo, -self.capital, 0), 0)
        datos = []
        saldo = self.capital
        
        for i in range(1, self.plazo + 1):
            pago_capital = npf.ppmt(self.tasa, i, self.plazo, -self.capital,0)
            pago_int = cuota - pago_capital
            saldo -= pago_capital
            linea = [i, format(cuota, '0,.0f'), format(pago_capital, '0,.0f'), format(pago_int, '0,.0f'), format(saldo, '0,.0f')]
            datos.append(linea)
        return datos
    
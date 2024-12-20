from ElegirMercado import AgenteDeCompras
from AgenteComprador import elegirTransporte
class Main:
    def __init__(self):
        self.mapa = [
            ['c', 'l1', '0', 'l2', 'l2', 'l2', '0', '0', '0', '0', '0'],
            ['l2', 'i', 'l2', 'l2', '0', 'l2', '0', '0', '0', '0', 'm1'],
            ['0', 'l1', '0', '0', '0', 'l2', '0', '0', 'l4', 'l4', 'l4'],
            ['0', 'l1', '0', '0', '0', 'l2', '0', '0', 'l4', '0', 'l4'],
            ['0', 'l1', '0', '0', '0', 'l2', 'l2', '0', 'l4', '0', 'l4'],
            ['0', 'l1', 'l1', 'l1', '0', '0', 'l2', '0', 'l4', '0', 'l4'],
            ['0', '0', '0', 'l1', '0', 'l2', 'l2', '0', 'l4', '0', 'l4'],
            ['0', '0', '0', 'l1', 'l1', 'pl', 'l4', 'l4', 'l4', '0', 'l4'],
            ['0', '0', '0', '0', '0', 'l3', '0', '0', '0', '0', 'l4'],
            ['0', 'l3', 'l3', 'l3', 'l3', 'l3', '0', '0', '0', '0', 'l4'],
            ['0', 'l3', '0', '0', '0', '0', '0', '0', '0', '0', 'l4'],
            ['0', 'l3', 'm2', '0', '0', '0', '0', '0', 'l4', 'l4', 'l4'],
            ['0', 'l3', '0', '0', '0', '0', '0', '0', 'l4', '0', '0'],
            ['0', 'l3', 'l3', 'l3', 'l3', 'l3', 'l3', '0', 'l4', '0', '0'],
            ['0', '0', '0', '0', '0', '0', 'm3', 'l4', 'l4', '0', '0']
        ]
        
        self.mercados = [
            {'leche': 7, 'maple de huevo': 20, 'fideo': 5, 'coca cola': 14, 'panetón': 30},
            {'leche': 6, 'pan': 10, 'queso': 32, 'jamón': 15, 'cereal': 25},
            {'carne': 28, 'pollo': 20, 'mayonesa': 16, 'papa': 64, 'pan': 9}
        ]

        self.tarifas = {'l1': 1, 'l2': 2, 'l3': 2, 'l4': 3}
        self.tiempos = {'l1': 11, 'l2': 15, 'l3': 15, 'l4': 25}
        self.bolsa_vacia = {}
        self.eleccion = AgenteDeCompras(self.mercados)
        
    def ejecutar(self, lista_compras, dinero, tiempo):

        #elegir el mejor mercado
        mejor_mercado = self.eleccion.encontrar_mejor_mercado(lista_compras)
        nombre_m = mejor_mercado.nombre
        
        agente = elegirTransporte(self.mapa, self.tarifas, self.tiempos, dinero, tiempo, nombre_m, lista_compras, self.bolsa_vacia)
        agente.subir()

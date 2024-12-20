from AgenteChofer import AgenteChofer
from ElegirLineaMercado import ElegirTransporteMercado
from AgenteVendedor import AgenteVendedor
from mapa import MapaGrafico
from mapa_CBBA import MapaDinamico

class elegirTransporte:
    def __init__(self, matriz, tarifas, tiempos, dinero, tiempo, mercado_objetivo, lista_compras, bolsa):
        self.matriz = matriz
        self.tarifas = tarifas
        self.tiempos = tiempos
        self.dinero = dinero
        self.tiempo = tiempo
        self.mercado_objetivo = mercado_objetivo
        self.lista_compras = lista_compras
        self.bolsa = bolsa
        self.posicion_actual = self.encontrar_posicion_inicial()
        self.recorrido = [self.encontrar_posicion_inicial()]

    def encontrar_posicion_inicial(self):
        for i, fila in enumerate(self.matriz):
            for j, elemento in enumerate(fila):
                if elemento == 'c':
                    return (i, j)
        return None

    def elementos_alrededor_de_c(self):
        i, j = self.posicion_actual
        direcciones = [
            (i-1, j), (i+1, j),  # Arriba y abajo
            (i, j-1), (i, j+1),  # Izquierda y derecha
        ]
        elementos_alrededor = []
        for x, y in direcciones:
            if 0 <= x < len(self.matriz) and 0 <= y < len(self.matriz[0]) and self.matriz[x][y] != '0':
                elementos_alrededor.append(self.matriz[x][y])
        return elementos_alrededor

    def encontrar_mas_barato(self, elementos_alrededor, dinero_disponible, tiempo_disponible):
        if not elementos_alrededor:
            return None  # No hay elementos alrededor
        # Filtrar elementos basándonos en el dinero disponible
        elementos_con_dinero = [elemento for elemento in elementos_alrededor if self.tarifas.get(elemento) is not None and self.tarifas.get(elemento) <= dinero_disponible]
        if elementos_con_dinero:
            # Si hay elementos con dinero disponible, elegir el que tenga menos tiempo
            mejor_elemento = min(elementos_con_dinero, key=lambda x: self.tiempos.get(x, float('inf')))
        else:
            # Si no hay elementos con dinero disponible, elegir el más barato en dinero
            mejor_elemento = min(elementos_alrededor, key=lambda x: self.tarifas.get(x, float('inf')))
            
        return mejor_elemento

    def mover_a_mejor_elemento(self):
        elementos_alrededor = self.elementos_alrededor_de_c()
        mejor_elemento = self.encontrar_mas_barato(elementos_alrededor, self.dinero, self.tiempo)
        
        if mejor_elemento:
            i, j = self.posicion_actual
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < len(self.matriz) and 0 <= y < len(self.matriz[0]) and self.matriz[x][y] == mejor_elemento:
                    self.posicion_actual = (x, y)
                    return True
        return False

    def mover(self, lugar):
        i, j = self.posicion_actual
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < len(self.matriz) and 0 <= y < len(self.matriz[0]) and self.matriz[x][y] == lugar:
                self.posicion_actual = (x, y)

    def bajar(self, lugar):
        i, j = self.posicion_actual
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < len(self.matriz) and 0 <= y < len(self.matriz[0]) and self.matriz[x][y] == lugar:
                self.posicion_actual = (x, y)
                self.recorrido.append(self.posicion_actual)

    
    def subir(self):
        #elegir primer transporte
        elementos_alrededor = self.elementos_alrededor_de_c()
        self.mover_a_mejor_elemento()
        mejor_l = self.encontrar_mas_barato(elementos_alrededor, self.dinero, self.tiempo)
        
        agente_chofer1 = AgenteChofer(self.matriz, self.posicion_actual)
        self.recorrido.extend(agente_chofer1.encontrar_posiciones_l(mejor_l, 'pl'))
        
        self.posicion_actual = agente_chofer1.posicion_actual
        self.dinero = self.dinero-agente_chofer1.cobrar_pasaje(mejor_l)
        self.tiempo = self.tiempo-agente_chofer1.tiempo_viaje(mejor_l, 'pl')
        
        #elegir transporte para ir a mercado
        lineasM = ElegirTransporteMercado(self.matriz)
        linea_a_mercado = lineasM.elementos_alrededor_de_mercado(self.mercado_objetivo)       
        mejor_l = self.encontrar_mas_barato(linea_a_mercado, self.dinero, self.tiempo)
        self.mover(mejor_l)
        agente_chofer2 = AgenteChofer(self.matriz, self.posicion_actual)
        self.recorrido.extend(agente_chofer2.encontrar_posiciones_l(mejor_l, self.mercado_objetivo))
        
        self.posicion_actual = agente_chofer2.posicion_actual
        self.dinero = self.dinero-agente_chofer2.cobrar_pasaje(mejor_l)
        self.tiempo = self.tiempo-agente_chofer2.tiempo_viaje(mejor_l, self.mercado_objetivo)
        
        if self.mercado_objetivo == 'm2' or self.mercado_objetivo == 'm1':
            vuelta = agente_chofer2.encontrar_posiciones_l(mejor_l, self.mercado_objetivo)
            vuelta.pop()
            vuelta1 = vuelta[::-1]
        
        #comprar productos
        agente_vendedor = AgenteVendedor(self.mercado_objetivo)
        total_pagado = agente_vendedor.vender(self.lista_compras, self.bolsa)
        self.dinero = self.dinero-total_pagado
        self.tiempo = self.tiempo-agente_vendedor.tiempo_venta()
        
        #volver del mercado a la pl
        agente_chofer1 = AgenteChofer(self.matriz, self.posicion_actual)
        if self.mercado_objetivo == 'm2' or self.mercado_objetivo == 'm1':
            self.recorrido.extend(vuelta1)
            self.posicion_actual = self.recorrido[-1]
            self.bajar('pl')
            self.dinero = self.dinero-agente_chofer1.cobrar_pasaje(mejor_l)
            self.tiempo = self.tiempo-agente_chofer1.tiempo_viaje(mejor_l, self.mercado_objetivo)
        else:
            elementos_alrededor = self.elementos_alrededor_de_c()
            self.mover_a_mejor_elemento()
            mejor_l = self.encontrar_mas_barato(elementos_alrededor, self.dinero, self.tiempo)
            self.recorrido.extend(agente_chofer1.encontrar_posiciones_l(mejor_l, 'pl'))
            self.posicion_actual = agente_chofer1.posicion_actual
            self.dinero = self.dinero-agente_chofer1.cobrar_pasaje(mejor_l)
            self.tiempo = self.tiempo-agente_chofer1.tiempo_viaje(mejor_l, 'pl')

        
        #volver a casa
        elementos_alrededor = self.elementos_alrededor_de_c()
        self.mover_a_mejor_elemento()
        mejor_l = self.encontrar_mas_barato(elementos_alrededor, self.dinero, self.tiempo)
        
        agente_chofer1 = AgenteChofer(self.matriz, self.posicion_actual)
        self.recorrido.extend(agente_chofer1.encontrar_posiciones_l(mejor_l, 'c'))
        
        self.posicion_actual = agente_chofer1.posicion_actual
        self.dinero = self.dinero-agente_chofer1.cobrar_pasaje(mejor_l)
        self.tiempo = self.tiempo-agente_chofer1.tiempo_viaje(mejor_l, 'c')

        #resultados del agente
        print(f"posicion final {self.posicion_actual}")
        print("recorrido total")
        print(self.recorrido)
        if self.dinero < 0:
            print(f"falto dinero {self.dinero}")
        else:
            print(f"dinero sobrante {self.dinero}")
        if self.tiempo < 0:
            print(f"falto tiempo {self.tiempo}")
        else:
            print(f"tiempo sobrante {self.tiempo}")

        #Usamos la primera versiòn para mostrar el mapa
        mapa_grafico = MapaGrafico(self.matriz)
        mapa_grafico.graficar_mapa(self.recorrido)

        #Usamos la segun versiòn para mostrar el mapa
        mapa_dinamico = MapaDinamico(self.recorrido,self.matriz)
        mapa_dinamico.run()
        



class AgenteChofer:
    def __init__(self, mapa, posicion_inicial):
        self.mapa = mapa
        self.posicion_actual = posicion_inicial
        self.lineas_visitadas = set()
        self.posiciones_l = [posicion_inicial]

    def encontrar_posiciones_l(self, linea, destino):
        cambios = True
        while cambios:
            cambios = False

            i, j = self.posicion_actual

            direcciones = [
                (i-1, j), (i+1, j),  # Arriba y abajo
                (i, j-1), (i, j+1),  # Izquierda y derecha
            ]

            # Verificar las direcciones adyacentes y agregarlas a la lista si cumplen con la condición
            for x, y in direcciones:
                if 0 <= x < len(self.mapa) and 0 <= y < len(self.mapa[0]) and (self.mapa[x][y] == linea or self.mapa[x][y] == 'i'):
                    nueva_posicion = (x, y)
                    if nueva_posicion not in self.posiciones_l:
                        self.posiciones_l.append(nueva_posicion)
                        self.posicion_actual = nueva_posicion
                        cambios = True
            elementos_alrededor = self.elementos_alrededor_de_c(linea)
            if destino in elementos_alrededor:
                break

        # Agregar la dirección del destino a la lista después de salir del bucle
        i_destino, j_destino = self.encontrar_posicion_destino(destino)
        if (i_destino, j_destino) not in self.posiciones_l:
            self.posiciones_l.append((i_destino, j_destino))
            self.posicion_actual = (i_destino, j_destino)

        return self.posiciones_l

    def elementos_alrededor_de_c(self, linea):
        i, j = self.posicion_actual

        direcciones = [
            (i-1, j), (i+1, j),  # Arriba y abajo
            (i, j-1), (i, j+1),  # Izquierda y derecha
        ]

        elementos_alrededor = []
        for x, y in direcciones:
            if 0 <= x < len(self.mapa) and 0 <= y < len(self.mapa[0]) and self.mapa[x][y] != linea and self.mapa[x][y] != '0':
                elementos_alrededor.append(self.mapa[x][y])

        return elementos_alrededor

    def encontrar_posicion_destino(self, destino):
        for i, fila in enumerate(self.mapa):
            for j, elemento in enumerate(fila):
                if elemento == destino:
                    return i, j
        return None, None
    
    def cobrar_pasaje(self, linea):
        monto = 0
        if linea == 'l1':
            monto = 1
        elif linea == 'l2':
            monto = 2
        elif linea == 'l3':
            monto = 2
        elif linea == 'l4':
            monto = 3
        return monto

    def tiempo_viaje(self, linea, destino):
        tiempo = 0
        if linea == 'l1':
            tiempo = 11
        elif linea == 'l2':
            tiempo = 15
        elif linea == 'l3' and destino == 'm2':
            tiempo = 8
        elif linea == 'l3':
            tiempo = 15
        elif linea == 'l4' and destino == 'm1':
            tiempo = 10
        elif linea == 'l4':
            tiempo = 25
        return tiempo

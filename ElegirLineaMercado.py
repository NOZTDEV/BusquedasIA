class ElegirTransporteMercado:
    def __init__(self, mapa):
        self.mapa = mapa
        self.posicion_actual = None

    def elementos_alrededor_de_mercado(self, mercado):
        i, j = self.encontrar_posicion(mercado)

        if i is None or j is None:
            return None  # Mercado no encontrado en la matriz

        direcciones = [
            (i-1, j), (i+1, j),  # Arriba y abajo
            (i, j-1), (i, j+1),  # Izquierda y derecha
        ]

        elementos_alrededor = []
        for x, y in direcciones:
            if 0 <= x < len(self.mapa) and 0 <= y < len(self.mapa[0]) and self.mapa[x][y] != '0':
                elementos_alrededor.append(self.mapa[x][y])

        return elementos_alrededor

    def encontrar_posicion(self, elemento):
        for i, fila in enumerate(self.mapa):
            for j, valor in enumerate(fila):
                if valor == elemento:
                    return i, j
        return None, None

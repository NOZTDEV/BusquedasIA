import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

class MapaGrafico:
    def __init__(self, mapa):
        self.mapa = mapa
        self.colores = {
            '0': 'grey',
            'c': 'cyan',
            'i': 'orange',
            'pl': 'purple',
            'm1': 'red',
            'm2': 'white',
            'm3': 'blue',
            'l1': 'green',
            'l2': 'yellow',
            'l3': 'brown',
            'l4': 'pink'
        }
        self.img_casa = "./imagen/casaimg.png"
        self.img_mercado = "./imagen/mercadoimg.png"
        self.img_pl = "./imagen/plimg.png"
        self.img_punto = "./imagen/puntoimg.png"

    def graficar_mapa(self, posiciones):
        num_filas, num_columnas = len(self.mapa), len(self.mapa[0])

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))  # Crear una figura con dos subgráficos

        for posicion in posiciones:
            ax1.clear()  # Limpia el subgráfico del mapa
            for j in range(num_columnas):
                for i in range(num_filas):
                    valor = self.mapa[i][j]
                    color = self.colores.get(valor, 'black')
                    ax1.fill_between([j, j + 1], num_filas - i - 1, num_filas - i, color=color)

                    # Agregar imagen si es diferente de '0'
                    if valor == '0' or valor == 'c':
                        self.agregar_imagen(ax1, j + 0.5, num_filas - i - 0.5, self.img_casa)
                    elif valor.startswith('m'):
                        self.agregar_imagen(ax1, j + 0.5, num_filas - i - 0.5, self.img_mercado)
                    elif valor == 'pl':
                        self.agregar_imagen(ax1, j + 0.5, num_filas - i - 0.5, self.img_pl)

            # Agregar la imagen del punto encima de las demás
            y, x = posicion
            self.agregar_imagen(ax1, x + 0.5, num_filas - y - 0.5, self.img_punto)

            # Configurar ejes para el subgráfico del mapa
            ax1.invert_yaxis()
            ax1.set_title('Mapa')

            # Agregar mensajes en consola al subgráfico de mensajes
            mensajes = self.obtener_mensaje(posicion)
            ax2.clear()  # Limpia el subgráfico de mensajes
            ax2.text(0.1, 0.5, mensajes, fontsize=10, ha='left', va='center')
            ax2.axis('off')  # Desactivar ejes en el subgráfico de mensajes

            plt.pause(0.1)  # velocidad de ejecucion

    def agregar_imagen(self, ax, x, y, imagen_path):
        imagen = plt.imread(imagen_path)
        imagebox = OffsetImage(imagen, zoom=0.05) #tamaño de imagen
        ab = AnnotationBbox(imagebox, (x, y), frameon=False, pad=0)
        ax.add_artist(ab)

    def obtener_mensaje(self, posicion):
        x, y = posicion
        if posicion == (0, 0):
            return f"Posición actual: {posicion} en casa"
        elif posicion == (7, 5):
            return f"Posición actual: {posicion} realizando transbordo"
        elif posicion == (11, 2):
            return f"Posición actual: {posicion} comprando en m1"
        elif posicion == (1, 10):
            return f"Posición actual: {posicion} comprando en m2"
        elif posicion == (14, 6):
            return f"Posición actual: {posicion} comprando en m3"
        else:
            return f"Posición actual: {posicion}"

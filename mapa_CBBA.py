import pygame
import sys

class MapaDinamico:
    def __init__(self, lista_posiciones, matriz):
        pygame.init()

        # Tamaño de la ventana
        self.ventana_ancho = 640
        self.ventana_alto = 690

        # Colores
        self.blanco = (255, 255, 255)
        self.negro = (0, 0, 0)

        # Crear la ventana
        self.ventana = pygame.display.set_mode((self.ventana_ancho, self.ventana_alto))
        pygame.display.set_caption("Mapa Dinámico")

        # Cargar la imagen del mapa
        self.mapa_imagen = pygame.image.load("./imagen/mapa_CBBA.png")
        self.mapa_imagen = pygame.transform.scale(self.mapa_imagen, (self.ventana_ancho, self.ventana_alto))

        # Puntero
        self.puntero_imagen = pygame.image.load("./imagen/navegacion.png")
        self.puntero_imagen = pygame.transform.scale(self.puntero_imagen, (30, 30))
        self.puntero_posicion = [self.ventana_ancho // 2, self.ventana_alto // 2]

        # Matriz recorrido
        self.matriz_recorrido = matriz

        # Lista de posiciones para el recorrido
        self.lista_posiciones = lista_posiciones
        self.indice_posicion_actual = 0

        # Lista para almacenar la trayectoria
        self.trayectoria = []

    def dibujar_matriz(self):
        for fila in range(len(self.matriz_recorrido)):
            for columna in range(len(self.matriz_recorrido[0])):
                if self.matriz_recorrido[fila][columna] == 1:
                    pygame.draw.rect(self.ventana, self.negro, (columna * 50, fila * 50, 50, 50))

    def dibujar_trayectoria(self):
        for punto in self.trayectoria:
            pygame.draw.circle(self.ventana, self.negro, ((punto[1]+0.045) * 50 + 25, (punto[0]+0.5) * 50 + 25), 5)

    def run(self):
        # Bucle principal
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Lógica de movimiento del puntero
            if self.indice_posicion_actual < len(self.lista_posiciones):
                # Obtener la posición actual de la lista
                posicion_actual = self.lista_posiciones[self.indice_posicion_actual]

                # Calcular la posición en píxeles
                self.puntero_posicion[0] = (posicion_actual[1]) * 50 + 25  # Columna * Tamaño de celda + Desplazamiento en X
                self.puntero_posicion[1] = posicion_actual[0] * 50 + 25  # Fila * Tamaño de celda + Desplazamiento en Y

                # Agregar la posición a la trayectoria
                self.trayectoria.append(posicion_actual)

                # Incrementar el índice para la próxima iteración
                self.indice_posicion_actual += 1

            # Limpiar la pantalla
            self.ventana.fill(self.blanco)

            # Dibujar el mapa
            self.ventana.blit(self.mapa_imagen, (0, 0))

            # Dibujar la matriz de recorrido
            self.dibujar_matriz()

            # Dibujar la trayectoria
            self.dibujar_trayectoria()

            # Dibujar el puntero
            self.ventana.blit(self.puntero_imagen, self.puntero_posicion)

            # Actualizar la pantalla
            pygame.display.flip()

            # Controlar la velocidad de actualización
            pygame.time.Clock().tick(2)  # Puedes ajustar la velocidad según tus necesidades

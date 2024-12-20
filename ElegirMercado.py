class Mercado:
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def calcular_costo_total(self, lista_compras):
        costo_total = 0
        for producto, cantidad in lista_compras.items():
            if producto in self.productos:
                costo_total += self.productos[producto] * cantidad
            else:
                return float('inf')  # Producto no disponible en este mercado
        return costo_total

class AgenteDeCompras:
    def __init__(self, mercados):
        self.mercados = [Mercado(f"m{i+1}", productos) for i, productos in enumerate(mercados)]

    def encontrar_mejor_mercado(self, lista_compras):
        mejor_precio = float('inf')
        mejor_mercado = None

        for mercado in self.mercados:
            precio_total = mercado.calcular_costo_total(lista_compras)
            if precio_total < mejor_precio:
                mejor_precio = precio_total
                mejor_mercado = mercado

        return mejor_mercado

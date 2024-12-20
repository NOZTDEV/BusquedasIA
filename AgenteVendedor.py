class AgenteVendedor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario1 = {'leche': 7, 'maple de huevo': 20, 'fideo': 5, 'coca cola': 14, 'panetón': 30}
        self.inventario2 = {'leche': 6, 'pan': 10, 'queso': 32, 'jamón': 15, 'cereal': 25}
        self.inventario3 = {'carne': 28, 'pollo': 20, 'mayonesa': 16, 'papa': 64, 'pan': 9}
        if nombre == 'm1':
            self.inventario = self.inventario1
        elif nombre == 'm2':
            self.inventario = self.inventario2
        elif nombre == 'm3':
            self.inventario = self.inventario3

    def vender(self, lista_de_compras, bolsa):
        total_a_pagar = 0

        for producto, cantidad in lista_de_compras.items():
            if producto in self.inventario:
                precio_unitario = self.inventario[producto]
                total_a_pagar += precio_unitario * cantidad
                bolsa[producto] = cantidad
        return total_a_pagar

    def tiempo_venta(self):
        tiempo = 0
        if self.nombre == 'm1':
            tiempo = 10
        elif self.nombre == 'm2':
            tiempo = 8
        elif self.nombre == 'm3':
            tiempo = 15
        return tiempo

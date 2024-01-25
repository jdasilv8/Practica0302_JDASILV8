class Producto:
    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
    
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor

    @property
    def nombre(self):
        return self.__nombre

    @codigo.setter
    def nombre(self, valor):
        self.__nombre = valor
        
    @property
    def precio(self):
        return self.__precio

    @codigo.setter
    def precio(self, valor):
        self.__precio = valor

    def calcular_total(self, unidades):
        total = self.__precio * unidades
        return str(total)

    def __str__(self):
        return 'Codigo: ' + str(self.__codigo) + ', nombre: ' + str(self.__nombre) + ', precio: ' + str(self.__precio) + '€'
    
class Pedido:
    def __init__(self, producto, cantidades):
        self.__productos = producto
        self.__cantidades = cantidades

    def total_pedido(self):
        total = 0

        for (p, c) in zip(self.__productos, self.__cantidades):
            total = int(total) + int(p.calcular_total(c))

        return total

    def mostrar_pedido(self):
        for (p, c) in zip(self.__productos, self.__cantidades):
            print ('Producto: ' + str(p.nombre) + ', Cantidad: ' + str(c))


p1= Producto(1, 'Huevos', 10)
p2= Producto(2, 'Zumo naranja', 7)
p3= Producto(3, 'Pechugas', 50)
'''
print(p1)
print(p2)
print(p3)
'''
productos = [p1, p2, p3]
cantidades = [7, 5, 2]

pedido = Pedido(productos, cantidades)

print ('Total del pedido: ' + str(pedido.total_pedido()))

pedido.mostrar_pedido()
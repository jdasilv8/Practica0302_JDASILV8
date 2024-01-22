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
        return str(total) + '€'

    def __str__(self):
        return 'Codigo: ' + str(self.__codigo) + ', nombre: ' + str(self.__nombre) + ', precio: ' + str(self.__precio) + '€'
    
p1= Producto(1, 'Huevos', 10)
p2= Producto(2, 'Zumo naranja', 7)
p3= Producto(3, 'Pechugas', 50)

print(p1)
print(p2)
print(p3)

print(p1.calcular_total(5))
print(p2.calcular_total(15))
print(p3.calcular_total(3))
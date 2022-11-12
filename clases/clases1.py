from math import pi


class Circulo(object):

    def __init__(self, rad):
        if rad <= 0:
            raise ValueError("El radio debe ser mayor a 0.")
        self._radio = rad
        
    def __str__(self):
        return f"EL radio es de: {self._radio}, {circulo.area()} y {circulo.perimetro()}"

    def __mul__(self, new):
        if new <= 0:
            raise ValueError("El multiplicador debe ser mayor a '0'")
        n_radio = self._radio * new
        return  f"El nuevo radio multiplicado por {new} es: {n_radio}"
    

    def radio(self):
        return self._radio


    def area(self):
        area = (pi * self._radio ** 2)
        return f"El area es de: {area}"


    def perimetro(self):
        perimetro = (2 * self._radio * pi)
        return f"El perimetro es de: {perimetro}"




circulo = Circulo(16)

print(circulo)
print(circulo * 2)
print(circulo.area())
print(circulo.perimetro())
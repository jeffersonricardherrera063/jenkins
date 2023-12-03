import app
import math


class InvalidPermissions(Exception):
    pass


class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def substract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        if x < 0:
            raise TypeError("No es posible calcular la potencia de un número menor a cero")
        if x == 0 and y <= 0:
            raise TypeError("No es posible calcular la potencia con un exponente menor o igual a cero cuando la base es cero")
        return x ** y

    def logaritmo(self, x):
        self.check_types(x, 0)
        if x <= 0:
            raise TypeError("No es posible calcular el logaritmo en base 10 de un número menor o igual a cero")
        return math.log10(x)

    def raiz_cuadrada(self, x):
        self.check_types(x, 0)
        if x < 0:
            raise TypeError("No es posible calcular la raiz cuadrada de un número menor a cero")
        return math.sqrt(x)

    def factorial(self, x):
        self.check_types(x, 0)
        if x <= 0:
            raise TypeError("No es posible calcular el factorial de un número menor o igual cero")
        return math.factorial(x)

    def seno(self, x):
        return math.sin(self.radianes(x))

    def coseno(self, x):
        return math.cos(self.radianes(x))

    def tangente(self, x):
        return math.tan(self.radianes(x))

    def radianes(self,angulo):
        self.check_types(angulo, 0)
        return angulo * (math.pi / 180)

    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.seno(-1)
    print(result)

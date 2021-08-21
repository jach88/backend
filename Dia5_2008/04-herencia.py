class Vehiculo:
    def __init__(self,marca,modelo,numero_ruedas):
        """Documentacion del constructor de la clase padre"""
        self.marca = marca
        self.modelo = modelo
        self.numero_ruedas = numero_ruedas

    def acelerar(self):
        print("El auto esta acelerando 🚗")
    
    def estado(self):
        return f"Marca: {self.marca} \nModelo: {self.modelo} \nRuedas:{self.numero_ruedas} "

class Auto(Vehiculo):
    def __init__(self, sunroof, marca, modelo):
        self.sunroof = sunroof
        super().__init__(marca, modelo, 4)
    
    def estado(self):
        resultado_padre = super().estado()
        return resultado_padre +f"\nSuroof: {self.sunroof}"

class Camion(Vehiculo):
    def __init__(self, numero_cambios,marca, modelo):
        self.numero_cambios = numero_cambios    
        super().__init__(marca, modelo, 8)
    

class camion(Vehiculo):
    def __init__(self, numero_cambios, marca, modelo):
        self.numero_cambios = numero_cambios
        super().__init__(marca, modelo,8)

objAuto = Auto(True, "Chevrolet","Alto")
print(objAuto.marca)
print(objAuto.estado())

objCamion = Camion(7, "Scania", "F100")
print(objCamion.estado())

#en python el polimorfismo no funciona de la misma manera que los otros lenguajes

        
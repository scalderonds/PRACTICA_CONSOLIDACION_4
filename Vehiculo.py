# Parte 1

import csv


class Vehiculo:
    def __init__(self, marca, modelo, num_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = num_ruedas


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, num_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


class Particular(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, puestos):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.puestos = puestos


class Carga(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.carga = carga


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, tipo):
        super().__init__(marca, modelo, num_ruedas)
        self.tipo = tipo


class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, num_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, num_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios


def main():
    num_vehiculos = int(input("Cuantos Vehiculos desea insertar: "))
    vehiculos = []

    for i in range(num_vehiculos):
        print(f"Datos del automóvil {i+1}")
        marca = input("Inserte la marca del automóvil: ")
        modelo = input("Inserte el modelo: ")
        num_ruedas = int(input("Inserte el número de ruedas: "))
        velocidad = input("Inserte la velocidad en km/h: ")
        cilindrada = input("Inserte el cilindraje en cc: ")

        automovil = Automovil(marca, modelo, num_ruedas, velocidad, cilindrada)
        vehiculos.append(automovil)

    print("\nImprimiendo por pantalla los Vehículos:")
    for i, vehiculo in enumerate(vehiculos):
        print(

            f"Datos del automóvil {i+1}: Marca {vehiculo.marca}, Modelo {vehiculo.modelo}, {vehiculo.num_ruedas} ruedas, {vehiculo.velocidad} Km/h, {vehiculo.cilindrada} cc\n")


# Instancias
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta(
    "BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)


if __name__ == "__main__":
    main()

# Imprimir datos de instancias
print(f"Marca {particular.marca}, Modelo {particular.modelo}, {particular.num_ruedas} ruedas {particular.velocidad} Km/h, {particular.cilindrada} cc Puestos: {particular.puestos}")
print(f"Marca {carga.marca}, Modelo {carga.modelo}, {carga.num_ruedas} ruedas {carga.velocidad} Km/h, {carga.cilindrada} cc Carga: {carga.carga} Kg")
print(f"Marca {bicicleta.marca}, Modelo {bicicleta.modelo}, {bicicleta.num_ruedas} ruedas Tipo: {bicicleta.tipo}")
print(f"Marca {motocicleta.marca}, Modelo {motocicleta.modelo}, {motocicleta.num_ruedas} ruedas Tipo: {motocicleta.tipo} Motor: {motocicleta.motor}, Cuadro: {motocicleta.cuadro}, Nro Radios: {motocicleta.nro_radios}")


print("\nVerificar la relación que existe de la instancia motocicleta con: Vehículo, Automóvil, Particular, Carga, Bicicleta y Motocicleta:")
print("Motocicleta es instancia con relación a Vehículo:",
      isinstance(motocicleta, Vehiculo))
print("Motocicleta es instancia con relación a Automóvil:",
      isinstance(motocicleta, Automovil))
print("Motocicleta es instancia con relación a Vehículo particular:",
      isinstance(motocicleta, Particular))
print("Motocicleta es instancia con relación a Vehículo de Carga:",
      isinstance(motocicleta, Carga))
print("Motocicleta es instancia con relación a Bicicleta:",
      isinstance(motocicleta, Bicicleta))
print("Motocicleta es instancia con relación a Motocicleta:",
      isinstance(motocicleta, Motocicleta))


class VehiculoManager:
    @staticmethod
    def leer_datos_csv():
        try:
            with open("vehiculos.csv", "r") as archivo:
                archivo_csv = csv.reader(archivo)
                for vehiculo in archivo_csv:
                    clase = vehiculo[0].split("'")[1]
                    atributos = eval(vehiculo[1].strip('"'))

                    if clase == "Vehiculo.Particular":
                        print("\nLista de Vehículos Particular:")
                    elif clase == "Vehiculo.Carga":
                        print("Lista de Vehículos Carga:")
                    elif clase == "Vehiculo.Bicicleta":
                        print("Lista de Vehículos Bicicleta:")
                    elif clase == "Vehiculo.Motocicleta":
                        print("Lista de Vehículos Motocicleta:")
                    else:
                        print("Clasificación de vehículo desconocida")

                    print(atributos)

        except FileNotFoundError:
            print("Archivo no encontrado")
        except Exception as e:
            print("Ocurrió un error al leer el archivo:", str(e))


VehiculoManager.leer_datos_csv()

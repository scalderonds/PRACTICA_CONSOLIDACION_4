# Parte 3
from Vehiculo import Particular, Carga, Bicicleta, Motocicleta
import csv


def guardar(nombre_archivo, *vehiculos):
    with open(nombre_archivo, "w", newline="") as archivo:
        archivo_csv = csv.writer(archivo)
        for vehiculo in vehiculos:
            clase = str(type(vehiculo).__name__)
            atributos = str(vehiculo.__dict__).replace('"', "'")
            linea = [f"<class 'Vehiculo.{clase}'>", atributos]
            archivo_csv.writerow(linea)


def recuperar(nombre_archivo):
    vehiculos = []
    with open(nombre_archivo, "r") as archivo:
        archivo_csv = csv.reader(archivo)
        for vehiculo in archivo_csv:
            vehiculos.append(vehiculo)

    return vehiculos


particular = Particular("Ford", "Fiesta", "4", "180", "500", "5")
carga = Carga("Daft Trucks", "G 38", "10", "120", "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta(
    "BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

guardar("vehiculos.csv", particular, carga, bicicleta, motocicleta)
automoviles = recuperar("vehiculos.csv")
for automovil in automoviles:
    print(automovil)

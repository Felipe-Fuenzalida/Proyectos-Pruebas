import random, csv
from statistics import geometric_mean

trabajadores =["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
Sueldo=[]



def Azar():
    NumeroAzar=random.randint(300000,2500000)
    return NumeroAzar

def Asignar_Sueldo():
    for i in range(len(trabajadores)):
        NumeroAzar=Azar()
        Sueldo.append(NumeroAzar)

def Sueldo_Menor():
    print("="*30)
    cantidad1=0
    asd=True
    for i in range(len(trabajadores)):
        if Sueldo[i] < 800000:
            cantidad1=cantidad1+1
    for i in range(len(trabajadores)):
        if Sueldo[i] < 800000:
            while asd:
                print(f"Sueldos menores a $800.000\nTotal: {cantidad1}")
                print("Nombre empleado     Sueldo")
                asd=False
            print(f"{trabajadores[i]}{" "*(20-len(trabajadores[i]))}${Sueldo[i]}")
    print("="*30)
def Sueldo_Medio():
    print("="*30)
    cantidad2=0
    asd=True
    for i in range(len(trabajadores)):
        if Sueldo[i] >= 800000 and Sueldo[i] < 2000000:
            cantidad2=cantidad2+1
    for i in range(len(trabajadores)):
        if Sueldo[i] >= 800000 and Sueldo[i] < 2000000:
            while asd:
                print(f"Sueldos $800.000 y $2.000.000\nTotal: {cantidad2}")
                print("Nombre empleado     Sueldo")
                asd=False
            print(f"{trabajadores[i]}{" "*(20-len(trabajadores[i]))}${Sueldo[i]}")
    print("="*30)
def Sueldo_Superior():
    print("="*30)
    cantidad3=0
    asd=True
    for i in range(len(trabajadores)):
        if Sueldo[i] >= 2000000:
            cantidad3=cantidad3+1
    for i in range(len(trabajadores)):
        if Sueldo[i] >= 2000000:
            while asd:
                print(f"Sueldos superior a $2.000.000\nTotal: {cantidad3}")
                print("Nombre empleado     Sueldo")
                asd=False
            print(f"{trabajadores[i]}{" "*(20-len(trabajadores[i]))}${Sueldo[i]}")
    print("="*30)

def Estadisticas():
    temporal=0
    for i in trabajadores:
        temporal+=Sueldo[i]
        
    print(f"Sueldo mas alto: {max(Sueldo)}")
    print(f"Sueldo mas bajo: {min(Sueldo)}")
    print(f"Promedio de sueldos: {temporal/len(Sueldo)}")
    print(f"Media geometrica: {geometric_mean(Sueldo)}")

def Reporte():
    with open ('Reporte_sueldos.csv','w') as archivo:
        archivo.write("Nombre empleados || Sueldo Base || Descuento Salud || Descuento AFP || Sueldo Liquido\n")
        for i in range(len(trabajadores)):
            archivo.write(f"{trabajadores[i]} || {Sueldo[i]} || {Sueldo[i]*0.07:.2f} || {Sueldo[i]*0.12:.2f} || {(Sueldo[i]-(Sueldo[i]*0.07))-(Sueldo[i]*0.12):.2f}\n")
    
while True:
    print("1. Asignar sueldos aleatorio\n2. Clasificar sueldos\n3. Ver estadísticas.\n4. Reporte de sueldos\n5. Salir del programa")
    ops=input("Seleccione una opcion: ")
    match ops:
        case "1":
            try:
                Asignar_Sueldo()
            except:
                
                print("Faltan valores!")
        case "2":
            try:
                Sueldo_Menor()
                Sueldo_Medio()
                Sueldo_Superior()
            except:
                print("Faltan valores!")
        case "3":
            try:
                Estadisticas()
            except:
                print("Faltan valores!")
        case "4":
            try:
                Reporte()
            except:
                print("Faltan valores!")
        case "5":
            print("Finalizando programa...")
            print("Desarrollado por Felipe Fuenzalida")
            print("Rut 22.063.042-0")
            break
        case default:
            print("seleccione una opcion valida!")
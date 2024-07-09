# Solicitar el número de filas y columnas al usuario
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

# Dibujar la cuadrícula
for i in range(filas):
    for j in range(columnas):
        print("+---", end="")
    print("+")
    
    for j in range(columnas):
        print("|   ", end="")
    print("|")

# Dibuja la última fila de "+---"
for j in range(columnas):
    print("+---", end="")
print("+")
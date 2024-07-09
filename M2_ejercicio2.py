# Ingresar un número entero del 1 al 9.
num = int(input("Con qué número desea jugar: "))

# Inicializar una variable para seguir la secuencia.
i = 1

# Iniciar un bucle infinito.
while True:

    # Si i es múltiplo de num, aumentar i y continuar con la siguiente iteración.
    if i % num == 0:
        i += 1
        continue

    # Solicitar el siguiente número en la secuencia.
    val = int(input(f"Ingrese un número secuencial que no sea múltiplo de {num}: "))

    # Verificar si el número ingresado es correcto.
    if val != i:
        print(f"YOU LOSE!!!! Error en número ingresado, corresponde ingresar {i}")
        break
    
    # Aumentar i para seguir con la siguiente iteración.
    i += 1
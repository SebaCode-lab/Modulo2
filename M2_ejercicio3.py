from datetime import datetime

# Solicitar al usuario que ingrese el año de nacimiento y el año de muerte (0 si aún está vivo)
nacimiento = int(input("Ingrese el año de nacimiento: "))
muerte = int(input("Ingrese el año de muerte (0 si aún está vivo): "))

# Si el año de muerte es 0, se asume que la persona aún está viva y se usa el año actual
if muerte == 0:
    muerte = datetime.now().year

# Inicializar variables para contar años bisiestos y almacenarlos en una lista
anos_bisiestos = []

# Iterar sobre todos los años desde el nacimiento hasta la muerte (o el año actual)
for ano in range(nacimiento, muerte + 1):
    # Verificar si el año es bisiesto
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        anos_bisiestos.append(ano)

# Calcular la cantidad de años bisiestos que ha vivido la persona
anos = len(anos_bisiestos)

# Mostrar en pantalla cuántos años bisiestos ha vivido la persona y la lista de años bisiestos
print(f"La persona ha vivido {anos} años bisiestos.")
print(f"Los años bisiestos son: {anos_bisiestos}")
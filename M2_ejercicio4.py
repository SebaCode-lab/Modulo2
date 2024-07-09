# Solicitar al usuario que ingrese la primera palabra
palabra1 = input("Ingresa la primera palabra: ")

# Solicitar al usuario que ingrese la segunda palabra
palabra2 = input("Ingresa la segunda palabra: ")

# Solicitar al usuario que ingrese la frase a codificar
frase = input("Ingresa tu frase a codificar: ")

# Recorrer cada letra de la primera palabra y reemplazarla por la correspondiente de la segunda palabra en la frase
for i in range(len(palabra1)):
    letra1 = palabra1[i]
    letra2 = palabra2[i]
    frase = frase.replace(letra1, letra2)

# La frase codificada se almacena en la variable frase_codificada
frase_codificada = frase

# Mostrar la frase codificada al usuario
print(f"Tu nueva frase es: {frase_codificada}")

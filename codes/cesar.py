def cifrar_cesar(mensaje, corrimiento):
    mensaje_cifrado = ""

    for letra in mensaje:
        if letra.isalpha():  # Solo cifrar letras
            if letra.isupper():
                ascii_inicio = ord('A')
            else:
                ascii_inicio = ord('a')

            indice_original = ord(letra) - ascii_inicio
            indice_cifrado = (indice_original + corrimiento) % 26
            letra_cifrada = chr(ascii_inicio + indice_cifrado)
            mensaje_cifrado += letra_cifrada
        else:
            mensaje_cifrado += letra

    return mensaje_cifrado

mensaje_original = input("Ingrese el mensaje a cifrar: ")
corrimiento = int(input("Ingrese el valor de corrimiento: "))

mensaje_cifrado = cifrar_cesar(mensaje_original, corrimiento)
print("Mensaje cifrado:", mensaje_cifrado)

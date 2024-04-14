
def contar_vocales(mi_string):
    mi_string = mi_string.lower()
    vocales = ('a', 'á', 'e', 'é', 'i','í', 'o', 'ó', 'u' , 'ú')
    resultado = {}
    for letra in mi_string:
        # if letra in 'aeiou':
        if letra in vocales:
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] += 1
    return resultado
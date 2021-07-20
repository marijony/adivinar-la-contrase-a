import time

clave = input("Dime una contraseña de 5 caracteres: ")

alfabeto = "abcdefghijklmnñopqrstuwxyzABCDEFGHIJKLMNÑOPQRSTUWXYZ1234567890"

inicio = time.time()

for c1 in alfabeto:
    for c2 in alfabeto:
        for c3 in alfabeto:
            for c4 in alfabeto:
                for c5 in alfabeto:
                    intento = c1+c2+c3+c4+c5
                    if intento == clave:
                        print("Era muy facil tu contaseña era :", intento)
final = time.time()

print("Tiempo consumido: {:5.2f}".format(final - inicio))

#aAbBcCdDeEfFgGhHiIjJkKlLmMnNñÑoOpPqQrRsStTuUwWxXyYzZ1234567890

#ABCDEFGHIJKLMNÑOPQRSTUWXYZ

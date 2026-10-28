def factorial (n):
  resultado = 1
  for i in range(1,n + 1):
    resultado *= i
    return resultado

    print (factorial (30))

import random

numero_secreto = random.randint(1,30)
intentos = 3

print(" Adivina el numero entre 1 y 30 Tienes 3 intentos . ")

for i in range( intentos):
    intento = int(input(f"intento (i+1): "))
    if intento ==numero_secreto:
        print(" que bueno lo lograste . ")
        break

    elif intento < numero_secreto:
        print ("Muy bajo. ")
    else:
            print("Muy alto. ")
else:
    print(f" se te acabaron los intentos. El numero secreto era {numero_secreto} ") 
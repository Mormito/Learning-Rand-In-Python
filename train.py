import random
import time

contador = 0
visor = 0
threads = 5

#int(input("Insira o numero de threads: "))

while contador < threads:
    visor = random.uniform(0, 2.5)
    time.sleep(visor)
    contador = contador + 1
    print("Print | Numero " + str(contador) + " | delay = " + str(visor))
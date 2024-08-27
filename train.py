import random
import time

sum = 0.0
average = 0.0
visor = 0
threads = int(input("Insira o numero de threads: "))
print()

for contador in range(1, threads + 1):
    visor = random.uniform(0.25, 2.5)
    time.sleep(visor)
    sum += visor
    print("Print | Request Number #" + str(contador) + " | Delay = " + str(visor))
    


average = sum/threads
print("― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ―")
print("Total Time: " + str(sum))
print("Requests Average: " + str(average))
print("― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ―")
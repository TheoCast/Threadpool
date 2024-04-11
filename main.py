import threading
import time
import logging
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s') #Tiempo de ejecución de hilo por hilo, es informativo (DEBUG)


print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Dos hilos")


globalArrayNum = []
def contadorDos( inicio, fin ):
    logging.info(f'Función con rango: {inicio} - {fin}') #Cada que se ejecute un hilo muestra el rango con el que comienza y con el que finaliza
    for i in range (inicio, fin+1, 1):
        globalArrayNum.append( i )
        time.sleep(0.01)
    return 0



t0 = time.time()
listaHilos = []
t = threading.Thread(target=contadorDos, args=(1,50))
listaHilos.append(t)
t.start()
t = threading.Thread(target=contadorDos, args=(51,100))
listaHilos.append(t)
t.start()

for t in listaHilos:
    t.join()
tf = time.time()-t0

globalArrayNum.sort()
print(f"Tiempo de ejecución: {tf}")
print(globalArrayNum)


print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Pool de Hilos")

def printHW():
    logging.info(f'Función HW') #Con el logging.info te da información de que hilo está ejecutando 
    print(" Hola Mundo :) ")

globalArrayNum = []
with ThreadPoolExecutor( max_workers=2 ) as executor:
    #executor.submit(contadorDos, 1,50)
    #executor.submit(contadorDos, 51,100)
    #executor.submit(contadorDos, 101,150)
    #executor.submit(contadorDos, 151,200)
    #executor.submit(printHW)
    for i in range(1,200,50)



t0 = time.time() #Te muestra el tiempo que tarda en realizar la ejecución

globalArrayNum.sort()
print(f"Tiempo de ejecución: {tf}")
print(globalArrayNum)


#Gabriel Vicente & Pedro Arriola
#Algoritmos y estructuras de datos 10

import random
import statistics
import simpy
Cantidad_de_procesos = 25
velocidad_procesador = 3.0
Intervalation = 10
Corsair = 100
def Procc(env, RAM, velocidad_procesador, tiempo_inicio, proceso_num):    
    global Totalidad
    global Tiempo_procesando
    yield env.timeout(tiempo_inicio)
    Ingresando_SO = round(env.now,3)
    instrucciones = random.randint(1,10)
    cantidad = random.randint(1,10)
    finalizando = 0
    print("El proceso# %d ingresa al SO %s ,necesita %d de RAM y tiene %s instrucciones" % (proceso_num,Ingresando_SO,cantidad,instrucciones))
    yield RAM.get(cantidad)
    

env = simpy.Environment()
random.seed(4573)
esperando = simpy.Resource (env, capacity=2) 
CPU = simpy.Resource (env, capacity=1)        
RAM = simpy.Container(env, init = Corsair, capacity = Corsair)
         
env.run()



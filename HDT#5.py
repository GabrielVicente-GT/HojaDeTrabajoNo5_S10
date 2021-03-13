#Gabriel Vicente & Pedro Arriola
#Algoritmos y estructuras de datos 10


#Imports necesarios para que funcione el programa

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
    while finalizando < instrucciones:
        with CPU.request() as ready:
            yield ready
            print("El proceso# %d ingresa al CPU en... %s " % (proceso_num,round(env.now,3)))
            if velocidad_procesador <=(instrucciones - finalizando) : instrucciones_restantes = velocidad_procesador
            else:instrucciones_restantes = (instrucciones - finalizando)
            print("El proceso# %s tiene %d instrucciones " % (proceso_num,instrucciones_restantes))
            # Tiempo de instrucciones a ejecutar
            yield env.timeout(instrucciones_restantes/velocidad_procesador)   
            finalizando += instrucciones_restantes
            print("El proceso %s le quedan %s instrucciones" % ( proceso_num, round((instrucciones - finalizando),3)))
            print("El proceso# %d sale de; CPU en... %s " % (proceso_num,round(env.now,3))) 
        wating = random.randint(1,2)
        if (finalizando < instrucciones) and (wating == 1):
            with esperando.request() as esperandos:
                print("El proceso# %d sale de; CPU en... %s " % (proceso_num,env.now))
                yield env.timeout(1)  
                yield esperandos
    yield RAM.put(cantidad)
    Tiempo_procesando.append(env.now - Ingresando_SO)
    Totalidad += (env.now - Ingresando_SO)
    
def realizando(env, RAM, Cantidad_de_procesos,Intervalation):
    for i in range(Cantidad_de_procesos):
        tiempo_inicio = random.expovariate(1.0 / Intervalation)
        env.process(Procc(env, RAM, velocidad_procesador,tiempo_inicio, i))

env = simpy.Environment()
random.seed(4573)
esperando = simpy.Resource (env, capacity=2) 
CPU = simpy.Resource (env, capacity=1)        
RAM = simpy.Container(env, init = Corsair, capacity = Corsair)
Tiempo_procesando=[]
Totalidad = 0.0         

realizando(env, RAM, Cantidad_de_procesos,Intervalation)
env.run()



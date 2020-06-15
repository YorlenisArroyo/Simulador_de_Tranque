import simpy

def tranque(env):
    while True:
        print('Despejado %d ' % env.now)
        despejado = 3
        yield env.timeout(despejado)

        print('Tranque en la Tarde! por %d horas, luego estara despejado  ' % env.now)
        duracion_mañana = 1
        yield env.timeout(duracion_mañana)

        print('Tranque en la Noche! por %d horas, luego estara despejado  ' % env.now)
        duracion_tarde = 1
        yield env.timeout(duracion_tarde)

        print('Tranque en la manana! por %d horas, luego estara despejado  '% env.now)
        yield env.timeout(4)

# Creamos nuestro Entorno
env = simpy.Environment()
# Lo agregamos la función de tranque, al Proceso del Entorno
env.process(tranque(env))
# Ejecutamos agregando el tiempo de 6 
env.run(until=6)

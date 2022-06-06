import random
import pprint

cualtos = {
    'cama_individual': [1,2,5],
    'cama_doble': [3,4,6]
}

maricos = ('Carlos','Luis')

parejas = [
    ('Domenico','Caro'),
    ('Paul', 'Victoria'),
    ('Valen','Hector'),
    ('Edward','Elizabeth'),
    ('Gustavo','Shumi'),
    maricos
]

tuCualto = {}

if __name__ == "__main__":
    # Asignamos un cuarto individual random para la pareja de maricos ('Carlos', 'Luis')
    parejas.remove(maricos)
    tuCualto[maricos] = random.choice(cualtos['cama_individual'])
    
    # Quitamos cuarto asignado de la lista
    cualtos['cama_individual'].remove(tuCualto[maricos])

    # Hacemos join de cuartos individuales con dobles y los mezclamos random
    todosLosCualtos = cualtos['cama_individual'] + cualtos['cama_doble']
    random.shuffle(todosLosCualtos)

    #Asignamos resto de los cuartos a cada pareja y vamos eliminando de la lista de cualtos disponibles para seleccion
    for pareja in parejas:
        tuCualto[pareja] = random.choice(todosLosCualtos)
        todosLosCualtos.remove(tuCualto[pareja])

    pprint.pprint(tuCualto)
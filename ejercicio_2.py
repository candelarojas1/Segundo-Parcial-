from grafo import Grafo 

grafo = Grafo(dirigido=False)


personajes = [
    'Luke Skywalker', 'Darth Vader', 'Yoda', 'Boba Fett', 'C-3PO', 
    'Leia Organa', 'Rey', 'Kylo Ren', 'Chewbacca', 'Han Solo', 'R2-D2', 'BB-8'
]

for personaje in personajes:
    grafo.insert_vertice(personaje)

grafo.insert_arista('Luke Skywalker', 'Darth Vader', 4)
grafo.insert_arista('Luke Skywalker', 'Leia Organa', 5)
grafo.insert_arista('Luke Skywalker', 'Yoda', 2)
grafo.insert_arista('Leia Organa', 'Han Solo', 3)
grafo.insert_arista('Han Solo', 'Chewbacca', 4)
grafo.insert_arista('Chewbacca', 'R2-D2', 2)
grafo.insert_arista('R2-D2', 'C-3PO', 6)
grafo.insert_arista('Leia Organa', 'Yoda', 1)
grafo.insert_arista('Darth Vader', 'Kylo Ren', 3)
grafo.insert_arista('Kylo Ren', 'Rey', 4)
grafo.insert_arista('Rey', 'BB-8', 3)
grafo.insert_arista('BB-8', 'R2-D2', 2)
grafo.insert_arista('Boba Fett', 'Darth Vader', 2)
grafo.insert_arista('Leia Organa', 'C-3PO', 2)
grafo.insert_arista('Chewbacca', 'Han Solo', 5)



# arbol_expansion_minima, peso_total = grafo.kruskal('Luke Skywalker')
# print(f"Árbol de expansión mínima (peso total: {peso_total}):")
# print(arbol_expansion_minima)

# if 'Yoda' in arbol_expansion_minima:
#     print("El árbol de expansión mínima contiene a Yoda.")
# else:
#     print("El árbol de expansión mínima no contiene a Yoda.")

# max_episodios = 0
# arista_maxima = None

# for arista in grafo.aristas:
#     peso = arista['peso']
#     if peso > max_episodios:
#         max_episodios = peso
#         arista_maxima = arista

# print(f"El número máximo de episodios compartidos es: {max_episodios}")
# print(f"Entre los personajes: {arista_maxima['origen']} y {arista_maxima['destino']}")

# Función para encontrar el MST y verificar si contiene a Yoda
def arbol_expansion_minimo_yoda(graph):
    bosque = graph.kruskal("Yoda")  # "Yoda" es solo un punto de partida
    contiene_yoda = any("Yoda" in arbol for arbol in bosque)
    return bosque, contiene_yoda

# Función para encontrar el número máximo de episodios compartidos
def maximo_episodios_compartidos(graph):
    max_episodios = 0
    for nodo in graph.elements:
        for arista in nodo['aristas']:
            if arista['peso'] > max_episodios:
                max_episodios = arista['peso']
    return max_episodios

# Ejecutar las funciones
bosque, yoda_presente = arbol_expansion_minimo_yoda(grafo)
print("Árbol de expansión mínimo contiene a Yoda:", yoda_presente)

max_episodios = maximo_episodios_compartidos(grafo)
print("Máximo de episodios compartidos:", max_episodios)
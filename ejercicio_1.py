from arbol_avl import BinaryTree

pokemones = {
    # Primera Generación
    1: {"nombre": "Bulbasaur", "tipo": ["Planta", "Veneno"], "nivel": 5},
    2: {"nombre": "Ivysaur", "tipo": ["Planta", "Veneno"], "nivel": 16},
    3: {"nombre": "Venusaur", "tipo": ["Planta", "Veneno"], "nivel": 32},
    4: {"nombre": "Charmander", "tipo": ["Fuego"], "nivel": 5},
    5: {"nombre": "Charmeleon", "tipo": ["Fuego"], "nivel": 16},
    6: {"nombre": "Charizard", "tipo": ["Fuego", "Volador"], "nivel": 36},
    7: {"nombre": "Squirtle", "tipo": ["Agua"], "nivel": 5},
    8: {"nombre": "Wartortle", "tipo": ["Agua"], "nivel": 16},
    9: {"nombre": "Blastoise", "tipo": ["Agua"], "nivel": 36},
    25: {"nombre": "Pikachu", "tipo": ["Eléctrico"], "nivel": 5},
    26: {"nombre": "Raichu", "tipo": ["Eléctrico"], "nivel": 26},
    133: {"nombre": "Eevee", "tipo": ["Normal"], "nivel": 5},
    134: {"nombre": "Vaporeon", "tipo": ["Agua"], "nivel": 20},
    135: {"nombre": "Jolteon", "tipo": ["Eléctrico"], "nivel": 20},
    136: {"nombre": "Flareon", "tipo": ["Fuego"], "nivel": 20},

    # Segunda Generación
    152: {"nombre": "Chikorita", "tipo": ["Planta"], "nivel": 5},
    155: {"nombre": "Cyndaquil", "tipo": ["Fuego"], "nivel": 5},
    158: {"nombre": "Totodile", "tipo": ["Agua"], "nivel": 5},

    # Tercera Generación
    252: {"nombre": "Treecko", "tipo": ["Planta"], "nivel": 5},
    255: {"nombre": "Torchic", "tipo": ["Fuego"], "nivel": 5},
    258: {"nombre": "Mudkip", "tipo": ["Agua"], "nivel": 5},

    # Cuarta Generación
    387: {"nombre": "Turtwig", "tipo": ["Planta"], "nivel": 5},
    390: {"nombre": "Chimchar", "tipo": ["Fuego"], "nivel": 5},
    393: {"nombre": "Piplup", "tipo": ["Agua"], "nivel": 5},

    # Quinta Generación
    495: {"nombre": "Snivy", "tipo": ["Planta"], "nivel": 5},
    498: {"nombre": "Tepig", "tipo": ["Fuego"], "nivel": 5},
    501: {"nombre": "Oshawott", "tipo": ["Agua"], "nivel": 5},

    # Sexta Generación
    650: {"nombre": "Chespin", "tipo": ["Planta"], "nivel": 5},
    653: {"nombre": "Fennekin", "tipo": ["Fuego"], "nivel": 5},
    656: {"nombre": "Froakie", "tipo": ["Agua"], "nivel": 5},

    # Séptima Generación
    722: {"nombre": "Rowlet", "tipo": ["Planta", "Volador"], "nivel": 5},
    725: {"nombre": "Litten", "tipo": ["Fuego"], "nivel": 5},
    728: {"nombre": "Popplio", "tipo": ["Agua"], "nivel": 5},

    # Octava Generación
    810: {"nombre": "Grookey", "tipo": ["Planta"], "nivel": 5},
    813: {"nombre": "Scorbunny", "tipo": ["Fuego"], "nivel": 5},
    816: {"nombre": "Sobble", "tipo": ["Agua"], "nivel": 5},
    880: {"nombre": "Dracozolt", "tipo": ["Eléctrico", "Dragón"], "nivel": 40},
    881: {"nombre": "Arctozolt", "tipo": ["Eléctrico", "Hielo"], "nivel": 40},
    882: {"nombre": "Dracovish", "tipo": ["Agua", "Dragón"], "nivel": 40},
    883: {"nombre": "Arctovish", "tipo": ["Agua", "Hielo"], "nivel": 40}
}

arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

# Insertar Pokémon en los árboles
for numero, datos in pokemones.items():
    arbol_nombre.insert_node(datos["nombre"], datos)
    arbol_numero.insert_node(numero, datos)
    for tipo in datos["tipo"]:
        arbol_tipo.insert_node(tipo, datos)

# B- Función para buscar y mostrar todos los datos de los Pokémon por proximidad
def mostrar_pokemons_por_proximidad(nombre_parcial):
    pokemons_encontrados = arbol_nombre.proximity_search(nombre_parcial)
    if pokemons_encontrados:
        print(f"\nPokémons que contienen '{nombre_parcial}':")
        for pokemon in pokemons_encontrados:
            tipos = ""
            for tipo in pokemon["tipo"]:
                tipos += tipo + ", "
            tipos = tipos[:-2]  # Eliminar la última coma y espacio
            print(f"Nombre: {pokemon['nombre']}, Tipo: {tipos}, Nivel: {pokemon['nivel']}")

mostrar_pokemons_por_proximidad("D")

# C- Mostrar todos los nombres de Pokémon de un tipo específico
def mostrar_pokemons_por_tipo(tipo_especifico):
    print(f"\nPokémons de tipo '{tipo_especifico}':")
    for datos in pokemones.values():
        if tipo_especifico in datos["tipo"]:
            print(datos["nombre"])

mostrar_pokemons_por_tipo("Agua")

# D- Listado en orden ascendente por número y nombre
def ordenar_por_nombre(pokemon):
    return pokemon["nombre"]

def listado_pokemons_ordenado():
    print("\nListado de Pokémons en orden ascendente por número:")
    for numero in sorted(pokemones.keys()):
        print(f"Número: {numero}, Nombre: {pokemones[numero]['nombre']}")

    print("\nListado de Pokémons en orden ascendente por nombre:")
    for nombre in sorted(pokemones.values(), key=ordenar_por_nombre):
        print(f"Nombre: {nombre['nombre']}, Nivel: {nombre['nivel']}")

listado_pokemons_ordenado()

# E- Mostrar todos los datos de Pokémon específicos
def mostrar_datos_pokemons_especificos(nombres):
    print("\nDatos de los Pokémons específicos:")
    for nombre in nombres:
        for datos in pokemones.values():
            if datos["nombre"] == nombre:
                tipos = ""
                for tipo in datos["tipo"]:
                    tipos += tipo + ", "
                tipos = tipos[:-2]
                print(f"Nombre: {datos['nombre']}, Tipo: {tipos}, Nivel: {datos['nivel']}")

mostrar_datos_pokemons_especificos(["Jolteon", "Lycanroc", "Tyrantrum"])

# F- Contar Pokémon de tipo eléctrico y acero
def contar_pokemons_por_tipo():
    contador_electrico = sum(1 for datos in pokemones.values() if "Eléctrico" in datos["tipo"])
    contador_acero = sum(1 for datos in pokemones.values() if "Acero" in datos["tipo"])
    
    print(f"\nNúmero de Pokémons de tipo Eléctrico: {contador_electrico}")
    print(f"Número de Pokémons de tipo Acero: {contador_acero}")

contar_pokemons_por_tipo()


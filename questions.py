import random

# Diccionario de categorías
categorias = {
    "programacion": ["python", "variable", "funcion", "bucle", "lista"],
    "matematica": ["entero", "fraccion", "derivada", "integral", "matriz"],
    "tecnologia": ["servidor", "internet", "computadora", "teclado", "pantalla"]
}

# Copia de palabras disponibles para que no se repitan
palabras_disponibles = {}
for categoria in categorias:
    palabras_disponibles[categoria] = categorias[categoria].copy()

puntaje_total = 0

while True:
    print("\nCategorías disponibles:")
    for categoria in categorias:
        print("-", categoria)

    categoria_elegida = input("Elegí una categoría: ").strip().lower()

    if categoria_elegida not in categorias:
        print("Categoría no válida")
        continue

    # Si no quedan palabras en esa categoría, reiniciamos esa lista
    if len(palabras_disponibles[categoria_elegida]) == 0:
        palabras_disponibles[categoria_elegida] = categorias[categoria_elegida].copy()

    palabra = random.choice(palabras_disponibles[categoria_elegida])
    palabras_disponibles[categoria_elegida].remove(palabra)

    adivinadas = []
    intentos = 6
    puntaje_ronda = 0

    print("\n¡Bienvenido al Ahorcado!")
    print("Categoría elegida:", categoria_elegida)

    while intentos > 0:
        progreso = ""
        for letra in palabra:
            if letra in adivinadas:
                progreso += letra + " "
            else:
                progreso += "_ "

        print("\n" + progreso)

        if "_" not in progreso:
            print("¡Ganaste!")
            puntaje_ronda += 6
            puntaje_total += puntaje_ronda
            print("Puntaje de esta ronda:", puntaje_ronda)
            print("Puntaje total:", puntaje_total)
            break

        print("Intentos restantes:", intentos)
        print("Letras usadas:", ", ".join(adivinadas))

        letra = input("Ingresá una letra: ").strip().lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Entrada no válida")
            continue

        if letra in adivinadas:
            print("Ya usaste esa letra.")
        elif letra in palabra:
            adivinadas.append(letra)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            adivinadas.append(letra)
            intentos -= 1
            puntaje_ronda -= 1
            print("Esa letra no está en la palabra.")

    else:
        print("\n¡Perdiste! La palabra era:", palabra)
        puntaje_ronda = 0
        print("Puntaje de esta ronda:", puntaje_ronda)
        print("Puntaje total:", puntaje_total)

    seguir = input("\n¿Querés jugar otra ronda? (si/no): ").strip().lower()
    if seguir != "si":
        print("Gracias por jugar.")
        break
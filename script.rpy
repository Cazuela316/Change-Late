# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen", color="#33fff0")
define a = Character("[Jugador]")
define n = Character("???")
define Cha = 0
define Int = 0
image bg camino = "Camino_a_la_ula_edit.png"
image bg entrada_ula = "Entrada_Ula_edit.png"
image bg entrada_edf = "Entrada_al_edificio_principal_edit.png"
image bg pasillo_1 = "Pasillo_1.png"
image bg pasillo_2 = "Pasillo_2.png"
image bg pasillo_3 = "Pasillo_3.png"
image bg pasillo_3b = "Pasillo_3b.png"
      

# El juego comienza aquí.

#label start:  

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

#scene bg 

    # Presenta las líneas del diálogo.


    # Finaliza el juego:

label start:

    $ Jugador = renpy.input("Cual es tu nombre?")
    $ Jugador = Jugador.strip()

    if Jugador == "":
        $ Jugador = "Jugador"

    n "Y cuales son tus pronombres?"

    menu:
        "Ella":
            $ player_pronoun = "la"
            $ player_pronoun_possessive = "su"
            $ player_pronoun_reflexive = "ella misma"
            $ player_pronoun_subject = "she"
        "El":
            $ player_pronoun = "el"
            $ player_pronoun_possessive = "su"
            $ player_pronoun_reflexive = "el mismo"
            $ player_pronoun_subject = "he"
        "Elles":
            $ player_pronoun = "elle"
            $ player_pronoun_possessive = "their"
            $ player_pronoun_reflexive = "elle misme"
            $ player_pronoun_subject = "they"


    scene bg camino
    e "Has creado un nuevo juego Ren'Py."
    e "bla bla bla bla bla"
    a "Dafok, ola mi pronombre es: [player_pronoun!c]"

    return


    return

# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define c = Character("Catalina", color="#d72bee")
define a = Character("[Jugador]")
define n = Character("???")
define p = Character("Profe Andre", color="#b1ea35")
define t = Character("Kevinzo", color="#51ee32")
define j = Character("Juan II", color="#3d3b96")
define Cha = 0
define Int = 0
define Intro = 0
define Extro = 0
define Carrera_jugador = Character("[Carrera]")
image bg camino = "Camino_a_la_ula_edit.png"
image bg entrada_ula = "Entrada_Ula_edit.png"
image bg entrada_edf = "Entrada_al_edificio_principal_edit.png"
image bg pasillo_1 = "Pasillo_1_edit.png"
image bg pasillo_2 = "Pasillo_2_edit.png"
image bg pasillo_3 = "Pasillo_3_edit.png"
image bg pasillo_3b = "Pasillo_3b_edit.png"
image bg cafe = "Cafeteria.jpg"
image bg jardin = "Jardin_botanico.jpg"
image bg jardin_b = "Jardin_botanico_b.jpg"
image bg gym = "Gimnasio.jpg"
image bg clase = "Sala_de_clase.jpg"
      

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
    
    $ Carrera = renpy.input("Cual es tu carrera?")
    $ Carrera = Carrera.strip()

    if Carrera == "":
        $ Carrera = "Informatica"

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


    a "Waah… Fuh… Todavía tengo sueño…"
    narrator "Con algo de dificultad y aun no teniendo todos tus sentidos despiertos, extendiste tu mano para alcanzar tu celular."
    a "¿Qué horas son?"
    narrator "Te dijiste a ti mismo mientras lo prendías, aturdiéndote un poco el brillo de la pantalla."
    a "Erm..."
    a "Ah! Son las 7 en punto."
    a "Fuh… Mi alarma ni suena aun… Podría dormir un poco más…"
    # show catalina feliz at mitad_mitad_izquierda
    #c "¡Hola! ¿Qué tal te ha ido este fin de semana [Jugador]?"


default menuset = set()


menu primera_decision:

    set menuset
    "Oh, es catalina. Como deberia responderle?"

    "!Oh, Cata, bastante bien! ¿Como te ha ido a ti?":
            $ Cha = 2
            c "A mí me ha ido muy bien, fui al cine a ver una película muy buena. ¿Vas a la universidad?"

    "Oh, bastante bien":
        $ Cha = -1
        c "Uhmm... ¡Bueno! Es bueno oírlo. ¿Estas yendo a la universidad?"

    "Decente.":
        $ Cha = -1
        c "Uhmm... ¡Bueno! Es bueno oírlo. ¿Estas yendo a la universidad?"

label wow_pero_despues_2:
    a "Si, si. Dicen que los primeros días son algo complicados, no?"
    c "Claro! Yo aun no estoy 100 por ciento segura si es que estoy en la clase correcta! Jeje."
    scene bg entrada_ula
    show catalina feliz at mitad_mitad_izquierda with dissolve
    c "Llegamos! Ah... Que cansancio."
    a "Si honestamente."
    scene bg entrada_edf
    show catalina feliz at mitad_mitad_izquierda with dissolve
    c "Bueno ¿Que clase tienes ahora? Yo tengo Química… Wahh…"
    a "Fuh… Buena suerte… A mí me toca matemáticas."
    a "Aunque espero que el profe no me pregunte nada, No he estudiado…"
    c "Jaja! Entiendo, Bueno. Me voy a mi clase. Nos vemos!"
    a "Nos vemos! Fuh..."
    scene bg pasillo_3b
    narrator "Después de esquivar a todos los estudiantes apurados por llegar a sus clases, lograste llegar a la puerta de la clase."
    narrator "Tomando aire y exhalándolo, abriste la puerta de la sala de clases, pasando a esta."
    scene bg clase
    narrator "Dentro de esta estaban todos los alumnos, menos el profesor. Rápidamente fuiste a un puesto vacío y te sentaste."
    narrator "A penas te sentaste, el profesor irrumpió dentro de la sala de clases."
    show profe feliz at entrada_lenta_izquierda
    p "Buenas tardes alumnos! Hoy haremos un repaso para el parcial que tendremos mañana. A si que espero hayan estudiado!"
    narrator "La clase paso con normalidad... Hasta que..."
    p "Bien… Quien sabe la respuesta de este ejercicio?"
    narrator "Todos se quedaron callados intentando ver a donde sea menos hacia la pizarra o al profesor."
    p "… Bien, erm… [Jugador]! Podrías decirme cómo se resuelve este ejercicio?"
    a "Ah!? Eh... Yo… Erm…"
    narrator "Diablos… No recuerdo como se hacía esto…"

menu segundad_decision:
    set menuset
    "¿Qué debería decir?"

    "Se resuelve usando la formula a":
            $ Int = 1
            p "Mh... Veamos."
            "El profesor utilizo al formula que antes mencione, resolviendo el ejercicio rapidamente."
            p "Correcto! Felicidades [Jugador]."
            a "¡Bien! Menos mal estudie un poco ayer."

    "Se resuelve usando la formula b":
            $ Int = -1
            p "Mh... Veamos."
            "El profesor utilizo al formula que antes mencione, resolviendo el ejercicio rapidamente."
            p "Mh... Incorrecto... Estudie mas [Jugador], esto aparecera en el parcial."
            a "Tch, tendré que estudiar mas hoy."

    "Simplemente se suma":
            $ Int = -1
            p "Mh... Veamos."
            "El profesor sumo el problema..."
            p "Mh... Incorrecto... Estudie mas [Jugador], esto aparecera en el parcial."
            a "Tch, tendré que estudiar mas hoy."

    "No lo sé":
            $ Cha = +1
            a "Lo siento profesor, No se la respuesta."
            p "... Entiendo, alguien mas sabe la respuesta?" 
            a "Haa, parece que tendré que estudiar un poco más..."


label wow_pero_despues_22:
    narrator "Después de una larga clase, finalmente podre irme a casa…"
    narrator "Hasta que..."
    p "Disculpa, [Jugador] Podrías vernir un segundo"
    a "Uy... Claro..."
    narrator "Con algo de nervios, fui hacia el profesor, preguntándome si es que dije algo malo."
    p "Bueno, veo que tus notas no son del todo buenas, pero veo que prestas atención en clase. ¿Hay algún problema que deba saber?"
menu tercera_desicion:
    set menuset
    "Qué incómodo... ¿Qué debería decirle?"

    "Uhm, no, no hay ningún problema, profesor.":
        $ Cha = Cha - 1
        if Cha >= 2:
            jump ruta_extra_1  # ← Esto te lleva a la ruta secreta
        else:
                p "Ya veo... Deberías ir a ver al jefe de carrera, veremos si puedes hacer una prueba recuperativa. Dependerá de la nota de tu siguiente parcial."
                p "Por cierto, se llama Juan II."
                a "Vale... Muchas gracias, profesor."


    "Bueno, la verdad, no he tenido mucho tiempo para estudiar":
            p "Ya veo... Podrías ir a ver al jefe de carrera. Podrías hablar un poco sobre el tema."
            a "Vale... Muchas gracias profesor."

    "Eh... No...":
        $ Cha = Cha - 2
        p "Hmmm, ve a ver al jefe de carrera. Si sigues así, tendrás que tomar recuperativas."
        p "Por cierto, se llama Juan II."
        a "Vale... Muchas gracias, profesor."

label wow_pero_despues_3:
    scene bg pasillo_3b
    narrator "Después de esa incomoda conversación con el profesor, saliste de la sala de clases."
    a "Bueno, supongo que buscare al jefe de carrera."
    a "Aunque… Huh…"

    menu cuarta_desicion:

        set menuset
        "Donde podria estar?"

        "En la cafeteria":
            scene bg cafe
            a "Uy... No lo veo por aqui... mejor regreso a donde estaba."
            jump cuarta_desicion

        "En el pasillo":
            scene bg pasillo_2
            a "Ahi esta! Aunque esta con alguien..."

        "En el gimnasio":
            scene bg gym
            a "Uy... No lo veo por aqui... mejor regreso a donde estaba."
            jump cuarta_desicion

        "En el jardin botanico":
            scene bg jardin
            a "Uy... No lo veo por aqui... mejor regreso a donde estaba."
            jump cuarta_desicion
label wow_pero_despues_4:

menu quinta_desicion:

        set menuset
        "Le voy a hablar?"

        "Hablemosle de todas formas!":
            $ Intro = Intro + 1
            narrator "Dando un suspiro, y llenándome de valor, fui hacia el jefe de carrera mientras conversaba con esa otra persona."
            a "Buenas tardes...! Usted es el jefe de carrera de [Carrera], Verdad...?"
            j "Oh! Sip, ...Y tu eres..?"

    "Que vergüenza... Mejor espero a que deje de hablar con esa persona...":
            "Es mejor, asi no los interrumpo... Puede que esten hablando algo importante..."
            "Aunque... El jefe de carrera se percato que lo quede viendo, y junto con la otra persona, vinieron hacia donde estaba."
            j "Vi que te quedaste viendonos... Querias hablar con alguno de nosotros?"
            a "A...ah! Sip, vera..."
            
label wow_pero_despues_5:
a "Mi nombre es [Jugador]... El profesor Andre me dijo que venga a hablar con usted... Les molesto...?"
t "Oh! No, no... El jefe de carrera es todo tuyo, y tambien quisiera hablarte un poco despues."






 

return


return

# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define c = Character("Catalina", color="#33fff0")
define a = Character("[Jugador]")
define n = Character("???")
define p = Character("Andre", color="#f02626")
define t = Character("Kevinzo", color="#51ee32")
define j = Character("Juan II", color="#3d3b96")
define CHA = 0
define INT = 0
define INTRO = 0
define EXTRO = 0
define Carrera_jugador = Character("[Carrera]")
image bg camino = "Camino_a_la_ula_edit.png"
image bg entrada_ula = "Entrada_Ula_edit.png"
image bg entrada_edf = "Entrada_al_edificio_principal_edit.png"
image bg pasillo_1 = "Pasillo_1_edit.png"
image bg pasillo_2 = "Pasillo_2_edit.png"
image bg pasillo_3 = "Pasillo_3_edit.png"
image bg pasillo_3b = "Pasillo_3b_edit.png"
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


    scene bg camino
    narrator "Otro día de universidad, espero hoy me vaya bien."
    c "¡Hola! ¿Qué tal te ha ido este fin de semana [Jugador]?"


default menuset = set()


menu primera_decision:

    set menuset
    "Oh, es catalina. Como deberia responderle?"

    "!Oh, Cata, bastante bien! ¿Como te ha ido a ti?":
            $ CHA = CHA +2
            c "A mí me ha ido muy bien, fui al cine a ver una película muy buena. ¿Vas a la universidad?"

    "Oh, bastante bien":
        $ CHA = CHA-1
        c "Uhmm... ¡Bueno! Es bueno oírlo. ¿Estas yendo a la universidad?"

    "Decente.":
        $ CHA = CHA-2
        c "Uhmm... ¡Bueno! Es bueno oírlo. ¿Estas yendo a la universidad?"

label wow_pero_despues:

    a "Sí, sí. ¿Los primeros días son bastante complicados no?"
    c "Y claro. Yo aun no estoy del todo segura de si estoy en la clase correcta"
    scene bg entrada_ula
    c "Fiu, que cansancio. ¿Qué clase tienes ahora? A mí me toca Química Wahh..."
    a "Tengo mates. Espero el profesor no me pregunte nada. Aún no he estudiado."
    c "Jajaja, bueno, nos vemos luego [Jugador]."
    scene bg clase
    p "Buenos días alumnos, hoy estaremos haciendo el repaso final antes del parcial de mañana. Espero estén preparados."
    "~ Un tiempo despues ~"
    p "Bien! Alguien que quiera resolver el ejercicio?"
    "..."
    p "...Vale, Umh... [Jugador] Como se resuelve el problema?"
    a "Uh? Emh..."

menu segunda_decision:

    set menuset
    "Diablos, No recuerdo esto... Que deberia decir?"

    "Se resuelve usando la formula a":
            $ INT = INT+2
            p "Mh... Veamos."
            "El profesor utilizo al formula que antes mencione, resolviendo el ejercicio rapidamente."
            p "Correcto! Felicidades [Jugador]."
            a "¡Bien! Menos mal estudie un poco ayer."

    "Se resuelve usando la formula b":
            $ INT = INT-1
            p "Mh... Veamos."
            "El profesor utilizo al formula que antes mencione, resolviendo el ejercicio rapidamente."
            p "Mh... Incorrecto... Estudie mas [Jugador], esto aparecera en el parcial."
            a "Tch, tendré que estudiar mas hoy."

    "Simplemente se suma":
            $ INT = INT-2

            p "Mh... Veamos."
            "El profesor sumo el problema..."
            p "Mh... Incorrecto... Estudie mas [Jugador], esto aparecera en el parcial."
            a "Tch, tendré que estudiar mas hoy."

    "No lo sé":
            $ CHA = CHA+1
            a "Lo siento profesor, No se la respuesta."
            p "... Entiendo, alguien mas sabe la respuesta?" 
            a "Haa, parece que tendré que estudiar un poco más..."

label wow_pero_despues_2:
    "Despues de una larga clase... era tiempo de la ventana de 4 hora para mi proxima clase... hasta que..."
    p "Disculpa, [Jugador] Puedes venir un segundo?"
    a "Uy... claro..."
    p "Veo que tus notas no son del todo buenas, aun así, te veo prestando atención en clases. ¿Hay algún problema?"

menu tercera_desicion:

    set menuset
    "Que incomodo... Que deberia decirle?"

    "Uhm, no... No, ningún problema profesor.":
            p "Ya veo... Deberias ir a ver al jefe de carrera, veremos si puedes hacer una prueba recuperativa, dependera de la nota de tu siguiente parcial."
            a "Vale... Muchas gracias profesor."

    "Bueno, la verdad, no he tenido mucho tiempo para estudiar":
            $ CHA = CHA+1
            p "Ya veo... Podrías ir a ver al jefe de carrera. Podrías hablar un poco sobre el tema."
            a "Vale... Muchas gracias profesor."

    "Umh... No...":
            p "Hmmm, Ve a ver al jefe de carrera, si sigues así tendrás que tomar recuperativas."
            a "Vale... Muchas gracias profesor."
label wow_pero_despues_3:
scene bg pasillo_3b
a "Bien! Tengo que encontrar al jefe de carrera!"
a "Aunque... Umh..."
menu cuarta_desicion:

    set menuset
    "Donde podria estar?"

    "En la cafeteria":
            a "Uy... No lo veo por aqui... mejor regreso a donde estaba."
            jump cuarta_desicion

    "En el pasillo":
            a "Ahi esta! Aunque esta con alguien..."

    "En el gimnasio":
            a "Uy... No lo veo por aqui... mejor regreso a donde estaba."
            jump cuarta_desicion
    "En el jardin botanico":
            a "Uy... No lo veo por aqui... mejor regreso a donde estaba."
            jump cuarta_desicion
label wow_pero_despues_4:

menu quinta_desicion:

    set menuset
    "Le voy a hablar?"

    "Hablemosle de todas formas!":
            "Dando un suspiro, y llenandome de valor, fui hacia el jefe de carrera mientras conversaba con alguien mas."
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
j "Bueno, sobre que tenias que hablarme?"

menu cuarta_desicion:

    set menuset
    "Okay, que podria decirle?"

    "O-Oh, bueno, nada en especifico":
            j "Ok? Bueno, en ese caso quizas deberias ir a hablar con tu tutor, cuando estaba en primer año como tu era un muy buen estudiante."
            a "Eso haré..."

    "Venia sobre la posibilidad de un remedial":
            j "Hmmm, entonces asumo que tus notas estan regular. Bueno,, esperaremos a las notas del de mañana y despues hablamos okay?"
            a "Okay...Okay, eso haré."

    "Umh... Venia acerca de mis notas":
            j "Hmmm, entonces asumo que tus notas estan regular. Bueno,, esperaremos a las notas del de mañana y despues hablamos okay?"
            a "Okay...Okay, eso haré."
label wow_pero_despues_6:
    a "Hmmm, tenias algo que decirme?"
    t "Bueno, simplemente queria saber como les va a los de primero este año"

menu quinta_desicion:

    set menuset
    "Que le digo?"

    "Oh, si, claro... Bien... Bastante bien.":
            $ CHA = CHA-1
            t "Hmm... Bien, si todo esta bien, entonces deberia retirarme. Ten un buen día"
    "Bueno, aguantando como puedo":
            t "Haa, eso es lo mas normal, sigue como estas y te acostumbraras algun dia. Y lo digo por experiencia.
            Pero bueno, es tiempo de que me retire"
    "Pues, de eso venia a hablarle a el jefe de carrera. Mis notas no van muy bien":
            t "Bueno, aun quedan las remediales, si tienes alguna pregunta no dudes en enviarme un correo. Ahora, me tengo que ir, asi que suerte"

return


return

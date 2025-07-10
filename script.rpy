# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define c = Character("Catamaran", color="#d72bee")
define a = Character("[Jugador]")
define n = Character("???")
define p = Character("Profe Andre", color="#b1ea35")
define t = Character("Kevinzo", color="#51ee32")
define j = Character("Juan II", color="#3d3b96")
define f = Character("Felipe", color="#e63c3c")
image catalina feliz = "CATA_FELIZ.png"
image catalina triste = "CATA_TRISTE.png"
image catalina neutral = "CATA_NORMAL.png"
image catalina incomodo = "CATA_INC.png"
image felipe feliz = "FELIPE_FELIZ.png"
image felipe neutral = "FELIPE_NORMAL.png"
image felipe enojado = "FELIPE_ENOJADO.png"
image felipe incomodo = "FELIPE_INC.png"
image kevin feliz = "KEVIN_FELIZ.png"
image kevin triste = "KEVIN_TRISTE.png"
image kevin neutral = "KEVIN_NORMAL.png"
image kevin incomodo = "KEVIN_INC.png"
image juan feliz = "JUAN_FELIZ.png"
image juan triste = "JUAN_TRISTE.png"
image juan neutral = "JUAN_NORMAL.png"
image juan incomodo = "JUAN_INC.png"
image profe feliz = "PROFE_FELIZ.png"
image profe triste = "PROFE_TRISTE.png"
image profe neutral = "PROFE_NORMAL.png"
image profe incomodo = "PROFE_INC.png"
image pieza_dia = "Pieza(Dia).png"
image pieza_noche = "Pieza(Noche).png"
image bg negro = "#000000"
image bg cielo = "image.png"
image bg pizarra_ejercicio = "Sala_de_clase(formula).jpg"
image cuadrado = "color2.png"
transform amongus:
    xzoom 1.7 yzoom 0.5
    xalign 0.5
    yalign 0.5
transform mitad_derecha:
    zoom 0.5
    xalign 1.0

transform mitad_mitad_derecha:
    zoom 0.5
    xalign 0.7

transform mitad_izquierda:
    zoom 0.5
    xalign 0.0 

transform mitad_mitad_izquierda:
    zoom 0.5
    xalign 0.3 

transform mitad_centro:
    zoom 0.5
    xalign 0.5

transform entrada_lenta_izquierda:
    zoom 0.5
    xalign -0.3  # empieza más allá del borde izquierdo
    linear 0.3 xalign 0.3  # en 0.3 segundos va a la posición deseada

transform entrada_lenta_derecha:
    zoom 0.5
    xalign 1.0  # empieza más allá del borde izquierdo
    linear 0.3 xalign 0.7  # en 2 segundos va a la posición deseada

transform salida_derecha:
    zoom 0.5
    xalign 0.7
    linear 0.3 xalign 1.0

transform salida_izquierda_lenta:
    zoom 0.5
    xalign 0.3
    linear 1.0 xalign -1.0

transform salida_izquierda_rapida:
    zoom 0.5
    xalign 0.3
    linear 0.3 xalign -1.0

transform derecha_al_centro:
    zoom 0.5
    xalign 0.7
    linear 0.5 xalign 0.5

transform fuera_izquierda_al_centro:
    zoom 0.5
    xalign -1.0
    linear 0.5 xalign 0.5

transform entrada_lenta_izquierda:
    zoom 0.5
    xalign -0.3  # empieza más allá del borde izquierdo
    linear 0.3 xalign 0.1  # en 0.3 segundos va a la posición deseada

define Cha = 0
define Int = 0
define Intro = 0
define Extro = 0
define Res = 0
define act_l = 0 #Si el usuario es de otra parte o no
define act_m = 0 #Si el usuario tiene sus metas claras
define Carrera_jugador = Character("[Carrera]")
define Ruta_tutor = 0
define Voley = 0
define dormir =0
define x = 0
define Flag1 = 0
define wow = 0
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
image bg pieza_dia = "Pieza_Dia.png"
image bg pieza_noche = "Pieza_Noche.png"
      

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

    play music "Pajaritos.mp3" fadein 2.0 loop
    show bg pieza_dia with dissolve
    a "Waah… Fuh… Todavía tengo sueño…"
    narrator "Con algo de dificultad y aún no teniendo todos tus sentidos despiertos, extendiste tu mano para alcanzar tu celular."
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
    "¿Vuelves a dormir?"

    "Si":
            $ Res = Res - 1
            $ dormir = dormir + 1
            a "Bah, unas cuantas horas de sueño extra no harán mal…"
            narrator "Te dijiste a ti mismo, mientras te volvías a recostar, cerrando tus ojos…"
            show bg negro with dissolve
            stop music fadeout 1.0
            show bg pieza_noche with dissolve
            narrator "De la nada, te despertaste de repente, incluso hasta un poco con miedo, pero con tus 8 horas de sueño."
            
            a "Wahhh! Que buena dormida. Uy, ¿Qué hora es?"
            a "..."
            play audio "SFX_Shock.mp3" noloop
            a "¿¡LAS 1 DE LA TARDE?!"
            a "Diablos… Me perdí todas mis clases!"
            narrator "Soltaste un largo suspiro."
            a "Bueno, supongo que si no fui a clase al menos debería ordenar la casa..."
            narrator "Dijiste mientras te levantabas de la cama, vistiendote..."
            play music "BMG_Tarde-Noche.mp3" fadein 3.0 loop
            show bg negro with dissolve
            narrator "...Y comenzando a ordenar."
            narrator "Estuviste todo el dia ordenando tu casa. Ya en la tarde..."
            show bg pieza_noche with dissolve
            a "Fuah... Estuve todo el dia limpiando... ¡Pero al menos la casa quedo limpiecita!"
            narrator "Aunque, ahora tienes que decidir que hacer..."
            jump wow_pero_despues

    "No":
        $ Res = Res + 1
        a "Urm… No! Tengo que ir a clase, Además es la hora perfecta para ir!"
        stop music fadeout 1.0
        narrator "Dijiste, levantándote con todo el animo que podías, vistiéndote..."
        narrator "Lavándote los dientes y finalmente, saliendo de tu casa, sin antes dejar bien cerrado."
        play sound "SFX_Salir.mp3" noloop
        scene bg camino
        play music "BMG_Dia.mp3" fadein 4.0 loop
        narrator "Tomando un buen puñado de aire, empezaste a caminar hacia la universidad."
        narrator "Mientras veías como el chat grupal de la carrera se llenaba de mensajes."
        a "Tsk... No es necesario que cuenten toda su vida..."
        narrator "Decías mientras guardabas tu teléfono en tu bolsillo, hasta que de la nada, escuchaste a alguien llamando tu nombre."
        n "[Jugador]!!!"
        narrator "Miraste con curiosidad hacia la direccion de donde venian los gritos."
        narrator "Venia corriendo hacia ti una chica bastante alegre."
        show catalina feliz at entrada_lenta_izquierda
        c "Wahh!!! Qué bueno encontrarte [Jugador]!"
        narrator "Es Catamaran, una de las únicas amigas que, hasta el momento tengo en la universidad."
        narrator "Es una buena amiga, aunque puede llegar a ser algo molesta."
        c "Bueno... Cuéntame. ¿Cómo estuvo tu fin de semana?"
        menu segunda_decision:
            set menuset
            "Como debería responderle?"

            "De muy buena manera":
                $ Cha = Cha + 2
                a "Bastante bien la verdad! Fui al cine a ver una película."
                a "Aunque la verdad ni me gusto, pero bueno."
                c "Jaja! Entiendo! Yo la verdad no he hecho mucho!"
                c "Pero bueno, vas de camino a la universidad?"

            "Normal":
                $ Cha = Cha - 1
                a "Bien, Nada que decir la verdad."
                c "Oh, entiendo!"
                c "Bueno, vas de camino a la universidad?"

            "De mala manera":
                $ Cha = Cha - 2
                a "Decente."
                c "…Ya veo… Ejem, es bueno oírlo!"
                c "Pero bueno, vas de camino a la universidad?"

label wow_pero_despues_2:
    a "Si, si. Dicen que los primeros días son algo complicados, no?"
    c "Claro! Yo aun no estoy 100 por ciento segura si es que estoy en la clase correcta! Jeje."
    play sound "SFX_Pasos.mp3" noloop
    scene bg entrada_ula
    show catalina feliz at mitad_mitad_izquierda with dissolve
    c "Llegamos! Ah... Que cansancio."
    a "Si honestamente."
    play sound "SFX_Pasos.mp3" noloop
    scene bg entrada_edf
    show catalina feliz at mitad_mitad_izquierda with dissolve
    c "Bueno ¿Que clase tienes ahora? Yo tengo Química… Wahh…"
    a "Fuh… Buena suerte… A mí me toca matemáticas."
    a "Aunque espero que el profe no me pregunte nada, No he estudiado…"
    c "Jaja! Entiendo, Bueno. Me voy a mi clase. Nos vemos!"
    a "Nos vemos! Fuh..."
    play sound "SFX_Pasos.mp3" noloop
    scene bg pasillo_3b with dissolve
    narrator "Después de esquivar a todos los estudiantes apurados por llegar a sus clases, lograste llegar a la puerta de la clase."
    narrator "Tomando aire y exhalándolo, abriste la puerta de la sala de clases, pasando a esta."
    scene bg clase
    narrator "Dentro de esta estaban todos los alumnos, menos el profesor. Rápidamente fuiste a un puesto vacío y te sentaste."
    narrator "A penas te sentaste, el profesor irrumpió dentro de la sala de clases."
    show profe feliz zorder 99 at entrada_lenta_izquierda
    p "Buenas tardes alumnos! Hoy haremos un repaso para el parcial que tendremos mañana. A si que espero hayan estudiado!"
    show bg pizarra_ejercicio zorder 0 with dissolve
    narrator "La clase paso con normalidad... Hasta que..."
    p "Bien… Quien sabe la respuesta de este ejercicio?"
    narrator "Todos se quedaron callados intentando ver a donde sea menos hacia la pizarra o al profesor."
    p "… Bien, erm… [Jugador]! Podrías decirme cómo se resuelve este ejercicio?"
    a "Ah!? Eh... Yo… Erm…"
    narrator "Diablos… No recuerdo como se hacía esto…"

menu segundad_decision:
    set menuset
    "¿Qué debería decir?"

    "Se resuelve usando la fórmula del cuadrado de binomio":
        $ Int = 1
        p "Mh... Veamos."
        "El profesor utilizó la fórmula que antes mencionaste, resolviendo el ejercicio rápidamente."
        p "¡Correcto! Felicidades, [Jugador]."
        a "¡Bien! Menos mal estudié un poco ayer."

    "Se resuelve usando la fórmula del cubo de binomio":
        $ Int = -1
        p "Mh... Veamos."
        "El profesor utilizó la fórmula que antes mencionaste, resolviendo el ejercicio rápidamente."
        p "Mh... Incorrecto... Estudia más, [Jugador], esto aparecerá en el parcial."
        a "Tch, tendré que estudiar más hoy."

    "Simplemente se suma":
        $ Int = -1
        p "Mh... Veamos."
        "El profesor sumó el problema..."
        p "Mh... Incorrecto... Estudia más, [Jugador], esto aparecerá en el parcial."
        a "Tch, tendré que estudiar más hoy."

    "No lo sé":
        $ Cha += 1
        a "Lo siento profesor, no sé la respuesta."
        p "... Entiendo, ¿alguien más sabe la respuesta?"
        a "Haa, parece que tendré que estudiar un poco más..."


label wow_pero_despues_22:
    narrator "Después de una larga clase, finalmente podre irme a casa…"
    narrator "Hasta que..."
    p "Disculpa, [Jugador] Podrías vernir un segundo"
    a "Uy... Claro..."
    narrator "Con algo de nervios, fui hacia el profesor, preguntándome si es que dije algo malo."
    show profe neutral
    p "Bueno, veo que tus notas no son del todo buenas, pero veo que prestas atención en clase. ¿Hay algún problema que deba saber?"
menu tercera_desicion:
    set menuset
    "Qué incómodo... ¿Qué debería decirle?"

    "Uhm, no, no hay ningún problema, profesor.":
        $ Cha = Cha - 1
        if Cha >= 2:
            $ Ruta_tutor = Ruta_tutor + 1
            jump ruta_extra_1  # ← Esto te lleva a la ruta secreta
        else:
                $ wow = wow + 1
                p "Ya veo... Deberías ir a ver al jefe de carrera, veremos si puedes hacer una prueba recuperativa."
                p "Dependerá de la nota de tu siguiente parcial."
                show profe feliz
                p "Por cierto, se llama Juan II."
                a "Vale... Muchas gracias, profesor."


    "La verdad no he tenido mucho tiempo para estudiar.":
        $ Cha = Cha + 1
        p "Ya veo... Deberías ir a ver al jefe de carrera, veremos si puedes hacer una prueba recuperativa."
        p "Dependerá de la nota de tu siguiente parcial."
        p "Por cierto, se llama Juan II."
        show profe feliz
        a "Vale... Muchas gracias, profesor."

    "Eh... No...":
        $ Cha = Cha - 2
        p "Hmmm, ve a ver al jefe de carrera. Si sigues así, tendrás que tomar recuperativas."
        p "Por cierto, se llama Juan II."
        show profe feliz
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
            play sound "SFX_Pasos.mp3" noloop
            a "Uy... No lo veo por aqui... mejor regreso a donde estaba."
            scene bg pasillo_3b
            jump cuarta_desicion

        "En el pasillo":
            play sound "SFX_Pasos.mp3" noloop
            scene bg pasillo_2
            a "Ahí esta! Aunque esta con alguien..."

        "En el gimnasio":
            play sound "SFX_Pasos.mp3" noloop
            scene bg gym
            a "Uy... No lo veo por aqui... mejor regreso a donde estaba."
            scene bg pasillo_3b
            jump cuarta_desicion

        "En el jardin botanico":
            play sound "SFX_Pasos.mp3" noloop
            scene bg jardin
            a "Uy... No lo veo por aqui... mejor regreso a donde estaba."
            scene bg pasillo_3b
            jump cuarta_desicion
label wow_pero_despues_4:

menu quinta_desicion:

        set menuset
        "Le voy a hablar?"

        "Hablemosle de todas formas!":
            $ Intro = Intro + 1
            narrator "Dando un suspiro, y llenándome de valor, fui hacia el jefe de carrera mientras conversaba con esa otra persona."
            show juan neutral at entrada_lenta_derecha
            show kevin neutral at entrada_lenta_izquierda
            a "Buenas tardes...! Usted es el jefe de carrera de [Carrera], Verdad...?"
            j "Oh! Sip, ...Y tu eres..?"

        "Que vergüenza... Mejor espero a que deje de hablar con esa persona...":
            $ Extro = Extro + 1
            "Es mejor, asi no los interrumpo... Puede que esten hablando algo importante..."
            "Aunque... El jefe de carrera se percato que lo quede viendo, y junto con la otra persona, vinieron hacia donde estaba."
            show juan neutral at entrada_lenta_derecha
            show kevin neutral at entrada_lenta_izquierda
            j "Vi que te quedaste viendonos... Querías hablar con alguno de nosotros?"
            a "A...ah! Sip, vera..."
            
label wow_pero_despues_5:
    a "Mi nombre es [Jugador]... El profesor Andre me dijo que venga a hablar con usted... Les molesto?"
    show kevin feliz
    show juan feliz
    t "Oh, No no… El jefe de carrera es todo tuyo. Aunque también me gustaría hablarte después."
    show kevin feliz at salida_izquierda_lenta
    narrator "Dijo el tutor mientras se iba un poco al lado para no estorbar entre la conversación."
    narrator "Poniéndose sus audífonos y viendo su teléfono."
    show juan feliz at derecha_al_centro
    menu quintaa_desicion:

        set menuset
        j "Bueno, ¿Cuéntame para que necesitas hablarme?"

        "Nada en específico":
            a "Pues nada en específico la verdad. Como dije antes, el profesor me envió para que hablara con usted."
            show juan neutral
            j "Huh, Supongo que si te dijo que vinieras a hablarme es por algo de tus notas, o lo del remedial…"
            show juan feliz
            j "Para eso tienes que hablarle al tutor. Él sabe sobre eso."

        "Sobre los remediales":
            a "Pues, quería ver si es que tenía la oportunidad de dar una prueba remedial."
            show juan neutral
            j "Ah, ya veo…"
            show juan feliz 
            j "Para eso tienes que hablarle al tutor. Él sabe sobre eso."

        "Sobre mis notas":
            a "Pues, es sobre mis notas… No han estado muy bien…"
            show juan neutral
            j "Ah, ya veo…"
            show juan feliz
            j "Para eso tienes que hablarle al tutor. Él sabe sobre eso."
            
label wow_pero_despues_55: 

    a "Ah! ¡Perfecto! ¿Y quién es el tutor?"
    j "Pues, el chico con en que estaba hablando antes."
    a "Oh, ya veo. Bueno, en ese caso le hablare a él. Muchas gracias!"
    j "Por cierto..."
    menu Sexta_desicion:

        set menuset
        j "De donde eres?"

        "De aquí":
            a "Pues de aquí, Por que la pregunta?"
            j "Oh! No, por nada."

        "De otra parte":
            $ act_l = 1
            a "De otra parte, Por qué pregunta?"
            j "Oh, por nada."
label wow_pero_despues_6: 
    narrator "De la nada a juan le llego un mensaje a su teléfono, se sorprendió un poco y lo guardo rapidamente."
    j "Uy... me tengo que ir. Nos vemos después!"
    a "Oh! Está bien, nos vemos!"
    show juan feliz at salida_izquierda_rapida
    narrator "Después de hablar con el jefe de carrera, me gire hacia donde estaba el tutor, aun viendo su celular con sus audífonos puestos."
    a "Eh... ¿Disculpa?"
    show kevin neutral at fuera_izquierda_al_centro
    t "Ah? Si si, perdona… Cuéntame, que necesitas?"
    a "Pues… No sé si escuchaste…"
    show kevin feliz
    t "Jaja! No te preocupes, ni me puse música. Así que escuche todo."
    a "Oh! Fuh... qué alivio. No quería volver a repetirlo."
    t "Mhm, Por cierto..."
    menu Septima_desicion:

        set menuset
        t "¿Como les va a los de primer año?"

        "Bastante bien":
            a "Pues bastante bien! Aunque a mí me ha costado un poco…"
            t "Entiendo, bueno. Ahí te hablare para coordinar mejor ese tema. ¿Vale?"
            t "No te preocupes. A todos les cuesta un poco."
            a "Vale! Muchas gracias."
        "Aguantando como puedes":
            a "Pues he estado aguantando como puedo."
            t "Claro, entiendo. Bueno, Ahí te hablare para coordinar mejor ese tema. ¿Vale?"
            a "Vale! Muchas gracias."
        "Decirle porque vienes a hablarle":
            a "Bueno… Si enserio escucho como me ha ido, pues…"
            show kevin neutral
            t "Entiendo, bueno. Ahí te hablare para coordinar mejor ese tema. ¿Vale?"
            show kevin feliz
            t "Tu solo enfócate en estudiar mas, vale?"
            a "Vale! Muchas gracias."
label wow_pero_despues_7: 
    narrator "Despues de hablarle al tutor, sentiste como un peso se liberó de ti."
    narrator "Ya no quedaba nada más que hacer, que irte a casa."
    stop music fadeout 2.0
    hide kevin feliz with dissolve
    show bg camino with dissolve
    play music "BMG_Tarde-Noche.mp3" fadein 3.0 loop
    narrator "Despues de una larga caminata, llegaste a tu casa."
    show bg pieza_noche with dissolve #aun no existe este sprite lol
    narrator "Aunque ahora tenias que decidir..."
    if wow == 1:
        jump wow_pero_despues
    else:
        jump wow_pero_despues

label ruta_extra_1:
            p "Entiendo, Bueno. No tengo nada mas que decirte mas que estudies harto para que te vaya bien en esta prueba."
            show profe feliz
            p "¿Vale? Aun puedes remontar."
            a "Si profesor! Lo hare."
            p "Bien. Ya puedes irte. Que te vaya bien."
            a "Vale, Nos vemos mañana profe."
            play sound "SFX_Pasos.mp3" noloop
            scene bg pasillo_3b with dissolve
            narrator "Saliste rápidamente de la sala de clase, soltando un suspiro..."
            play sound "SFX_Pasos.mp3" noloop
            scene bg camino with dissolve
            stop music fadeout 2.0
            play music "BMG_Tarde-Noche.mp3" fadein 4.0 loop
            a "Para después irte rápidamente de la universidad, te pusiste tus audífonos y empezaste a caminar lentamente…"
            narrator "…Hasta que un extraño chico se te posiciono al lado tuyo mientras caminas hacia tu casa."
            show kevin neutral at fuera_izquierda_al_centro
            n "Hola. ¿Cómo estás? Eres de primer año en la carrera [Carrera], ¿No?"
            narrator "Miraste al chico algo extrañado… ¿Quién inicia una conversación así? Aunque aún así le respondiste sin pensarlo mucho."
            a "Uh… ¿Si? Como lo sabes?"
            show kevin feliz
            n "Jeje! Me presento. Me llamo Kevinazo, soy el tutor de matemáticas."
            a "Oh! Buenas. Me llamo [Jugador]."
            t "Mh, Ya veo..."
            t "Bueno, cuentame..."
            menu decision_EX1:

                set menuset
                t "¿De donde eres?"

                "De aquí":
                    a "Pues de aqui, Por que la pregunta?"
                    t "No, por nada. Solo curiosidad."

                "De otra parte":
                    $ act_l = 1
                    a "De otra parte, Por qué pregunta?"
                    t "Mh! Ya veo. Es solo para conocerte mejor."
label wow_pero_despues_EX1: 
        menu decision_EX2:

            set menuset
            t "Y… ¿Cómo te va haciendo amigos? ¿Has hecho muchos?"

            "Muchos amigos!":
                a "Tengo muchos amigos! Ya hasta tengo un grupito."
                t "Qué bueno! Es bueno tener muchos amigos, así se pueden apoyar mutuamente."

            "Por ahora solo tengo uno":
                a "Por ahora solo tengo un amigo, pero espero ser amigo de más personas!"
                t "Eso es bueno! Mientras tengas las ganas de hacer amigos, todo será más fácil."

            "Estoy trabajando en ello":
                a "Pues estoy trabajando en ello la verdad."
                t "Entiendo. Espero puedas conseguir un buen grupo de amigos pronto."
            
label wow_pero_despues_EX2: 
        menu decision_EX3:

            set menuset
            t "Y cómo van tus notas? He escuchado que a muchos les ha costado bastante."

            "Bien":
                a "Pues bastante bien! Nada que decir la verdad."
                t "Entiendo, bueno. Pues sigue dándolo todo, así conseguirás mejores resultados!"
                a "Entiendo, lo daré todo!"

            "Aguantando como puedo":
                a "Pues he estado aguantándolo como puedo."
                t "Entiendo, bueno. Pues sigue dándolo todo, así conseguirás mejores resultados!"
                a "Entiendo, Daré lo mejor de mí!"

            "Honestamente, Mal":
                a "Bueno… La verdad es que no me ha ido tan bien… Pero puedo remontarla!"
                t "Ya veo, mientras estudies y comprendas los contenidos, Estas para el 7!"
                a "Vale, Estudiare mucho hoy entonces!"
label wow_pero_despues_EX3: 
                narrator "Derrepente, Kevinazo se quedo parado."
                show kevin neutral
                t "Bueno, Aquí nos separamos. Nos vemos! Espero verte mas seguido."
                a "Ah- Claro! ¡Nos vemos!"
                show kevin feliz at salida_izquierda_lenta
                narrator "Después de hablarle al tutor, sentiste como un peso se liberó de ti. Ya no quedaba nada más que llegar a casa."
                play sound "SFX_Pasos.mp3" noloop
                show bg pieza_noche with dissolve #aun no existe este sprite lol
                narrator "Ya una vez en esta… Tenías que decidir qué hacer."
                jump wow_pero_despues

label wow_pero_despues: #Escribe despues de este cuando ya tengas todo el primer dia hecho.
    menu ya_no_se_que_decision_es_esta:

        set menuset
        "¿Que debería hacer?"

        "Dormir sin más":
            a "Fuh.. Que cansancio... Mejor me voy a dormir…"
            stop music fadeout 1.5
            show bg negro with dissolve
            narrator "Y sin más, te acostaste, tus ojos se cerraron por sí solos."
        "Estudiar un poco antes de dormir":
            a "Yo creo que es buena idea estudiar un poco antes de dormir, después de todo tengo un parcial mañana…"
            narrator "Y sin más, te dispusiste a estudiar antes de irte a dormir."
            narrator "Te dormiste un poco más tarde, pero ya estabas para el parcial de mañana."
            narrator "Ya una vez en tu cama, tus ojos se cerraron por sí solos."
            stop music fadeout 1.5
            show bg negro with dissolve
        "No dormir":
            a "¡Es muy temprano como para dormir! ¡Tengo que aprovechar todo el tiempo que tengo!"
            narrator "Así que, empezaste a hacer todo lo posible, estudiar, repasar. Hasta ordenaste tu pieza."
            narrator "Caíste a tu cama totalmente exhausto, durmiéndote casi instantáneamente."
            stop music fadeout 2.0
            show bg negro with dissolve
            if dormir == 1:
                jump fin2
            else:
                jump sales_comprar

            
label wow_pero_despues_de_la_hiper_decision: 
    narrator "Después de una buena dormida..."
    narrator "...Despiertas con las energías totalmente renovadas."
    show bg pieza_dia with dissolve
    play music "Pajaritos.mp3" fadein 2.0 loop
    a "Waah, otro día más de universidad, me pregunto, ¿que hora será?"
    narrator "Te estiras para agarrar tu celular y ver la hora, el cual muestra las 7:30 de la mañana."
    a "¡Que buena hora para despertar e ir a la universidad!"
    narrator "Dijiste, levantándote con todo el ánimo con mucha energía, vistiéndote..."
    narrator "Lavándote los dientes y, finalmente, saliendo de tu casa, sin antes dejar bien cerrado."
    play sound "SFX_Salir.mp3" noloop
    scene bg camino
    play music "BMG_Dia.mp3" fadein 4.0 loop
    a "Huh, ¡Veamos si me pillo a Catamaran de camino!"
    narrator "Decías caminando rápido, esperando a que lo que dijiste se haga realidad."
    narrator "De repente, ves como tu amiga se va acercando hacia ti, solo que..."
    narrator "¿Venía con alguien mas...?"
    narrator "Decidiste acercarte con algo de timidez."
    show catalina feliz at entrada_lenta_izquierda
    show felipe feliz at entrada_lenta_derecha
    a "Emh... Ejem."
    narrator "...No sabes si saludar solo a tu amiga o a ambos."
    menu DIA2_DEC1:

        set menuset
        "¿A quién saludo?"

        "Saludas solo a tu amiga":
            a "¡Ah! Hola Cata ¿cómo estuviste ayer? Al final no te perdiste, ¿o sí?"
            c "¡No, no me perdí!, y creo que me fue bastante bien ayer, además de que entendí todo."
            a "Ah… eso es bueno, me alegro por ti."
            show felipe neutral
            $  Cha = Cha - 1
            jump DIA2_DES2_C
        "Saludas a ambos":
            a "¡Hola Cata! ...Y hola a ti también."
            c "¡Hola, [Jugador]! ¿Cómo te fue ayer?"
            if dormir == 1:
                a "Oh... Pues, digamos que... No fui a la universidad ayer."
                c "¡Oh! ¡Entiendo, Jeje!"
                a "Pero bueno... ¿Y a ti cómo te fue?"
                c "¡Pues a mí me fue bastante bien! Además de que entendí casi todo lo que vi ayer."
                narrator "Miraste hacia el desconcido, como si quisieras iniciar una conversación con él indirectamente."
                n "Ejem, ¡Hola amigo! ¿Cuál es tu nombre? Para saber cómo llamarte."
                $  Cha = Cha + 1
            else:
                a "Bastante bien, la verdad. Hablé con el jefe de carrera y el tutor. ¿Y a ti cómo te fue?"
                c "A mí me fue bastante bien, además de que entendí casi todo lo que vi ayer."
                narrator "Miraste hacia el desconcido, como si quisieras iniciar una conversacion con él indirectamente."
                n "Ejem, ¡Hola amigo! ¿Cuál es tu nombre? Para saber cómo llamarte."    
                $  Cha = Cha + 1
label nombre:
    menu HOLAA:
        set menuset
        narrator "No estás seguro de querer decirle tu nombre a alguien que no conoces, pero también podría servir para hacer amigos."

        "Le digo mi nombre":
            a "Ah, soy [Jugador], un gusto."
            $ Cha = Cha + 1
            $ Flag1 = Flag1 +1
        "No le digo mi nombre":
            a "La verdad es que no veo por qué te debería importar."
            show felipe incomodo 
            show catalina neutral
            narrator "Felipe y Catamaran se quedaron viéndose. Se notaban algo incómodos."
            $ Cha = Cha -1
            jump DIA2_DES2_C
label DIA2_DES1:
    show felipe feliz
    n "Yo me llamo Felipe. ¡Te ves super buena onda! Asi de pasada ha sido un gusto conocerte."
    narrator "Decia Felipe, mientras extendía su mano."
    menu DIA2_DEC2:
        set menuset
        narrator "Aun estás algo inseguro de darle la mano... ¿Qué debería hacer?"
        "Le dices que ha sido un gusto conocerlo también y le das la mano":
            narrator "Tú y Felipe se dieron un buen apretón de manos."
            narrator "...Su mano estaba fría."
            f "Jeje. ¿Y que planes tienen para hoy?"
            $ Voley = Voley + 1
            $ Cha = Cha + 1
            jump DIA2_DES2
        "Le dices que ok de manera insegura y no le das la mano":
            f "...Erm ...Y qué planes tienen para hoy?"
            $ Cha = Cha - 1
        "Le dices que es un gusto, pero no le das la mano":
            f "Y bueno... ¿Qué planes tienen para hoy?"
            $ Cha = Cha + 1

label DIA2_DES2_C:
    if Flag1 == 1:
        jump DIA2_DES2
    c "...Bueno, Eh... ¿Qué planes tienen para hoy?"
    show catalina feliz
    show felipe neutral 
label DIA2_DES2:
    menu DIA2_DEC3:

        set menuset
        "Huh... ¿Qué deberia decir?"

        "La verdad es que no tengo nada en mente de momento":
            c "Oh, eso es normal, con todas las vueltas en la U en estos pocos días."
        "La verdad es que planeo estudiar un poco más rato":
            c "Suena buena idea, siempre es bueno repasar y estudiar un poco para estar seguros en cualquier situación."
        "La verdad es que planeo estudiar toda la tarde llegando a mi casa":
            c "No deberías sobresaturarte mucho estudiando, ¡Te puede hacer mal!"
label DIA2_DES3:
    narrator "Los tres seguimos conversando, hasta llegar a la universidad."
    play sound "SFX_Pasos.mp3" noloop
    scene bg entrada_ula
    show catalina feliz at mitad_mitad_izquierda
    show felipe feliz at mitad_mitad_derecha
    a "Bueno, ¡nos vemos más tarde! O quizás en un rato más, quién sabe."
    c "Sí, nos vamos rápido porque ya estamos algo tarde."
    f "¡Eso! ¡Adiós!"
    hide catalina feliz with dissolve
    hide felipe feliz with dissolve
    play sound "SFX_Pasos.mp3" noloop
    scene bg clase with dissolve
    narrator "Entras a la sala que te corresponde y buscas un asiento vacío para poder sentarte."
    narrator "Rapidamente te sientas y esperas que llegue el profesor."
    if Voley == 1:
                narrator "Viendo cómo se demora un poco, sacaste tu celular, viendo todas las notificaciones."
                narrator "Notando como alguien llamado 'Xx_Felipe_Kawaii_xX' en Instagram te envió solicitud de amistad."
                a "Huh..."
    narrator "De la nada, el profesor entró a la sala de clases."
    show profe feliz at fuera_izquierda_al_centro
    p "Bueno chicos y chicas, ¿recuerdan que dije que íbamos a hacer un parcial el día de hoy?"
    show profe neutral
    p "Resulta que... Todo el departamento de [Carrera] había hablado de que este parcial iba a ser una nota grupal..."
    show profe feliz
    p "¡Así que! Reúnanse en grupos para hacer la actividad por favor."
    narrator "Decía el profesor, mientras se iba a sentar en su mesa para corregir unas pruebas de otra sección."
    hide profe feliz with dissolve
    menu DIA2_DEC4:
        
        set menuset
        "¿Qué haces?"

        "Decides ir y preguntarle a algunos de tus compañeros si quieren hacer grupo contigo":
            narrator "Miraste hacia los lados, viendo como a muchas personas les faltaba grupo."
            narrator "Te paraste y decidiste ir hacia la persona que estaba más cerca de ti."
            a "¡Hola! ¿Quería saber si puedo hacer grupo con ustedes? Si no es molestia"
            n "Oh, ¡sí puedes ser con nosotros!"
            narrator "Decían mientras hacían un espacio para que te sentaras."
            a "¡Oh! ¡Perfecto!"
            narrator "Decías mientras te sentabas, empezando a realizar el trabajo."
            narrator "Después de un rato, el tiempo se acabó y la clase terminó."
            narrator "Te preparaste para, finalmente, irte."
            play sound "SFX_Pasos.mp3" noloop
            stop music fadeout 2.0
            scene bg entrada_ula
            play music "BMG_Tarde-noche.mp3" fadein 3.0
            narrator "Caminando lentamente, sin ninguna prisa."
            scene bg camino
            play sound "SFX_Pasos.mp3" noloop
            narrator "De la nada, notaste una cara conocida..."
            a "Ese no es...?"
            $ Cha = Cha + 2
            $ Extro = Extro + 1
            $ Voley = Voley - 1
            jump DIA2_DES4
        "Esperas a ver si alguno de tus compañeros te pregunta":
            narrator "Te quedaste viendo a la nada, esperando si es que alguien te venía..."
            narrator "¡Cuando de repente!"
            n "Oye, vi que estás solo. ¿Te falta grupo? De ser así puedes ser con nosotros."
            a "Oh, gracias, ¡de hecho sí me faltaba un grupo para trabajar!"
            n "¡Ah! Perfecto, ¡entonces hagámoslo!"
            narrator "Despues de un rato, el tiempo se acabó y la clase terminó."
            narrator "Te preparaste para, finalmente, irte."
            play sound "SFX_Pasos.mp3" noloop
            stop music fadeout 3.0
            scene bg entrada_ula
            play music "BMG_Tarde-noche.mp3" fadein 3.0
            narrator "Caminando lentamente, sin ninguna prisa."
            scene bg camino
            play sound "SFX_Pasos.mp3" noloop
            narrator "De la nada, notaste una cara conocida..."
            a "Ese no es...?"
            $ Cha = Cha - 1
            $ Intro = Intro + 1
            $ Voley = Voley - 1
            jump DIA2_DES4
        "Decides hacer el trabajo solo":
            $ Cha = Cha - 2
            $ Intro = Intro + 2
label DIA2_PROF:
    narrator "El profesor se te quedó viendo, yendo hacia donde estabas."
    show profe neutral at fuera_izquierda_al_centro
    menu DIA2_DEC5_PROF:

        set menuset
        p "Veo que sigue sin equipo, ¿Planea hacer el trabajo sin compañeros?"

        "Le dices que no encontraste grupo.":
            a "Sí, profesor, es que no logré encontrar un grupo al que le faltaran persona."
            show profe incomodo
            p "...Está bien."
            hide profe feliz with dissolve
            narrator "Luego de preguntarme, el profesor volvió a sentarse para volver a corregir pruebas."
            narrator "Aunque el profesor no se veía muy satisfecho con mi respuesta..."
            narrator "...Considerando que habian muchos grupos que les faltaban personas, pero bueno."

        "Le dices que preferías hacerlo de manera individual":
            a "Sí, profesor, me gusta más trabajar individualmente que en grupo, ¿me entiende?"
            show profe feliz
            p "¡Oh! Está bien."
            hide profe feliz with dissolve
            narrator "Luego de preguntarme, el profesor volvió a sentarse para volver a corregir pruebas."
    narrator "Después de realizar el trabajo, la clase terminó."
    scene bg pasillo_3b
label saltito:
    if Voley == 1:
        jump voley
    else:
        narrator "Y empezaste a caminar hacia tu casa."
        play sound "SFX_Pasos.mp3" noloop
        stop music fadeout 3.0
        scene bg entrada_ula
        play music "BMG_Tarde-noche.mp3" fadein 3.0
        narrator "Caminando lentamente, sin ninguna prisa."
        scene bg camino
        play sound "SFX_Pasos.mp3" noloop
        narrator "De la nada, notaste una cara conocida..."
        a "Ese no es...?"

label DIA2_DES4:
    if Ruta_tutor != 1:
        narrator "¡Justo te encuentras con el jefe de carrera de camino!"
        show juan feliz at fuera_izquierda_al_centro
        j "Hola, [Jugador], ¿cómo has estado desde ayer?"
    else:
        narrator "¡Justo te encuentras con el tutor de camino!"
        show kevin feliz at fuera_izquierda_al_centro
        t "Hola, [Jugador], ¿cómo has estado desde ayer?"
    menu DIA2_DEC6:

        set menuset
        "Piensas un poco en tu día antes de responderle"

        "¡Gracias por preguntar! He estado bien hoy":
            $ Cha = Cha + 1
        "La verdad es que he estado normal desde ayer":
            $ Cha = Cha - 1
    if Ruta_tutor != 1:
        j "Es bueno que no estés mal, ¿y como te fue con el tutor ayer?"
        if dormir == 1:
            a "Eh? De que habla?"
            j "¡Oh! No fuiste a la universidad ayer?"
            a "Erm... Pues no."
            show juan neutral
            j "Ya veo..."
            narrator "El jefe de carrera se rasco la cabeza... Parecía algo incomodo."
            j "Chu... Se suponía que el tutor iba a preguntar esto, pero bueno."
            narrator "Decía el jefe de carrera, aclarando su garganta antes de preguntar."
            show juan feliz
            menu DIOS_MIO:
            
                set menuset
                j "De donde eres?"

                "De aquí":
                    a "Pues de aquí, Por que la pregunta?"
                    j "Oh, erm... No por nada."
                    a "Huh..."
                    j "Ejem, ¡Ah!"

                "De otra parte":
                    $ act_l = 1
                    a "De otra parte, Por qué pregunta?"
                    j "Oh, Ejem... Por nada."
                    a "Huh..."
                    j "Ejem, ¡Ah!"
        else:
            a "Ayer, hablé con él, pero me dijo que me hablaría para organizar bien las fechas, así que no he sabido nada."
            j "Ya veo..."
    else:
        t "Es bueno que no estés mal, ¿y como te fue con el jefe de carrera ayer?"
        if dormir == 1:
            a "Eh? De que habla?"
            t "¡Oh! No fuiste a la universidad ayer?"
            a "Erm... Pues no."
            show kevin neutral
            t "Ya veo..."
            show kevin feliz
            menu DIOS_MIO2:
            
                set menuset
                t "De donde eres?"

                "De aquí":
                    a "Pues de aquí, Por que la pregunta?"
                    t "Oh! No, por nada."

                "De otra parte":
                    $ act_l = 1
                    a "De otra parte, Por qué pregunta?"
                    t "Oh, por nada."
        else:
            a "Ayer, hablé con él, pero me dijo que me hablaría para organizar bien las fechas, así que no he sabido nada."
            t "Ya veo..."
label DIA2_DES5:
    if Voley == 1:
        show felipe feliz at mitad_centro
        f "A todo esto, ¿sabes cuáles son tus metas?"
        a "¿Eh...? ¿A qué te refieres?"
        f "Tipo, por qué te metiste a la carrera? ¿Que meta quieres cumplir?"
    elif Ruta_tutor == 1:
        show kevin feliz at mitad_centro
        t "A todo esto, ¿sabes cuáles son tus metas?"
        a "¿Eh...? ¿A qué te refieres?"
        t "Tipo, por qué te metiste a la carrera? ¿Que meta quieres cumplir?"
    else:
        show juan feliz at mitad_centro
        j "A todo esto, ¿sabes cuáles son tus metas?"
        a "¿Eh...? ¿A qué te refieres?"
        j "Tipo, por qué te metiste a la carrera? ¿Que meta quieres cumplir?"
    menu DIA2_DEC7:
        set menuset
        "Huh... ¿Que le digo?"

        "La verdad es que me meti a la carrera porque eh escuchado que pagan bien.":
            if Voley == 1:
                f "No creo que ese sea un buen motivo ni meta, pero en algunos casos si pagan bien."
                f "¡Pero igual! Es bueno que tengas una meta, ¡Espero puedas cumplirla!"
                a "¡Jeje! ¡Muchas gracias!"
                jump SALTA
            elif Ruta_tutor == 1:
                t "¡Pero igual! Es bueno que tengas una meta, ¡Espero puedas cumplirla!"
                a "¡Jeje! ¡Muchas gracias!"
                t "Bueno, Tengo cosas que hacer. ¡Nos vemos!"
                a "Ah! Claro, ¡nos vemos!"
                hide kevin feliz with dissolve
                narrator "Luego de eso, el tutor se fue caminando, Tu, por tu parte seguiste caminando hacia tu casa."
            else:
                j "¡Pero igual! Es bueno que tengas una meta, ¡Espero puedas cumplirla!"
                a "¡Jeje! ¡Muchas gracias!"
                j "Bueno, Tengo cosas que hacer. ¡Nos vemos!"
                a "Ah! Claro, ¡nos vemos!"
                hide juan feliz with dissolve
                narrator "Luego de eso, el jefe de carrera se fue caminando, Tu, por tu parte seguiste caminando hacia tu casa."
        "Si, tengo muy claras mis metas para ahora y el futuro":
            $ act_m = act_m+1
            if Voley == 1:
                f "Eso es muy bueno, ¡tener asi de claras tus metas te va a ayudar mucho!"
                a "¡Claro! ¡Ya se lo que quiero!"
                f "¡Jaja! Eso es bueno."
                jump SALTA
            elif Ruta_tutor == 1:
                t "Eso es muy bueno, ¡tener asi de claras tus metas te va a ayudar mucho!"
                a "¡Claro! ¡Ya se lo que quiero!"
                t "¡Jaja! Eso es bueno."
                t "Bueno, Tengo cosas que hacer. ¡Nos vemos!"
                a "Ah! Claro, ¡nos vemos!"
                hide kevin feliz with dissolve
                narrator "Luego de eso, el tutor se fue caminando, Tu, por tu parte seguiste caminando hacia tu casa."
            else:
                j "Eso es muy bueno, ¡tener asi de claras tus metas te va a ayudar mucho!"
                a "¡Claro! ¡Ya se lo que quiero!"
                j "¡Jaja! Eso es bueno."
                j "Bueno, Tengo cosas que hacer. ¡Nos vemos!"
                a "Ah! Claro, ¡nos vemos!"
                hide juan feliz with dissolve
                narrator "Luego de eso, el jefe de carrera se fue caminando, Tu, por tu parte seguiste caminando hacia tu casa."
        "La verdad es que no tengo tanta seguridad de mis metas, me meti a la carrera porque es la que más me llamo la atención":
            if Voley == 1:
                f "Hum… Eso no es muy bueno, puede que te aburras durante la carrera o incluso que en el proceso encuentres tus metas."
                f "¡Te recomiendo seguir buscando para que definas lo que quieras hacer!"
                a "Entiendo. ¡Muchas gracias por el consejo!"
                f "¡Jaja! ¡Para eso estamos!"
                jump SALTA
            if Ruta_tutor == 1:
                t "Hum… Eso no es muy bueno, puede que te aburras durante la carrera o incluso que en el proceso encuentres tus metas."
                t "¡Te recomiendo seguir buscando para que definas lo que quieras hacer!"
                a "Entiendo. ¡Muchas gracias por el consejo!"
                t "¡Jaja! ¡Para eso estamos!"
                t "Bueno, Tengo cosas que hacer. ¡Nos vemos!"
                a "¡Ah! Claro, ¡nos vemos!"
                hide kevin feliz with dissolve
                narrator "Luego de eso, el tutor se fue caminando, Tu, por tu parte seguiste caminando hacia tu casa."
            else:
                j "Hum… Eso no es muy bueno, puede que te aburras durante la carrera o incluso que en el proceso encuentres tus metas."
                j "¡Te recomiendo seguir buscando para que definas lo que quieras hacer!"
                a "Entiendo. ¡Muchas gracias por el consejo!"
                j "¡Jaja! ¡Para eso estamos!"
                j "Bueno, Tengo cosas que hacer. ¡Nos vemos!"
                a "Ah! Claro, ¡nos vemos!"
                hide juan feliz with dissolve
                narrator "Luego de eso, el jefe de carrera se fue caminando, Tu, por tu parte seguiste caminando hacia tu casa."

label fin:
    show bg camino with dissolve
    narrator "Y despues de una larga caminata, llegaste a tu casa."
    show bg pieza_noche with dissolve
    a "Fuah... Que cansancio tengo..."
    stop music fadeout 2.0
    narrator "Decías, recostandote en la cama y cerrando tus ojos."
    show bg negro with dissolve
    show catalina feliz at fuera_izquierda_al_centro
    c "¡Oye! ¡Aun el juego no puede terminar sabes!"
    play music "Resultados.mp3" loop
    show bg pieza_noche
    a "¿¡UAH!? ¿¡Catamaran!? ¿¡Que haces aqui!?"
    show catalina neutral
    c "¿Que no es obvio?"
    show catalina feliz
    c "¡Vengo a darte los resultados!"
    a "¿Resultados...? ¿Que estas hablando...?"
    show catalina incomodo
    c "Ugh! No te hablo a ti."
    show catalina feliz
    c "¡Te hablo a TI!"
    c "¡Si! ¡Tu, jugador!"
    a "¿Eh...? ¿Que...?"
    c "Dejame te enseño los resultados, ¿vale?~"
    scene bg cielo with dissolve
    a "¡Wahh...! ¿¡Donde estoy...!?"
    show catalina feliz at entrada_lenta_izquierda
    c "Eso no importa. ¡Lo que importa es esto! ¡Mira atentamente!"
    hide catalina feliz with dissolve
    show cuadrado at amongus
    centered "{color=#ffffff}¡Resultados!{/color}"
    if Cha>=-8 and Cha<=-5:
        centered "{color=#ffffff}Cha:[Cha]/6\nNo es por sonar pesada... pero con tu forma de ser, se te puede resultar complicado hacer amigos.\n"
    elif Cha>=-4 and Cha <= -1:
        centered "{color=#ffffff}Cha:[Cha]/6\nTe va a costar hacer amigos, te recomiendo mejorar tu forma de responder para que hacer amigos se te sea más fácil.\n"
    elif Cha==1 or Cha==0:
        centered "{color=#ffffff}Cha:[Cha]/6\nEs una persona neutra puede que le cueste hacer amigos o no, depende de cómo te sientas.\n"
    elif Cha>=2 and Cha<=5:
        centered "{color=#ffffff}Cha:[Cha]/6\nNo tendrás problemas en hacer amigos, pero con algunos tipos de persona no te puedes relacionar tan bien.\n"
    else:   
        centered "{color=#ffffff}Cha:[Cha]/6\nCon tu forma de ser, no se le hará problema hacer amigos, asi que ve y cosigue un buen grupo de amigos!~\n"
    
    if Res==-2 or Res==-1:
        centered "{color=#ffffff}Res:[Res]/3\nTienes poco sentido de la responsabilidad, se te va a complicar adaptarte a muchas cosas en la universidad.\n"
        centered "{color=#ffffff}Res:[Res]/3\nPero con esfuerzo, Puedes mejorarlo!.\n"
    elif Res==0:
        centered "{color=#ffffff}Res:[Res]/3\nTe va costar el cambio a la universidad."
        centered "{color=#ffffff}Res:[Res]/3\nTe recomiendo mejorar tu sentido de la responsabilidad para adaptarte mejor a la universidad.\n"
    elif Res==1 or Res==2:
        centered "{color=#ffffff}Res:[Res]/3\nTienes un buen sentido de la responsabilidad, pero puedes mejorarlo aun mas!\n"
    else:
        centered "{color=#ffffff}Res:[Res]/3\nTienes un fuerte sentido de la responsabilidad, no te constara tanto al cambio!~\n"

    if Int==-4 or Int==-3:
        centered "{color=#ffffff}Int:[Int]/5\nAdaptarte te será difícil, pero si aprendes sobre hábitos de estudio y te mantienes constante puedes mejorarlo.\n"
    elif Int==-2 or Int==-1:
        centered "{color=#ffffff}Int:[Int]/5\nQuizas aun no estas perfectamente acostumbrado a la universidad, debes seguir estudiando con regularidad para adaptarte.\n"
    elif Int==0:
        centered "{color=#ffffff}Int:[Int]/5\nEres una persona  que tiene potencial pero que quizás no lo intenta lo suficiente.\n"
    elif Int==1 or Int==2:
        centered "{color=#ffffff}Int:[Int]/5\nSabes algunas cosas pero es importante siempre aprender más.\n"
    elif Int==3 or Int==4:
        centered "{color=#ffffff}Int:[Int]/5\nEres bastante inteligente, si estudias usualmente tu adaptación estará casi asegurada.\n"
    else: 
        centered "{color=#ffffff}Int:[Int]/5\nEres muy inteligente, no deberías tener problemas adaptándose mientras tengas un poco de cuidado.\n"

    if Intro>Extro:
        centered "{color=#ffffff}Intro:[Intro]\nEres una persona muy introvertida, puede que se te haga problemas hacer amigos, pero si es que te determinas a ello, podrás lograrlo!\n"
    elif Extro>Intro:
        centered "{color=#ffffff}Extro:[Extro]\nEres una persona muy extrovertida, no se te hará problemas hacer amigos. ¡Así que consigue un buen grupo de amigos!\n"
    else:
        centered "{color=#ffffff}Intro:[Intro]=Extro:[Extro]\n No eres ni extremadamente introvertido o extrovertido, lo cual es algo bueno! Puede que se haga fácil o se te complique hacer amigos, dependiendo de la situacion.\n"

    if act_m==1:
        centered "{color=#ffffff}Como tienes tus metas claras, sabes a lo que vienes, asi que se te hara más fácil adaptarte a la universidad."

    else:
        centered "{color=#ffffff}Como no tienes tus metas claras, se te puede dificultar un poco adaptarte a la universidad, ya que no sabes con certeza a lo que vienes a esta.\n"

    if act_l==1:
        centered "{color=#ffffff}Como eres de otra parte, lo más probable es que perderá su círculo social, es importante que busque un grupo en donde apoyarse.\n"
    else:
        centered "{color=#ffffff}Como eres de aquí, no perderás tu circulo social, asi que igual es bueno apoyar a las personas que pierdan su circulo social, asi podras tener mas amigos.\n"

    show catalina feliz at fuera_izquierda_al_centro
    c "Bien! Con esto dicho, Espero te haya gustado el juego."
    c "Y que te haya dando algunos consejos para poder adaptarte de mejor manera a la vida universitaria!"
    show catalina triste
    c "Recuerda que, puede que sea un camino dificil."
    show catalina feliz
    c "Pero hechandole ganas, podras lograr cualquier cosa!"
    c "Bien, Nos vemos y gracias por jugar!"
    hide catalina feliz with dissolve
    show bg negro with dissolve
    centered "{color=#ffffff}Final Bueno! Lograste que catamaran te diera tus resultados!"

    return
return


return
# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define c = Character("Catamaran", color="#d72bee")
define a = Character("[Jugador]")
define n = Character("???")
define p = Character("Profe Andre", color="#b1ea35")
define t = Character("Kevinzo", color="#51ee32")
define j = Character("Juan II", color="#3d3b96")
define f = Character("Felipe")
image catalina feliz = "CATA_FELIZ.png"
image catalina triste = "CATA_TRISTE.png"
image catalina neutral = "CATA_NORMAL.png"
image catalina incomodo = "CATA_INC.png"
image felipe feliz = "FELIPE_INC.png"
image felipe neutral = "FELIPE_INC.png"
image felipe triste = "FELIPE_INC.png"
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
    linear 0.3 xalign 0.3  # en 2 segundos va a la posición deseada

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
    "¿Vuelves a dormir?"

    "Si":
            $ Res = Res - 1
            a "Bah, unas cuantas horas de sueño extra no harán mal…"
            narrator "Te dijiste a ti mismo, mientras te volvías a recostar, cerrando tus ojos…"
            narrator "De la nada, te despertaste de repente, incluso hasta un poco con miedo, pero con tus 8 horas de sueño."
            a "Wahhh! Que buena dormida. Uy, ¿Qué hora es?"
            a "..."
            a "¿¡LAS 1 DE LA TARDE?!"
            a "Diablos… Me perdí todas mis clases!"
            narrator "Soltaste un largo suspiro."
            a "Bueno, supongo que si no fui a clase al menos debería ordenar la casa..."
            narrator "Dijiste mientras te levantabas de la cama, vistiendote y comenzando a ordenar."
            narrator "Estuviste todo el dia ordenando tu casa. Ya en la tarde..."
            a "Fuah... Estuve todo el dia limpiando... ¡Pero al menos la casa quedo limpiecita!"
            narrator "Aunque, ahora tienes que decidir que hacer..."
            jump wow_pero_despues

    "No":
        $ Res = Res + 1
        a "Urm… No! Tengo que ir a clase, Ademas es la hora perfecta para ir!"
        narrator "Dijiste, levantándote con todo el animo que podias, vistiéndote..."
        narrator "Lavándote los dientes y finalmente, saliendo de tu casa, sin antes dejar bien cerrado."
        scene bg camino
        narrator "Tomando un buen puñado de aire, empezaste a caminar hacia la universidad."
        narrator "Mientras veías como el chat grupal de la carrera se llenaba de mensajes."
        a "Tsk... No es necesario que cuenten toda su vida..."
        narrator "Decías mientras guardabas tu teléfono en tu bolsillo, hasta que de la nada, escuchaste a alguien llamando tu nombre."
        n "[Jugador]!!!"
        narrator "Miraste con curiosidad hacia la direccion de donde venian los gritos."
        narrator "Venia corriendo hacia ti una chica bastante alegre."
        show catalina feliz at entrada_lenta_izquierda
        c "Wahh!!! Qué bueno encontrarte [Jugador]!"
        narrator "Es Catalina, una de las únicas amigas que, hasta el momento tengo en la universidad."
        narrator "Es una buena amiga, aunque puede llegar a ser algo molesta."
        c "Bueno... Cuéntame. ¿Cómo estuvo tu fin de semana?"
        menu segunda_decision:
            set menuset
            "Como deberia responderle?"

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

    "Se resuelve usando la fórmula del cubo de binomio":
        $ Int = 1
        p "Mh... Veamos."
        "El profesor utilizó la fórmula que antes mencionaste, resolviendo el ejercicio rápidamente."
        p "¡Correcto! Felicidades, [Jugador]."
        a "¡Bien! Menos mal estudié un poco ayer."

    "Se resuelve usando la fórmula del cuadrado perfecto":
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
                p "Ya veo... Deberías ir a ver al jefe de carrera, veremos si puedes hacer una prueba recuperativa. Dependerá de la nota de tu siguiente parcial."
                p "Por cierto, se llama Juan II."
                a "Vale... Muchas gracias, profesor."


    "La verdad no he tenido mucho tiempo para estudiar.":
        $ Cha = Cha + 1
        p "Ya veo... Deberías ir a ver al jefe de carrera, veremos si puedes hacer una prueba recuperativa. Dependerá de la nota de tu siguiente parcial."
        p "Por cierto, se llama Juan II."
        a "Vale... Muchas gracias, profesor."

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
            $ Extro = Extro + 1
            "Es mejor, asi no los interrumpo... Puede que esten hablando algo importante..."
            "Aunque... El jefe de carrera se percato que lo quede viendo, y junto con la otra persona, vinieron hacia donde estaba."
            j "Vi que te quedaste viendonos... Querias hablar con alguno de nosotros?"
            a "A...ah! Sip, vera..."
            
label wow_pero_despues_5:
    a "Mi nombre es [Jugador]... El profesor Andre me dijo que venga a hablar con usted... Les molesto?"
    t "Oh, No no… El jefe de carrera es todo tuyo. Aunque también me gustaría hablarte después."
    narrator "Dijo el tutor mientras se iba un poco al lado para no estorbar entre la conversación, poniéndose sus audífonos y viendo su telefono."
    menu quintaa_desicion:

        set menuset
        j "Bueno, ¿Cuéntame para que necesitas hablarme?"

        "Nada en específico":
            a "Pues nada en específico la verdad. Como dije antes, el profesor me envió para que hablara con usted."
            j "Huh, Supongo que si te dijo que vinieras a hablarme es por algo de tus notas, o lo del remedial…"
            j "Para eso tienes que hablarle al tutor. Él sabe sobre eso."

        "Sobre los remediales":
            a "Pues, quería ver si es que tenía la oportunidad de dar una prueba remedial."
            j "Ah, ya veo…"
            j "Para eso tienes que hablarle al tutor. Él sabe sobre eso."

        "Sobre mis notas":
            a "Pues, es sobre mis notas… No han estado muy bien…"
            j "Ah, ya veo…"
            j "Para eso tienes que hablarle al tutor. Él sabe sobre eso."
            
label wow_pero_despues_55: 

    a "Ah! ¡Perfecto! ¿Y quién es el tutor?"
    j "Pues, el chico con en que estaba hablando antes."
    a "Oh, ya veo. Bueno, en ese caso le hablare a él. Muchas gracias!"
    j "Por cierto..."
    menu Sexta_desicion:

        set menuset
        j "De donde eres?"

        "De aqui":
            a "Pues de aqui, Por que la pregunta?"
            j "Oh! No, por nada."

        "De otra parte":
            $ act_m = 1
            a "De otra parte, Por qué pregunta?"
            j "Oh, por nada."
label wow_pero_despues_6: 
    j "Bueno, me tengo que ir. Nos vemos despúes."
    a "Oh! Está bien, nos vemos!"
    narrator "Después de hablar con el jefe de carrera, me gire hacia donde estaba el tutor, aun viendo su celular con sus audífonos puestos."
    a "Eh... ¿Disculpa?"
    t "Ah? Si si, perdona… Cuéntame, que necesitas?"
    a "Pues… No sé si escuchaste…"
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
            a "Pues he estado aguantándo como puedo."
            t "Claro, entiendo. Bueno, Ahí te hablare para coordinar mejor ese tema. ¿Vale?"
            a "Vale! Muchas gracias."
        "Decirle porque vienes a hablarle":
            a "Bueno… Si enserio escucho como me ha ido, pues…"
            t "Entiendo, bueno. Ahí te hablare para coordinar mejor ese tema. ¿Vale?"
            t "Tu solo enfócate en estudiar mas, vale?"
            a "Vale! Muchas gracias."
label wow_pero_despues_7: 
    narrator "Despues de hablarle al tutor, sentiste como un peso se liberó de ti. Ya no quedaba nada más que hacer, que irte a casa."

label ruta_extra_1:
    p "Entiendo, Bueno. No tengo nada mas que decirte mas que estudies harto para que te vaya bien en esta prueba. ¿Vale? Aun puedes remontar."
    a "Si profesor! Lo hare."
    p "Bien. Ya puedes irte. Que te vaya bien."
    a "Vale, Nos vemos mañana profe."
    scene bg camino
    narrator "Saliste rápidamente de la sala de clase, soltando un suspiro para después irte rápidamente de la universidad, te pusiste tus audífonos y empezaste a caminar lentamente…"
    narrator "…Hasta que un extraño chico se te posiciono al lado tuyo mientras caminas hacia tu casa."
    show kevin neutral at entrada_lenta_izquierda
    n "Hola. ¿Cómo estás? Eres de primer año en la carrera [Carrera], ¿No?"
    narrator "Miraste al chico algo extrañado… ¿Quien inicia una conversación así? Aunque aún así le respondiste sin pensarlo mucho."
    a "Uh… ¿Si? Como lo sabes?"
    n "Jeje! Me presento. Me llamo Kevinazo, soy el tutor de matemáticas."
    a "Oh! Buenas. Me llamo [Jugador]."
    t "Mh, Ya veo..."
    menu decision_EX1:

        set menuset
        t "¿Como les va a los de primer año?"

        "De aquí":
            a "Pues de aqui, Por que la pregunta?"
            t "No, por nada. Solo curiosidad."

        "De otra parte":
            $ act_m = 1
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
            narrator "Así que si más, Te pusiste tus audífonos y empezaste a caminar hacia tu casa."
label wow_pero_despues_EX3: 
    narrator "Derrepente, Kevinazo se quedo parado."
    t "Bueno, Aquí nos separamos. Nos vemos! Espero verte mas seguido."
    a "Ah- Claro! ¡Nos vemos!"
    narrator "Después de hablarle al tutor, sentiste como un peso se liberó de ti. Ya no quedaba nada más que llegar a casa."
    narrator "Ya una vez en esta… Tenías que decidir qué hacer."
    jump wow_pero_despues

label wow_pero_despues: #Escribe despues de este cuando ya tengas todo el primer dia hecho.

    menu ya_no_se_que_decision_es_esta:

        set menuset
        "¿Que deberia hacer?"

        "Dormir sin más":
            a "Fuh.. Que cansancio... Mejor me voy a dormir…"
            narrator "Y sin más, Te acostaste, tus ojos se cerraron por si solos."
        "Estudiar un poco antes de dormir":
            a "Yo creo que es buena idea estudiar un poco antes de dormir, después de todo tengo un parcial mañana…"
            narrator "Y sin más, Te dispusiste a estudiar antes de irte a dormir. Te dormiste un poco más tarde, pero ya estabas para el parcial de mañana."
            narrator "Ya una vez en tu cama, tus ojos se cerraron por si solos."
        "No dormir":
            a "Es muy temprano como para dormir! Tengo que aprovechar todo el tiempo que tengo!"
            narrator "Así que, empezaste a hacer todo lo posible, estudiar, repasar, Hasta ordenaste tu pieza"
            narrator "Caíste a tu cama totalmente exhausto, durmiéndote casi instantáneamente."
            
label wow_pero_despues_de_la_hiper_decision: 

    a "Waah, otro día más de universidad, me pregunto que hora será"
    narrator "Te estiras para agarrar tu celular y ver la hora, el cual muestra las 7:30 de la mañana"
    a "Que buena hora para despertar e ir a la universidad"
    narrator "Te levantas y te arreglas para salir de a la U, en el camino hacia esta, ves a lo lejos a tu amiga, y al mirar mejor pareciera que esta con alguien que no conoces."
    narrator "Te acercas y no estas seguro si saludar solo a tu amiga o ambos."
    scene bg camino
    menu DIA2_DEC1:

        set menuset
        "¿A quien saludo?"

        "Saludas solo a tu amiga":
            a "¡Ah! Hola cata ¿Como estuviste ayer? al final no te perdiste ¿O si?"
            c "¡No, no me perdi!, y creo que me fue bastante bien ayer, además de que entendí todo"
            a "Ah… eso es bueno, me alegro por ti"
        "Saludas a ambos":
            a "¡Hola cata! Y hola a ti también"
            c "¡Hola [Jugador]! ¿Como te fue ayer?"
            a "Bastante bien, la verdad hable con el jefe de carrera y el tutor ¿Y a ti como te fue?"
            c "A mi me fue bastante bien, además de que entendí casi todo lo que vi ayer"
            n "Hola amigo ¿Cual es tu nombre? Para saber como llamarte"
label DIA2_DES1:
    narrator "No estas seguro de querer decirle tu nombre a alguien que no conoces, pero también podría servir para hacer amigos"
    a "Oh perdón, no me presente, soy [Jugador] ¿El tuyo?"
    menu DIA2_DEC2:
        
        set menuset
        n "Yo me llamo Felipe, te ves super buena onda!, asi de pasada ah sido un gusto conocerte"

        "Te extiende la mano, y no estas seguro si tomarla o no, o como responderle":
            f "Y que planes tienen para hoy?"
            Voley = Voley + 1
            jump DIA2_DES2
        "Le dices que ah sido un gusto conocerlo también y le das la mano":
        "Le dices que ok de manera insegura y no le das la mano":
        "Le dices que es un gusto pero no le das la mano":
label DIA2_DES2_C:
    narrator "Esto lleva a que Cata haga una pregunta"
    c "Y que planes tienen para hoy?"
label DIA2_DES2:
    menu DIA2_DEC3:

        set menuset
        "En respuesta a la pregunta de que planes hay"

        "La verdad es que no tengo nada en mente de momento":
            c "Oh, eso es normal, con todas las vueltas en la U en estos pocos días"
        "La verdad es que planeo estudiar un poco más rato":
            c "Suena buena idea, siempre es bueno repasar y estudiar un poco para estar seguros en cualquier situación"
        "La verdad es que planeo estudiar toda la tarde llegando a mi casa":
            c "No deberías sobresaturarte mucho estudiando, te puede hacer mal"
label DIA2_DES3:
    narrator "Durante la conversación llegan los tres a la universidad y se separan llendo cada uno a sus clases"
    scene bg entrada_ula
    a "Bueno, nos vemos más tarde!, o quizás en un rato más, quien sabe"
    c "Si, nos vamos rápido porque ya vamos algo tarde"
    f "Eso!, adiós!"
    scene bg clase
    narrator "Entras a la sala que te corresponde y buscas un asiento vacio para poder sentarte, cuando lo encuentras te sientas y esperar que llegue el profesor"
    narrator "El profesor llega a la clase dando un anuncio"
    p "Bueno chicos y chicas, lo que sigue ahora es nuestro proyecto semestral grupal, asi que espero que puedan hacer todos grupos"
    menu DIA2_DEC4:
        
        set menuset
        "Que haces?"

        "Decides ir y preguntarle a algunos de tus compañeros si quieren hacer grupo contigo":
            a "Hola! Quería saber si puedo hacer grupo con ustedes, si no es molestia"
            un pibe?? "Si, puedes ser con nosotros"
            jump DIA2_DES4
        "Esperas a ver si alguno de tus compañeros te pregunta":
            narrator "Se te acerca un compañero"
            n "Oye, vi que estas solo, te falta grupo? De ser asi puedes ser con nosotros"
            a "Oh gracias, de echo si me faltaba un grupo para trabajar"
            jump DIA2_DES4
        "Decides hacer el trabajo solo":
label DIA2_PROF:
    
    menu DIA2_DEC5_PROF:

        set menuset
        p "Veo que sigue sin equipo, planea hacer el trabajo sin compañeros?"

        "Le dices que no encontraste grupo":
            a "Si profesor, es que no logre encontrar un grupo que le faltara persona"
            p "Esta bien"
        "Le dices que quisiste hacerlo solo":
            a "Si profesor, me gusta más trabajar individualmente"
            p "Esta bien"
    scene bg pasillo
label saltito:
    if Voley == 1:
        jump voley
label DIA2_DES4:
    scene bg camino
    if Ruta_tutor != 1:
        narrator "Asi la clase concluye, y decides irte a tu casa, en el camino a esta te encuentras con el jefe de carrera"
        j "Hola [Jugador], como has estado desde ayer?"
    else:
        narrator "Asi la clase concluye, y decides irte a tu casa, en el camino a esta te encuentras con el tutor"
        t "Hola [Jugador], como has estado desde ayer?"
    menu DIA2_DEC6:

        set menuset
        "Piensas un poco en tu día antes de responderle"

        "Gracias por preguntar! Eh estado bien hoy":
        "La verdad es que eh estado normal desde ayer":
    if Ruta_tutor != 1:
        j "Es bueno que no estes mal, y como te fue con el tutor ayer?"
    else:
        t "Es bueno que no estes mal, y como te fue con el jefe de carrera ayer?"
    a "Ayer, hable con el, pero me dijo que me hablaría para organizar bien las fechas, asi que no eh sabido nada"
    if Ruta_tutor != 1:
        j "Las remediales aveces son dificiles, asi que te recomiendo prepararte desde ya estudiando de apoco"
    else:
        t "Las remediales aveces son dificiles, asi que te recomiendo prepararte desde ya estudiando de apoco"
    a "Gracias por el consejo, lo tomare en cuenta"
label DIA2_DES5:
    if Ruta_tutor == 1:
        j "A todo esto, sabes cuales son tus metas?"
    elif Voley == 1:
        f "A todo esto, sabes cuales son tus metas?"
    else:
        j "A todo esto, sabes cuales son tus metas?"
    menu DIA2_DEC7:
    scene bg camino
        set menuset
        "Que le digo?"

        "La verdad es que me meti a la carrera porque eh escuchado que pagan bien":
            if Ruta_tutor == 1:
                j "No creo que ese sea un buen motivo ni meta, pero en algunos casos si pagan bien"
            elif Voley == 1:
                f "No creo que ese sea un buen motivo ni meta, pero en algunos casos si pagan bien"
            else:
                j "No creo que ese sea un buen motivo ni meta, pero en algunos casos si pagan bien"
        "Si, tengo muy claras mis metas para ahora y el futuro":
            if Ruta_tutor == 1:
                j "Eso es muy bueno, tener asi de claras tus metas te va a ayudar mucho"
            elif Voley == 1:
                f "Eso es muy bueno, tener asi de claras tus metas te va a ayudar mucho"
            else:
                j "Eso es muy bueno, tener asi de claras tus metas te va a ayudar mucho"
        "La verdad es que no tengo tanta seguridad de mis metas, me meti a la carrera porque es la que más me llamo la atención":
            if Ruta_tutor == 1:
                j "Hum… Eso no es muy bueno, puede que te aburras durante la carrera o incluso que en el proceso encuentres tus metas, te recomiendo seguir buscando para que definas lo que quieras hacer"
            elif Voley == 1:
                n "Hum… Eso no es muy bueno, puede que te aburras durante la carrera o incluso que en el proceso encuentres tus metas, te recomiendo seguir buscando para que definas lo que quieras hacer"
            else:
                j "Hum… Eso no es muy bueno, puede que te aburras durante la carrera o incluso que en el proceso encuentres tus metas, te recomiendo seguir buscando para que definas lo que quieras hacer"
label fin:
    #ACA NO SE COMO ES CUANDO SE ACABA
        
return


return

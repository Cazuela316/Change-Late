
label voley:
    narrator "Aunque justo al salir de la clase, te encuentras con Felipe"
    show felipe feliz at entrada_lenta_izquierda
    menu voley_1:
        set menuset
        f "Oye! [Jugador]!, te gustaría venir conmigo al taller de vóley?"

        "No gracias, no estoy muy interesado en los deportes la verdad":
            f "Esta bien! Entonces nos vemos luego"
            $ Voley = Voley - 1
            show felipe neutral at salida_izquierda_lenta
            narrator "Sin mas que hacer en la universidad. Empezaste irte a tu casa."
            show bg camino with dissolve
            narrator "Aunque justo de camino, te encuentras con una cara conocida!"
            a "Ese no es...?"
            jump saltito
        "Bueno, te acompaño, así conozco más!":
            f "Va! Vamos"
label VO_DES1:
    narrator "Ambos caminan hasta el gimnasio y Felipe te pregunta"
    scene bg gym
    menu voley_2:
        set menuset
        f "Oye, te caigo bien?"

        "Si de echo me caes bastante bien":
            $ Cha = Cha + 1
        "Super si, eres muy cool":
            $ Cha = Cha + 1
label VO_DES2:
    narrator "En esa pregunta llegan al gimnasio y Felipe hace la pregunta de las metas"
    narrator "Despues de estar jugando un rato"
    menu voley_3:
        set menuset
        f "Oye, para ser un novato eres bastante bueno. ¿Has jugado antes? Por ejemplo... Hmmm ¿Sabes que hace un libero?"

        "Es un jugador que se especializa en atacar":
            f "Hmmm, no, los liberos se encargan de la defensa por lo general."
            $ Int = Int - 1
        "Es un jugador que se especializa en defender":
            f "Oh, muy bien. Los liberos siempre son los encargados de la defensa."
            $ Int = Int + 1
label VO_DES3:
    f "Bueno, se esta haciendo tarde, creo que me voy ya"
    a "Hmm, bueno, entonces creo que tambien me ire antes de que se oscurezca mucho mas"
    f "Bien. Adios entonces [jugador]"
    a "Adios."
    jump DIA2_DES5

label sales_comprar:
        narrator "De la nada, te despertaste de repente, incluso hasta un poco con miedo, pero con tus 8 horas de sueño."
        a "Wahhh! Que buena dormida. Uy, ¿Qué hora es?"
        a "..."
        a "¿¡LAS 3 DE LA TARDE?!"
        a "Diablos… Me perdí todas mis clases!"
        narrator "Soltaste un largo suspiro."
        a "Bueno, supongo que si no fui a clase, deberia ir a comprarme algo con la baes..."
        a "Tengo que aprovechar! Mañana vence despues de todo."
        narrator "Entonces empezaste a vestirte, tomaste una de tus bolsas reutilizables y fuiste de camino al supermercado."
        #cambiar escena a la calle
        narrator "Estabas de camino al supermercado, hasta que viste a una cara conocida."
        a "Ese no es...?"
        jump saltito

label fin2:

    narrator "De la nada, te despertaste, el sol choco tu vista."
    a "…Tengo un mal presentimiento."
    narrator "Rápidamente fuiste por tu celular, prendiéndolo y revisando la hora."
    a "..."
    a "¿¡LAS 3 DE LA TARDE!?"
    a "Maldita sea… Me quede dormido de nuevo!"
    narrator "Soltaste un muy largo suspiro."
    a "Tsh… Supongo que podría ir a comprar cosas cocinar algo…"
    a "Aghhh!!! Porque tuve que quedarme dormido denuevo...!!!"
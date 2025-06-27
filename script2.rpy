label voley:
    narrator "Al salir de la clase te encuentras con Felipe"
    scene bg camino
    menu voley_1:
        set menuset
        f "Oye! [Jugador]!, te gustaría venir conmigo al taller de vóley?"

        "No gracias, no estoy muy interesado en los deportes la verdad":
            f "Esta bien! Entonces nos vemos luego"
            Voley = Voley - 1
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
            f "Hmmm, no, los liberos se encargan de la defensa por lo general.":
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
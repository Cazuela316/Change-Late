label voley:
    narrator "Al salir de la clase te encuentras con Felipe"
    scene bg camino
    menu voley_1:
        set menuset
        n "Oye! [Jugador]!, te gustaría venir conmigo al taller de vóley?"

        "No gracias, no estoy muy interesado en los deportes la verdad":
            n "Esta bien! Entonces nos vemos luego"
            Voley = Voley - 1
            jump saltito
        "Bueno, te acompaño, así conozco más!":
            n "Va! Vamos"
label VO_DES1:
    narrator "Ambos caminan hasta el gimnasio y Felipe te pregunta"
    scene bg gym
    menu voley_2:
        set menuset
        n "Oye, te caigo bien?"

        "Si de echo me caes bastante bien":
        "Super si, eres muy cool":
label VO_DES2:
    narrator "En esa pregunta llegan al gimnasio y Felipe hace la pregunta de las metas"
    narrator "Despues de estar jugando un rato"
    menu voley_3:
        set menuset
        n "Oye, para ser un novato eres bastante bueno. ¿Has jugado antes? Por ejemplo... Hmmm ¿Sabes que hace un libero?"

        "Es un jugador que se especializa en atacar":
            n "Hmmm, no, los liberos se encargan de la defense por lo general.":
        "Es un jugador que se especializa en defender":
            n "Oh, muy bien. Los liberos siempre son los encargados de la defensa."
label VO_DES3:
    n "Bueno, se esta haciendo tarde, creo que me voy ya"
    a "Hmm, bueno, entonces creo que tambien me ire antes de que se oscurezca mucho mas"
    n "Bien. Adios entonces [jugador]"
    a "Adios."
    jump DIA2_DES5
label voley:
    play music "BMG_Tarde-Noche.mp3" fadein 3.0 loop
    narrator "Aunque justo al salir de la clase, te encuentras con Felipe"
    show felipe feliz at entrada_lenta_izquierda
    menu voley_1:
        set menuset
        f "¡Oye, [Jugador]!, ¿te gustaría venir conmigo al taller de vóley?"

        "No gracias, no estoy muy interesado en los deportes la verdad":
            f "¡Esta bien! Entonces nos vemos luego."
            $ Voley = Voley - 1
            show felipe neutral at salida_izquierda_lenta
            narrator "Sin más que hacer en la universidad. Empezaste a irte a tu casa."
            show bg camino with dissolve
            narrator "Aunque justo de camino, ¡te encuentras con una cara conocida!"
            a "Ese no es...?"
            jump saltito
        "Bueno, te acompaño, ¡así conozco más!":
            f "¡Va! Vamos"
label VO_DES1:
    narrator "Ambos caminan hasta el gimnasio sin decir nada."
    scene bg gym with dissolve
    show felipe neutral at mitad_centro
    narrator "Despues de entrar, felipe te pregunta algo..."
    menu voley_2:
        set menuset
        f "Oye, ¿te caigo bien?"

        "Si, de hecho me caes bastante bien":
            show felipe feliz
            f "¡Ah! Que alivio saberlo, ¡jeje!"
            $ Cha = Cha + 1
        "Super si, eres muy cool":
            show felipe feliz
            f "¡Ah! Que alivio saberlo, ¡jeje!"
            $ Cha = Cha + 1
label VO_DES2:
    narrator "Sin mas que decir, felipe saco de su mochila una pelota de voley y te la lanza."
    f "¡Pues bueno! ¡Juguemos de una buena vez!"
    a "Oof... Vale vale. Aunque te advierto que no soy bueno."
    narrator "Decias mientras te posicionabas para comenzar a jugar."
    narrator "Despues de estar jugando un rato..."
    show felipe neutral
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
    jump DIA2_DES5

label SALTA: 
    narrator "Luego de esa conversacion, seguimos jugando."
    narrator "Hasta que fueron las 6 PM."
    f "Bueno, se esta haciendo tarde, creo que me voy ya"
    a "Hmm, bueno, entonces creo que tambien me ire antes de que se oscurezca mucho mas"
    f "¡Bien! Nos vemos entonces [Jugador]!"
    a "¡Nos vemos!"
    narrator "Decias mientras se separaban, llendo por caminos distintos."
    hide felipe feliz with dissolve
    jump fin

label sales_comprar:
        narrator "De la nada, te despertaste de repente, incluso hasta un poco con miedo, pero con tus 8 horas de sueño."
        show bg pieza_noche with dissolve
        a "Wahhh! Que buena dormida. Uy, ¿Qué hora es?"
        a "..."
        play audio "SFX_Shock.mp3" noloop
        a "¿¡LAS 3 DE LA TARDE?!"
        a "Diablos… ¡Me perdí todas mis clases!"
        narrator "Soltaste un largo suspiro."
        a "Bueno, supongo que si no fui a clase, deberia ir a comprarme algo con la baes..."
        a "¡Tengo que aprovechar! Mañana vence despues de todo."
        narrator "Entonces empezaste a vestirte, tomaste una de tus bolsas reutilizables y fuiste de camino al supermercado."
        play music "BMG_tarde-noche.mp3" fadein 2.0 loop
        show bg camino with dissolve
        narrator "Estabas de camino al supermercado, hasta que viste a una cara conocida."
        a "¿Ese no es...?"
        jump saltito

label fin2:
    show bg pieza_dia
    narrator "De la nada, te despertaste, el sol choco tu vista."
    a "…Tengo un mal presentimiento."
    narrator "Rápidamente fuiste por tu celular, prendiéndolo y revisando la hora."
    a "..."
    play audio "SFX_Shock.mp3" noloop
    a "¿¡LAS 3 DE LA TARDE!?"
    a "Maldita sea… Me quede dormido de nuevo!"
    narrator "Soltaste un muy largo suspiro."
    a "Tsh… Supongo que podría ir a comprar cosas cocinar algo…"
    a "¡¡¡Aghhh!!! ¡¡¡Porque tuve que quedarme dormido denuevo...!!!"
    show catalina feliz at fuera_izquierda_al_centro
    c "¡Hehe! ¡Eso te pasa por dormirte muy tarde!~"
    a "¿¡...Eh!? ¿¡Catamaran!? ¿Que haces aqui...?"
    show catalina neutral
    c "Bueno... Venia a darte tus resultados, pero..."
    show catalina feliz
    c "No puedo entregarte los resultados, ¡ya que no tengo nada que evaluar! ¡Jaja!"
    a "Umh... Supongo que a la proxima deberia ser tener mas responsabilidad..."
    c "Sipi, Bueno... No tengo nada mas que hacer aqui. Asi que... ¡Nos vemos!"
    a "Eh... Adios..."
    show catalina feliz at salida_izquierda_lenta
    narrator "Decia mientras catamalan se iba por la puerta principal de la casa."
    narrator "Soltando un largo suspiro."
    a "Bueno. Supongo que seguire durmiendo."
    show bg negro with dissolve
    narrator "Te decias a ti mismo, mientras volvias a cerrar los ojos."
    centered "{color=#ffffff}¡Final Malo! ¡Ganale a la flojera e intenta ir a clases!"


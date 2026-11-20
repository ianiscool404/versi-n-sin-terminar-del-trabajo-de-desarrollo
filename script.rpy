define Mi = Character("Micaela", color="#c8a2c8")
define Pe = Character("Micaela (Pensamiento)", color="#c8a2c8", what_italic=True)
define Ma = Character("Marta", color="#d9a066")
define Ag = Character("Agustín", color="#7fb3d5")
define Em = Character("Ema", color="#f5b7b1")
define So = Character("Sol", color="#a9dfbf")
define Mat = Character("Mateo", color="#f9e79f")
define C1 = Character("Compañera 1", color="#a9dfbf")
define C2 = Character("Compañera 2", color="#a9dfbf")
define En = Character("Enfermera", color="#47252e")

init python:
    import abc

    class EstadoMicaela(object):
        """Guarda el estado interno de Micaela.

        Los atributos son privados: solo se modifican mediante metodos.
        """

        def __init__(self):
            self.__confianza_agustin = 0   # sube si acepta la ayuda de Agustin
            self.__energia = 10            # baja si rechaza la ayuda

        def aceptar_cuaderno(self):
            """Micaela acepta el cuaderno: gana confianza en Agustin."""
            self.__confianza_agustin += 1

        def pasar_de_largo(self):
            """Micaela rechaza la ayuda: pierde energia."""
            self.__energia -= 1

        def confianza(self):
            """Devuelve la confianza actual en Agustin."""
            return self.__confianza_agustin

        def energia(self):
            """Devuelve la energia actual de Micaela."""
            return self.__energia


    class Publicacion(abc.ABC):
        """Clase abstracta: cualquier publicacion de redes sociales.

        No se instancia directamente. Cada hija implementa texto().
        """

        def __init__(self, texto_post):
            self.__texto_post = texto_post

        def get_texto_post(self):
            """Devuelve el contenido original de la publicacion."""
            return self.__texto_post

        @abc.abstractmethod
        def texto(self):
            """Devuelve el texto tal como se muestra en pantalla."""
            pass


    class PublicacionFoto(Publicacion):
        """Publicacion con foto de Micaela."""

        def texto(self):
            return "Foto de Micaela: \"" + self.get_texto_post() + "\""


    class PublicacionViral(Publicacion):
        """Publicacion que circula por todas las redes."""

        def texto(self):
            return "Viral (" + str(len(self.get_texto_post())) + " caracteres): " + self.get_texto_post()

# Saves
default estado = EstadoMicaela()
default post = None

# Canal extra para los sonidos
init python:
    renpy.music.register_channel("canal1", mixer="sfx")
    renpy.music.register_channel("canal2", mixer="sfx")

# El juego comienza acá

label start:

    scene black
    play music dark_piano

    show text "{size=60}{b}LO QUE NUNCA SE DIJO{/b}{/size}" with dissolve
    pause 3.0
    hide text with dissolve

    show text "{size=40}PRESENTADO POR: KINTSUKO{/size}" with dissolve
    pause 3.0
    hide text with dissolve

    jump acto1_escena1

label acto1_escena1:

    scene cuarto_micaela
    play music whatwentwe volume 2.5
    play canal1 alarm_clock loop
    play canal2 phone_vibration loop

    show micaela_cansadaf at left with dissolve

    Mi "..."

    show micaela_cansadaf at center with move

    play sound item_equip volume 2

    hide micaela_cansadaf

    show publicacion_micaela at center with dissolve
    pause 2

    show insultos_pantalla at center with dissolve
    Mi "Otra vez no."

    hide publicacion_micaela
    hide insultos_pantalla with dissolve

    show micaela_cansadaf at center with dissolve

    menu:
        "Apagar la alarma y alistarte":
            jump acto1_escena2

        "Volver a cubrirte con la sábana":
            jump acto1_escena1b


label acto1_escena1b:

    hide micaela_cansadaf
    show micaela_devastada at left
    show micaela_devastada at slot2 with move
    stop music fadeout 2
    play sound sheet_rustle volume 10

    stop canal1 fadeout 10
    pause 4
    play canal2 notification_sound
    pause 4
    play canal1 sobbing

    scene black with Dissolve(2.0)
    pause 1.0

    centered "{b}FINAL 1 DE 3: FUERA DE LÍNEA{/b}"

    jump creditos


label acto1_escena2:

    play sound pasos

    scene cocina with fade
    play music musica_tension
    play canal2 radio_tuning
    play canal1 water_drop

    show marta_resentida at slot1 with dissolve
    show micaela_cansada2 at right with dissolve
    pause 1
    show micaela_cansada2 at slot3 with move
    hide micaela_cansada2
    show micaela_cansada2f at slot3
    hide micaela cansada2f

    play sound item_equip
    show micaela_cansada2f at slot3, temblar
    show mano_billete at truecenter with dissolve
    pause 0.5
    hide mano_billete with dissolve

    play sound item_equip
    show micaela_cansada2f at slot3, temblar
    show mano_manzana at truecenter with dissolve
    pause 0.5
    hide mano_manzana with dissolve

    play sound phone_notification

    pause 2

    Ma "Y dale con el celular."
    Ma "¿No podés dejar esa porquería por al menos un día? ¡Hacé algo útil por una vez en tu vida y salí a buscar laburo!"

    hide micaela_cansada2f
    show micaela_iraf at slot3

    show manzana_machucada at truecenter with dissolve

    pause 1
    hide mano_manzana

    play sound manzana_aplastandose
    with hpunch

    pause 3
    hide manzana_machucada with dissolve

    Ma "¡Y no me ensucies el piso que lo acabo de limpiar!"

    show micaela_iraf at right with move

    Mi "Quedate tranquila que ya me voy."

    hide marta_resentida with dissolve
    hide micaela_iraf with moveoutright

    stop canal1
    stop canal2
    stop music
    play sound door_slam
    with vpunch

    jump acto1_escena3


label acto1_escena3:

    play canal1 pasos
    scene entrada_colegio
    play music sabbath
    play canal2 crowd_murmur

    show micaela_desconfiada at right with moveinright
    stop canal1

    show agustin_idlef at left with dissolve
    pause 1
    show agustin_idlef at slot3 with move
    hide agustin_idlef
    show agustin_amablef at slot3

    Ag "Hola. Se te cayó ayer en el aula."

    show agustin_amablef at slot3, temblar
    play sound item_equip
    show cuaderno at truecenter with dissolve
    pause 1
    hide cuaderno with dissolve

    show micaela_brazosx at right
    hide micaela_desconfiada

    Mi "..."

    menu:
        "Aceptar el cuaderno":
            $ estado.aceptar_cuaderno()
            jump acto1_escena3a

        "Pasar de largo":
            $ estado.pasar_de_largo()
            jump acto1_escena3b


label acto1_escena3a:

    hide micaela_brazosx
    show micaela_idle22 at right
    Ag "Tu mochila..."

    show mochila_micaela at truecenter with dissolve

    pause 1

    hide mochila_micaela with dissolve

    Ag "Si querés, en el recreo la arreglamos."

    play sound ajustar_mochila volume 3

    Mi "Así aguanta. Igual gracias."

    hide agustin_amablef
    show agustin_amablef at slot3, temblar_vertical
    pause 1.5
    hide agustin_amablef
    show agustin_amable
    hide agustin_amable with moveoutleft

    jump acto1_escena4

label acto1_escena3b:

    hide agustin_amablef
    show agustin_idlef at slot3
    hide micaela_brazosx with moveoutleft
    hide agustin_idlef
    show agustin_idle at slot3
    pause 1

    jump acto1_escena4


label acto1_escena4:

    # sfx: chirrido de neumáticos sobre el asfalto

    # soundtrack: entra una nota aguda y brillante, demasiado dulce (tono: falso, incómodo)
    
    scene entrada_colegio2

    with hpunch

    show micaela insegura at left
    show ema sonrisa_falsa at right with moveinright

    "Un auto moderno frena junto al cordón. Ema baja con un bolso de diseño y te ve."

    Em "¡Mica, gorda! Vení."

    "Ema engancha su brazo en el tuyo y te arrastra hacia el interior del colegio."

    hide ema with dissolve
    hide micaela with dissolve
    scene black with fade

    jump acto1_escena5


label acto1_escena5:

    scene pasillo with fade
    # soundtrack: tenso, notas sostenidas y pulso creciente (tono: humillante)
    # sfx: murmullos en el pasillo y risas contenidas

    show micaela humillada at left with dissolve
    show ema at center with dissolve
    show companeras burlonas at right with dissolve

    "Un corredor largo con casilleros metálicos. Tres compañeras bloquean el paso con los celulares en alto, apuntando a tu correa gastada."

    C1 "Che, Ema. ¿La trajiste de obra de caridad?"

    "Ema suelta una risa breve, te rodea los hombros con un brazo y te aprieta contra su costado."

    Em "No sean malas, chicas. Micaela hace lo que puede con lo que tiene."
    Em "Por eso yo siempre le doy una mano."

    "Apretás la mandíbula y bajás la vista hacia tus zapatillas gastadas."
    "Ema te suelta y avanza con las tres compañeras hacia el aula."

    hide ema with moveoutright
    hide companeras with moveoutright

    "Sacás el celular del bolsillo y desbloqueás la pantalla."

    # sfx: notificación de celular
    $ post = PublicacionFoto("La perrita faldera del curso")
    show insert pantalla_post at truecenter with dissolve
    "[post.texto()]"
    hide insert with dissolve

    # sfx: timbre escolar agudo

    scene black with fade
    jump acto2_escena1

label acto2_escena1:

    scene aula with fade
    # soundtrack: tenso, bajo y contenido (tono: frío, distante)
    # sfx: murmullos dispersos y rasguño de tiza sobre el pizarrón

    show micaela desconcertada at left with dissolve
    show ema fria at right with dissolve

    "Caminás hacia el banco libre junto a Ema. Ella apoya su bolso sobre la silla vacía para que no te sientes."

    Em "Hoy mejor sentate atrás, Mica. No da que nos vean tan pegadas después de esa foto."
    Em "...Es por tu bien."

    hide ema with dissolve

    # La energia de Micaela (clase EstadoMicaela) cambia como camina
    if estado.energia() < 10:
        "Frenás, apretás la correa de tu mochila y llegás a la última fila arrastrando los pies."
    else:
        "Frenás, apretás la correa de tu mochila y llegás a la última fila con la cabeza gacha."

    show agustin sereno at right with dissolve

    "Dejás tu mochila sobre el pupitre vacío junto a Agustín y te sentás en silencio."

    # sfx: timbre de recreo
    show companeras apuntando at center with dissolve

    "Ema sale al corredor. Las tres compañeras apuntan sus celulares hacia vos desde la puerta."

    show agustin alerta at right

    "Agustín abre la puerta lateral que conecta con el Salón de Arte."

    Ag "Salí por acá."

    "Colgás la mochila en tu hombro y cruzás rápido hacia el salón contiguo."

    hide companeras with dissolve
    hide agustin with dissolve
    hide micaela with dissolve

    jump acto2_escena2

label acto2_escena2:

    scene salon_arte with fade
    # soundtrack: agradable, guitarra suave o piano cálido (tono: refugio, alivio)
    # sfx: pestillo trabándose

    show micaela aliviada at left with dissolve
    show agustin concentrado at right with dissolve

    "Un taller luminoso con mesas largas, atriles y láminas de dibujo colgadas."
    "Agustín cierra la puerta con pestillo. Apoyás tu mochila sobre una silla y mirás la costura deshilachada de la correa."
    "Agustín saca de su mochila un estuche con un carretel de hilo negro y una aguja."

    # La confianza de Micaela (clase EstadoMicaela) decide quién cose
    if estado.confianza() > 0:
        "Agustín enhebra la aguja con rapidez y da cuatro puntadas firmes mientras vos sostenés la tela tensa."

        Ag "Listo. Con ese nudo tirás hasta fin de año."

        "Tirás de la correa para probar la costura y esbozás una sonrisa breve."
    else:
        "Agustín apoya el hilo y la aguja sobre la mesa, junto a tu mochila, y da un paso atrás en silencio."
        "Tomás la aguja enhebrada y cosés vos misma la costura floja con cuatro puntadas rápidas."

        Ag "Hacé doble nudo al final. Así no se suelta."

    jump acto2_escena3

label acto2_escena3:

    # soundtrack: agradable, se suma una melodía liviana (tono: calidez, pertenencia)

    show sol curiosa at left with moveinright
    show mateo incomodo at far_right_pos with moveinright

    "Sol y Mateo entran al salón con carpetas de dibujo bajo el brazo y se acercan a la mesa."

    Mat "Eu, Agus. ¿Trajiste visita?"
    Mat "Pará... ¿vos no sos la piba de la foto que pasaron recién?"

    show sol enojada at left

    So "Cerrá el pico, Mateo."

    show sol amable at left

    So "No le des cabida, siempre tira cualquiera. ¿Te das maña dibujando? Necesito que me tires un centro con la perspectiva antes de entregar."

    show micaela tranquila at slot2
    "Asentís, descruzás los brazos y ocupás la silla entre Agustín y Sol."

    # soundtrack: la música se corta en seco
    # sfx: golpe de puerta que se abre par en par
    with vpunch

    show ema furiosa at center with dissolve

    "Ema se detiene en el umbral. Borra su sonrisa al verte compartir la mesa con ellos."

    jump acto2_escena4


label acto2_escena4:

    # soundtrack: tenso, cuerdas graves y notas sostenidas (tono: confrontación)

    show ema falsa_amabilidad at center
    show micaela insegura at left

    "Ema recompone su sonrisa, camina detrás de tu silla y apoya ambas manos sobre tus hombros, presionando justo sobre la costura nueva."

    show insert dedos_sobre_costura at truecenter with dissolve
    pause 1.0
    hide insert with dissolve

    Em "Mica, querida, te busqué por todo el pasillo. Vení conmigo, no te expongas acá con gente que ni conocés."

    show agustin serio at right

    Ag "Estaba por mirar un dibujo con nosotros, Ema. Si se quiere ir, te avisa sola."

    "Bajás la mirada hacia el tablero de madera y apretás las manos sobre tus rodillas."
    "Mirás los dedos de Ema sobre tu hombro. Después mirás a Agustín, a Sol y a Mateo, que esperan en silencio frente a la mesa."

    menu:
        "Quedarte en la mesa con Agustín, Sol y Mateo":
            jump acto3_escena1a

        "Tomar la mochila y salir del salón con Ema":
            jump acto3_escena1b


label acto3_escena1a:

    # soundtrack: tenso que se va resolviendo (tono: valentía, tensión que cede)

    show micaela segura at left
    show ema tensa at center
    show sol ironica at cl
    show mateo desafiante at far_right_pos

    "Girás el torso hacia adelante y zafás tu hombro de los dedos de Ema."
    "Ema retrocede medio paso, borra su sonrisa por un segundo y clava los ojos en Agustín."

    Em "Después no me pidas que te cubra cuando te vuelvan a subir algo, Mica."

    So "¿Cubrirla? Si la única que la estaba apretando recién eras vos."

    "Mateo toma su celular de la mesa y apunta la cámara hacia Ema."

    Mat "Che, ¿querés que te filme cómo la amenazás o te tomás el palo sola?"

    Ag "Ya escuchaste, Ema. Dejala tranquila."

    "Ema aprieta la correa de su bolso de diseño con los nudillos blancos, gira sobre sus talones y camina rápido hacia la salida."

    hide ema with moveoutright
    # sfx: portazo

    "Exhalás despacio, tomás un lápiz de la mesa y trazás una línea sobre la lámina de Sol."

    scene black with fade
    # soundtrack: silencio breve antes del salto de tiempo (tono: calma)
    centered "{i}DOS SEMANAS DESPUÉS...{/i}"

    jump acto3_escena3a

label acto3_escena3a:

    scene patio with fade
    # soundtrack: agradable y luminoso, guitarra y piano (tono: redención, empoderamiento)
    # sfx: murmullo del patio y notificación de celular

    show micaela tranquila at left with dissolve
    show taller alumnos at center with dissolve
    show agustin seguro at right with dissolve

    "Compartís una mesa de cemento con Agustín, Sol, Mateo y cuatro alumnos del taller. Todos dibujan bajo la luz de la tarde."

    "Una notificación suena en tu celular. Desbloqueás la pantalla."

    $ post = PublicacionViral("De perrita faldera a ciruja del fondo")
    show insert pantalla_post at truecenter with dissolve
    "[post.texto()]"
    hide insert with dissolve

    # soundtrack: baja la música, entra una nota tensa breve (tono: amenaza)
    show ema preocupacion_falsa at far_right_pos with moveinright

    Em "Mica, ya vi lo que acaban de subir. Vení conmigo antes de que te sigan descansando, yo te cubro."

    "Los siete compañeros del taller rodean la mesa en silencio."
    "Presionás el botón de bloquear la cuenta, apagás el teléfono y lo guardás en la mochila."

    # soundtrack: la melodía luminosa vuelve y crece (tono: triunfo tranquilo)
    Mi "No hace falta, Ema. Ya elegí dónde quedarme."

    "Ema borra su sonrisa al ver los siete rostros alrededor de la mesa. Una de las compañeras tira de su cárdigan hacia atrás."

    hide ema with moveoutright

    "Sol te extiende un marcador negro. Lo tomás y trazás tu firma en la esquina de tu lámina."

    scene black with Dissolve(2.0)
    pause 1.0

    centered "{b}FINAL 3 DE 3: CAMBIO DE RED{/b}"

    jump creditos

label acto3_escena1b:

    scene pasillo with fade
    # soundtrack: tenso, cuerdas disonantes (tono: humillación, derrota)
    # sfx: risas y clics de cámara de celular

    show micaela derrotada at left with dissolve
    show ema triunfante at center with dissolve
    show companeras burlonas at right with dissolve

    "Salís del salón de arte con Ema. En el pasillo, las seguidoras de Ema esperan junto a los casilleros con los celulares en la mano."

    Em "Por suerte la rescaté a tiempo, chicas. Casi se queda pegada con los raros del salón."

    show insert costura_hilo_negro at truecenter with dissolve
    pause 1.2
    hide insert with dissolve

    C1 "Mirá esa costura trucha, Ema."
    C1 "¿Ahora también te hacés la costurera profesional?"

    Em "No sean malas. Ella hoy me lleva las cosas para compensar. Alcanzame el bolso hasta el aula, Mica."

    "Sostenés el bolso pesado con ambas manos y bajás la vista hacia el piso."

    # sfx: clic de cámara de celular
    "Una compañera levanta el celular y te saca una foto cargando el bolso de diseño."

    hide ema with moveoutright
    hide companeras with moveoutright

    "Ema cruza la esquina del corredor hacia el aula junto a sus seguidoras. Quedás sola."
    "Apoyás el bolso sobre un banco de madera y caminás rápido hacia la puerta de salida."
    "Apretás los labios, tenés los ojos húmedos. Empujás la puerta hacia la calle."

    # sfx: timbre del fin del recreo, a lo lejos

    scene black with fade
    jump acto3_escena2b


label acto3_escena2b:

    scene bano with fade
    # soundtrack: casi silencio, un zumbido grave y sostenido (tono: angustia, tensión máxima)
    # sfx (canal1): zumbido continuo del teléfono
    # sfx (canal2): agua corriendo

    show micaela devastada at left with dissolve

    "Un baño pequeño, con el espejo empañado y azulejos viejos. Tu celular vibra sin pausa sobre el estante."

    $ post = PublicacionViral("Micaela cargando el bolso de Ema")
    show insert pantalla_post at truecenter with dissolve
    "[post.texto()]"
    hide insert with dissolve

    "Abrís el botiquín, tomás un frasco de pastillas y volcás un puñado en tu boca. Inclinás la cabeza bajo el chorro de la canilla y tragás."

    # sfx: golpe violento de puerta abriéndose
    with vpunch

    show marta aterrada at right with moveinright

    "Marta irrumpe en el baño. Avanza dos pasos, te manotea el frasco y desparrama las pastillas sobre las baldosas. Te sujeta de los hombros y te sacude con fuerza."

    Ma "¿Qué mierda tomaste, pendeja? ¡Escupí eso ya!"

    show micaela en_el_suelo at left

    "Perdés fuerza en las rodillas y resbalás contra la pared hasta el suelo, con la mirada perdida."
    "Marta recoge el frasco vacío, lee la etiqueta con el ceño fruncido y saca su celular del bolsillo."

    scene black with fade
    jump acto3_escena3b


label acto3_escena3b:

    scene hospital with fade
    # soundtrack: ninguna, solo el ambiente del hospital (tono: ambiguo, agotado)
    # sfx: pitido lento y regular del monitor cardíaco

    show micaela camilla_dormida at left with dissolve
    show marta agotada at right with dissolve
    show enfermera neutra at center with dissolve

    "Una sala de internación iluminada por el reflejo verde de un monitor. Micaela descansa sobre una camilla blanca."

    En "El lavaje agarró a tiempo, señora. Por ahora sigue estable, pero todavía no reacciona."

    hide enfermera with dissolve

    # sfx: notificación de celular
    "Sobre la mesa de luz, el celular de Micaela enciende su pantalla."

    show insert marta_apagando_celular at truecenter with dissolve
    pause 1.5
    hide insert with dissolve

    "Marta toma el celular, mantiene apretado el botón lateral y lo apaga por completo. Lo apoya boca abajo sobre la mesa y cubre la mano inmóvil de Micaela con la suya."

    # sfx: pitido continuo del monitor cardíaco

    scene black with Dissolve(2.5)
    pause 1.0

    centered "{b}FINAL 2 DE 3: SIN SEÑAL{/b}"

    jump creditos

label creditos:
    stop canal1
    stop canal2

    scene black with fade
    play music cierre_bgm
    pause 5.0

    centered "Desarrollado por Kintsuko\n\nDaza David\nSharif Dib\nFrancisco Rey"
    centered "Programadores:\n\nDaza David"
    centered "Guionistas:\n\nDaza David\nSharif Dib"
    centered "Arte:\n\nFrancisco Rey"
    centered "Música, SFX y BGM:\n\nFrancisco Rey\nDaza David"
    centered "{size=60}{b}LO QUE NUNCA SE DIJO{/b}{/size}"

    scene black with fade

    return
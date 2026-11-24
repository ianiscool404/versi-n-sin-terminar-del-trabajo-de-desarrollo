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
define Un = Character ("???")

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
            return "Nuevo post: \"" + self.get_texto_post() + "\""


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
        "Silenciar el teléfono y bajar a la cocina":
            jump acto1_escena2

        "Volver a la cama a dormir":
            jump acto1_escena1b

label acto1_escena1b:

    hide micaela_cansadaf
    show micaela_devastadaf at center
    show micaela_devastadaf at slot2 with move
    stop music fadeout 2
    play sound sheet_rustle volume 10

    stop canal1 fadeout 10
    pause 4
    play canal2 notification_sound
    hide micaela_devastadaf with dissolve
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
    show micaela_idle2 at right

    Mi "Gracias."

    Ag "Tu mochila... esta medio..."

    show mochila_micaela at truecenter with dissolve

    pause 1

    hide mochila_micaela with dissolve

    Ag "Si querés, en el recreo con los chicos te la arreglamos."

    play sound ajustar_mochila volume 3

    Mi "Así aguanta. No te preocupes."

    "Agustín asiente en silencio y camina hacia el portón."

    hide agustin_amablef
    show agustin_amable at slot3
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

    stop music
    play music musica_tension

    stop canal2

    play sound tire_screeching

    scene entrada_colegio2

    with hpunch
    pause 2
    show micaela_idle2 at left

    play sound car_door_openclosed
    "Un auto moderno frena junto al cordón. Ema baja con un bolso de diseño y te ve."
    pause 1
    show ema_falsa at right with moveinright
    Em "¡Mica, gorda! Vení."

    "Ema engancha su brazo en el tuyo y te arrastra hacia el interior del colegio."

    Em "Lleváme el bolso, ¿dale?"

    hide ema_falsa with dissolve
    hide micaela_idle2 with dissolve
    scene black with fade

    jump acto1_escena5

label acto1_escena5:

    play sound pasos
    stop music
    play music youandmeandher
    scene pasillo with fade
    play canal1 crowd_murmur

    show micaela_humillada at left with dissolve
    show ema_burlona at center with dissolve
    show companera_burlona at right with dissolve

    "Tres compañeras bloquean el paso con los celulares en alto, apuntándote."

    C1 "Che, Ema. ¿La trajiste de obra de caridad?"

    "Ema suelta una risa breve, te rodea los hombros con un brazo y te aprieta contra su costado."

    Em "No sean malas, chicas. Micaela hace lo que puede con lo que tiene."
    Em "Y siempre estaré ahí para darle una mano."
    Em "Para eso son las amigas, ¿no?"

    "Apretás la mandíbula y bajás la vista hacia tus zapatillas gastadas."

    Mi "Sí..."

    "Ema te suelta y avanza con las tres compañeras hacia el aula."

    hide ema_burlona with moveoutright
    hide companera_burlona with moveoutright

    "Sacás el celular del bolsillo y desbloqueás la pantalla."

    play sound phone_notification
    $ post = PublicacionFoto("La perrita faldera de Ema")
    show publicacion_foto at truecenter with dissolve
    "[post.texto()]"
    hide insert with dissolve

    play sound schoolbell

    stop canal1
    scene black with fade
    jump acto2_escena1

label acto2_escena1:

    stop music
    play music whatwentwe volume 2.5
    play canal1 crowd_whisper
    play canal2 chalkboard volume 1.5
    scene aula with fade

    show micaela_humillada at left with dissolve
    show ema_tensa at right with dissolve

    "Caminás hacia el banco libre junto a Ema. Ella apoya su bolso sobre la silla vacía para que no te sientes."

    Em "Hoy mejor sentate atrás, Mica. No da que nos vean tan pegadas después de esa foto."
    Em "...Es por tu bien."

    Mi "Sí... nos vemos después."

    hide ema_tensa with dissolve

    # La energia de Micaela (clase EstadoMicaela) cambia como camina (no es la gran cosa pero bueno)
    if estado.energia() < 10:
        "Frenás, apretás la correa de tu mochila y llegás a la última fila arrastrando los pies."
    else:
        "Frenás, apretás la correa de tu mochila y llegás a la última fila con la cabeza gacha."

    show agustin_idle at right with dissolve

    "Dejás tu mochila sobre el pupitre vacío junto a Agustín y te sentás en silencio."

    play sound schoolbell
    show companera_burlona at center with dissolve

    "Ema sale al corredor. Las tres compañeras apuntan sus celulares hacia vos desde la puerta."

    hide agustin_idle
    show agustin_serio at right

    "Agustín abre la puerta lateral que conecta con el Salón de Arte."

    Ag "Salí por acá."

    "Colgás la mochila en tu hombro y cruzás rápido hacia el salón contiguo."

    hide companera_burlona with dissolve
    hide agustin_serio with dissolve
    hide micaela_humillada with dissolve

    stop canal1
    stop canal2

    jump acto2_escena2

label acto2_escena2:

    play music sabbath

    scene salon_arte with fade

    play sound pestillo

    show micaela_idle22 at left with dissolve
    show agustin_amable at right with dissolve

    "Agustín cierra la puerta con pestillo. Apoyás tu mochila sobre una silla y mirás la costura deshilachada de la correa."
    "Agustín saca de su mochila un estuche con un carretel de hilo negro y una aguja."

    # La confianza de Micaela (clase EstadoMicaela) decide quién cose, Micaela o Agustin
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

    show sol_idle at center with moveinright
    show mateo_idle at slot4 with moveinright

    play sound door_close
    "Dos alumnos entran al salón por la puerta principal con carpetas de dibujo bajo el brazo y se acercan a la mesa."

    hide mateo_idle
    hide sol_idle
    show sol_curiosa at center
    show mateo_incomodo at slot4
    Un "Eu, Agus. ¿Trajiste visita?"
    Un "Pará... ¿vos no sos la piba de la foto que pasaron recién?"

    hide sol_curiosa
    show sol_enojada at center

    Un "Cerrá el pico, Mateo."

    "La chica de da un pequeño golpe al hombro con su cuaderno al chico."

    hide sol_enojada
    show sol_amable at center
    hide mateo_incomodo
    show mateo_idle at slot4

    Un "No le des cabida, siempre tira cualquiera."
    Mat "Perdón, che. No fue con intención de ofender."
    Un "Soy Sol, y él es Mateo."
    So "¿Te das maña dibujando? Necesito que me tires un consejo con la perspectiva antes de entregar."

    hide micaela_idle22
    show micaela_seguraf at left
    "Asentís, descruzás los brazos y ocupás la silla entre Agustín y Sol."

    play sound door_close
    with vpunch

    hide micaela_seguraf
    hide sol_amable
    hide agustin_amable
    hide mateo_idle

    stop music

    show ema_tensa at center with dissolve

    "Ema entra por la puerta principal. Borra su sonrisa al verte compartir la mesa con ellos."

    jump acto2_escena4

label acto2_escena4:

    play music decision_final

    hide ema_tensa
    show ema_falsa at center
    hide micaela_segura
    show micaela_cansada2f at left

    "Ema recompone su sonrisa, camina detrás de tu silla y apoya ambas manos sobre tus hombros, presionando justo sobre la costura nueva."

    Em "Mica, querida, te busqué por todo el pasillo. Vení conmigo, no te expongas acá con gente que ni conocés."

    hide agustin_amable
    show agustin_serio at right

    Ag "Estaba por mirar un dibujo con nosotros, Ema. Si se quiere ir, te avisa sola."

    "Bajás la mirada hacia el tablero de madera y apretás las manos sobre tus rodillas."
    "Mirás los dedos de Ema sobre tu hombro. Después mirás a Agustín, a Sol y a Mateo, que esperan en silencio frente a la mesa."

    menu:
        "Quedarte en la mesa con Agustín, Sol y Mateo":
            jump acto3_escena1a

        "Tomar la mochila y salir del salón con Ema":
            jump acto3_escena1b

label acto3_escena1a:
    
    hide micaela_cansada2
    show micaela_seguraf at left
    hide ema_falsa
    show ema_tensa at center
    show sol_ironica at slot2
    show mateo_desafiante at slot4
    "Girás el torso hacia adelante y zafás tu hombro de los dedos de Ema."
    "Ema retrocede medio paso, borra su sonrisa por un segundo y clava los ojos en Agustín."

    Em "Después no me pidas que te cubra cuando te vuelvan a subir algo, Mica."

    So "¿Cubrirla? Si la única que la estaba apretando recién eras vos."

    "Mateo toma su celular de la mesa y apunta la cámara hacia Ema."

    Mat "Che, ¿querés que te filme cómo la amenazás o te tomás el palo sola?"

    Ag "Ya escuchaste, Ema. Dejala tranquila."

    "Ema aprieta la correa de su bolso de diseño con los nudillos blancos, gira sobre sus talones y camina rápido hacia la salida."

    hide ema_tensa with moveoutright
    play sound door_slam

    "Exhalás despacio, tomás un lápiz de la mesa y trazás una línea sobre la lámina de Sol."

    scene black with fade
    stop music
    centered "{i}DOS SEMANAS DESPUÉS...{/i}"

    jump acto3_escena3a

label acto3_escena3a:

    scene patio with fade
    play music soundtrack67
    play canal1 crowd_murmur

    show micaela_seguraf at left with dissolve
    show taller_alumnos at center with dissolve
    show agustin_amable at right with dissolve

    "Compartís una mesa de cemento con Agustín, Sol, Mateo y cuatro alumnos del taller. Todos dibujan bajo la luz de la tarde."

    "Una notificación suena en tu celular. Desbloqueás la pantalla."

    Pe "Otro post de esos..."

    stop music
    hide taller_alumnos
    hide agustin_amable
    show ema_falsa at far_right_pos with moveinright

    Em "Mica, ya vi lo que acaban de subir. Vení conmigo antes de que te sigan descansando, yo te cubro."

    show taller_alumnos at slot2 with dissolve

    "Los siete compañeros del taller rodean la mesa en silencio."
    "Presionás el botón de bloquear la cuenta, apagás el teléfono y lo guardás en la mochila."

    play music esperanza1

    Mi "No hace falta, Ema. Ya elegí dónde quedarme."

    hide ema_falsa
    show ema_tensa at far_right_pos

    "Ema borra su sonrisa al ver los siete rostros alrededor de la mesa. Una de las compañeras tira de su cárdigan hacia atrás."

    hide ema_tensa with moveoutright

    "Sol te extiende un marcador negro. Lo tomás y trazás tu firma en la esquina de tu lámina."

    scene black with Dissolve(2.0)
    pause 1.0

    centered "{b}FINAL 3 DE 3: CAMBIO DE RED{/b}"

    jump creditos

label acto3_escena1b:

    play sound pasos

    scene pasillo with fade
    play music youandmeandher

    show micaela_humilladaf at left with dissolve
    show ema_burlona at center with dissolve
    show companera_burlona at right with dissolve

    "Salís del salón de arte con Ema. En el pasillo, las seguidoras de Ema esperan junto a los casilleros con los celulares en la mano."

    Em "Por suerte la rescaté a tiempo, chicas. Casi se queda pegada con los raros del salón."

    play sound laughs

    C1 "Mirá esa costura trucha, Ema."
    C1 "¿Ahora también te hacés la costurera profesional?"

    Em "No sean malas. Ella hoy me lleva las cosas para compensar. Alcanzame el bolso hasta el patio, Mica."

    "Sostenés el bolso pesado con ambas manos y bajás la vista hacia el piso."

    play sound camera_clic
    "Una compañera levanta el celular y te saca una foto cargando el bolso de diseño."

    hide ema_burlona with moveoutright
    hide companera_burlona with moveoutright

    "Ema cruza la esquina del corredor hacia el aula junto a sus seguidoras. Quedás sola."
    "Tirás el bolso al piso y caminás rápido hacia la puerta de salida. Escapás"
    
    scene black with fade
    
    stop music
    play sound running
    "Apretás los labios, tenés los ojos húmedos. La gente te mira en la calle."

    jump acto3_escena2b

label acto3_escena2b:

    play music final_hospital

    scene bano with fade

    show micaela_devastadaf at center with dissolve

    "Llegás a tu casa y te escondés en el baño."
    play sound item_equip
    "Abrís el botiquín, tomás un frasco de pastillas y volcás un puñado en tu boca."
    play canal1 faucet
    "Inclinás la cabeza bajo el chorro de la canilla y tragás."
    stop canal1
    play sound door_slam
    with vpunch

    show marta_resentida at right with moveinright

    "Marta irrumpe en el baño."
    play sound slap
    "Avanza dos pasos, te manotea el frasco y desparrama las pastillas sobre las baldosas."
    "Te sujeta de los hombros y te sacude con fuerza."

    Ma "¿Qué mierda tomaste, pendeja?"
    Ma "¿¡Me querés arruinar la vida a mí también!? ¡Escupí eso ya!"

    hide micaela_devastadaf with dissolve

    "Perdés fuerza en las rodillas y resbalás contra la pared hasta el suelo, con la mirada perdida."
    "Marta recoge el frasco vacío, lee la etiqueta con el ceño fruncido y saca su celular del bolsillo."

    scene black with fade
    jump acto3_escena3b

label acto3_escena3b:

    stop canal1

    scene hospital with fade

    play canal1 heartrate volume 2

    show marta_agotada at right with dissolve
    show enfermera at center with dissolve

    "Despertás. O eso crees, no podés ver ni hablar pero escuchas a alguien conversando con tu madrastra."

    En "El lavaje agarró a tiempo, señora. Por ahora sigue estable, pero todavía no reacciona."

    "Marta asiente en silencio. La enfermera abandona la habitación."

    hide enfermera with dissolve

    play sound phone_notification

    "Escuchás la notificación de tu celular, un escalofrío recorre por tu cuerpo."
    "Marta toma el celular, mantiene apretado el botón lateral y lo apaga por completo."
    "Marta cubre tu mano inmóvil con la suya."
    "Pódes escuchar sollozar a alguien."

    scene black with Dissolve(2.5)
    pause 1.0

    centered "{b}FINAL 2 DE 3: SIN SEÑAL{/b}"

    jump creditos

label creditos:
    stop canal1
    stop canal2

    play music cierre_bgm

    scene black with fade
    pause 5.0

    centered "Desarrollado por Kintsuko\n\nDaza David\nSharif Dib\nFrancisco Rey"
    centered "Programadores:\n\nDaza David"
    centered "Guionistas:\n\nDaza David\nFrancisco Rey\nSharif Dib"
    centered "Arte:\n\nFrancisco Rey"
    centered "Música, SFX y BGM:\n\nFrancisco Rey\nDaza David"
    centered "{size=60}{b}LO QUE NUNCA SE DIJO{/b}{/size}"

    scene black with fade

    return

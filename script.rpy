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

    # Atributos de micaela como la confianza que gana con sus aliados y la energia para hablar
    class EstadoMicaela(object):
        def __init__(self):
            self.__confianza_agustin = 0
            self.__energia = 10

        def aceptar_cuaderno(self):
            self.__confianza_agustin += 1

        def pasar_de_largo(self):
            self.__energia -= 1

        def confianza(self):
            return self.__confianza_agustin

        def energia(self):
            return self.__energia
        
init python:
    import abc

    class Publicacion(abc.ABC):
        def __init__(self, texto_post):
            self.__texto_post = texto_post

        def get_texto_post(self):
            return self.__texto_post

        @abc.abstractmethod
        def texto(self):
            pass

    class PublicacionFoto(Publicacion):
        def texto(self):
            return "Foto de Micaela: \"" + self.get_texto_post() + "\""

    class PublicacionViral(Publicacion):
        def texto(self):
            return "Viral (" + str(len(self.get_texto_post())) + " caracteres): " + self.get_texto_post()

default estado = EstadoMicaela()

init python:
    renpy.music.register_channel("canal1", mixer="sfx")
#Para reproducir mas audios kjj
init python:
    renpy.music.register_channel("canal2", mixer="sfx")

# El juego comienza acá.
# Todos los "insert" llevan un plano cinematografico que tendré que meter despues

label start:
    #----------#
    #--ACTO I--#
    #----------#

    scene cuarto_micaela1 with fade
    play sound alarm_clock loop
    play canal1 phone_vibration loop

    "Abrís los ojos en la cama mientras el teléfono zumba sobre la mesa de luz."

    show micaela_acostada with fade

    "Estirás el brazo derecho, agarrás el celular y mirás la pantalla iluminada."

    scene pantalla_pd_insultos with fade
    pause 1.5

    Mi "Otra vez no..."

    menu:
        "Apagar la alarma e incorporarte":
            stop sound
            stop canal1
            jump escena_2

        "Volver a cubrirte con la sábana":
            jump escena_1b

label escena_1b:

    show micaela_ocultar_celular with fade

    "Girás el celular boca abajo y lo ocultás debajo de la almohada."

    show micaela_bajo_sabana with fade

    "Tapás tu cuerpo por completo con la sábana y apretás tus oídos con ambas manos."

    play canal1 notification_sound loop fadein 0.5 volume 1
    stop sound fadeout 3
    play canal1 notification_sound loop fadein 0.5 volume 5

    show micaela_cuerpo_tapado with fade
    pause 1

    show micaela_suspiro_largo with fade

    "Soltás el aire en un suspiro largo y dejás caer tus brazos a los costados."

    scene negro_absoluto with Dissolve(2.0)
    pause 1.5

    centered "{b}FINAL 1 DE 3: FUERA DE LÍNEA{/b}\n\nFIN DEL ACTO I"
    return

label escena_2:

    scene cocina with fade
    play sound water_drop loop

    show marta_pm at right with dissolve
    show micaela mochila_hombro at left with dissolve

    "Abrís la puerta de la cocina y agarrás los billetes junto a un pan duro de la mesa."

    Ma "¿Otra vez te quedaste hasta cualquiera con ese aparato, boludita?"

    "Apretás el pan dentro de tu puño y bajás la vista hacia el suelo."

    Ma "Esa piba te tiene de obra de caridad."

    "Mirás la manzana podrida sobre la mesa y apartás la mano sin tocarla."

    show insert manzana_podrida at truecenter with dissolve
    pause 1.0
    hide insert manzana_podrida with dissolve

    "Pasás una mano rápida por tu mejilla, girás hacia la puerta y cruzás el umbral."

    stop sound
    play sound door_slam
    with vpunch

    jump escena_3

label escena_3:

    scene bg porton_colegio with fade
    #play sound murmullo_calle

    show micaela walk at left with dissolve
    show agustin muro_cuaderno at right with dissolve
    pause 0.5
    
    show agustin ofreciendo_cuaderno at right
    Ag "Se te cayó ayer en el aula."

    "Cruzás los brazos y mirás el cuaderno a la altura de tu pecho."

    menu:
        "Aceptar el cuaderno":
            $ estado.aceptar_cuaderno()
            jump escena_3_nodo_a

        "Pasar de largo":
            $ estado.pasar_de_largo()
            jump escena_3_nodo_b

label escena_3_nodo_a:

    "Extendés la mano derecha y recibís el cuaderno."
    "Mientras abrís tu mochila, Agustín mira la correa deshilachada."

    show agustin mirando_correa at right
    Ag "Si querés, en el recreo la arreglamos."

    "Ajustás la correa con un tirón rápido y negás con la cabeza."

    Mi "Así tira. Igual gracias."

    hide agustin with dissolve
    jump escena_4

label escena_3_nodo_b:

    "Ignorás el brazo extendido de Agustín, apretás tu mochila y avanzás directo al portón."

    hide agustin with dissolve
    jump escena_4

label escena_4:

    #play sound frenada_auto
    with hpunch
    #stop sound

    "Un auto moderno frena junto al cordón; baja Ema con un bolso de diseño."

    show ema brazo_en_alto at right with moveinright

    Em "¡Mica, gorda! Vení."

    "Ema engancha su brazo en el tuyo y ambas cruzan el portón hacia el interior."

    jump escena_5

label escena_5:

    scene bg pasillo_casilleros with fade
    #play sound "murmullos_y_click_de_camara

    show micaela cabizbaja at left
    show ema abrazo_falso at center
    show companeras bloqueando_paso at right
    with dissolve

    "Las tres compañeras apuntan sus celulares a la correa deshilachada de tu mochila."

    C1 "Che, Ema. ¿La trajiste de obra de caridad?"

    Em "No sean malas, chicas. Mica hace lo que puede con lo que tiene."
    Em "Por eso yo siempre le doy una mano."

    "Apretás la mandíbula y bajás la vista hacia tus zapatillas gastadas."
    "Ema suelta tu hombro y avanza hacia el aula con las tres compañeras."

    hide ema with moveoutright
    hide companeras with moveoutright

    "Sacás tu celular del bolsillo y desbloqueás la pantalla."

    $ post = PublicacionFoto("La perrita faldera del curso")
    "[post.texto()]"

    pause 0.5

    #play sound timbre_escolar
    #pause 1.0

    jump escena_6

label escena_6:

    #-----------#
    #--ACTO II--#
    #-----------#

    scene bg aula_clases with fade
    #play sound risas_bajas

    show micaela entrando at left with dissolve
    show ema sentada_primera_fila at right with dissolve

    "Caminás hacia el banco libre junto a Ema; ella apoya su bolso en la silla vacía."

    show ema poniendo_bolso at right
    Em "Hoy mejor sentate atrás, Mica."
    Em "No da que nos vean tan pegadas después de esa foto.\nEs por tu bien."

    "Frenás tu marcha, apretás la correa de tu mochila y caminás hasta la última fila."

    show agustin ultima_fila at center with dissolve

    "Dejás tu mochila sobre el pupitre vacío junto a Agustín y tomás asiento."

    #play sound timbre_recreo
    pause 0.8

    "Ema sale al corredor; las tres compañeras apuntan sus cámaras desde la puerta."

    hide ema with moveoutright
    show companeras apuntando_celulares at right with dissolve

    "Agustín gira hacia la pared lateral y abre la puerta conectora al Salón de Arte."

    show agustin alerta_puerta at center
    Ag "Salí por acá."

    "Colgás la mochila en tu hombro y cruzás rápido hacia el salón contiguo."

    jump escena_7

label escena_7:

    scene bg salon_arte with fade

    show micaela alivio at left with dissolve
    show agustin cerrando_pestillo at right with dissolve
    #play sound clicl de pestillo

    "Apoyás tu mochila sobre una silla y observás la costura deshilachada."
    "Agustín saca de su mochila un estuche con hilo negro y aguja."

    show agustin hilo_y_aguja at right

    if estado.confianza() > 0:
        "Sostenés la tela tensa mientras Agustín da cuatro puntadas firmes con hilo negro."

        Ag "Listo. Con este nudo tirás hasta fin de año."

        "Tirás de la correa para probar la costura y esbozás una sonrisa breve."
    else:
        "Agustín apoya el hilo y la aguja en la mesa; vos cosés la correa con cuatro puntadas."

        Ag "Hacé doble nudo al final, así no se zafa."

    jump escena_8

label escena_8:

    show micaela alerta at left

    show sol carpeta_dibujo at center with moveinright

    show mateo carpeta_dibujo at slot4 with moveinright
    Mat "Che, Agus. ¿Trajiste visita?"
    Mat "Pará... ¿vos no sos la piba de la foto que pasaron recién?"

    "Sol golpea el hombro de Mateo con su carpeta de dibujo."

    show sol molesta at center
    So "Cerrá el pico, Mateo."

    show sol amable at center
    So "No le des cabida, siempre tira cualquiera."

    show mateo arrepentido at slot4
    Mat "Perdón, che."

    show agustin tranquilo at slot2 with moveinright
    Ag "Sentate. Acá es re tranqui."

    show micaela confiada at left

    So "¿Te das maña dibujando?\nNecesito que me tires un centro con la perspectiva."

    "Asentís, descruzás los brazos y ocupás la silla entre Agustín y Sol."
    "De golpe se abre la puerta principal de par en par."

    #play sound puerta_abriendose
    with vpunch

    hide agustin tranquilo
    hide sol amable
    hide mateo arrepentido

    show micaela insegura at left

    show ema umbral_molesta at right with dissolve
    # PPP
    pause 1.0

    jump escena_9

label escena_9:

    "Ema guarda su celular, recompone su sonrisa y camina detrás de tu silla."

    show ema sonrisa_falsa_detras at slot2 with moveinright

    "Apoya ambas manos sobre tus hombros, presionando justo sobre la costura nueva."

    show insert dedos_sobre_costura at truecenter with dissolve
    #play sound vibracion_corta
    pause 1.0
    hide insert dedos_sobre_costura with dissolve

    Em "Mica, querida, te busqué por todo el pasillo."
    Em "Vení conmigo, no te expongas acá con gente que ni conocés."

    "Bajás la mirada hacia el tablero de madera y apretás tus manos sobre tus rodillas."

    show agustin serio at right
    Ag "Estaba por mirar un dibujo con nosotros, Ema.\nSi se quiere ir, te avisa sola."

    Pe "Si vuelvo con ella, le doy el gusto.\nPero si me quedo acá... me la tengo que jugar con ellos."

    menu:
        "Quedarte en la mesa con Agustín, Sol y Mateo":
            jump escena_10a

        "Agarrar la mochila y salir del salón con Ema":
            jump escena_10b

label escena_10a:

    #---------------------#
    #--ACTO III (Ruta A)--#
    #---------------------#

    "Girás el torso hacia adelante y zafás tu hombro de los dedos de Ema."

    show ema tensa at center with move
    Em "Después no me pidas que te cubra cuando te vuelvan a subir algo, Mica."

    show sol ironica at slot2
    So "¿Cubrirla? Si la única que la estaba apretando recién eras vos."

    "Mateo levanta su celular y apunta la lente de la cámara hacia Ema."

    show mateo celular_en_mano at slot4
    Mat "Che, ¿querés que te filme cómo la apurás o te tomás el palo sola?"

    "Ema aprieta su bolso con los nudillos blancos y sale rápido del salón."
    hide ema with moveoutright
    play sound "sfx_portazo.ogg"

    "Exhalás despacio, agarrás un lápiz de la mesa y trazás una línea sobre la lámina de Sol."

    jump escena_11a

label escena_11a:

    scene bg patio_colegio with fade
    centered "{i}DOS SEMANAS DESPUÉS{/i}"
    pause 1.0

    #play sound murmullo_general

    "Compartís una mesa de cemento con Agustín, Sol, Mateo y cuatro alumnos del taller."
    show grupo_taller_completo at left with dissolve

    "Agarrás tu celular de la mesa y desbloqueás la pantalla."

    $ post = PublicacionViral("De perrita faldera a ciruja del fondo")
    "[post.texto()]"

    pause 1.5

    "Sol apoya una mano firme sobre tu hombro; Ema avanza desde el pasillo lateral."

    show ema dulce at slot3 with moveinright
    show companeras detras at right with dissolve

    Em "Mica, ya vi lo que acaban de subir."
    Em "Vení conmigo antes de que te sigan descansando, yo te cubro."

    "Agustín, Sol, Mateo y los cuatro alumnos del taller rodean la mesa en silencio."

    "Presionás el botón de bloquear cuenta y apagás el teléfono por completo."

    "Guardás el celular en tu mochila, ajustás la correa cosida y mirás a Ema."

    Mi "No hace falta, Ema. Ya elegí dónde quedarme."

    "Ema borra su sonrisa al ver los siete rostros alrededor de la mesa."

    show ema derrotada at slot3
    hide ema with moveoutright
    hide companeras with moveoutright

    "Agarrás el marcador negro que te extiende Sol y trazás tu firma en tu lámina."

    stop sound
    scene bg negro_absoluto with Dissolve(2.0)

    centered "{b}FINAL 3 DE 3: CAMBIO DE RED{/b}\n\nFIN DEL ACTO III"
    return

    # Finaliza el juego:

label escena_10b:

    #---------------------#
    #--ACTO III (Ruta B)--#
    #---------------------#

    scene bg pasillo_casilleros with fade

    show micaela cabizbaja at left with dissolve
    show ema sonriente at center with dissolve
    show companeras casilleros at right with dissolve

    Em "Por suerte la rescaté a tiempo, chicas.\nCasi se queda pegada con los raros del salón."

    show insert costura_hilo_negro at truecenter with dissolve
    play sound "sfx_risas_y_camara.ogg"
    pause 1.2
    hide insert costura_hilo_negro with dissolve

    C1 "Mirá esa costura trucha, Ema."
    C2 "¿Ahora también hacés arreglos de costura?"

    "Ema cuelga su bolso de diseño sobre tu brazo."

    show ema entregando_bolso at center
    Em "No sean malas. Hoy me lleva las cosas para compensar."
    Em "Alcanzame el bolso hasta el aula, Mica."

    "Sostenés el bolso pesado con ambas manos mientras la Compañera 3 te saca una foto."
    #play sound camara_celular

    "Ema y las tres compañeras doblan la esquina hacia el aula."

    hide ema with moveoutright
    hide companeras with moveoutright

    "Apoyás el bolso sobre un banco de madera y huís del colegio hacia la calle."
    #play sound timbre_lejos

    jump escena_11b

label escena_11b:

    scene bg bano_casa with fade
    #play sound zumbido_y_canilla

    show micaela ojos_rojos at center with dissolve

    "Apoyás ambas manos en el lavabo mientras tu celular vibra sin pausa en el estante."

    # post bolso viral: ña foto de micaela con el bolso circula en estados con burlas
    show insert post_bolso_viral at truecenter with dissolve
    pause 1.5
    hide insert post_bolso_viral with dissolve

    "Abrís el botiquín, volcás un puñado de pastillas en tu boca y tragás agua de la canilla."

    if estado.energia() < 10:

        "Volvés a inclinar el frasco sobre tu palma abierta."
        "Tragás de nuevo."

    else:
        
        "Mirás el frasco de pastillas por unos segundos."
        "Te arrepentís pero ya es tarde."

    "La puerta del baño golpea contra la pared; entra Marta con su uniforme de limpieza."

    #stop sound
    #play sound golpe_puerta
    #play sound pastillas_impactando_con_el_suelo
    with vpunch

    show marta furiosa_uniforme at right with moveinright
    show micaela en_el_suelo at left with moveinbottom

    "Marta manotea el frasco, desparrama las pastillas y te sacude de los hombros."

    Ma "¿Qué mierda tomaste, pendeja? ¡Escupí eso ya!"

    with hpunch
    "Resbalás contra la pared hasta el suelo mientras Marta agarra el frasco y saca su celular."
    jump escena_12b

label escena_12b:

    scene bg habitacion_hospital with fade
    #play sound "monitor_cardiaco

    show micaela camilla_dormida at left with dissolve
    show marta silla_plastica at right with dissolve
    show enfermera planilla at center with dissolve

    En "El lavaje agarró a tiempo, señora.\nPor ahora sigue estable, pero todavía no reacciona."

    hide enfermera with moveoutright

    "Sobre la mesa de luz, tu celular enciende su pantalla con una notificación nueva."

    #play sound "vibracion_corta

    show insert marta_apagando_celular at truecenter with dissolve
    pause 1.5
    hide insert marta_apagando_celular with dissolve

    "Marta cubre tu mano inmóvil con la suya bajo el reflejo verde del monitor."

    scene bg negro_absoluto with Dissolve(2.5)
    pause 1.0
    stop sound

    centered "{b}FINAL 2 DE 3: SIN SEÑAL{/b}\n\nFIN DEL ACTO III"

    return

return
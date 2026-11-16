import pygame
import sys

pygame.init()
pygame.mixer.init()

# Configuración
ANCHO, ALTO = 900, 500
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Aprender A Quererte - Morat")
reloj = pygame.time.Clock()
fuente = pygame.font.SysFont("arial", 40)

COLOR_TEXTO = (255, 255, 255)
COLOR_FONDO = (20, 20, 20)

# Ruta de la canción
RUTA_CANCION = (
    r"C:/Users/Robert Ribas/Documents/curso_de_POO/reproducion/cancion.mp3"
)

def letras():
    # Cargar y reproducir música
    pygame.mixer.music.load(RUTA_CANCION)
    pygame.mixer.music.play()

    letras_1 = [
        "PARA APRENDER A QUERERTEE",
        "VOY A ESTUDIAR COMO SE CUMPLEN TUS SUEÑOS",
        "VOY A LEERTE SIEMPRE MUY LENTAMENTE",
        "QUIERO ENTENDERTEEEEEEE",
        "............",
        "CUANDO TE VI TUVE UN BUEN PRESENTIMIENTOOO",
        "DE ESOS QUE LLEGAN UNA SOLA VEZ EN LA VIDA",
        "QUIERO TENERTE AUNQUE SEA SOLO UN MOMENTO",
        "Y SI ME DEJAS TAL VEZ TODOS LOS DIASs"
        
    ]

    # Tiempo de espera entre líneas
    pausa_entre_lineas = 1

    # Tiempo de espera entre caracteres
    velocidad_escritura = 90

    for line in letras_1:
        texto_actual = ""

        for char in line:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            texto_actual += char
            pantalla.fill(COLOR_FONDO)

            texto = fuente.render(texto_actual, True, COLOR_TEXTO)

            x = (ANCHO - texto.get_width()) // 2
            y = (ALTO - texto.get_height()) // 2

            pantalla.blit(texto, (x, y))
            pygame.display.update()
            pygame.time.wait(velocidad_escritura)
        pygame.time.wait(pausa_entre_lineas * 1000)


# Fondo inicial
pantalla.fill(COLOR_FONDO)
pygame.display.update()

# Ejecutar letras
letras()

# Mantener ventana abierta
ejecutando = True

while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    reloj.tick(30)

pygame.quit()
sys.exit()
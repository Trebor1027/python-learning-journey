import pygame
import random
import math

# Inicializar Pygame
pygame.init()
pygame.font.init()

# --- CONFIGURACIÓN DE PANTALLA Y DISEÑO ---
ANCHO_VENTANA = 850
ALTO_VENTANA = 720
ANCHO_JUEGO = 300   # 10 columnas * 30px
ALTO_JUEGO = 600    # 20 filas * 30px
TAMAÑO_BLOQUE = 30

# Centrado dinámico del tablero
ORIGEN_X = (ANCHO_VENTANA - ANCHO_JUEGO) // 2
ORIGEN_Y = (ALTO_VENTANA - ALTO_JUEGO) // 2 + 20

# --- COLORES NEÓN Y DISEÑO ---
NEGRO_FONDO = (10, 10, 14)
GRIS_PANEL = (20, 20, 28)
GRIS_LINEA = (30, 30, 42)
BLANCO = (245, 245, 250)
COLOR_TEXTO_MUTED = (120, 125, 140)

# Colores brillantes de las piezas (Tetriminos) con su variante neón/brillante
COLORES_PIEZAS = [
    (0, 0, 0),
    (0, 240, 240),      # I - Cian neón
    (0, 100, 255),      # J - Azul eléctrico
    (255, 140, 0),      # L - Naranja ardiente
    (255, 220, 0),      # O - Amarillo vibrante
    (0, 230, 80),       # S - Verde ácido
    (180, 40, 255),     # T - Violeta místico
    (255, 40, 80)       # Z - Rojo neón
]

FORMAS = [
    # I
    [['.....',
      '..X..',
      '..X..',
      '..X..',
      '..X..'],
     ['.....',
      'XXXX.',
      '.....',
      '.....']],
    # J
    [['.....',
      '..X..',
      '..X..',
      '.XX..',
      '.....'],
     ['.....',
      '.X...',
      '.XXX.',
      '.....',
      '.....'],
     ['.....',
      '..XX.',
      '..X..',
      '..X..',
      '.....'],
     ['.....',
      '.....',
      '.XXX.',
      '...X.',
      '.....']],
    # L
    [['.....',
      '..X..',
      '..X..',
      '..XX.',
      '.....'],
     ['.....',
      '.....',
      '.XXX.',
      '.X...',
      '.....'],
     ['.....',
      '.XX..',
      '..X..',
      '..X..',
      '.....'],
     ['.....',
      '...X.',
      '.XXX.',
      '.....',
      '.....']],
    # O
    [['.....',
      '.....',
      '.XX..',
      '.XX..',
      '.....']],
    # S
    [['.....',
      '.....',
      '..XX.',
      '.XX..',
      '.....'],
     ['.....',
      '.X...',
      '.XX..',
      '..X..',
      '.....']],
    # T
    [['.....',
      '..X..',
      '.XX..',
      '..X..',
      '.....'],
     ['.....',
      '.....',
      '.XXX.',
      '..X..',
      '.....'],
     ['.....',
      '..X..',
      '..XX.',
      '..X..',
      '.....'],
     ['.....',
      '..X..',
      '.XXX.',
      '.....',
      '.....']],
    # Z
    [['.....',
      '.....',
      '.XX..',
      '..XX.',
      '.....'],
     ['.....',
      '..X..',
      '.XX..',
      '.X...',
      '.....']]
]

class Particula:
    """Representa una partícula brillante tras destruir líneas"""
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.vx = random.uniform(-4, 4)
        self.vy = random.uniform(-6, 2)
        self.color = color
        self.vida = 255  # Opacidad inicial
        self.gravedad = 0.15
        self.tamano = random.randint(3, 7)

    def actualizar(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += self.gravedad
        self.vida -= 10  # Se desvanece rápido
        if self.vida < 0:
            self.vida = 0

    def dibujar(self, superficie):
        if self.vida > 0:
            # Crear una superficie pequeña para manejar el canal alfa
            temp_surf = pygame.Surface((self.tamano*2, self.tamano*2), pygame.SRCALPHA)
            pygame.draw.circle(temp_surf, (*self.color, self.vida), (self.tamano, self.tamano), self.tamano)
            superficie.blit(temp_surf, (self.x - self.tamano, self.y - self.tamano))


class Pieza:
    def __init__(self, x, y, tipo):
        self.x = x
        self.y = y
        self.tipo = tipo
        self.forma = FORMAS[tipo]
        self.color = COLORES_PIEZAS[tipo + 1]
        self.rotacion = 0


def crear_cuadricula(posiciones_fijas={}):
    cuadricula = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]
    for y in range(20):
        for x in range(10):
            if (x, y) in posiciones_fijas:
                cuadricula[y][x] = posiciones_fijas[(x, y)]
    return cuadricula


def convertir_formato_pieza(pieza, offset_x=0, offset_y=0, rotacion_custom=None):
    """Convierte la pieza a posiciones en la rejilla, permitiendo offsets de prueba"""
    posiciones = []
    rot = pieza.rotacion if rotacion_custom is None else rotacion_custom
    formato = pieza.forma[rot % len(pieza.forma)]

    for i, linea in enumerate(formato):
        for j, columna in enumerate(linea):
            if columna == 'X':
                posiciones.append((pieza.x + j - 2 + offset_x, pieza.y + i - 4 + offset_y))
    return posiciones


def espacio_valido(pieza, cuadricula, offset_x=0, offset_y=0, rotacion_custom=None):
    """Evalúa si una posición hipotética de la pieza es válida en el tablero"""
    posiciones_aceptadas = [[(x, y) for x in range(10) if cuadricula[y][x] == (0, 0, 0)] for y in range(20)]
    posiciones_aceptadas = [x for sublista in posiciones_aceptadas for x in sublista]

    formato_pieza = convertir_formato_pieza(pieza, offset_x, offset_y, rotacion_custom)

    for pos in formato_pieza:
        if pos[1] >= 0:
            if pos not in posiciones_aceptadas:
                return False
        else:
            if pos[0] < 0 or pos[0] >= 10:
                return False
    return True


def comprobar_perdiste(posiciones_fijas):
    for pos in posiciones_fijas:
        _, y = pos
        if y < 0:
            return True
    return False


def obtener_pieza_aleatoria():
    return Pieza(5, 0, random.randint(0, len(FORMAS) - 1))


def dibujar_texto(superficie, texto, tamaño, color, x, y, centrado=True, negrita=True):
    fuente = pygame.font.SysFont('Consolas', tamaño, bold=negrita)
    etiqueta = fuente.render(texto, True, color)
    if centrado:
        superficie.blit(etiqueta, (x - etiqueta.get_width() // 2, y - etiqueta.get_height() // 2))
    else:
        superficie.blit(etiqueta, (x, y))


def dibujar_bloque_estilizado(superficie, x, y, color, es_fantasma=False):
    """Dibuja un bloque con relieve 3D brillante o estilo fantasma futurista"""
    rect = pygame.Rect(x, y, TAMAÑO_BLOQUE, TAMAÑO_BLOQUE)
    
    if es_fantasma:
        # Silueta neón translúcida
        pygame.draw.rect(superficie, color, rect, 2, border_radius=4)
        # Sutil relleno interno muy oscuro/transparente
        sombra = pygame.Surface((TAMAÑO_BLOQUE - 4, TAMAÑO_BLOQUE - 4), pygame.SRCALPHA)
        sombra.fill((*color, 40))
        superficie.blit(sombra, (x + 2, y + 2))
    else:
        # Bloque Sólido con Relieve/Glow
        pygame.draw.rect(superficie, color, rect, border_radius=5)
        
        # Borde exterior más brillante
        pygame.draw.rect(superficie, (255, 255, 255), rect, 1, border_radius=5)
        
        # Brillo interno (Highlight superior izquierdo)
        highlight = pygame.Surface((TAMAÑO_BLOQUE - 6, TAMAÑO_BLOQUE - 6), pygame.SRCALPHA)
        highlight.fill((255, 255, 255, 45))  # Blanco translúcido
        superficie.blit(highlight, (x + 3, y + 3))


def dibujar_tablero_y_rejilla(superficie):
    """Dibuja el fondo de la zona de juego con una rejilla de estilo cyberpunk"""
    # Fondo interno del juego
    pygame.draw.rect(superficie, (12, 12, 18), (ORIGEN_X, ORIGEN_Y, ANCHO_JUEGO, ALTO_JUEGO))
    
    for i in range(20):
        # Líneas horizontales con muy baja opacidad
        pygame.draw.line(superficie, GRIS_LINEA, (ORIGEN_X, ORIGEN_Y + i * TAMAÑO_BLOQUE), 
                         (ORIGEN_X + ANCHO_JUEGO, ORIGEN_Y + i * TAMAÑO_BLOQUE), 1)
    for j in range(10):
        # Líneas verticales
        pygame.draw.line(superficie, GRIS_LINEA, (ORIGEN_X + j * TAMAÑO_BLOQUE, ORIGEN_Y), 
                         (ORIGEN_X + j * TAMAÑO_BLOQUE, ORIGEN_Y + ALTO_JUEGO), 1)


def eliminar_filas(cuadricula, posiciones_fijas, particulas):
    """Elimina las filas y genera partículas coloridas en los bloques eliminados"""
    filas_eliminadas = 0
    for i in range(len(cuadricula)-1, -1, -1):
        fila = cuadricula[i]
        if (0, 0, 0) not in fila:
            filas_eliminadas += 1
            indice_fila_eliminada = i
            
            # Generar explosión de partículas antes de eliminar
            for j in range(10):
                color_particula = cuadricula[i][j] if cuadricula[i][j] != (0, 0, 0) else (255, 255, 255)
                px = ORIGEN_X + j * TAMAÑO_BLOQUE + TAMAÑO_BLOQUE // 2
                py = ORIGEN_Y + i * TAMAÑO_BLOQUE + TAMAÑO_BLOQUE // 2
                for _ in range(3):  # 3 partículas por cada bloque destruido
                    particulas.append(Particula(px, py, color_particula))
                    
            # Eliminar bloques de posiciones fijas
            for j in range(len(fila)):
                try:
                    del posiciones_fijas[(j, i)]
                except KeyError:
                    continue
            
            # Desplazar posiciones fijas superiores
            nuevas_posiciones = {}
            for clave in posiciones_fijas:
                x, y = clave
                if y < indice_fila_eliminada:
                    nuevas_posiciones[(x, y + 1)] = posiciones_fijas[clave]
                else:
                    nuevas_posiciones[(x, y)] = posiciones_fijas[clave]
            posiciones_fijas.clear()
            posiciones_fijas.update(nuevas_posiciones)
            
            # Subida recursiva en caso de múltiples filas consecutivas
            filas_eliminadas += eliminar_filas(cuadricula, posiciones_fijas, particulas)
            break

    return filas_eliminadas


def dibujar_siguiente_pieza(pieza, superficie):
    """Panel lateral derecho de la siguiente pieza"""
    sx = ORIGEN_X + ANCHO_JUEGO + 40
    sy = ORIGEN_Y + 10
    
    # Contenedor elegante
    pygame.draw.rect(superficie, GRIS_PANEL, (sx, sy, 160, 170), border_radius=12)
    pygame.draw.rect(superficie, GRIS_LINEA, (sx, sy, 160, 170), 2, border_radius=12)
    
    dibujar_texto(superficie, 'SIGUIENTE', 16, COLOR_TEXTO_MUTED, sx + 80, sy + 25)
    
    # Dibujar la pieza centrada en el contenedor
    formato = pieza.forma[pieza.rotacion % len(pieza.forma)]
    
    # Centrado fino según el tipo de bloque
    offset_dibujo_x = 10 if pieza.tipo in [0, 3] else 20
    
    for i, linea in enumerate(formato):
        for j, columna in enumerate(linea):
            if columna == 'X':
                dibujar_bloque_estilizado(
                    superficie, 
                    sx + j * 24 + offset_dibujo_x, 
                    sy + i * 24 + 45, 
                    pieza.color
                )


def dibujar_interfaz_lateral(superficie, puntuacion, lineas, record):
    """Panel lateral izquierdo de información de juego"""
    sx = ORIGEN_X - 200
    sy = ORIGEN_Y + 10

    # Contenedor de estadísticas
    pygame.draw.rect(superficie, GRIS_PANEL, (sx, sy, 160, 320), border_radius=12)
    pygame.draw.rect(superficie, GRIS_LINEA, (sx, sy, 160, 320), 2, border_radius=12)

    # Récord Histórico (Dorado)
    dibujar_texto(superficie, 'RÉCORD', 14, COLOR_TEXTO_MUTED, sx + 80, sy + 30)
    dibujar_texto(superficie, str(record), 28, (255, 215, 0), sx + 80, sy + 65)

    # Separador sutil
    pygame.draw.line(superficie, GRIS_LINEA, (sx + 20, sy + 105), (sx + 140, sy + 105), 1)

    # Puntos actuales
    dibujar_texto(superficie, 'PUNTOS', 14, COLOR_TEXTO_MUTED, sx + 80, sy + 135)
    dibujar_texto(superficie, str(puntuacion), 28, BLANCO, sx + 80, sy + 170)

    # Separador sutil
    pygame.draw.line(superficie, GRIS_LINEA, (sx + 20, sy + 210), (sx + 140, sy + 210), 1)

    # Líneas eliminadas
    dibujar_texto(superficie, 'LÍNEAS', 14, COLOR_TEXTO_MUTED, sx + 80, sy + 240)
    dibujar_texto(superficie, str(lineas), 28, (0, 240, 240), sx + 80, sy + 275)

    # Panel de Controles inferior
    ayuda_y = sy + 350
    pygame.draw.rect(superficie, GRIS_PANEL, (sx, ayuda_y, 160, 200), border_radius=12)
    pygame.draw.rect(superficie, GRIS_LINEA, (sx, ayuda_y, 160, 200), 2, border_radius=12)

    dibujar_texto(superficie, 'CONTROLES', 14, BLANCO, sx + 80, ayuda_y + 25)
    controles = [
        "← → : Mover",
        "↑   : Rotar",
        "↓   : Caída Rápida",
        "ESP : Caída Inst.",
        "P   : Pausar"
    ]
    for i, linea in enumerate(controles):
        dibujar_texto(superficie, linea, 12, COLOR_TEXTO_MUTED, sx + 80, ayuda_y + 60 + i * 25, negrita=False)


def juego():
    posiciones_fijas = {}
    cuadricula = crear_cuadricula(posiciones_fijas)

    cambiar_pieza = False
    ejecutando = True
    pausado = False
    pieza_actual = obtener_pieza_aleatoria()
    siguiente_pieza = obtener_pieza_aleatoria()
    
    reloj = pygame.time.Clock()
    
    tiempo_caida = 0
    velocidad_caida = 0.45
    
    puntuacion = 0
    lineas_eliminadas = 0
    record = 0

    # Partículas y efecto de sacudida
    particulas = []
    shake_intensity = 0

    try:
        with open("record.txt", "r") as f:
            record = int(f.readline())
    except (FileNotFoundError, ValueError):
        record = 0

    while ejecutando:
        cuadricula = crear_cuadricula(posiciones_fijas)
        tiempo_caida += reloj.get_rawtime()
        reloj.tick()

        # Decaimiento del efecto de sacudida
        if shake_intensity > 0:
            shake_intensity -= 1

        velocidad_actual = max(0.08, velocidad_caida - (lineas_eliminadas // 8) * 0.05)

        # Caída por gravedad
        if tiempo_caida/1000 >= velocidad_actual:
            tiempo_caida = 0
            if not pausado:
                pieza_actual.y += 1
                if not espacio_valido(pieza_actual, cuadricula) and pieza_actual.y > 0:
                    pieza_actual.y -= 1
                    cambiar_pieza = True

        # --- EVENTOS DE JUEGO ---
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
                pygame.display.quit()
                quit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    pausado = not pausado

                if not pausado:
                    if evento.key == pygame.K_LEFT:
                        pieza_actual.x -= 1
                        if not espacio_valido(pieza_actual, cuadricula):
                            pieza_actual.x += 1
                    
                    elif evento.key == pygame.K_RIGHT:
                        pieza_actual.x += 1
                        if not espacio_valido(pieza_actual, cuadricula):
                            pieza_actual.x -= 1
                    
                    elif evento.key == pygame.K_UP:
                        # Probar rotación válida
                        pieza_actual.rotacion = (pieza_actual.rotacion + 1) % len(pieza_actual.forma)
                        if not espacio_valido(pieza_actual, cuadricula):
                            # Rotación reversa si falla
                            pieza_actual.rotacion = (pieza_actual.rotacion - 1) % len(pieza_actual.forma)
                    
                    elif evento.key == pygame.K_DOWN:
                        pieza_actual.y += 1
                        if not espacio_valido(pieza_actual, cuadricula):
                            pieza_actual.y -= 1
                    
                    elif evento.key == pygame.K_SPACE:
                        # Caída Instantánea (Hard Drop)
                        caidas = 0
                        while espacio_valido(pieza_actual, cuadricula):
                            pieza_actual.y += 1
                            caidas += 1
                        pieza_actual.y -= 1
                        cambiar_pieza = True
                        
                        # Sacudir pantalla proporcionalmente a la distancia de caída
                        if caidas > 2:
                            shake_intensity = min(12, caidas * 1.5)

        # --- GESTIÓN DE PIEZA FANTASMA (GHOST PIECE) ---
        sombra_y = pieza_actual.y
        if not pausado:
            while espacio_valido(pieza_actual, cuadricula, offset_y=sombra_y - pieza_actual.y + 1):
                sombra_y += 1

        # --- DIBUJADO DE LA PANTALLA ---
        # Aplicar sacudida de pantalla al lienzo principal
        offset_shake_x = random.randint(-int(shake_intensity), int(shake_intensity)) if shake_intensity > 0 else 0
        offset_shake_y = random.randint(-int(shake_intensity), int(shake_intensity)) if shake_intensity > 0 else 0

        # Crear una superficie auxiliar para dbiujar todo con offset de sacudida
        lienzo = pygame.Surface((ANCHO_VENTANA, ALTO_VENTANA))
        lienzo.fill(NEGRO_FONDO)

        # Dibujar decoraciones de fondo elegantes
        dibujar_texto(lienzo, 'TETRIS ULTRA', 42, (30, 35, 50), ANCHO_VENTANA // 2, 40)
        dibujar_texto(lienzo, 'TETRIS ULTRA', 40, BLANCO, ANCHO_VENTANA // 2, 38)

        # Tablero y Rejilla
        dibujar_tablero_y_rejilla(lienzo)

        # Dibujar bloques fijados en el tablero
        for i in range(20):
            for j in range(10):
                color_bloque = cuadricula[i][j]
                if color_bloque != (0, 0, 0):
                    dibujar_bloque_estilizado(lienzo, ORIGEN_X + j * TAMAÑO_BLOQUE, ORIGEN_Y + i * TAMAÑO_BLOQUE, color_bloque)

        # Dibujar la sombra de la pieza fantasma
        if not pausado and sombra_y > pieza_actual.y:
            posiciones_sombra = convertir_formato_pieza(pieza_actual, offset_y=sombra_y - pieza_actual.y)
            for pos in posiciones_sombra:
                x, y = pos
                if y >= 0:
                    dibujar_bloque_estilizado(lienzo, ORIGEN_X + x * TAMAÑO_BLOQUE, ORIGEN_Y + y * TAMAÑO_BLOQUE, pieza_actual.color, es_fantasma=True)

        # Dibujar la pieza activa actual
        posiciones_pieza = convertir_formato_pieza(pieza_actual)
        for pos in posiciones_pieza:
            x, y = pos
            if y >= 0:
                dibujar_bloque_estilizado(lienzo, ORIGEN_X + x * TAMAÑO_BLOQUE, ORIGEN_Y + y * TAMAÑO_BLOQUE, pieza_actual.color)

        # Actualizar y dibujar partículas
        for particula in particulas[:]:
            particula.actualizar()
            particula.dibujar(lienzo)
            if particula.vida <= 0:
                particulas.remove(particula)

        # Si la pieza se consolida
        if cambiar_pieza:
            for pos in posiciones_pieza:
                posiciones_fijas[(pos[0], pos[1])] = pieza_actual.color
            pieza_actual = siguiente_pieza
            siguiente_pieza = obtener_pieza_aleatoria()
            cambiar_pieza = False

            # Limpiar filas y generar puntos / partículas
            filas_limpias = eliminar_filas(cuadricula, posiciones_fijas, particulas)
            if filas_limpias > 0:
                puntuacion += {1: 100, 2: 350, 3: 600, 4: 1000}.get(filas_limpias, 0)
                lineas_eliminadas += filas_limpias
                shake_intensity = min(15, filas_limpias * 4)  # Gran sacudida al destruir líneas
                if puntuacion > record:
                    record = puntuacion
                    with open("record.txt", "w") as f:
                        f.write(str(record))

            if comprobar_perdiste(posiciones_fijas):
                ejecutando = False

        # Paneles de Interfaz
        dibujar_siguiente_pieza(siguiente_pieza, lienzo)
        dibujar_interfaz_lateral(lienzo, puntuacion, lineas_eliminadas, record)

        if pausado:
            # Oscurecer suavemente la cuadrícula de juego
            sombra_pausa = pygame.Surface((ANCHO_JUEGO, ALTO_JUEGO), pygame.SRCALPHA)
            sombra_pausa.fill((0, 0, 0, 180))
            lienzo.blit(sombra_pausa, (ORIGEN_X, ORIGEN_Y))
            dibujar_texto(lienzo, 'PAUSA', 36, BLANCO, ORIGEN_X + ANCHO_JUEGO // 2, ORIGEN_Y + ALTO_JUEGO // 2 - 20)
            dibujar_texto(lienzo, 'Presiona P para reanudar', 16, COLOR_TEXTO_MUTED, ORIGEN_X + ANCHO_JUEGO // 2, ORIGEN_Y + ALTO_JUEGO // 2 + 20)

        # Dibujar lienzo con la sacudida aplicada a la ventana de Windows
        ventana.fill(NEGRO_FONDO)
        ventana.blit(lienzo, (offset_shake_x, offset_shake_y))
        pygame.display.update()

    # --- MENÚ DE JUEGO TERMINADO ---
    ejecutando_game_over = True
    while ejecutando_game_over:
        ventana.fill(NEGRO_FONDO)
        dibujar_texto(ventana, 'JUEGO TERMINADO', 48, (255, 40, 80), ANCHO_VENTANA // 2, ALTO_VENTANA // 2 - 80)
        dibujar_texto(ventana, f'Puntaje Final: {puntuacion}', 24, BLANCO, ANCHO_VENTANA // 2, ALTO_VENTANA // 2)
        dibujar_texto(ventana, 'Presiona CUALQUIER TECLA para volver a jugar', 16, COLOR_TEXTO_MUTED, ANCHO_VENTANA // 2, ALTO_VENTANA // 2 + 80)
        dibujar_texto(ventana, 'o ESCAPE para salir', 14, COLOR_TEXTO_MUTED, ANCHO_VENTANA // 2, ALTO_VENTANA // 2 + 110)
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando_game_over = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    ejecutando_game_over = False
                else:
                    juego()
                    ejecutando_game_over = False


def menu_inicio():
    ejecutando_menu = True
    
    reloj = pygame.time.Clock()
    animacion_bucle = 0

    while ejecutando_menu:
        ventana.fill(NEGRO_FONDO)
        reloj.tick(60)
        animacion_bucle += 0.05
        
        # Efecto de pulso neon flotante para el título
        desplazamiento_y = math.sin(animacion_bucle) * 10
        
        dibujar_texto(ventana, 'TETRIS', 72, (20, 30, 45), ANCHO_VENTANA // 2, ALTO_VENTANA // 2 - 120 + desplazamiento_y)
        dibujar_texto(ventana, 'TETRIS', 70, BLANCO, ANCHO_VENTANA // 2, ALTO_VENTANA // 2 - 122 + desplazamiento_y)
        
        dibujar_texto(ventana, 'ULTRA EDITION', 22, (0, 240, 240), ANCHO_VENTANA // 2, ALTO_VENTANA // 2 - 50 + desplazamiento_y)
        
        # CORREGIDO: Mapeamos la onda senoidal para que el color siempre esté entre 100 y 255 (nunca sobrepase 255)
        alfa_jugar = int(((math.sin(animacion_bucle * 2.5) + 1) / 2) * 155) + 100
        color_jugar = (alfa_jugar, alfa_jugar, min(255, alfa_jugar + 100))
        
        dibujar_texto(ventana, 'Presiona CUALQUIER TECLA para empezar', 18, color_jugar, ANCHO_VENTANA // 2, ALTO_VENTANA // 2 + 80)
        
        # Créditos y motor
        dibujar_texto(ventana, 'Powered by Pygame • Engine 2026', 14, COLOR_TEXTO_MUTED, ANCHO_VENTANA // 2, ALTO_VENTANA - 40)

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando_menu = False
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                juego()
                ejecutando_menu = False


# Crear Ventana Principal
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption('Tetris Ultra Edition')

if __name__ == '__main__':
    menu_inicio()
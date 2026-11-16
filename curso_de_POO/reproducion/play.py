import time
import sys
import os
import pygame

pygame.mixer.init()

def letras():
    pygame.mixer.music.load(
        r"c:\\Users\\Robert Ribas\\Documents\\curso_de_POO\\reproducion\cancion.mp3"
        )
    pygame.mixer.music.play()
    
    letras_1 = [
        "PARA APRENDER A QUERERTEE📖",
        "VOY A ESTUDIAR COMO SE CUMPLEN TUS SUEÑOS✨",
        "VOY A LEERTE SIEMPRE MUY LENTAMENTE🐢",
        "QUIERO ENTENDERTEEEEEEE❤️",
        "CUANDO TE VI TUVE UN BUEN PRESENTIMIENTOOO😩",
        "DE ESOS QUE LLEGAN UNA SOLA VEZ EN LA VIDA🥹",
        "QUIERO TENERTE AUNQUE SEA SOLO UN MOMENTO",
        "Y SI ME DEJAS TAL VEZ TODOS LOS DIASs"
        ]
    letras_retraso = [0.7,0.8,0.7,2,0.8,0.8,0.8,0.8]
    time.sleep(0.4)
     
    for i, line in enumerate(letras_1):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        print()
        time.sleep(letras_retraso[i])


letras()
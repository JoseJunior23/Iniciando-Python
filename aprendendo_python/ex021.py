#esse programa deve tocar uma musica em mp3 pelo python

import pygame
pygame.mixer.init()
pygame.mixer_music.load('human.mp3')
pygame.mixer_music.play()
input()
pygame.event.wait()

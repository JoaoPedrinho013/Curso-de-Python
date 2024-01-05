#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer_music.load('ex021.mp3')
pygame.mixer_music.play()
pygame.event.clear()
pygame.event.wait()
pygame.quit()

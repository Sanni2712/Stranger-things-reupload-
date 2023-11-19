import pygame
import time
from pygame import mixer

mixer.init()
pygame.init()
white = (255, 255, 255)
X = 950
Y = 615
display_surface = pygame.display.set_mode((X, Y))
dtx = ''
pygame.display.set_caption('Stranger things')

default = pygame.image.load(r'C:/Users/sanni/Desktop/lights/defaultimg.jpg').convert_alpha()
default = pygame.transform.scale(default, (X, Y))
display_surface.blit(default, (0, 0))
pygame.display.update()
mixer.music.load(r'C:/Users/sanni/Desktop/lights/my audio.mp3')
runtime = True
while runtime:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            dtx = event.unicode
            a = pygame.image.load(f'C:/Users/sanni/Desktop/lights/wall letters/{dtx}.png').convert_alpha()
            a = pygame.transform.scale(a, (X, Y))
            display_surface.blit(a, (0, 0))
            pygame.display.update()

            mixer.music.play()
            time.sleep(.5)
            display_surface.blit(default, (0, 0))
            pygame.display.update()
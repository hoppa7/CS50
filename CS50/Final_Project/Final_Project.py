import pygame
import sys
pygame.init()

white = (255,255,255)

rect_position = (100, 100)
rect_size = (50, 100)
rect = pygame.Rect(rect_position, rect_size)

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Pong Project")
pygame.draw.rect(screen, white, rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.draw.rect(screen, white, rect)
    pygame.display.flip()
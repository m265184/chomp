import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600

blue = (0, 0, 255)
brown = (139, 69, 19)


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Blue Background with brown rectangle")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(blue)
    rectangle_height = 500
    pygame.draw.rect(screen, brown, (0, screen_height - rectangle_height, screen_width, rectangle_height))
    pygame.display.flip()

pygame.quit()
sys.exit()
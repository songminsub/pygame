import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
BLANK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BURE = (0, 0, 255)

color = (BLANK, RED, GREEN, BURE)

pygame.init()
pygame.display.set_caption("pygame")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

color = BLANK

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                color = random.choice([BLANK, RED, GREEN, BURE])
    screen.fill(WHITE)
    rect = pygame.Rect(0, 0, 100, 100)
    rect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    pygame.draw.rect(screen, color, rect, 0)
    pygame.display.flip()

pygame.quit()
                
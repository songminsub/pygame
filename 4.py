import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
BLANK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BURE = (0, 0, 255)

rc_x = int(SCREEN_WIDTH/2)
rc_y = int(SCREEN_HEIGHT/2)
rc_dx = 0
rc_dy = 0

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
            if event.key == pygame.K_LEFT:
                rc_dx = -3
            elif event.key == pygame.K_RIGHT:
                rc_dx = 3
            elif event.key == pygame.K_UP:
                rc_dy = -3
            elif event.key == pygame.K_DOWN:
                rc_dy = 3
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                rc_dx = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                rc_dy = 0
        if rc_x <= 0 or rc_x >= SCREEN_WIDTH:
            rc_dx = rc_dx * -1
        elif rc_y <= 0 or rc_y >= SCREEN_HEIGHT:
            rc_dy = rc_dy * -1

    rc_x += rc_dx
    rc_y += rc_dy

    screen.fill(WHITE)
    rect = pygame.Rect(rc_x, rc_y, 20, 20)
    pygame.draw.rect(screen, BLANK, rect, 0)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
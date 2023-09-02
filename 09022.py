import pygame
import random

SCREEN_WIDHT = 600
SCREEN_HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
clock = pygame.time.Clock()

ball_x = SCREEN_WIDHT//2
ball_y = SCREEN_HEIGHT//2
ball_dx = random.randint(1, 10)
ball_dy = random.randint(1, 10)
ball_size = 30

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball_x += ball_dx
    ball_y += ball_dy
        
    if (ball_x + ball_size) > SCREEN_WIDHT or (ball_x - ball_size) < 0:
            ball_dx *= -1
    if (ball_y + ball_size) > SCREEN_HEIGHT or (ball_y - ball_size) < 0:
            ball_dy *= -1


    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, [ball_x, ball_y], ball_size, 0)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
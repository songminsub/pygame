import pygame
import os


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
SKYBLUE = (128, 231, 252)
RED = (255, 0, 0)


pygame.init()
pygame.display.set_caption("복습")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')
fish_image = pygame.image.load(os.path.join(assets_path, 'fish.png'))

fish_x = SCREEN_WIDTH//2
fish_y = SCREEN_HEIGHT//2
fish_dx = 0
fish_dy = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keyboard_dx = -5
            elif event.key == pygame.K_RIGHT:
                keyboard_dx = 5
            elif event.key == pygame.K_UP:
                keyboard_dy = -5
            elif event.key == pygame.K_DOWN:
                keyboard_dy = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                keyboard_dx = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                keyboard_dy = 0

    fish_x += fish_dx
    fish_y += fish_dy

    screen.fill(WHITE)
    pygame.draw.line(screen, RED, [0,0], [SCREEN_WIDTH,SCREEN_HEIGHT], 5)
    pygame.draw.line(screen, RED, [SCREEN_WIDTH,0], [0,SCREEN_HEIGHT], 5)
    pygame.draw.rect(screen, GREEN, [200,200,50,50], 0)
    pygame.draw.circle(screen,BLACK, [300,300],10,3)

    font = pygame.font.SysFont("Malgun Gothic", 30, False, False)
    font1 = pygame.font.SysFont("Malgun Gothic", 20, False, False)
    text = font.render("안녕 파이게임", True, BLACK)
    text1 = font1.render("9월 2일 토요일", True, BLACK)
    screen.blit(text, [10,10])
    screen.blit(text1, [10,50])
    screen.blit(fish_image, [fish_x, fish_y])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
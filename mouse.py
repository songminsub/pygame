import pygame
import os

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

WHITE = (255, 255, 255)

pygame.init()

pygame.display.set_caption("마우스")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')
mouse_image = pygame.image.load(os.path.join(assets_path, 'mouse.png'))
mouse_x = int(WINDOW_WIDTH/2)
mouse_y = int(WINDOW_HEIGHT/2)
pygame.mouse.set_visible(False)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pos = pygame.mouse.get_pos()
    screen.fill(WHITE)
    screen.blit(mouse_image, pos)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
import pygame
import os

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 400

BLANK = (0, 0, 0)

pygame.init()

pygame.display.set_caption("sound")

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')
background_image = pygame.image.load(os.path.join(assets_path, 'equalizer.png'))
pygame.mixer.music.load(os.path.join(assets_path, 'bgm.wav'))
pygame.mixer.music.play(-1)
sound = pygame.mixer.Sound(os.path.join(assets_path, "sound.wav"))


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            sound.play()
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(BLANK)
    screen.blit(background_image, background_image.get_rect())
    pygame.display.flip()
    clock.tick(60)
pygame.quit
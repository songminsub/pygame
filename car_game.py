import pygame

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150,150,150)
RED = (200, 0, 0)

CAR_COUNT = 3
LANE_COUNT = 5
SPEED = 10

class Lane():
    def __init__(self):
        self.color = WHITE
        self.width = 10
        self.height = 80
        self.gap = 20
        self.space = (SCREEN_WIDTH - (self.width*LANE_COUNT)) / (LANE_COUNT-1)
        self.count = 10
        self.x = 0
        self.y = -self.height
    def move(self, speed, screen):
        self.y += speed
        if self.y > 0:
            self.y = -self.height
        self.draw(screen)
    def draw(self,screen):
        next_lane = self.y
        for i in range(self.count):
            pygame.draw.rect(screen, self.color, (self.x, next_lane, self.width, self.height))
            next_lane += self.height + self.gap

def main():
    pygame.init()
    pygame.display.set_caption("자동차게임")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(GRAY)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

main()
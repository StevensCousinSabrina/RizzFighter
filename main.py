import pygame
from fighter import Fighter

pygame.init()

SCREEN_WIDTH = 1456
SCREEN_HEIGHT = 728

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fighting DUh")

# set framerate
clock = pygame.time.Clock()
FPS = 60

bg_image = pygame.image.load("images/backgrounds/plane.gif").convert_alpha()


# function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


# create two instances of fighters
fighter_1 = Fighter(200, 350)
fighter_2 = Fighter(1000, 350)

# game loop
run = True
while run:
    clock.tick(FPS)

    # draw background
    draw_bg()

    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
    # fighter_2.move()

    # draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update display
    pygame.display.update()

pygame.quit()

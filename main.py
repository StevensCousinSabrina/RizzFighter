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

# define colors
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

#define fighter variables
WARRIOR_SIZE = 162
WARRIOR_SCALE = 7
WARRIOR_OFFSET = [69,57]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
WIZARD_SIZE = 250
WIZARD_SCALE = 6
WIZARD_OFFSET = [112, 116]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

# load background image
bg_image = pygame.image.load("assets/images/backgrounds/plane.gif").convert_alpha()

# load spritesheets
wizard_sheets = pygame.image.load("assets/Fighters/Evil Wizard/EvilWizard.png").convert_alpha()
warrior_sheets = pygame.image.load("assets/Fighters/Fantasy Warrior/FantasyWarrior.png").convert_alpha()
martial2_sheets = pygame.image.load("assets/Fighters/Martial Hero 2/MartialHero2.png").convert_alpha()
martial3_sheets = pygame.image.load("assets/Fighters/Martial Hero 3/MartialHero3.png").convert_alpha()

# define number of steps in each animation
WIZARD_ANIMATION_STEPS = [8, 8, 2, 8, 8, 3, 7]
WARRIOR_ANIMATION_STEPS = [10, 8, 3, 7, 7, 3, 7]
MARTIAL2_ANIMATION_STEPS = [4, 8, 2, 4, 4, 3, 7]
MARTIAL3_ANIMATION_STEPS = [10, 8, 3, 7, 6, 3, 11]


# function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


# function for drawing fighter health bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 5, y - 5, 435, 40))
    pygame.draw.rect(screen, RED, (x, y, 425, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 425 * ratio, 30))


character1 = warrior_sheets
character1_sheet = WARRIOR_ANIMATION_STEPS
character1_data = WARRIOR_DATA
character2 = wizard_sheets
character2_sheet = WIZARD_ANIMATION_STEPS
character2_data = WIZARD_DATA

# create two instances of fighters
fighter_1 = Fighter(200, 350, False, character1_data, character1, character1_sheet)
fighter_2 = Fighter(1000, 350, True, character2_data, character2, character2_sheet)

# game loop
run = True
while run:
    clock.tick(FPS)

    # draw background
    draw_bg()

    # show player stats
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 1011, 20)

    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
    # fighter_2.move()

    #update fighters
    fighter_1.update()
    fighter_2.update()

    # draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update display
    pygame.display.update()

pygame.quit()

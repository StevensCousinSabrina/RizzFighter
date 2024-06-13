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
BLACK = (0, 0, 0)

# define game variables
intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0] #player scores, [p1, p2]
match_over = False
ROUND_OVER_COOLDOWN = 2000

# define fighter variables
WARRIOR_SIZE = 162
WARRIOR_SCALE = 7
WARRIOR_OFFSET = [69, 57]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
WIZARD_SIZE = 250
WIZARD_SCALE = 6
WIZARD_OFFSET = [112, 116]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]
MARTIAL2_SIZE = 200
MARTIAL2_SCALE = 6
MARTIAL2_OFFSET = [84, 78]
MARTIAL2_DATA = [MARTIAL2_SIZE, MARTIAL2_SCALE, MARTIAL2_OFFSET]
MARTIAL3_SIZE = 126
MARTIAL3_SCALE = 6
MARTIAL3_OFFSET = [44, 32]
MARTIAL3_DATA = [MARTIAL3_SIZE, MARTIAL3_SCALE, MARTIAL3_OFFSET]

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

# font!
count_font = pygame.font.Font("assets/Fonts/Turok.ttf", 80)
count_font_border = pygame.font.Font("assets/Fonts/Turok.ttf", 90)
score_font = pygame.font.Font("assets/Fonts/Turok.ttf", 30)


# function for drawing text
def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


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
character2 = martial3_sheets
character2_sheet = MARTIAL3_ANIMATION_STEPS
character2_data = MARTIAL3_DATA

# create two instances of fighters
fighter_1 = Fighter(1, 200, 350, False, character1_data, character1, character1_sheet)
fighter_2 = Fighter(2, 1000, 350, True, character2_data, character2, character2_sheet)

# game loop
run = True
while run:
    clock.tick(FPS)

    # draw background
    draw_bg()

    # show player stats
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 1011, 20)

    if intro_count <= 0:
        # move fighters
        fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1)
    else:
        #draw count timer
        draw_text(str(intro_count), count_font_border, BLACK, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
        draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH/2, SCREEN_HEIGHT/3)
        # update count timer
        if pygame.time.get_ticks() - last_count_update >= 1000:
            intro_count -= 1
            last_count_update = pygame.time.get_ticks()
    # update fighters
    fighter_1.update()
    fighter_2.update()

    # draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #check for player death

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update display
    pygame.display.update()

pygame.quit()

import pygame


class FunNote:
    def __init__(self, x, y, color, text, font):
        self.x = x
        self.y = y
        self.color = color
        self.text = text
        self.font = font
        self.rect = pygame.Rect(self.x, self.y, 100, 100)
        self.delta = 2

    def move_note(self):
        self.x = self.x - self.delta
        if self.x < -100:
            self.x = 7500

    def draw(self, surface):
        img = self.font.render(self.text, True, self.color)
        surface.blit(img, (self.x, self.y))
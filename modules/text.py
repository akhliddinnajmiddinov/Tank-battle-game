import pygame as pg
import os

class Text():
    def __init__(self, screen, x, y, fontSize, buttonText, color):
        self.screen = screen
        self.x = x
        self.y = y

        pg.font.init()
        self.font = pg.font.Font("fonts/evil.ttf", fontSize)

        self.textSurf = self.font.render(buttonText, True, color)
        self.screen.blit(self.textSurf, (x, y))
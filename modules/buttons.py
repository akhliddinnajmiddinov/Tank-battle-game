import pygame as pg
import os
class Button():
    def __init__(self, screen, x, y, width, height, buttonText, fontSize, onclickFunction=None):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        pg.font.init()
        self.font = pg.font.Font("fonts/evil.ttf", fontSize)


        self.fillColors = {
            'normal': pg.Color(0, 255, 0, 0),
            'hover': pg.Color(0, 200, 0, 0)
        }

        self.buttonSurface = pg.Surface((self.width, self.height))
        self.buttonRect = pg.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = self.font.render(buttonText, True, (20, 20, 20))

    def process(self, mousePos):
        
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pg.mouse.get_pressed()[0]:
                self.onclickFunction()

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        self.screen.blit(self.buttonSurface, self.buttonRect)
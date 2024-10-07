import pygame as pg
import pymunk as pm
from .text import Text


class Platform():
    def __init__(self, space, screen, x1, y1, x2, y2, platformcolor, collision_type):
        self.screen = screen
        self.platformcolor = platformcolor
        self.body = pm.Body(body_type = pm.Body.STATIC)
        self.shape = pm.Poly(self.body, [(x1, y1), (x2, y1), (x2, y2), (x1, y2)])
        self.shape.density = 0.5
        self.shape.friction = 1
        self.shape.elasticity = 0
        self.shape.collision_type = collision_type
        space.add(self.body, self.shape)
    
    
    def draw(self):
        points = self.vec2d_to_points(self.shape.get_vertices())
        pg.draw.polygon(self.screen, self.platformcolor, points)

    def vec2d_to_points(self, vectors):
        points = []
        for vec in vectors:
            points.append((vec[0], vec[1]))
        return points
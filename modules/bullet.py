import pygame as pg
import pymunk as pm
from  math import degrees, sin, cos, radians


class Bullet():
    def __init__(self, space, screen, x1, y1, angle, collision_type):
        self.space = space
        self.screen = screen
        self.image = pg.transform.scale(pg.image.load("photos/bullet.png"), (20, 5))
        self.body = pm.Body(body_type = pm.Body.DYNAMIC)
        self.body.position = x1, y1
        self.angle = angle
        self.shape = pm.Poly.create_box(self.body, (3, 3))
        self.shape.density = 1
        self.shape.elasticity = 0
        self.shape.friction = 1
        self.shape.collision_type = collision_type
        self.space.add(self.body, self.shape)
        self.impulse = 1500
        impulses = self.impulse * cos(self.angle), - self.impulse * sin(self.angle)
        self.sound = pg.mixer.Sound('sounds/bullet.mp3')
        self.sound.play()
        self.body.apply_impulse_at_local_point(impulses, (0, 0))

    def draw(self):
        rot_image = pg.transform.rotate(self.image, degrees(self.angle))
        size = rot_image.get_size()
        pos = self.body.position
        image_pos = [pos[0] - size[0] // 2, pos[1] - size[1] // 2]
        self.screen.blit(rot_image, image_pos)
import pygame as pg
import pymunk as pm
from  math import degrees, sin, cos, radians
from .bullet import Bullet
from .text import Text

class Player():
    def __init__(self, space, screen, name, x1, y1, width, additional_angle_for_image, imagename, key, collision_type, ammoX, ammoY, ammoWidth, ammoHeight):
        self.width = width
        self.screen = screen
        self.name = name
        self.image = pg.transform.scale(pg.image.load(imagename), (self.width, self.width))
        self.body = pm.Body(body_type = pm.Body.DYNAMIC)
        self.body.position = x1, y1
        self.shape = pm.Poly.create_box(self.body, (self.width, self.width))
        self.shape.density = 1
        self.shape.elasticity = 0
        self.shape.friction = 1
        self.shape.collision_type = collision_type
        self.key = key
        self.space = space
        self.direction = 1
        self.pressing_count = 0
        self.shooting_time = 10
        self.forward_dist = 3
        self.rotating_angle = 3
        self.additional_angle_for_image = additional_angle_for_image
        self.bullets = []
        self.bulletsCount = 5
        self.ammoX = ammoX
        self.ammoY = ammoY
        self.ammoWidth = ammoWidth
        self.ammoHeight = ammoHeight
        space.add(self.body, self.shape)

    
    def draw(self, screenWidth, screenHeight):
        rot_image = pg.transform.rotate(self.image, degrees(self.body.angle - radians(self.additional_angle_for_image)))
        size = rot_image.get_size()
        pos = self.body.position
        image_pos = [pos[0] - size[0] // 2, pos[1] - size[1] // 2]
        self.screen.blit(rot_image, image_pos)
        bulletImage = pg.transform.scale(pg.image.load("photos/bullet.png"), (self.ammoWidth, self.ammoHeight // 5))
        pg.draw.rect(self.screen, (255, 0, 0), (self.ammoX, self.ammoY, self.ammoWidth, self.ammoHeight), 2)
        for i in range(self.bulletsCount):
            self.screen.blit(bulletImage, (self.ammoX, self.ammoY + i * (self.ammoHeight // 5)))
        distX = 60
        distY = 350
        if self.name == "Q":
            txtW = Text(self.screen, distX, distY, 40, "Q", (204, 153, 0))
        elif self.name == "M":
            txtN = Text(self.screen, screenWidth - distX - 20, distY, 40, "M", (204, 153, 0))
        elif self.name == "V":
            txtV = Text(self.screen, distX, screenHeight - distY - 36, 40, "V", (204, 153, 0))
        elif self.name == "5":
            txt5 = Text(self.screen, screenWidth - distX - 20, screenHeight - distY - 36, 40, "5", (204, 153, 0))

    def forward(self):
        pos = self.body.position
        angle = self.body.angle
        self.body.position = self.find_point_from_dist_and_angle(pos, angle, self.forward_dist)


    def process(self, pressed_buttons):
        if pressed_buttons[self.key]:
            self.pressing_count += 1
            if self.pressing_count == 1:
                self.shoot()
                self.change_direction()
            elif self.pressing_count >= self.shooting_time:
                self.forward()
        else:
            self.pressing_count = 0
            self.rotate()
        #
    def change_direction(self):
        self.direction *= -1
    

    def rotate(self):
        angle = self.body.angle
        self.body.angle = angle + self.direction * radians(self.rotating_angle)


    def addBullet(self):
        self.bulletsCount = min(5, self.bulletsCount + 1)

    def shoot(self):
        # pass
        if self.bulletsCount:
            bullet = Bullet(self.space, self.screen, * self.find_point_from_dist_and_angle(self.body.position, self.body.angle, 20), self.body.angle, 3)
            self.bullets.append(bullet)
            self.bulletsCount -= 1

    def find_point_from_dist_and_angle(self, pos, angle, dist):
        dx = dist * cos(angle)
        dy = dist * sin(angle)
        return (pos[0] + dx, pos[1] - dy)

    def play_death_music(self):
        # print("Music")
        pg.mixer.init()
        sound = pg.mixer.Sound('sounds/explosion.mp3')
        sound.set_volume(0.5)
        sound.play()
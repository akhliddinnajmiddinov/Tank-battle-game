import sys
import pygame as pg
import pymunk as pm
from modules.buttons import Button
from modules.zone import Zone
from modules.player import Player
from modules.text import Text
from datetime import datetime


class Game():
    def __init__(self):
        self.screenWidth = 1200
        self.screenHeight = 800
        self.caption = "Tank battle game"
        self.fps = 60
        self.clock = pg.time.Clock()
        self.bgcolor = "#e6ac00"
        self.screen = pg.display.set_mode((self.screenWidth, self.screenHeight))
        self.bg_images = []
        
        self.bg_image = pg.transform.scale(pg.image.load("photos/bg.jpg").convert(), (self.screenWidth, self.screenHeight))

        pg.display.set_caption(self.caption)
        self.show_start_window()


    def show_start_window(self):
        pg.init()

        pg.mixer.music.load('sounds/background.mp3')
        pg.mixer.music.play(-1)
        pg.mixer.music.set_volume(0.2)

        self.screen.blit(self.bg_image, (0, 0))
        btn_start = Button(self.screen, self.screenWidth // 2 - 100, self.screenHeight//2 - 50, 250, 100, "Boshlash", 40, self.show_choosing_players_window)

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            btn_start.process(pg.mouse.get_pos())
            pg.display.update()
            self.clock.tick(self.fps)


    def show_choosing_players_window(self):

        self.space = pm.Space()
        self.space.friction = 1
        self.space.gravity = 0, 0

        self.screen.blit(self.bg_image, (0, 0))
        btn2player = Button(self.screen, self.screenWidth // 2 - 500, self.screenHeight - 200, 300, 100, "2 ta o'yinchi", 40, lambda: self.start_game(2))
        btn3player = Button(self.screen, self.screenWidth // 2 - 150, self.screenHeight - 200, 300, 100, "3 ta o'yinchi", 40, lambda: self.start_game(3))
        btn4player = Button(self.screen, self.screenWidth // 2 + 200 , self.screenHeight - 200, 300, 100, "4 ta o'yinchi", 40, lambda: self.start_game(4))
        pg.display.update()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                btn2player.process(pg.mouse.get_pos())
                btn3player.process(pg.mouse.get_pos())
                btn4player.process(pg.mouse.get_pos())
            self.clock.tick(self.fps)
            pg.display.update()

    def playerAndBulletColl(self, arbiter, space, data):
        self.space.remove(arbiter.shapes[0].body, arbiter.shapes[0])
        self.space.remove(arbiter.shapes[1].body, arbiter.shapes[1])
        return False

    def wallAndBulletColl(self, arbiter, space, data):
        self.space.remove(arbiter.shapes[1].body, arbiter.shapes[1])
        return False

    def start_game(self, player_count):
        platformWidth = 20
        self.platformcolor = "#008000"
        zone = Zone(self.screen, self.space, self.screenWidth, self.screenHeight, platformWidth, self.platformcolor)
        platforms = zone.platforms

        playerWidth = 40
        dist = 60
        ammoWidth = 30
        ammoHeight = 50
        all_players = [Player(self.space, self.screen, "Q", dist, dist, playerWidth, 90, "photos/tank1.png", pg.K_q, 2, platformWidth + 4, self.screenHeight // 2 - platformWidth // 2 - ammoHeight - 4, ammoWidth, ammoHeight),
                   Player(self.space, self.screen, "5", self.screenWidth - dist - playerWidth, self.screenHeight - dist - playerWidth, playerWidth, 90, "photos/tank1.png", pg.K_KP5, 2, self.screenWidth - platformWidth - 4 - ammoWidth, self.screenHeight // 2 + platformWidth // 2 + 4, ammoWidth, ammoHeight),
                   Player(self.space, self.screen, "M", self.screenWidth - dist - playerWidth, dist, playerWidth, 90, "photos/tank1.png", pg.K_m, 2, self.screenWidth - platformWidth - 4 - ammoWidth, self.screenHeight // 2 - platformWidth // 2 - 4 - ammoHeight, ammoWidth, ammoHeight),
                   Player(self.space, self.screen, "V", dist, self.screenHeight - dist - playerWidth, playerWidth, 90, "photos/tank1.png", pg.K_v, 2, platformWidth + 4, self.screenHeight // 2 + platformWidth // 2 + 4, ammoWidth, ammoHeight)
            ]

        players = all_players[:player_count]

        handler = self.space.add_collision_handler(2, 3)
        handler.begin = self.playerAndBulletColl

        handler2 = self.space.add_collision_handler(1, 3)
        handler2.begin = self.wallAndBulletColl

        time_start = datetime.now()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.screen.fill(self.bgcolor)


            for platform in platforms:
                platform.draw()

            pressed_buttons = pg.key.get_pressed()

            time_now = datetime.now()
            time_delta = time_now - time_start
            if time_delta.seconds >= 1:
                for player in players:
                    player.addBullet()
                time_start = datetime.now()
            for i in range(len(players) - 1, -1, -1):
                if players[i].body in self.space.bodies:
                    players[i].process(pressed_buttons)
                    players[i].draw(self.screenWidth, self.screenHeight)
                    for j in range(len(players[i].bullets) - 1, -1, -1):
                        if players[i].bullets[j].body in self.space.bodies:
                            players[i].bullets[j].draw()
                        else:
                            del players[i].bullets[j]
                else:
                    players[i].play_death_music()
                    del players[i]

            if len(players) == 1:
                txt = Text(self.screen, self.screenWidth // 2 - 80, self.screenHeight - 530, 50, f"{players[0].name.upper()} YUTDI!!!", (255, 255, 255))
                btn_restart = Button(self.screen, self.screenWidth // 2 - 200, self.screenHeight - 450, 400, 100, "Qayta boshlash", 40, self.restart_game)

                while True:
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            pg.quit()
                            sys.exit()
                    btn_restart.process(pg.mouse.get_pos())
                    pg.display.update()

            self.space.step(0.1)
            self.clock.tick(self.fps)
            pg.display.update()

    def restart_game(self):
        del self.space
        self.show_choosing_players_window()

if __name__ == "__main__":
    new_game = Game()
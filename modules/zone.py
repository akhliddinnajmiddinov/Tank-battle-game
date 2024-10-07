from .platform import Platform

class Zone():
    def __init__(self, screen, space, screenWidth, screenHeight, platformWidth, platformcolor):
        self.screen = screen
        self.space = space
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.platformcolor = platformcolor
        self.platforms = [Platform(self.space, self.screen, 0, self.screenHeight - platformWidth, self.screenWidth, self.screenHeight, self.platformcolor, 1), #1
                             Platform(self.space, self.screen, 0, 0, platformWidth, self.screenHeight, self.platformcolor, 1), #2
                             Platform(self.space, self.screen, 0, 0, self.screenWidth, platformWidth, self.platformcolor, 1), #3
                             Platform(self.space, self.screen, self.screenWidth - platformWidth, 0, self.screenWidth, self.screenHeight, self.platformcolor, 1), #4
                             Platform(self.space, self.screen, platformWidth, self.screenHeight//2 - platformWidth//2, 100 + platformWidth, self.screenHeight//2 + platformWidth//2, self.platformcolor, 1),#5
                             Platform(self.space, self.screen, self.screenWidth - 100 - platformWidth, self.screenHeight//2 - platformWidth//2, self.screenWidth - platformWidth, self.screenHeight//2 + platformWidth//2, self.platformcolor, 1),#6
                             Platform(self.space, self.screen, platformWidth + 100 + 100, self.screenHeight//2 - platformWidth//2, 100 + platformWidth + 100 + 100, self.screenHeight//2 + platformWidth//2, self.platformcolor, 1),#7
                             Platform(self.space, self.screen, self.screenWidth - 100 - platformWidth - 100 - 100, self.screenHeight//2 - platformWidth//2, self.screenWidth - platformWidth - 100 - 100, self.screenHeight//2 + platformWidth//2, self.platformcolor, 1),#8
                             Platform(self.space, self.screen, 100 + platformWidth + 100 + 100, self.screenHeight//3, 100 + platformWidth + 100 + 100 + platformWidth, 2 * self.screenHeight//3, self.platformcolor, 1),#9
                             Platform(self.space, self.screen, self.screenWidth - platformWidth - 100 - platformWidth - 100 - 100, self.screenHeight//3, self.screenWidth - 100 -  100 - 100 - platformWidth, 2 * self.screenHeight//3, self.platformcolor, 1),#10
                             Platform(self.space, self.screen, 350 + 2 * platformWidth, self.screenHeight//4 - platformWidth//2, 400 + 2 * platformWidth + 100, self.screenHeight//4 + platformWidth // 2, self.platformcolor, 1),#11
                             Platform(self.space, self.screen, self.screenWidth - 500 - 2 * platformWidth, self.screenHeight//4 - platformWidth//2, self.screenWidth - 350 - 2 * platformWidth, self.screenHeight//4 + platformWidth // 2, self.platformcolor, 1),#11
                             Platform(self.space, self.screen, 350 + 2 * platformWidth, 3 * self.screenHeight//4 - platformWidth//2, 400 + 2 * platformWidth + 100,  3 * self.screenHeight//4 + platformWidth // 2, self.platformcolor, 1),#13
                             Platform(self.space, self.screen, self.screenWidth - 500 - 2 * platformWidth, 3 * self.screenHeight//4 - platformWidth//2, self.screenWidth - 350 - 2 * platformWidth, 3 * self.screenHeight//4 + platformWidth // 2, self.platformcolor, 1),#14
                             ]

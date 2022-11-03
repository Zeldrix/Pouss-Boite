# -*- coding: utf-8 -*-

from classes import Image

class Caisse(Image):
    def __init__(self, pygame, window_surface, case_size, pattern, chemin, x=0, y=0):
        self.pygame = pygame
        self.window_surface = window_surface
        self.case_size = case_size
        self.pattern = pattern
        self.image_idle = chemin + "sprites\\caisse\\caisse.png"
        self.image_win = chemin + "sprites\\caisse\\Caisse Valide.png"
        self.x = case_size * x
        self.y = case_size * y

        self.facing = "right"
        self.moving_step = 2
        self.moving = False
        self.step_count = 0
        self.moving = False
        self.winning = False

        self.sound_winning = self.pygame.mixer.Sound(chemin + "sounds\\caisse\\caisse_winning.wav")
        self.sound_winning.set_volume(0.1)


        self.load_image(self.image_idle)
        self.isWinning(self.pattern, True)

    def step(self, direction=None):
        if direction != None:
            self.facing = direction
        
        self.step_count += self.moving_step
        
        if self.facing == "right":
            self.x += self.moving_step
        if self.facing == "left":
            self.x -= self.moving_step
        if self.facing == "down":
            self.y += self.moving_step
        if self.facing == "up":
            self.y -= self.moving_step

    def move(self, pattern, direction=None):
        if direction != None:
            self.facing = direction

        if(self.moving == True):
            self.step(self.facing)

        if self.step_count >= self.case_size:
            self.stop_moving(pattern)

    def collideCaisse(self, direction, caisses):
        canMove = True
        for i in range(len(caisses)):
            if direction == "right":
                if (caisses[i].x == self.x + self.case_size) and (self.y == caisses[i].y):
                    canMove = False
            if direction == "left":
                if (caisses[i].x == self.x - self.case_size) and (self.y == caisses[i].y):
                    canMove = False
            if direction == "down":
                if (caisses[i].y == self.y + self.case_size) and (self.x == caisses[i].x):
                    canMove = False
            if direction == "up":
                if (caisses[i].y == self.y - self.case_size) and (self.x == caisses[i].x):
                    canMove = False

        return canMove
    
    def can_move(self, direction, pattern, caisses):
        x_case = int(self.x / self.case_size)
        y_case = int(self.y / self.case_size)
        
        if direction == "right":
            if pattern[y_case][x_case + 1] != 0:
                return self.collideCaisse(direction, caisses)
            else:
                return False
        elif direction == "left":
            if pattern[y_case][x_case - 1] != 0:
                return self.collideCaisse(direction, caisses)
            else:
                return False
        elif direction == "down":
            if pattern[y_case + 1][x_case] != 0:
                return self.collideCaisse(direction, caisses)
            else:
                return False
        elif direction == "up":
            if pattern[y_case - 1][x_case] != 0:
                return self.collideCaisse(direction, caisses)
            else:
                return False

    def start_moving(self, direction):
        self.facing = direction

        self.step_count = 0

        if self.facing == "right":
            self.moving = True
        elif self.facing == "left":
            self.moving = True
        elif self.facing == "down":
            self.moving = True
        elif self.facing == "up":
            self.moving = True

    def stop_moving(self, pattern):
        self.step_count = 0
        self.moving = False
        self.isWinning(pattern)

    def isWinning(self, pattern, startup=False):
        x_case = int(self.x / self.case_size)
        y_case = int(self.y / self.case_size)

        if pattern[y_case][x_case] == 2:
            if self.winning == False:
                self.load_image(self.image_win)
                self.winning = True
                if startup == False:
                    self.playSound(self.sound_winning)
        else:
            if self.winning == True:
                self.load_image(self.image_idle)
                self.winning = False
        
        return self.winning
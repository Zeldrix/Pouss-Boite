# -*- coding: utf-8 -*-

from classes import Image

class Player(Image):
    def __init__(self, pygame, window_surface, case_size, chemin, x=0, y=0):
        self.pygame = pygame
        self.window_surface = window_surface
        self.case_size = case_size
        self.chemin_images = chemin + 'sprites\\player\\'
        self.image_up = self.chemin_images + "Perso stop haut.png"
        self.image_down = self.chemin_images + "Perso stop bas.png"
        self.image_left = self.chemin_images + "Perso stop gauche.png"
        self.image_right = self.chemin_images + "Perso stop droite.png"
        self.image_right_walk1 = self.chemin_images + "Perso marche droite 1.png"
        self.image_right_walk2 = self.chemin_images + "Perso marche droite 2.png"
        self.image_push_right_walk1 = self.chemin_images + "Pousse marche droite 1.png"
        self.image_push_right_walk2 = self.chemin_images + "Pousse marche droite 2.png"
        self.image_left_walk1 = self.chemin_images + "Perso marche gauche 1.png"
        self.image_left_walk2 = self.chemin_images + "Perso marche gauche 2.png"
        self.image_push_left_walk1 = self.chemin_images + "Pousse marche gauche 1.png"
        self.image_push_left_walk2 = self.chemin_images + "Pousse marche gauche 2.png"
        self.image_down_walk1 = self.chemin_images + "Perso marche bas 1.png"
        self.image_down_walk2 = self.chemin_images + "Perso marche bas 2.png"
        self.image_push_down_walk1 = self.chemin_images + "Pousse marche bas 1.png"
        self.image_push_down_walk2 = self.chemin_images + "Pousse marche bas 2.png"
        self.image_up_walk1 = self.chemin_images + "Perso marche haut 1.png"
        self.image_up_walk2 = self.chemin_images + "Perso marche haut 2.png"
        self.image_push_up_walk1 = self.chemin_images + "Pousse marche haut 1.png"
        self.image_push_up_walk2 = self.chemin_images + "Pousse marche haut 2.png"
        self.x = case_size * x
        self.y = case_size * y

        self.facing = "right"
        self.moving_step = 2
        self.moving = False
        self.step_count = 0
        self.moving = False
        self.pushing = False

        self.sound_step = self.pygame.mixer.Sound(chemin + "\\sounds\\player\\step.wav")
        self.sound_step.set_volume(0.25)

        self.load_image(self.image_right)

    def step(self, direction=None):
        if direction != None:
            self.facing = direction
        
        if (self.step_count == 0) or (self.step_count == (0.5*self.case_size)):
            self.playSound(self.sound_step)

        self.step_count += self.moving_step
        
        if self.facing == "right":
            if self.step_count < (0.5*self.case_size):
                if self.pushing == False:
                    self.load_image(self.image_right_walk1)
                else:
                    self.load_image(self.image_push_right_walk1)
            else:
                if self.pushing == False:
                    self.load_image(self.image_right_walk2)
                else:
                    self.load_image(self.image_push_right_walk2)
            self.x += self.moving_step
        if self.facing == "left":
            if self.step_count < (0.5*self.case_size):
                if self.pushing == False:
                    self.load_image(self.image_left_walk1)
                else:
                    self.load_image(self.image_push_left_walk1)
            else:
                if self.pushing == False:
                    self.load_image(self.image_left_walk2)
                else:
                    self.load_image(self.image_push_left_walk2)
            self.x -= self.moving_step
        if self.facing == "down":
            if self.step_count < (0.5*self.case_size):
                if self.pushing == False:
                    self.load_image(self.image_down_walk1)
                else:
                    self.load_image(self.image_push_down_walk1)
            else:
                if self.pushing == False:
                    self.load_image(self.image_down_walk2)
                else:
                    self.load_image(self.image_push_down_walk2)
            self.y += self.moving_step
        if self.facing == "up":
            if self.step_count < (0.5*self.case_size):
                if self.pushing == False:
                    self.load_image(self.image_up_walk1)
                else:
                    self.load_image(self.image_push_up_walk1)
            else:
                if self.pushing == False:
                    self.load_image(self.image_up_walk2)
                else:
                    self.load_image(self.image_push_up_walk2)
            self.y -= self.moving_step

    def move(self):

        if(self.moving == True):
            self.step(self.facing)

        if self.step_count >= self.case_size:
            self.stop_moving()

    def canPushingCaisse(self, pattern, caisses, direction):
        theReturn = True
        for i in range(len(caisses)):
            if theReturn == True:
                if direction == "right":
                    if (caisses[i].x == self.x + self.case_size) and (self.y == caisses[i].y):
                        if caisses[i].can_move(direction, pattern, caisses):
                            theReturn = True
                        else:
                            theReturn = False
                    else:
                        theReturn = True
                elif direction == "left":
                    if (caisses[i].x == self.x - self.case_size) and (self.y == caisses[i].y):
                        if caisses[i].can_move(direction, pattern, caisses):
                            theReturn = True
                        else:
                            theReturn = False
                    else:
                        theReturn =  True
                elif direction == "down":
                    if (caisses[i].y == self.y + self.case_size) and (self.x == caisses[i].x):
                        if caisses[i].can_move(direction, pattern, caisses):
                            theReturn = True
                        else:
                            theReturn = False
                    else:
                        theReturn = True
                elif direction == "up":
                    if (caisses[i].y == self.y - self.case_size) and (self.x == caisses[i].x):
                        if caisses[i].can_move(direction, pattern, caisses):
                            theReturn = True
                        else:
                            theReturn = False
                    else:
                        theReturn = True

        return theReturn
    
    def can_move(self, direction, pattern, caisses):
        x_case = int(self.x / self.case_size)
        y_case = int(self.y / self.case_size)
        
        if direction == "right":
            self.load_image(self.image_right)
            if pattern[y_case][x_case + 1] != 0:
                return self.canPushingCaisse(pattern, caisses, direction)
            else:
                return False
        elif direction == "left":
            self.load_image(self.image_left)
            if pattern[y_case][x_case - 1] != 0:
                return self.canPushingCaisse(pattern, caisses, direction)
            else:
                return False
        elif direction == "down":
            self.load_image(self.image_down)
            if pattern[y_case + 1][x_case] != 0:
                return self.canPushingCaisse(pattern, caisses, direction)
            else:
                return False
        elif direction == "up":
            self.load_image(self.image_up)
            if pattern[y_case - 1][x_case] != 0:
                return self.canPushingCaisse(pattern, caisses, direction)
            else:
                return False

    def pushCaisse(self, pattern, caisses, direction):
        for i in range(len(caisses)):
            if direction == "right":
                if (caisses[i].x == self.x + self.case_size) and (self.y == caisses[i].y):
                    caisses[i].start_moving(direction)
                    self.pushing = True
            if direction == "left":
                if (caisses[i].x == self.x - self.case_size) and (self.y == caisses[i].y):
                    caisses[i].start_moving(direction)
                    self.pushing = True
            if direction == "down":
                if (caisses[i].y == self.y + self.case_size) and (self.x == caisses[i].x):
                    caisses[i].start_moving(direction)
                    self.pushing = True
            if direction == "up":
                if (caisses[i].y == self.y - self.case_size) and (self.x == caisses[i].x):
                    caisses[i].start_moving(direction)
                    self.pushing = True
    
    def start_moving(self, direction, pattern, caisses):
        self.facing = direction

        self.step_count = 0

        if self.facing == "right":
            self.load_image(self.image_right)
            self.moving = True
            self.pushCaisse(pattern, caisses, direction)
        elif self.facing == "left":
            self.load_image(self.image_left)
            self.moving = True
            self.pushCaisse(pattern, caisses, direction)
        elif self.facing == "down":
            self.load_image(self.image_down)
            self.moving = True
            self.pushCaisse(pattern, caisses, direction)
        elif self.facing == "up":
            self.load_image(self.image_up)
            self.moving = True
            self.pushCaisse(pattern, caisses, direction)


    def stop_moving(self):
        self.step_count = 0
        self.moving = False
        self.pushing = False

        if self.facing == "right":
            self.load_image(self.image_right)
        elif self.facing == "left":
            self.load_image(self.image_left)
        elif self.facing == "down":
            self.load_image(self.image_down)
        elif self.facing == "up":
            self.load_image(self.image_up)
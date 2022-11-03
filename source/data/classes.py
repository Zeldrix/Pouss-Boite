# -*- coding: utf-8 -*-

class Image:
    def __init__(self, pygame, window_surface, image, x=0, y=0):
        self.pygame = pygame
        self.window_surface = window_surface
        self.image = image
        self.x = x
        self.y = y
        self.load_image(self.image)
    
    def load_image(self, image):
        self.image = image
        self.image_loaded = self.pygame.image.load(self.image)

    def display(self):
        self.window_surface.blit(self.image_loaded, [self.x, self.y])
    
    def playSound(self, sound):
        self.pygame.mixer.Sound.play(sound)



class Background:
    def __init__(self, pygame, window_surface, width, height, case_size, pattern, chemin):
        self.pygame = pygame
        self.window_surface = window_surface
        self.width = width
        self.height = height
        self.case_size = case_size
        self.pattern = pattern
        self.objects = pattern
        self.image_brique = chemin + "sprites\\background\\brique.png"
        self.image_sol = chemin + "sprites\\background\\sol.png"
        self.image_arrivee = chemin + "sprites\\background\\Caisse manquante.png"

    def create(self):
        for y in range(len(self.pattern)):
            for x in range(len(self.pattern[y])):
                if self.pattern[y][x] == 0:
                    self.objects[y][x] = Image(self.pygame, self.window_surface, self.image_brique, x * self.case_size, y * self.case_size)
                elif self.pattern[y][x] == 1:
                    self.objects[y][x] = Image(self.pygame, self.window_surface, self.image_sol, x * self.case_size, y * self.case_size)
                elif self.pattern[y][x] == 2:
                    self.objects[y][x] = Image(self.pygame, self.window_surface, self.image_arrivee, x * self.case_size, y * self.case_size)

    def display(self):
        for y in range(len(self.objects)):
            for x in range(len(self.objects[y])):
                self.objects[y][x].display()
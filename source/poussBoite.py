# -*- coding: utf-8 -*-
import sys, os, pygame

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

chemin = resource_path('data\\')
sys.path.append(chemin)

from game import Game

FPS = 60
win = False
case_size = 64
screen_width = 15
screen_height = 15
window_resolution = (screen_width * case_size , screen_height * case_size)

game = Game(chemin, pygame, case_size, screen_width, screen_height)
gameSettings = game.init("Pouss'Boite", window_resolution, chemin + 'poussBoite.ico')
window_surface = gameSettings['windowSurface']
clock = gameSettings['clock']


launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    
    #Corps du programme
    clock.tick(FPS)
    keys = pygame.key.get_pressed()

    if game.needToDisplayMenu():
        game.displayMenu()

    else:
        game.displayBackground()
        game.movePlayer(keys)
        game.displayPlayer()

    
    
    pygame.display.flip()

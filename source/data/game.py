# -*- coding: utf-8 -*-
import sys, os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

import fonctions
import texte
from menu import Menu

class Game():
    def __init__(self, chemin, pygame, case_size, screen_width, screen_height):
        self.chemin = chemin
        self.pygame = pygame
        self.case_size = case_size
        self.screen_width = screen_width
        self.screen_height = screen_height

    def init(self, gameName, windowsSize, icon):
        self.pygame.init()
        self.pygame.font.init()
        self.pygame.display.set_caption(gameName)
        self.windowSurface = self.pygame.display.set_mode(windowsSize)
        clock = self.pygame.time.Clock()
        self.pygame.display.set_icon(self.pygame.image.load(icon))

        self.menu = Menu(self.chemin, texte, self.pygame, self.windowSurface, self.case_size, self.screen_width, self.screen_height)

        gameParameters = {
            "windowSurface": self.windowSurface,
            "clock": clock
        }

        return gameParameters

    def setupGame(self, needSetup):
        gameParameters = fonctions.setupGame(needSetup, self.pygame, self.windowSurface, self.case_size, self.chemin)
        self.gameNumber = gameParameters["gameNumber"]
        self.pattern = gameParameters["pattern"]
        pattern_background = gameParameters["pattern_background"]
        self.player = gameParameters["player"]
        self.caisses = gameParameters["caisses"]

        self.background = fonctions.initBackground(self.pygame, self.windowSurface, self.screen_width, self.screen_height, self.case_size, pattern_background, self.chemin)
        
        self.menu.setupGameOverlay()

    def displayBackground(self, overlay=True):
        self.background.display()
        if overlay:
            self.menu.displayGameOverlay(self.gameNumber)

    def needToDisplayMenu(self):
        return self.menu.needToDisplay()

    def movePlayer(self, keys):
        if self.player.moving == False:
            if keys[self.pygame.K_LEFT]:
                if(self.player.can_move("left", self.pattern, self.caisses)):
                    self.player.start_moving("left", self.pattern, self.caisses)
            if keys[self.pygame.K_RIGHT]:
                if(self.player.can_move("right", self.pattern, self.caisses)):
                    self.player.start_moving("right", self.pattern, self.caisses)
            if keys[self.pygame.K_UP]:
                if(self.player.can_move("up", self.pattern, self.caisses)):
                    self.player.start_moving("up", self.pattern, self.caisses)
            if keys[self.pygame.K_DOWN]:
                if(self.player.can_move("down", self.pattern, self.caisses)):
                    self.player.start_moving("down", self.pattern, self.caisses)

        self.player.move()
        self.updateCaisses()

    def displayPlayer(self):
        self.player.display()

    def updateCaisses(self):
        #update du mouvement et de l'affichage des caisses + test de victoire
        isWinning = True
        for caisse in range(len(self.caisses)):
            self.caisses[caisse].move(self.pattern)
            if self.caisses[caisse].winning == False:
                isWinning = False
        self.displayCaisses()
        if isWinning == True:
            self.winGame()
    
    def displayCaisses(self):
        for caisse in range(len(self.caisses)):
            self.caisses[caisse].display()

    def winGame(self):
        self.displayBackground(False)
        self.displayCaisses()
        if self.gameNumber < 10:
            self.menu.setup('win')
        else:
            self.menu.setup('win_last')
    
    def displayMenu(self):
        displayButtonClicked = self.menu.display()        
        if displayButtonClicked == 'title_boutonPlay':
            self.setupGame(1)
        elif displayButtonClicked == 'win_nextLevel':
            self.setupGame(self.gameNumber + 1)
        elif displayButtonClicked == 'gameMenu_restart':
            self.setupGame(self.gameNumber)
        elif displayButtonClicked == 'levelSelect':
            self.setupGame(self.menu.levelSelected)
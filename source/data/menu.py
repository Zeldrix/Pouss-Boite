import sys, os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

from bouton import Bouton
from classes import Image

class Menu():
    def __init__(self, chemin, texte, pygame, windowSurface, case_size, screen_width, screen_height):
        self.chemin = chemin
        self.chemin_fonts = chemin + 'fonts\\'
        self.texte = texte
        self.pygame = pygame
        self.windowSurface = windowSurface
        self.case_size = case_size
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.menu = 'title'
        self.inMenu = True

        self.setup(self.menu)

    def display(self):
        if self.menu == 'title':
            self.displayTitle()
            if self.title_boutonPlay.isClicked():
                return self.exitMenu('title_boutonPlay')
            elif self.title_boutonLevelSelect.isClicked():
                self.setup('levelSelect')
        elif self.menu == 'win' or self.menu == 'win_last':
            self.displayWin()
            if self.win_boutonNextLevel.isClicked():
                return self.exitMenu('win_nextLevel')
            elif self.win_boutonBackToMenu.isClicked():
                self.setup('title')
        elif self.menu == 'gameMenu':
            self.displayGameMenu()
            if self.gameMenu_boutonBackToTitle.isClicked():
                self.setup('title')
            elif self.gameMenu_boutonRestart.isClicked():
                return self.exitMenu('gameMenu_restart')
            elif self.gameMenu_boutonResume.isClicked():
                self.exitMenu('gameMenu_resume')
        elif self.menu == 'levelSelect':
            self.displayLevelSelect()
            if self.levelSelect_boutonBackToTitle.isClicked():
                self.setup('title')
            else:
                for button in range(len(self.boutonsLevelSelect)):
                    if self.boutonsLevelSelect[button].isClicked():
                        self.levelSelected = button + 1
                        return self.exitMenu('levelSelect')

        return None

    def setup(self, menuToShow):
        self.menu = menuToShow
        self.inMenu = True
        if self.menu == 'title':
            self.setupTitle()
        elif self.menu == 'win':
            self.setupWin()
        elif self.menu == 'win_last':
            self.setupWin(True)
        elif self.menu == 'gameMenu':
            self.setupGameMenu()
        elif self.menu == 'levelSelect':
            self.setupLevelSelect()

    def needToDisplay(self):
        return self.inMenu
    
    def exitMenu(self, buttonName):
        self.inMenu = False
        return buttonName

    def setupTitle(self):
        self.title_background = Image(self.pygame, self.windowSurface, self.chemin + 'sprites\\background\\title_background.png')
        self.title_playerPush = Image(self.pygame, self.windowSurface, self.chemin + 'sprites\\player\\Pousse marche droite 1.png', (self.screen_width*self.case_size/2) - self.case_size, self.screen_height*self.case_size*2/5)
        self.title_caisse = Image(self.pygame, self.windowSurface, self.chemin + 'sprites\\caisse\\caisse.png', (self.screen_width*self.case_size/2), self.screen_height*self.case_size*2/5)
        
        boutonPlay_width = 275
        boutonPlay_height = 50
        boutonPlay_x = (self.screen_width*self.case_size)/2 - 50 - boutonPlay_width
        boutonPlay_y = (self.screen_height*self.case_size)*5.5/8
        self.title_boutonPlay = Bouton(self.texte, self.pygame, self.windowSurface, self.chemin, "Jouer", 40, boutonPlay_x, boutonPlay_y, boutonPlay_width, boutonPlay_height)
        
        boutonLevelSelect_width = boutonPlay_width
        boutonLevelSelect_height = boutonPlay_height
        boutonLevelSelect_x = (self.screen_width*self.case_size)/2 + 50
        boutonLevelSelect_y = boutonPlay_y
        self.title_boutonLevelSelect = Bouton(self.texte, self.pygame, self.windowSurface, self.chemin, "Sélection des Niveaux", 40, boutonLevelSelect_x, boutonLevelSelect_y, boutonLevelSelect_width, boutonLevelSelect_height)
    
    def displayTitle(self):
        self.title_background.display()
        self.texte.text_to_screen_center(self.windowSurface, "Pouss'Boite", self.screen_width*self.case_size/2, 200, 250, (255, 255, 255), self.chemin_fonts + "Dongle-Regular.ttf")
        
        self.title_playerPush.display()
        self.title_caisse.display()

        self.title_boutonPlay.display()
        self.title_boutonLevelSelect.display()

    def setupWin(self, level=None):
        if level == None:
            self.win_lastLevel = False
        else:
            self.win_lastLevel = True
        
        boutonBackToMenu_width = 200
        boutonBackToMenu_height = 50
        boutonBackToMenu_x = (self.screen_width*self.case_size)/2 - 100 - boutonBackToMenu_width
        boutonBackToMenu_y = (self.screen_height*self.case_size)*7/8
        self.win_boutonBackToMenu = Bouton(self.texte, self.pygame, self.windowSurface, self.chemin, "Retour au Menu", 40, boutonBackToMenu_x, boutonBackToMenu_y, boutonBackToMenu_width, boutonBackToMenu_height)
        
        boutonNextLevel_width = 200
        boutonNextLevel_height = 50
        boutonNextLevel_x = (self.screen_width*self.case_size)/2 + 100
        boutonNextLevel_y = (self.screen_height*self.case_size)*7/8
        self.win_boutonNextLevel = Bouton(self.texte, self.pygame, self.windowSurface, self.chemin, "Niveau Suivant", 40, boutonNextLevel_x, boutonNextLevel_y, boutonNextLevel_width, boutonNextLevel_height)
        self.texte.text_to_screen_center(self.windowSurface, 'Bravo !', self.screen_width*self.case_size/2, 50, 70, (255, 255, 255), self.chemin_fonts + "Dongle-Regular.ttf")
        self.texte.text_to_screen_center(self.windowSurface, 'Niveau ' + str(self.gameNumber) + ' terminé', self.screen_width*self.case_size/2, 100, 70, (255, 255, 255), self.chemin_fonts + "Dongle-Regular.ttf")
        

    def displayWin(self):
        self.win_boutonBackToMenu.display()
        if self.win_lastLevel == False:
            self.win_boutonNextLevel.display()

    def setupGameMenu(self):
        self.gameMenu_background = Image(self.pygame, self.windowSurface, self.chemin + 'sprites\\background\\title_background.png')
        
        boutonBackToTitle_width = 200
        boutonBackToTitle_height = 50
        boutonBackToTitle_x = (self.screen_width*self.case_size)/2 - boutonBackToTitle_width/2
        boutonBackToTitle_y = (self.screen_height*self.case_size)*5/8
        self.gameMenu_boutonBackToTitle = Bouton(self.texte, self.pygame, self.windowSurface, self.chemin, "Menu Pricipal", 40, boutonBackToTitle_x, boutonBackToTitle_y, boutonBackToTitle_width, boutonBackToTitle_height)

        boutonRestart_width = 200
        boutonRestart_height = 50
        boutonRestart_x = (self.screen_width*self.case_size)/2 - 100 - boutonRestart_width
        boutonRestart_y = (self.screen_height*self.case_size)*6/8
        self.gameMenu_boutonRestart = Bouton(self.texte, self.pygame, self.windowSurface, self.chemin, "Recommencer", 40, boutonRestart_x, boutonRestart_y, boutonRestart_width, boutonRestart_height)
        
        boutonResume_width = 200
        boutonResume_height = 50
        boutonResume_x = (self.screen_width*self.case_size)/2 + 100
        boutonResume_y = boutonRestart_y
        self.gameMenu_boutonResume = Bouton(self.texte, self.pygame, self.windowSurface, self.chemin, "Reprendre", 40, boutonResume_x, boutonResume_y, boutonResume_width, boutonResume_height)
    
    def displayGameMenu(self):
        self.gameMenu_background.display()
        self.texte.text_to_screen_center(self.windowSurface, 'Menu Pause', self.screen_width*self.case_size/2, 150, 150, (255, 255, 255), self.chemin_fonts + "Dongle-Regular.ttf")
        self.gameMenu_boutonResume.display()
        self.gameMenu_boutonRestart.display()
        self.gameMenu_boutonBackToTitle.display()

    def setupLevelSelect(self):
        self.levelSelect_background = Image(self.pygame, self.windowSurface, self.chemin + 'sprites\\background\\title_background.png')
        
        boutonBackToTitle_width = 100
        boutonBackToTitle_height = 50
        boutonBackToTitle_x = 20
        boutonBackToTitle_y = 20
        self.levelSelect_boutonBackToTitle = Bouton(self.texte, self.pygame, self.windowSurface, self.chemin, "Retour", 40, boutonBackToTitle_x, boutonBackToTitle_y, boutonBackToTitle_width, boutonBackToTitle_height)

        boutonLevelSelect_width = 200
        boutonLevelSelect_height = 50
        boutonLevelSelect_x1 = self.screen_width*self.case_size/2 - 40 - boutonLevelSelect_width
        boutonLevelSelect_x2 = self.screen_width*self.case_size/2 + 40

        self.boutonsLevelSelect = []

        for button in range(10):
            yOffset = 200
            yStep = 100
            if (button % 2) == 0:
                x = boutonLevelSelect_x1
                y = yOffset + yStep*(button/2)
            else:
                x = boutonLevelSelect_x2
                y = yOffset + yStep*((button-1)/2)

            self.boutonsLevelSelect.append(Bouton(self.texte, self.pygame, self.windowSurface, self.chemin, "Niveau " + str(button+1), 40, x, y, boutonLevelSelect_width, boutonLevelSelect_height))

    def displayLevelSelect(self):
        self.levelSelect_background.display()
        self.texte.text_to_screen_center(self.windowSurface, 'Sélection des niveaux', self.screen_width*self.case_size/2, 80, 100, (255, 255, 255), self.chemin_fonts + "Dongle-Regular.ttf")
        self.levelSelect_boutonBackToTitle.display()

        for button in range(len(self.boutonsLevelSelect)):
            self.boutonsLevelSelect[button].display()

    
    
    
    
    
    
    def setupGameOverlay(self):
        boutonMenu_width = 100
        boutonMenu_height = 50
        self.overlay_boutonMenu = Bouton(self.texte, self.pygame, self.windowSurface, self.chemin, "Menu", 40, self.case_size*self.screen_width - boutonMenu_width - 10, 10, boutonMenu_width, boutonMenu_height)

    def displayGameOverlay(self, gameNumber):
        self.gameNumber = gameNumber
        self.overlay_boutonMenu.display()
        self.texte.text_to_screen_center(self.windowSurface, 'Niveau ' + str(self.gameNumber), self.screen_width*self.case_size/2, 50, 70, (255, 255, 255), self.chemin_fonts + "Dongle-Regular.ttf")
        if self.overlay_boutonMenu.isClicked():
            self.setup('gameMenu')
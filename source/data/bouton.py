class Bouton():
    def __init__(self, texte, pygame, windowSurface, chemin, texteBouton, texteSize, x, y, dx, dy):
        self.texte = texte
        self.pygame = pygame
        self.windowSurface = windowSurface
        self.chemin_font = chemin + 'fonts\\'

        self.texteBouton = texteBouton
        self.texteSize = texteSize
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

        self.sound_buttonClick = self.pygame.mixer.Sound(chemin + "sounds\\menu\\button_click.wav")
        self.sound_buttonClick.set_volume(0.25)

    def display(self):
        mousePosition = self.pygame.mouse.get_pos()
        selected = self.isGettingSelected(mousePosition)
        clicked = self.isClicked()

        if selected:
            if clicked:
                buttonColor = (0, 100, 0)
                self.pygame.mixer.Sound.play(self.sound_buttonClick)
            else:
                buttonColor = (100, 100, 100)
        else:
            buttonColor = (255, 200, 100)

        self.pygame.draw.rect(self.windowSurface, buttonColor, self.pygame.Rect(self.x, self.y, self.dx, self.dy))
        self.texte.text_to_screen_center(self.windowSurface, self.texteBouton, self.x + self.dx/2, self.y + self.dy/2, self.texteSize, (0, 0, 0), self.chemin_font + "Dongle-Regular.ttf")

    def isGettingSelected(self, mousePosition):
        mouseX = mousePosition[0]
        mouseY = mousePosition[1]
        
        if ((mouseX > self.x) and (mouseX < (self.x + self.dx))) and ((mouseY > self.y) and (mouseY < (self.y + self.dy))):
            return True
        else:
            return False

    def isClicked(self):
        clicked = False

        mousePosition = self.pygame.mouse.get_pos()
        if self.isGettingSelected(mousePosition):
            if self.pygame.mouse.get_pressed()[0]:
                clicked = True
        
        return clicked
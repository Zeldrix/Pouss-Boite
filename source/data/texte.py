# -*- coding: utf-8 -*-
import pygame
import sys

def text_to_screen_center(screen, text, x, y, size = 50, color = (200, 000, 000), font_type = "Dongle-Regular.ttf"):
    try:
        text = str(text)
        font = pygame.font.Font(font_type, size)
        text = font.render(text, True, color)
        width = text.get_rect().width
        height = text.get_rect().height
        screen.blit(text, (x - width/2, y - height/2))

    except(Exception):
        print("Font Error", sys.exc_info()[0])

def text_to_screen(screen, text, x, y, size = 50, color = (200, 000, 000), font_type = "Dongle-Regular.ttf"):
    try:
        text = str(text)
        font = pygame.font.Font(font_type, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))

    except(Exception):
        print("Font Error", sys.exc_info()[0])
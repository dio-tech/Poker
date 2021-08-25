import pygame
import os

# IMPORT CARDS
cards = []
cards_text = []
for i in os.listdir('assets'):
    cards.append(pygame.image.load(os.path.join('assets', i)))
    i = i.replace('.png', '')
    cards_text.append(i)

print(cards_text, len(cards))
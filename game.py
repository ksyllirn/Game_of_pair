import pygame
import time
from random import choice
from random import randint
pygame.init()

mw = pygame.display.set_mode((500,500))
mw.fill((131, 58, 224))

card_color = (25,25,112)
label_color = (224,255,255) 

clock = pygame.time.Clock()

class Card():
    def __init__(self, x = 0, y = 0, width=90, height=90, color=(25,25,112)):
        self.rect = pygame.Rect(x,y,width,height)
        self.fill_color = color
    
    def set_label(self, label, fsize=75, text_color=label_color):
        self.label = label
        self.image = pygame.font.Font(None,fsize).render(label,True,text_color)

    def draw(self, shift_x=20, shift_y=20):
        pygame.draw.rect(mw, self.fill_color, self.rect)
        mw.blit(self.image,(self.rect.x + shift_x, self.rect.y + shift_y))

    def draw_back(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def is_clicked(self, x, y):
        return self.rect.collidepoint(x, y)


def check(first_card,second_card):
    if first_card.label != second_card.label:
        time.sleep(1)
        first_card.draw_back()
        second_card.draw_back()
    else:
        cards_to_play.remove(first_card)
        cards_to_play.remove(second_card)

first_card = ''

def pre_check(tryed):
    global first_card
    if first_card == '':
        first_card = tryed
    else:
        second_card = tryed
        check(first_card,second_card)
        first_card, second_card = '', ''
    

cards = []
cards_to_play = []
images = ['♘','♔','♕','♖','♗','♙','❀','☆']
x = 40
y = 30
cards_amount = 15
labels_number = 7
for a in range(4):
    for b in range(4):
        new_card = Card(x,y)
        cards.append(new_card)
        new_card.set_label('')
        new_card.draw()
        x += 110
    x = 40   
    y += 110

for c in range(16):
    for d in cards:
        first = cards.pop(randint(0,cards_amount))
        cards_amount -= 1
        second = cards.pop(randint(0,cards_amount))
        cards_amount -= 1
        pairs_label = images.pop(randint(0,labels_number))
        labels_number -= 1
        first.set_label(pairs_label)
        #first.draw(20,20)
        cards_to_play.append(first)
        second.set_label(pairs_label)
        #second.draw(20,20)
        cards_to_play.append(second)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                for card in cards_to_play:
                    if card.is_clicked(x, y):
                        card.draw()
                        #print("CLICKED!", cards_to_play.index(card))
                        pre_check(card)
                         

    pygame.display.update()
    clock.tick(40)

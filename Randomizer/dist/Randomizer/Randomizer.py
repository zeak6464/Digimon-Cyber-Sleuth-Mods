import pygame
import button

import starters
import shop
import dedigivolve
import digivolve
import market
import digimondata
import enskills

import easyest
import easy
import normal
import hard
import harder
import hardest

import numpy as np

print("version 3.1")

#create display window
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1080

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Digimon CSHM - Randomizer')

#load button images
start_img = pygame.image.load('start_btn.png').convert_alpha()
shop_img = pygame.image.load('shop_btn.png').convert_alpha()
de_img = pygame.image.load('de_btn.png').convert_alpha()
di_img = pygame.image.load('di_btn.png').convert_alpha()
en_img = pygame.image.load('en_btn.png').convert_alpha()
mar_img = pygame.image.load('mar_btn.png').convert_alpha()
done_img = pygame.image.load('done_btn.png').convert_alpha()
re_img = pygame.image.load('re_btn.png').convert_alpha()
digi_img = pygame.image.load('digi_btn.png').convert_alpha()
enskill_img = pygame.image.load('enskill_btn.png').convert_alpha()
easyest_img = pygame.image.load('easyest_btn.png').convert_alpha()
easy_img = pygame.image.load('easy_btn.png').convert_alpha()
normal_img = pygame.image.load('normal_btn.png').convert_alpha()
hard_img = pygame.image.load('hard_btn.png').convert_alpha()
harder_img = pygame.image.load('harder_btn.png').convert_alpha()
hardest_img = pygame.image.load('hardest_btn.png').convert_alpha()

#create button instances
re_button = button.Button(450, 650, re_img, 1)
en_button = button.Button(650, 50, en_img, 1)

start_button = button.Button(100, 50, start_img, 1)
done1 = button.Button(100, 50, done_img, 1)
re1_button = button.Button(100, 50, start_img, 1)

shop_button = button.Button(100, 150, shop_img, 1)
done2 = button.Button(100, 150, done_img, 1)
re2_button = button.Button(100, 150, shop_img, 1)

de_button = button.Button(100, 250, de_img, 1)
done3 = button.Button(100, 250, done_img, 1)
re3_button = button.Button(100, 250, de_img, 1)

digi_button = button.Button(100, 350, digi_img, 1)
done7 = button.Button(100, 350, done_img, 1)
re7_button = button.Button(100, 350, digi_img, 1)

di_button = button.Button(100, 450, di_img, 1)
done4 = button.Button(100, 450, done_img, 1)
re4_button = button.Button(100, 450, di_img, 1)

mar_button = button.Button(100, 550, mar_img, 1)
done6 = button.Button(100, 550, done_img, 1)
re6_button = button.Button(100, 550, mar_img, 1)

enskill_button = button.Button(100, 650, enskill_img, 1)
done8 = button.Button(100, 650, done_img, 1)
re8_button = button.Button(100, 650, enskill_img, 1)

easyest_button = button.Button(750, 150, easyest_img, 1)
done9 = button.Button(750, 150, done_img, 1)
re9_button = button.Button(750, 150, easyest_img, 1)

easy_button = button.Button(750, 250, easy_img, 1)
done10 = button.Button(750, 250, done_img, 1)
re10_button = button.Button(750, 250, easy_img, 1)

normal_button = button.Button(750, 350, normal_img, 1)
done11 = button.Button(750, 350, done_img, 1)
re11_button = button.Button(750, 350, normal_img, 1)

hard_button = button.Button(750, 450, hard_img, 1)
done12 = button.Button(750, 450, done_img, 1)
re12_button = button.Button(750, 450, hard_img, 1)

harder_button = button.Button(750, 550, harder_img, 1)
done13 = button.Button(750, 550, done_img, 1)
re13_button = button.Button(750, 550, harder_img, 1)

hardest_button = button.Button(750, 650, hardest_img, 1)
done14 = button.Button(750, 650, done_img, 1)
re14_button = button.Button(750, 650, hardest_img, 1)


#game loop
run = True
while run:
        
    screen.fill((202, 228, 241))
    en_button.draw(screen)
    
    if start_button.draw(screen):
        starters.starters_func()
        start_button = done1
        print('Starters Done')
    if shop_button.draw(screen):
        shop.shop_func()
        shop_button = done2
        print('Shop Done')
    if de_button.draw(screen):
        dedigivolve.dedigivolve_func(False) 
        de_button = done3
        print('Dedigivole Done')
    if di_button.draw(screen):
        digivolve.digivolve_func()
        di_button = done4
        print('Digivolve Done')
    if mar_button.draw(screen):
        market.market_func()
        mar_button = done6
        print('Market Done')
    if digi_button.draw(screen):
        digimondata.digimondata_func()
        digi_button = done7
        print('Digimon Data Done')
    if enskill_button.draw(screen):
        enskills.enskills_func()
        enskill_button = done8
        print('Encounter Skills Done')
    if easyest_button.draw(screen):
        easyest.encounters_func()
        easyest_button = done9
        print('Encounters Done')
    if easy_button.draw(screen):
        easy.encounters_func()
        easy_button = done10
        print('Encounters Done')
    if normal_button.draw(screen):
        normal.encounters_func()
        normal_button = done11
        print('Encounters Done')
    if hard_button.draw(screen):
        hard.encounters_func()
        hard_button = done12
        print('Encounters Done')
    if harder_button.draw(screen):
        harder.encounters_func()
        harder_button = done13
        print('Encounters Done')
    if hardest_button.draw(screen):
        hardest.encounters_func()
        hardest_button = done14
        print('Encounters Done')        
    if re_button.draw(screen):
        start_button = re1_button
        shop_button = re2_button
        de_button = re3_button
        di_button = re4_button
        en_button = re5_button
        mar_button = re6_button
        digi_button = re7_button
        enskill_button = re8_button
        easyest_button = re9_button
        easy_button = re10_button
        normal_button = re11_button
        hard_button = re12_button
        harder_button = re13_button
        hardest_button = re14_button
        print('Resetting Done')
#event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()

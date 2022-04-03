import pygame
import button

import starters
import shop
import dedigivolve
import digivolve
import encounters
import market
import digimondata

#create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

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

#create button instances
re_button = button.Button(250, 425, re_img, 1)

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

di_button = button.Button(450, 50, di_img, 1)
done4 = button.Button(450, 50, done_img, 1)
re4_button = button.Button(450, 50, di_img, 1)

en_button = button.Button(450, 150, en_img, 1)
done5 = button.Button(450, 150, done_img, 1)
re5_button = button.Button(450, 150, en_img, 1)

mar_button = button.Button(450, 250, mar_img, 1)
done6 = button.Button(450, 250, done_img, 1)
re6_button = button.Button(450, 250, mar_img, 1)

#game loop
run = True
while run:
        
    screen.fill((202, 228, 241))
    
    if start_button.draw(screen):
        starters.starters_func()
        start_button = done1
        print('Starters Done')
    if shop_button.draw(screen):
        shop.shop_func()
        shop_button = done2
        print('Shop Done')
    if de_button.draw(screen):
        dedigivolve.dedigivolve_func() 
        de_button = done3
        print('Dedigivole Done')
    if di_button.draw(screen):
        digivolve.digivolve_func()
        di_button = done4
        print('Digivolve Done')
    if en_button.draw(screen):
        encounters.encounters_func()
        en_button = done5
        print('Encounters Done')
    if mar_button.draw(screen):
        market.market_func()
        mar_button = done6
        print('Market Done')
    if digi_button.draw(screen):
        digimondata.digimondata_func()
        digi_button = done7
        print('Digimon Data Done')    
    if re_button.draw(screen):
        start_button = re1_button
        shop_button = re2_button
        de_button = re3_button
        di_button = re4_button
        en_button = re5_button
        mar_button = re6_button
        digi_button = re7_button
        print('Resetting Done')
#event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()

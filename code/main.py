import pygame
import button
import time
pygame.mixer.init()    

#create display window
SCREEN_HEIGHT = 360
SCREEN_WIDTH = 640
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#name window
pygame.display.set_caption('Ghost Opera')

#define variables and lists
menustate = 'menu'
playing = 'no'
checklist = [0,0,0,0,0,0,0,0]
musiclist = ['c','d','e','f','g','a','b','c2']
x=80

#Create ghost lists
ghosts_open = []
ghosts_closed = []

#Create open ghost ditionary
y=140
y2=240
ghost1_grid = {
    'ghost1':(x+0,y),
    'ghost2':(x+40,y),
    'ghost3':(x+80,y),
    'ghost4':(x+120,y),
    'ghost5':(x+0,y2),
    'ghost6':(x+40,y2),
    'ghost7':(x+80,y2),
    'ghost8':(x+120,y2),
    }

#Create closed ghost ditionary
y=150
y2=250
ghosts_open = []
ghosts_closed = []
ghost2_grid = {
    'ghost1':(x+0,y),
    'ghost2':(x+40,y),
    'ghost3':(x+80,y),
    'ghost4':(x+120,y),
    'ghost5':(x+0,y2),
    'ghost6':(x+40,y2),
    'ghost7':(x+80,y2),
    'ghost8':(x+120,y2),
    }

#Create open ghost buttons
for ghost, gridval in ghost1_grid.items():
    img = pygame.image.load('../graphics/'+str(ghost)+'_open.png').convert_alpha()
    test_button = button.Button(gridval[0]*2, gridval[1], img, 2)
    ghosts_open.append(test_button)
    
#Create closed ghost buttons
for ghost, gridval in ghost2_grid.items():
    img = pygame.image.load('../graphics/'+str(ghost)+'_closed.png').convert_alpha()
    test_button = button.Button(gridval[0]*2, gridval[1], img, 2)
    ghosts_closed.append(test_button)

#Load images and create menu buttons
curtains1 = pygame.image.load('../graphics/curtains1.png').convert_alpha()
menu_img = pygame.image.load("../graphics/play_button.png").convert_alpha()
menu_button = button.Button((SCREEN_WIDTH-167/2)/2, 220, menu_img, 0.5)
quit_img = pygame.image.load("../graphics/quit_button.png").convert_alpha()
quit_button = button.Button((SCREEN_WIDTH-167/2)/2, 270, quit_img, 0.5)
logo_img = pygame.image.load("../graphics/logo.png").convert_alpha()
logo = button.Button(100, 130, logo_img, 0.7)

#Optional menu music
# pygame.mixer.Channel(0).play(pygame.mixer.Sound('../audio/lofi2.wav'),-1)
# pygame.mixer.Channel(0).set_volume(0.08)

#Game loop
run = True
while run:
    
    #Draw background
    screen.blit(curtains1,(0,0))
    
    #Game loop for menu
    if menustate == 'menu':
        if logo.draw(screen):
            pass
        if menu_button.draw(screen):
            time.sleep(0.2)
            menustate = 'main'
        if quit_button.draw(screen):
            pygame.quit()
            sys.exit()
    
    #Game loop for main game
    if menustate == 'main':
        #Optional menu music
        #pygame.mixer.Channel(0).fadeout(500)
        
        for i in range (len(ghosts_open)):
            
            #When particular ghost playing
            if checklist[i] == 1:
                #Draw ghost    
                if ghosts_open[i].draw(screen):

                    #If click on that ghost to make stop
                    pygame.mixer.Channel(1).fadeout(1)
                    checklist[i] = 0
                    
                    time.sleep(0.2)
                    
            #When particular ghost not playing
            if checklist[i] == 0:
                #Draw ghost
                if ghosts_closed[i].draw(screen):
                    #If click on that ghost to make play
                    pygame.mixer.Channel(1).fadeout(1)
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('../audio/'+musiclist[i]+'.wav'),-1)
                    checklist [i] = 1
                    
                    #Change all other ghosts to closed sprite
                    for e in range(len(ghosts_open)):
                        if e != i:
                            if ghosts_closed[e].draw(screen):
                                pass
                            checklist [e] = 0
                    
                    time.sleep(0.2)
                         
    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

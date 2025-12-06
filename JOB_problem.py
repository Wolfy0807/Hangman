# JOB PROBLEM 

'''
--create movie list
--select a random movie from list
--create a list with all the letters of the movie
--check for which letter is being pressed
--if correct letter, display all instances of letter
--remove letter from list
--else, draw body of man
--if all letters are removed from list before man is drawn, player wins
--else player loses
--while loop to run it multiple times

display that all movies are english
display to press any letter

issues:
--condition check for each key takes a long time - cannot have that many if statements
incorporating that with pygame was difficult

--length of list changing when popping out elements 

pressing the correct letter twice results in letter becoming red + one limb drawn

--could press letters even after game ended

pressing wrong letter multiple times leads to losing a limb - fix it or not?
'''

import random
import pygame
import sys

# creating window
pygame.init()
win = pygame.display.set_mode((700,500))
pygame.display.set_caption("Hangman")

# initializing font
font = pygame.font.SysFont(None, 36)

# initializing global variables
movies = ["AVATAR","GLADIATOR","INCEPTION","TITANIC","UNCHARTED","INTERSTELLAR","OPPENHEIMER","SHREK","ANNABELLE","GOODFELLAS",
          "GODFATHER","MULAN","CINDERELLA","PINOCCHIO","PREDATOR","DEADPOOL","GRAVITY","MOONFALL","SPIDERMAN","MATILDA"]
m = movies[random.randint(0,len(movies)-1)]
# print(m) 
l = [i for i in m]
l_copy = l.copy()

count = 0

alpha=[i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

gamestate = "start"

# colours
wht=(255,255,255)
blk=(0,0,0)
red=(255,0,0)
grn=(0,255,0)
blu=(0,0,255)
ylw=(255,255,0)
pur=(255,0,255)

# drawing underlying dashes and reference letters
def draw_dashes():
    k = 0
    y=300
    for i in l:
        x1 = 300+k
        x2 = 320+k
        pygame.draw.line(win,wht,(x1,y),(x2,y))
        k+=30

def draw_letters():
    k=0
    for i in alpha:
        x=30+k
        alphabet = font.render(i,True,wht)
        win.blit(alphabet,(x,80))
        k+=25

draw_letters()

# main loop
run = True
while run:

    # quit game condition check
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        hangman = font.render("HANGMAN",True,wht)
        win.blit(hangman,(290,30))

        rules1 = font.render("Press any letter to guess",True,wht)
        rules2 = font.render("Single word English movies only",True,wht)
        win.blit(rules1,(20,450))
        win.blit(rules2,(20,470))
    
        pygame.draw.line(win,wht,(80,170),(180,170),width=3)
        pygame.draw.line(win,wht,(130,170),(130,200),width=3)

        if(gamestate=="start"):

            if e.type==pygame.KEYDOWN:
                char = chr(e.key)

                # correct letter pressed
                if(char.upper() in l):
                    for i in range(0,len(l_copy)):
                        if(l_copy[i]==char.upper()):
                            letter = font.render(f"{char.upper()}",True,wht)
                            xpos = 300+i*30
                            win.blit(letter,(xpos,270))
                            l.remove(char.upper())

                            alphabet = font.render(char.upper(),True,grn)
                            x=alpha.index(char.upper())
                            win.blit(alphabet,(30+x*25,80))

                # incorrect letter pressed
                else:
                    if(count==0):
                        pygame.draw.circle(win,wht,(130,230),30,width=3)
                    elif(count==1):
                        pygame.draw.line(win,wht,(130,260),(130,320),width=3)
                    elif(count==2):
                        pygame.draw.line(win,wht,(130,260),(100,300),width=3)
                    elif(count==3):
                        pygame.draw.line(win,wht,(130,260),(160,300),width=3)
                    elif(count==4):
                        pygame.draw.line(win,wht,(130,320),(100,360),width=3)
                    elif(count==5):
                        pygame.draw.line(win,wht,(130,320),(160,360),width=3)
                        game_over = font.render(f"Game over! The movie was: {m}",True,wht)
                        win.blit(game_over,(100,380))
                        gamestate="stop"
                    
                    count+=1
                    alphabet = font.render(char.upper(),True,red)
                    x=alpha.index(char.upper())
                    win.blit(alphabet,(30+x*25,80))
            
            # checking if hangman is not complete and list is empty
            if(count!=6 and not l):
                game_won = font.render("You won! Good job!",True,wht)
                win.blit(game_won,(230,380))
                gamestate="stop"

    # drawing underlying dashes
    draw_dashes()

    pygame.display.flip()


    




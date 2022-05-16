# Imports
import pygame
import sys
from tkinter import *
import os
from pygame.locals import *
from pygame import mixer
# Setting Up the Clock
mainClock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((1366, 768), 0, 32)
# Adding multiple fonts that i sis not end up using
font = pygame.font.SysFont("8-BIT WONDER.TTF", 100)
larger_font = pygame.font.SysFont("8-BIT WONDER.TTF", 20)
small_font = pygame.font.SysFont("8-BIT WONDER.TTF", 50)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def main_menu():
    global click
    while True:

        screen.fill((6, 12, 233))

#1366, 768
        mx, my = pygame.mouse.get_pos()
# 1st number is x than y than rectangle dimentions
        button_1 = pygame.Rect(20, 256, 400, 100)
        button_2 = pygame.Rect(483, 256, 400, 100)
        button_3 = pygame.Rect(946, 256, 400, 100)
        button_4 = pygame.Rect(20, 512, 400, 100)
        button_5 = pygame.Rect(483, 512, 400, 100)
        button_6 = pygame.Rect(946, 512, 400, 100)

# Decting if a button is clicked
        if button_1.collidepoint((mx, my)):
            if click:
                one()
        if button_2.collidepoint((mx, my)):
            if click:
                two()
        if button_3.collidepoint((mx, my)):
            if click:
                three()
        if button_4.collidepoint((mx, my)):
            if click:
                four()
        if button_5.collidepoint((mx, my)):
            if click:
                five()
        if button_6.collidepoint((mx, my)):
            if click:
                six()
        else:
            pass
# Adding the buttons
        pygame.draw.rect(screen, (0, 0, 0), button_1)
        pygame.draw.rect(screen, (0, 0, 0), button_2)
        pygame.draw.rect(screen, (0, 0, 0), button_3)
        pygame.draw.rect(screen, (0, 0, 0), button_4)
        pygame.draw.rect(screen, (0, 0, 0), button_5)
        pygame.draw.rect(screen, (0, 0, 0), button_6)
# Adding the Text
        draw_text('Geography', font, (255, 204, 0), screen, 33, 272, )
        draw_text('Coding', font, (255, 204, 0), screen, 555, 272, )
        draw_text('Trivia', font, (255, 204, 0), screen, 1050, 272, )
        draw_text('Colors', font, (255, 204, 0), screen, 98, 528, )
        draw_text('Puzzles', font, (255, 204, 0), screen, 550, 528, )
        draw_text('Hockey', font, (255, 204, 0), screen, 1025, 528, )
        draw_text("Cool Bots Quiz central", font, (255, 204, 0), screen, 300, 000, )



        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
# Updating the clock
        pygame.display.update()
        mainClock.tick(60)

# This is the code for if the button repeats. Very repetitive.
def one():
    running = True
    counter = 0
    while running:
        screen.fill((0, 0, 0))
        counter = counter +1
        draw_text('You will be redirected shortly', font, (255, 255, 255), screen, 20, 20)
        draw_text('Press ESC TO Exit this screen', font, (255, 255, 255), screen, 20, 100)
        # Appending to a text file
        if counter == 200:
            f = open("letter.txt", "w")
            f.write("1")
            os.startfile("Quiz file.py")
            f.close()
# Detecting if you want to leave
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                pygame.display.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
# Updating the clock
        pygame.display.update()
        mainClock.tick(60)


def two():
    running = True
    counter = 0
    while running:
        screen.fill((0, 0, 0))
        counter = counter + 1
        draw_text('You will be redirected shortly', font, (255, 255, 255), screen, 20, 20)
        draw_text('Press ESC TO Exit this screen', font, (255, 255, 255), screen, 20, 100)
        if counter == 200:
            f = open("letter.txt", "w")
            f.write("2")
            os.startfile("Quiz file.py")
            f.close()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                pygame.display.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

def three():
    running = True
    counter = 0
    while running:
        screen.fill((0, 0, 0))
        counter = counter + 1
        draw_text('You will be redirected shortly', font, (255, 255, 255), screen, 20, 20)
        draw_text('Press ESC TO Exit this screen', font, (255, 255, 255), screen, 20, 100)
        if counter == 200:
            f = open("letter.txt", "w")
            f.write("3")
            os.startfile("Quiz file.py")
            f.close()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                pygame.display.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)
def four():
    running = True
    counter = 0
    while running:
        screen.fill((0, 0, 0))
        counter = counter + 1
        draw_text('You will be redirected shortly', font, (255, 255, 255), screen, 20, 20)
        draw_text('Press ESC TO Exit this screen', font, (255, 255, 255), screen, 20, 100)
        if counter == 200:
            f = open("letter.txt", "w")
            f.write("4")
            os.startfile("Quiz file.py")
            f.close()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                pygame.display.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

def five():
    running = True
    counter = 0
    while running:
        screen.fill((0, 0, 0))
        counter = counter + 1
        draw_text('You will be redirected shortly', font, (255, 255, 255), screen, 20, 20)
        draw_text('Press ESC TO Exit this screen', font, (255, 255, 255), screen, 20, 100)
        if counter == 200:
            f = open("letter.txt", "w")
            f.write("5")
            os.startfile("Quiz file.py")
            f.close()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                pygame.display.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)
def six():
    running = True
    counter = 0
    while running:
        screen.fill((0, 0, 0))
        counter = counter + 1
        draw_text('You will be redirected shortly', font, (255, 255, 255), screen, 20, 20)
        draw_text('Press ESC TO Exit this screen', font, (255, 255, 255), screen, 20, 100)
        if counter == 200:
            f = open("letter.txt", "w")
            f.write("6")
            os.startfile("Quiz file.py")
            f.close()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                pygame.display.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

mixer.init()
mixer.music.load("Jeopardy Theme.wav")
mixer.music.play(loops = -1)

main_menu()

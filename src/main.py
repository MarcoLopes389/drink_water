from datetime import datetime
from os import system
from platform import platform
from pygame import init, Rect, Color
from pygame import FULLSCREEN, MOUSEBUTTONDOWN, KEYDOWN, K_BACKSPACE, HIDDEN
from pygame.time import Clock
from pygame.font import Font
from pygame.display import set_mode, flip
from pygame.draw import rect
from pygame.event import get as get_events
from constants import *


init()
screen = set_mode(screen_size, HIDDEN)
screen_size = screen.get_size()
user_text = ''
drank = False
x = (screen_size[0] // 2) - input_width // 2
y = (screen_size[1] // 2) - input_heigth // 2
clock = Clock()
base_font = Font(None, 32)
input_rect = Rect(x, y, input_width, input_heigth)
color_active = Color('lightskyblue3')
color_passive = Color('chartreuse4')
ask_color = Color('black')
color = color_passive

active = False

while True:
    for event in get_events():
        if event.type == MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode

    hour = datetime.now().hour
    if hour in hours and not drank:
        screen = set_mode(screen_size, FULLSCREEN)
        screen.fill((255, 255, 255))
    elif hour not in hours and drank:
        drank = False

    if user_text in valid_responses:
        screen = set_mode(screen_size, HIDDEN)
        drank = True
    if user_text in troll_responses:
        if platform() == 'Windows':
            system('shutdown -s -t 0')
        else:
            system('shutdown -h now')
            
    if active:
        color = color_active
    else:
        color = color_passive
    # desenha o input
    rect(screen, color, input_rect)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    ask_surface = base_font.render(ask_text, False, ask_color)
    # coloca o texto na tela
    screen.blit(ask_surface, (x,y - input_heigth))
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    # aqui ele define o comprimento do input como o comprimento do texto    
    input_rect.w = max(ask_surface.get_width(), text_surface.get_width()+10)
    flip()
    clock.tick(60)
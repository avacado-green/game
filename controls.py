import pygame
import sys
from bullet import Bullet

def events(gun, screen, bullets):
    """Обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            """Привсваивание клавиши d к правому повороту"""
            if event.key == pygame.K_d:
                gun.mright = True
            """Присваивание клавиши a к левому повороту"""
            elif event.key == pygame.K_a:
                gun.mleft = True
            """Присваичание клавиши пробел(SPACE) к стрельбе"""
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False




import pygame
import sys
from gun import Gun
from bullet import Bullet
import controls

def run():
    pygame.init()
    screen = pygame.display.set_mode((750, 800))
    pygame.display.set_caption("Star Wars")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = pygame.sprite.Group()

    while True:
        controls.events(gun, screen, bullets)
        gun.update_gun()
        bullets.update()
        screen.fill(bg_color)
        gun.output()
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

run()




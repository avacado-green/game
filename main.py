import pygame, controls
from gun import Gun

def run():
    pygame.init()
    screen = pygame.display.set_mode((750, 800))
    pygame.display.set_caption("Star Wars")
    bg_color = (0, 0, 0)
    gun = Gun(screen)

    while True:
        controls.events(gun)
        gun.update_gun()
        screen.fill(bg_color)
        gun.output()
        pygame.display.flip()

run()


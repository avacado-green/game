import pygame

class Bullet(pygame.sprite.Sprite):
        """Инициализация пули"""
    def __init__(self, screen, gun):
        """Создание пули в позиции пушки"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 5, 20)
        self.color = 139, 195, 74
        self.speed = 1
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """Перемещение пули вверх"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Рисуем пулю"""
        pygame.draw.rect(self.screen, self.color, self.rect)


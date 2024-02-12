import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""Класс для управления кораблем"""

	def __init__ (self, inv_alien):
		"""Инициализация корабля и его начальной позиции"""
		super().__init__()
		self.screen = inv_alien.screen
		self.settings = inv_alien.settings

		self.screen_rect = inv_alien.screen.get_rect()
		self.moving_right = False
		self.moving_left = False

		"""Загружает изображение корабля и получает прямоугольник"""
		self.image = pygame.image.load('images/ship_start.png')
		self.rect = self.image.get_rect()

		"""Каждый новый корабль появляется у нижнего края экрана"""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)

	def blitme(self):
		"""Рисует корабль в текущей позиции"""
		self.screen.blit(self.image, self.rect)

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
		self.rect.x = self.x

	def center_ship(self):
		#Размещает корабль в центре c нижней стороны
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)
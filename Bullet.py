import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	'''Класс управления снарядами, выпущенныи кораблем'''

	def __init__ (self, inv_alien):
		"""Создает объект снарядов в текущей позиции корабля"""
		super().__init__()
		self.screen = inv_alien.screen
		self.settings = inv_alien.settings
		self.color = self.settings.bullet_color
		"""Создание снаряда в позиции 0,0 и назначение правильной позиции"""
		self.image = pygame.image.load('images/fire.png')
		self.rect = self.image.get_rect()

		self.rect.midbottom = inv_alien.ship.rect.midtop
		"""Позиция снаряда хранится в вещественном формате"""
		self.y = float(self.rect.y)

	def draw_bullet (self):
		"""Вывод снарядов на экран"""
		self.screen.blit(self.image, self.rect)


	def update(self):
		"""Перемещает снаряд вверх по экрану"""
		#Обновление позиции сняряда в вещественном формате
		self.y -= self.settings.bullet_speed
		#Обновление позиции прямоугольника
		self.rect.y = self.y
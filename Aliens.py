import pygame
from pygame.sprite import Sprite

class Aliens(Sprite):
	"""Класс представляющий одного пришельца"""

	def __init__(self, inv_alien):
		"""Инициализирует прищельца и задает его начальную позицию"""
		super().__init__()
		self.screen = inv_alien.screen
		self.settings = inv_alien.settings

		#Загрузка изображения приельца и назначение атрибута rect
		self.image = pygame.image.load('images/alien.png')
		self.rect = self.image.get_rect()

		#Каждый пришелец появляется в левом верхнем углу экрана
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#Сохранение точной горизонтальной позиции пришельца
		self.x = float(self.rect.x)

	def update(self):
		#Перемещает пришельцев вправо или влево
		self.x += (self.settings.alien_speed * self.settings.fleet_direction)
		self.rect.x = self.x

	def check_edges(self):
		#Возвращает True, если пришелец находится у края экрана
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True
import pygame.font
from pygame.sprite import Group
from Ship import Ship

class BoardScore():
	"""Класс для вывода игровой информации"""
	def __init__(self, inv_alien):
		"""Инициализирует атрибуты подсчета очков"""
		self.inv_alien = inv_alien
		self.screen = inv_alien.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = inv_alien.settings
		self.stats = inv_alien.stats

		#Настройки шрифта для вывода счета
		self.text_color = (218, 218, 218)
		self.font = pygame.font.SysFont(None, 48)
		#Подготовка изображений счетов
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		"""Преобразует текущий счет в графическое изображение"""
		rounded_score = round(self.stats.score, -1)			#round округляет значение до десятков
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, self.text_color, None)

		#Вывод счета в правой верхней части экрана
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def prep_high_score(self):
		"""Преобразует рекордный счет в графическое изображение."""
		high_score = round(self.stats.high_score, -1)
		high_score_str = "Best: " + "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True, (132, 255, 0), None)

		#Рекорд выравнивается по центру верхней стороны
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx + 200
		self.high_score_rect.top = self.score_rect.top

	def prep_level(self):
		"""Преобразует уровень в графическое изображение"""
		level_str = "lev: " + str(self.stats.level)
		self.level_image = self.font.render(level_str, True, self.text_color, None)
		#Уровень выводится под текущим счетом
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10

	def prep_ships(self):
		"""Сообщает количество оставшихся кораблей"""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.inv_alien)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 5
			self.ships.add(ship)

	def check_high_score(self):
		"""Проверяет есть ли новый рекорд"""
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.prep_high_score()

	def show_score(self):
		#Выводит счет на экран
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)
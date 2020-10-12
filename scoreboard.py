import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
	"""scoring"""
	def __init__(self, ai_game):
		"""init score"""
		self.ai_game = ai_game
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats
		#font for score
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)
		#initial score image
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()
	def prep_score(self):
		"""render score"""
		rounded_score = round(self.stats.score, -1)
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True,
					self.text_color, self.settings.bg_color)
		#display score top right
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 10
	def prep_high_score(self):
		"""Render high score."""
		high_score = round(self.stats.high_score, -1)
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True,
				self.text_color, self.settings.bg_color)
		#Center high score at top of screen.
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.screen_rect.top
	def prep_level(self):
		"""Turn level into rendered image."""
		level_str = str(f"Level {self.stats.level}")
		self.level_image = self.font.render(level_str, True, 
					self.text_color, self.settings.bg_color)
		#Position the level top left.
		self.level_rect = self.level_image.get_rect()
		self.level_rect.left = self.screen_rect.left + 10
		self.level_rect.top = self.screen_rect.top + 10
	def prep_ships(self):
		"""Show number of ships."""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left - 1):
			ship = Ship(self.ai_game)
			ship.rect.x = 200 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)
	def check_high_score(self):
		"""Check for new high score."""
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.prep_high_score()
	def show_score(self):
		"""Draw score, ships and level to screen."""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)
		
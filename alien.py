import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""bad guy mgmt"""
	def __init__(self, ai_game):
		"""init alien and set starting point"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		#load image and set rect
		self.image = pygame.image.load("")
		self.rect = self.image.get_rect()
		# start alien at top left
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		#store aliens horizontal pos
		self.x = float(self.rect.x)
	def check_edges(self):
		"""return True at edge"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True
	def update(self):
		"""move to right"""
		self.x += (self.settings.alien_speed * 
					self.settings.fleet_direction)
		self.rect.x = self.x

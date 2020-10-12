import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	""" bullet mgmt"""
	def __init__(self, ai_game):
		"""bullet object from ship"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color
		#create bullet rect (0, 0) & then update
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
			self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop
		#store bullet pos as decimal
		self.y = float(self.rect.y)
	def update(self):
		"""move bullet up"""
		#update decimal pos of bullet
		self.y -= self.settings.bullet_speed
		#update rec
		self.rect.y = self.y
	def draw_bullet(self):
		"""draw bullet to screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)

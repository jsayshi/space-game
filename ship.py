import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""Overall class to manage ship."""
	def __init__(self, ai_game):
		"""Initialize the ship, and origin."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()
		#load ship image
		self.image = pygame.image.load("")
		self.rect = self.image.get_rect()
		#start at bottom
		self.rect.midbottom = self.screen_rect.midbottom
		# store decimal for horizontal
		self.x = float(self.rect.x)
		# Movement flag
		self.moving_right = False
		self.moving_left = False
	def update(self):
		"""update position based on flag"""
		# update x value not rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
		 	self.x -= self.settings.ship_speed
		 # update rect from self.x
		self.rect.x = self.x
	def center_ship(self):
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)
	def blitme(self):
		"""drawing current location"""
		self.screen.blit(self.image, self.rect)
	


   
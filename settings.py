class Settings:
	"""Overall class to manage settings."""
	def __init__(self):
		"""init static settings"""
		#screen
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (0, 0, 0)
		# Ship settings
		self.ship_speed = 8
		self.ship_limit = 3
		# Bullet settings
		self.bullet_speed = 5
		self.bullet_width = 8
		self.bullet_height = 10
		self.bullet_color = (255, 0, 0)
		self.bullets_allowed = 3
		# alien settings
		self.alien_speed = 8
		self.fleet_drop_speed = 10
		#difficulty level
		self.speedup_scale = 1.03
		#Alien point value incresase.
		self.score_sale = 1.05
		self.initialize_dynamic_settings()
	def initialize_dynamic_settings(self):
		"""init changing stats"""
		self.ship_speed = 6.0
		self.bullet_speed = 6.5
		self.alien_speed = 5.0
		self.bullet_width = 9
		# fleet_direction 1 is right -1 is left
		self.fleet_direction = 1
		# scoring
		self.alien_points = 50
	def increase_speed(self):
		"""Increase speed and alien point values."""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale * .9
		self.alien_points = int(self.alien_points * self.score_sale)
		self.bullet_width *= self.speedup_scale * .9
	







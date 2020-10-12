class GameStats:
	"""track stats"""
	def __init__(self, ai_game):
		"""init stats"""
		self.settings = ai_game.settings
		self.reset_stats()
		self.high_score = 0
		# start inactive
		self.game_active = True
	def reset_stats(self):
		"""init changing stats"""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1



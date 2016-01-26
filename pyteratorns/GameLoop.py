# This Class is a template for GameLoop
# -*- coding: utf-8 -*-
import threading

class GameLoop(threading.Thread):

	def __init__(self, threadID, threadName, game):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.threadName = threadName
		self.game = game

	def run(self):
		print self.threadID + "$" + self.threadName

		try: # if self.game is not None
			print "  Iterate GameWorld"

			print "  Draw Graphics"

		except None:
			print "No game is setted"

	def setGame(self, game):
		self.game = game

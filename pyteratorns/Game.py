# This class is a Game class :p. this class is abstract and should be implemented
# -*- coding: utf-8 -*-
import GameLoop

class Game():

	def __init__(self, gameName):
		self.__gameLoop = GameLoop(1, nameGame + " GameLoop", self)
		print gameName + " is ready!"
		pass 

	def start(self):
		print "Game started!"
		self.__gameLoop.start()
		pass

	def pause(self):
		print "Game paused!"
		pass

	def stop(self):
		print "Game stoped!"
		pass

	def save(self):
		print "Game saved!"
		pass

	def __del__(self):
		print "Game resources unloaded!"
		pass
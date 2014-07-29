from datetime import *
import time

class DifferenceTimes():
	def __init__(self, tasks):
		self.startTimes = []
		self.endTimes = []
		self.differenceTimes = []
		self.tasks = int(tasks)
		self.create_array_length()
	def create_array_length(self):
		for i in range(self.tasks):
			self.startTimes.append(0)
			self.endTimes.append(0)
			self.differenceTimes.append(0)
		print len(self.startTimes)
	def get_start_times(self):
		for i in range(self.tasks):
			self.startTimes[i] = datetime.now()
	def get_end_times(self):
		for i in range(self.tasks):
			self.endTimes[i] = datetime.now()
	def get_difference_times(self):
		for i in range(self.tasks):
			difference = (self.endTimes[i] - self.startTimes[i]).seconds
			self.differenceTimes[i] = difference
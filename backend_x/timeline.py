from datetime import datetime


class TimeLine(object):
	steps = None

	def __init__(self):
		self.steps = []

	def add_step(self, step):
		for s in self.steps:
			if s.id == step.id:
				return
		self.steps.append(step)
		self.sort_by_date()

	def remove_step(self, id):
		for i in range(len(self.steps)):
			if self.steps[i].id == id:
				del self.steps[i]
				return

	def sort_by_date(self):
		self.steps.sort(key=lambda x: datetime.strptime(x.date, '%Y-%m-%d'))

	def sort_by_due(self):
		self.steps.sort(key=lambda x: datetime.strptime(x.date, '%Y-%m-%d'))

	def to_dict(self):
		return self.as_dict()

	def as_dict(self):
		return {'steps': [s.to_dict() for s in self.steps]}

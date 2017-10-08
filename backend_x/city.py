import json

from step import Step
from timeline import TimeLine
from mysqlconnection import MySQL_Connection

mysql_connection = MySQL_Connection('mysql', 3306, 'root', 'blackforestmysql', 'hackathon')


class City(object):
	id = 0
	name = ''
	location = None
	steps = None
	buildings = None

	def __init__(self, name):
		self.name = name
		self.steps = []
		self.location = Location(48.46943049999999, 7.9427725)
		self.buildings = []

	def add_step(self, step):
		for s in self.steps:
			if s.id == step.id:
				return False
		self.steps.append(step)

	def remove_step(self, id):
		for i in range(len(self.steps)):
			if self.steps[i].id == id:
				del self.steps[i]
				return

	def get_timeline_from_profile(self, profile):
		tl = TimeLine()
		print len(self.steps)
		for step in self.steps:
			if step.applies(profile):
				tl.add_step(step)
		tl.sort_by_date()
		return tl

	def load(self):
		result = mysql_connection.select('SELECT * FROM cities WHERE name LIKE "%s"' % str(self.name))
		if result:
			self.id = result['id']
			self.steps = []
			self.location = Location(result['location_lat'], result['location_lng'])
			if result['buildings'] != '' and result['buildings'] is not None:
				self.buildings = json.loads(result['buildings'])
			steps_result = mysql_connection.select_all('SELECT id FROM steps WHERE city LIKE "%s"' % str(self.name))
			print steps_result
			if steps_result:
				for s in steps_result:
					step = Step()
					step.id = s['id']
					step.load()
					self.add_step(step)


class Location(object):
	latitude = 0.0
	longitude = 0.0

	def __init__(self, latitude, longitude):
		self.latitude = latitude
		self.longitude = longitude

	def to_json(self):
		return {'latitude': self.latitude, 'longitude': self.longitude}

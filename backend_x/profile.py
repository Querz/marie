import inspect

import sys
from enum import Enum
from datetime import date, datetime
import json

from step import Step, Status
from mysqlconnection import MySQL_Connection

# {
#     "age": 20,
#     "children": 1,
#     "email": "mor@vioma.de",
#     "language": 1,
#     "move_date": "2017-10-07",
#     "move_reasons": [
#         1,
#         2
#     ],
#     "name": "Moataz Rizk",
#     "nationality": 1,
#     "new_residence": 1,
#     "password": "pazzword",
#     "religion": 3,
#     "state_of_family": 0,
#     "state_of_work": 0
# }

mysql_connection = MySQL_Connection('mysql', 3306, 'root', 'blackforestmysql', 'hackathon')

class Profile(object):
	id = ''
	name = ''
	email = ''                  # acts as unique id
	password = ''
	language = None
	age = 0
	children = 0
	new_residence = ''
	move_reasons = None         # tags
	nationality = None
	move_date = None
	steps = None

	def __init__(self, email='', password=''):
		self.name = ''
		self.email = email          # acts as unique id
		self.password = password    # acts as a unique id
		self.language = Language.EN
		self.age = 0
		self.children = 0
		self.new_residence = ''
		self.move_reasons = []
		self.nationality = Nationality.ARABIC
		self.move_date = date.today()
		self.steps = []

	def to_dict(self):
		return self.as_dict()

	def from_dict(self, j):
		self.id = j['id'] if 'id' in j else 0
		self.name = j['name'] if 'name' in j else ''
		self.email = j['email'] if 'email' in j else ''
		self.password = j['password'] if 'password' in j else ''
		try:
			self.language = Language(int(j['language'])) if 'language' in j else Language.EN
		except:
			self.language = Language.EN
		self.age = int(j['age'])
		self.children = int(j['children']) if 'children' in j else 0
		self.new_residence = j['new_residence']
		self.move_reasons = [MoveReason(int(m)) for m in j['move_reasons']] if 'move_reasons' in j else []
		try:
			self.nationality = Nationality(j['nationality'])
		except:
			self.nationality = Nationality.ARABIC
		self.move_date = datetime.strptime(j['move_date'], '%Y-%m-%d') if type(j['move_date']) == str else j['move_date']
		self.steps = [s.from_dict() for s in j['steps']] if 'steps' in j else []

	def from_json(self, i):
		self.from_dict(json.loads(i))

	def as_dict(self):
		return {
			'name': self.name,
			'email': self.email,
			'password': self.password,
			'language': self.language.value,
			'age': self.age,
			'children': self.children,
			'new_residence': self.new_residence,
			'new_residence_lower': self.new_residence.lower(),
			'move_reasons': [m.value for m in self.move_reasons],
			'nationality': self.nationality.value,
			'move_date': self.move_date.strftime('%Y-%m-%d'),
			'steps': [s.to_dict() for s in self.steps]
		}

	def save(self):
		profile = {
			'name': self.name,
			'email': self.email,
			'password': self.password,
			'language': self.language.value,
			'age': self.age,
			'children': self.children,
			'new_residence': self.new_residence,
			'new_residence_lower': self.new_residence.lower(),
			'nationality': self.nationality.value,
			'move_date': self.move_date.strftime('%Y-%m-%d'),
		}

		keys = [k for k, v in profile.iteritems()]
		values = [v for k, v in profile.iteritems()]

		result = mysql_connection.select('SELECT id FROM profile WHERE email = "%s"' % self.email)
		if result:
			self.id = result['id']
			mysql_connection.update('profile', profile, {'email': self.email})
		else:
			mysql_connection.insert('profile', keys, values)
			result = mysql_connection.select('SELECT id FROM profile WHERE email = "%s"' % self.email)
			self.id = result['id']

		# save reasons

		existing_reasons = []
		for reason in self.move_reasons:
			result = mysql_connection.select('SELECT id FROM move_reasons WHERE profile = "%s" AND reason = "%s"' % (str(self.id), str(reason.value)))
			if result:
				mysql_connection.update('move_reasons', {'reason': reason.value}, {'id': result['id']})
				existing_reasons.append(result['id'])
			else:
				mysql_connection.insert('move_reasons', ['profile', 'reason'], [self.id, reason.value])
				result = mysql_connection.select('SELECT id FROM move_reasons WHERE profile = "%s AND reason = "%s"' % (str(self.id), str(reason.value)))
				existing_reasons.append(result['id'])
		mysql_connection.execute('DELETE FROM move_reasons WHERE id NOT IN (%s)' % (", ".join(existing_reasons)))

		# save profile steps

		existing_steps = []
		for step in self.steps:
			step.save()
			result = mysql_connection.select('SELECT id FROM profile_steps WHERE step = "%s" AND profile = "%s"' % (str(step.id), str(self.id)))
			if result:
				mysql_connection.update('profile_steps', {
					'date': step.date,
					'due': step.due,
					'time': step.time,
					'status': step.status.value
				}, {'id': result['id']})
				existing_steps.append(result['id'])
			else:
				mysql_connection.insert(
					'profile_steps',
					['step', 'profile', 'time_frame_start', 'time_frame_end', 'status'],
					[step.id, self.id, step.time_frame.start, step.time_frame.end, step.status.value]
				)
				result = mysql_connection.select('SELECT id FROM profile_steps WHERE step = "%s" AND profile = "%s"' % (str(step.id), str(self.id)))
				existing_steps.append(result['id'])
		mysql_connection.execute('DELETE FROM profile_steps WHERE id NOT IN (%s)' % (", ".join(existing_reasons)))

	def load(self):
		self.steps = []
		result = mysql_connection.select('SELECT * FROM profiles WHERE email = "%s" AND password = "%s"' % (self.email, self.password))
		if result:
			self.from_dict(result)
			profile_steps = mysql_connection.select_all('SELECT * FROM profile_steps WHERE profile = "%s"' % str(self.id))
			if profile_steps:
				for ps in profile_steps:
					step = Step()
					step.id = ps['step']
					step.load()
					step.date = ps['date']
					step.time = ps['time']
					step.due = ps['due']
					step.status = Status(ps['status'])
					self.steps.append(step)
			move_reasons = mysql_connection.select_all('SELECT * FROM move_reasons WHERE profile = "%s"' % str(self.id))
			if move_reasons:
				self.move_reasons = [MoveReason(r['reason']) for r in move_reasons]
			return True
		return False

	def get_tags(self):
		tags = [r.name for r in self.move_reasons]
		if self.nationality != Nationality.GERMAN:
			tags.append('OUTSIDE')
		else:
			tags.append('INLAND')
		return tags


class Language(Enum):
	DE = 0
	EN = 1


class MoveReason(Enum):
	STUDENT = 1
	EMPLOYED = 2
	SINGLE = 3
	MARRIED = 4
	RELATIONSHIP = 5
	WIDOWED = 6
	CHILDREN = 7


class Nationality(str, Enum):
	GERMAN = 'DE'
	ARABIC = 'AE'
	FRENCH = 'FR'

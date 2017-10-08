import copy
import json
from enum import Enum
from datetime import datetime
from mysqlconnection import MySQL_Connection

# {
#     "dependencies": [
#         1,
#         2,
#         3,
#         4
#     ],
#     "location": {
#         "latitude": 48.469430499999987,
#         "longitude": 7.9427725000000002
#     },
#     "status": 1,
#     "sub_steps": [
#         5,
#         6,
#         7,
#         8
#     ],
#     "tags": [
#         12
#     ],
#     "time_frame": {
#         "end": "2017-10-14",
#         "start": "2017-10-11"
#     }
# }

mysql_connection = MySQL_Connection('mysql', 3306, 'root', 'blackforestmysql', 'hackathon')


class Step(object):
	id = 0
	title = ''
	city = ''
	city_location = None
	location = None
	maps_url = 'https://www.google.com/maps/?q='
	child = None
	date = '0000-00-00'
	time = '00:00'
	due = '0000-00-00'
	status = None
	dependency = None       # type Step
	tags = None               # type tag
	description = ''
	location_name = ''
	mandatory = True

	def __init__(self):
		self.city = 'Offenburg'
		self.title = 'Lorem Ipsum'
		self.description = 'Gelber Sack'
		self.location = Location(48.46943049999999, 7.9427725)   # location of Rathaus
		self.maps_url = 'https://www.google.com/maps/?q=%s,%s' % (str(self.location.latitude), str(self.location.longitude))
		self.date = '2017-11-09'
		self.time = '08:00'
		self.due = '2017-11-15'
		self.status = Status.TODO
		self.tags = []
		self.add_tag(Tag.OUTSIDE)
		self.child = None
		self.dependency = None
		self.location_name = 'Rathaus'
		self.mandatory = True
		self.city_location = Location(48.4748511, 7.8750228)

	def add_tag(self, tag):
		if tag not in self.tags:
			self.tags.append(tag)

	def to_dict(self):
		return {
			'id': self.id,
			'title': self.title,
			'city': self.city,
			'location': self.location.to_json(),
			'maps_url': 'https://www.google.com/maps/?q=%s,%s' % (str(self.location.latitude), str(self.location.longitude)),
			'child': self.child,
			'date': self.date,
			'time': self.time,
			'due': self.due,
			'status': self.status.value,
			'tags': [t.value for t in self.tags],
			'dependency': self.dependency,
			'description': self.description,
			'location_name': self.location_name,
			'mandatory': self.mandatory,
			'city_location': self.city_location.to_json()
		}

	def from_dict(self, j):
		self.id = j['id'] if 'id' in j else 0
		self.title = j['title']
		self.city = j['city']
		self.location = Location(float(j['location']['latitude']), float(j['location']['longitude']))
		self.maps_url = 'https://www.google.com/maps/?q=%s,%s' % (str(self.location.latitude), str(self.location.longitude))
		self.child = [int(s) for s in j['next']] if 'next' in j else [int(s) for s in j['child']]
		self.date = j['date']
		self.time = j['time']
		self.due = j['due']
		self.status = Status(int(j['status']))
		self.tags = [Tag(int(t)) for t in j['tags']]
		self.dependency = [int(d) for d in j['dependency']]
		self.description = j['description']
		self.location_name = j['location_name']
		self.mandatory = True if j['mandatory'] else False
		self.city_location = Location(float(j['city_location']['latitude']), float(j['city_location']['longitude'])) if 'city_location' in j else Location(48.4748511, 7.8750228)

	def from_json(self, i):
		self.from_dict(json.loads(i))
		return self

	def applies(self, profile):
		ptags = profile.get_tags()
		print ptags
		print [t.name for t in self.tags]

		for pt in ptags:
			for t in self.tags:
				if pt == t.name:
					return True
		return False
	
	def save(self):
		step = {
			'title': self.title,
			'city': self.city,
			'location_lat': str(self.location.latitude),
			'location_lng': str(self.location.longitude),
			'description': self.description,
			'dependency': self.dependency,
			'child': self.child,
			'location_name': self.location_name,
			'mandatory': 1 if self.mandatory else 0,
		}

		keys = [k for k, v in step.iteritems()]
		values = [v for k, v in step.iteritems()]

		result = mysql_connection.select('SELECT id FROM steps WHERE id = "%s"' % str(self.id))
		if result:
			self.id = result['id']
			mysql_connection.update('steps', step, {'id': self.id})
		else:
			mysql_connection.insert('steps', keys, values)
			result = mysql_connection.select('SELECT id FROM steps ORDER BY id DESC')
			self.id = result['id']

		existing_tags = []
		for tag in self.tags:
			result = mysql_connection.select('SELECT id FROM step_tags WHERE step = "%s"' % str(self.id))
			if result:
				existing_tags.append(result['id'])
				mysql_connection.update('step_tags', {'tag': tag.value}, {'id': result['id']})
			else:
				mysql_connection.insert('step_tags', ['step', 'tag'], [self.id, tag.value])
				result = mysql_connection.select('SELECT id FROM step_tags WHERE step = "%s AND tag = "%s"' % (str(self.id), str(tag.value)))
				existing_tags.append(result['id'])
		mysql_connection.execute('DELETE FROM step_tags WHERE step = "%s" AND id NOT IN (%s)' % (str(self.id), ", ".join(existing_tags)))

	def load(self):
		if self.id == 0:
			return False
		step_result = mysql_connection.select('SELECT * FROM steps WHERE id = "%s"' % str(self.id))
		if step_result:
			self.title = step_result['title']
			self.city = step_result['city']
			self.location = Location(float(step_result['location_lat']), float(step_result['location_lng']))
			tags_result = mysql_connection.select_all('SELECT tag FROM step_tags WHERE step = "%s"' % str(self.id))
			if tags_result:
				self.tags = [Tag(tag['tag']) for tag in tags_result]

			# load dep and next

			self.dependency = step_result['dependency']
			self.child = step_result['child']
			self.location_name = step_result['location_name']
			self.mandatory = True if step_result['mandatory'] else False
			self.description = step_result['description']
			self.maps_url = 'https://www.google.com/maps/?q=%s,%s' % (str(self.location.latitude), str(self.location.longitude))

			city_result = mysql_connection.select('SELECT * FROM cities WHERE name LIKE "%s"' % self.city)
			if city_result:
				self.city_location = Location(city_result['location_lat'], city_result['location_lng'])


class Location(object):
	latitude = 0.0
	longitude = 0.0

	def __init__(self, latitude, longitude):
		self.latitude = latitude
		self.longitude = longitude

	def to_json(self):
		return {'latitude': self.latitude, 'longitude': self.longitude}


class Status(Enum):
	TODO = 0
	DONE = 1


class Tag(Enum):
	STUDENT = 1
	EMPLOYED = 2
	SINGLE = 3
	MARRIED = 4
	RELATIONSHIP = 5
	WIDOWED = 6
	CHILDREN = 7
	INLAND = 8
	OUTSIDE = 9

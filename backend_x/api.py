import json

from profile import Profile
from city import City


class MarieAPI(object):

	def get_steps_by_profile(self, json_profile):
		"""
		accepts a json string of a profile and returns a dict containing related steps in order of time_frame
		:param json_profile: json string
		:return: dict {steps: [<step>...]}
		"""
		profile = Profile()
		profile.from_dict(json_profile)
		city = City(profile.new_residence)
		city.load()
		timeline = city.get_timeline_from_profile(profile)

		print json.dumps(timeline.to_dict())

		return timeline.to_dict()

	def get_profile(self, email, password):
		"""
		returns a profile based on the email and password or creates a new profile
		:param email: email
		:param password: password
		:return: profile dict
		"""
		profile = Profile(email, password)
		if profile.load():
			return profile.to_dict()
		return None






import json

from api import MarieAPI

if __name__ == '__main__':
	a = MarieAPI()
	# print a.get_profile('mor@vioma.de', 'secret')

	d = json.loads('{ "age": 25, "move_date": "2017-10-18", "move_reasons": [1, 3, 5], "nationality": "AE", "new_residence": "Offenburg"}')

	print a.get_steps_by_profile(d)


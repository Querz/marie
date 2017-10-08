# -*- coding: utf-8 -*-
import googlemaps
import googlemaps.places
import googlemaps.geocoding
import json


class googleMapsSearch:
	gmaps = googlemaps.Client(key='AIzaSyAmgN4IZh9SILGetGtzplibnGXeuA3uu8o')

	def cityLoc(self, city):
		return json.dumps(googlemaps.geocoding.geocode(self.gmaps, address=city, components={'country': 'DE'})[0]['geometry']['location'])

	def searchPlace(self, keyword, city, radius=3000):
		return self.placeByKey(googlemaps.places.places_nearby(self.gmaps, json.loads(city), radius, keyword)['results'][0]['place_id'])

	def placeByKey(self, key):
		result = googlemaps.places.place(self.gmaps, key)['result']
		result.remove('reviews')

		return json.dumps(result)

if __name__ == '__main__':
	gms = googleMapsSearch()
	print(gms.searchPlace('Ausländerbüro', gms.cityLoc('Offenburg')))

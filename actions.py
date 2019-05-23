from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class ActionWeather(Action):
	def name(self):
		return 'action_weather'
		
	def run(self, dispatcher, tracker, domain):
		from apixu.client import ApixuClient
		api_key = '75831f61df2f451793283410191605'
		client = ApixuClient(api_key)
		
		loc = tracker.get_slot('location')
		current = client.current(q=loc) 
			
		country = current['location']['country']
		city = current['location']['name']
		condition = current['current']['condition']['text']
		temperature_c = current['current']['temp_c']
		humidity = current['current']['humidity']
		wind_mph = current['current']['wind_mph']
		
		res = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}%.""".format(condition, city, temperature_c, humidity)
						
		dispatcher.utter_message(res)
		return [SlotSet('location',loc)]
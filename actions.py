from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from tip_class import CravingTips
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy.orm import sessionmaker
import numpy as np

from rasa_sdk import Action


class ActionSideEffect(Action):
    def name(self):
        return "action_side_effect"

    def run(self, dispatcher, tracker, domain):
        side_effect = tracker.get_slot('side_effect')
        tips = {
            'nausea': "Make sure you drink enough water.",
        }
        tip = tips.get(side_effect, 'When in despair, try looking forward to shiny happy future.')
        dispatcher.utter_message(tip)
        return []


class ActionCravingTip(Action):
	def name(self):
		return "action_craving_tip"

	def run(self, dispatcher, tracker, domain):


		location = tracker.get_slot('location')

		#To create the same tags as the database

		if location == "home":
			loc = 1
		elif location == "work":
			loc = 2
		elif location == "social gathering":
			loc = 3
		elif location == "leisure":
			loc = 4
		elif location == "other":
			loc = 5


		k = 10^(5-i) 				#To obtain remainder from the location column values in the table

		q = "select * from Craving_tips where location\%" + k + " = " + loc

		engine = create_engine('sqlite:///Craving_tips.db')
		metadata = MetaData(engine)
		Session = sessionmaker()
		session = Session(bind=engine)
		result = session.query(q)

		if 	len(result) == 1:
			dispatcher.utter_message(result)
		else:
			rand = np.rand.randint(0,len(result)-1)
			dispatcher.utter_message(result[rand])
		return []

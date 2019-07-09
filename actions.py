from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from database.models import CravingTip
from database import Session
from sqlalchemy.sql.expression import func

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

        session = Session()
        # TODO: filter by location correctly
        tip = session.query(CravingTip).order_by(func.random()).first()
        # session.query(CravingTip).filter(CravingTip.locations.any(name='work')).order_by(func.random()).first()

        dispatcher.utter_message(tip.en_tips)

        return []

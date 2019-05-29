from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

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
        dispatcher.utter_message('Don\'t smoke!')
        return []

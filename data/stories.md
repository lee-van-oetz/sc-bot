## story_craving1
* help
 - utter_urge
* affirm
 - utter_where
* tell_location{"location": "home"}
 - action_craving_tip

## story_side_effect1
* help
 - utter_urge
* reject
 - utter_any_side_effects
* side_effect{"side_effect": "nausea"}
 - action_side_effect

## story_craving2
* help
 - utter_whatsup
* urge_bad
 - utter_where
* tell_location{"location": "home"}
 - action_craving_tip

## story_side_effect2
* help
 - utter_whatsup
* urge_ok
 - utter_any_side_effects
* side_effect{"side_effect": "nausea"}
 - action_side_effect
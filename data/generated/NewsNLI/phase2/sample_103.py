# Premise: The International Atomic Energy Agency said it was aware of reports that the Nuclear Regulation Authority plans to rate the leak as a level 3 incident.
# Hypothesis: Nuclear Regulation Authority says new toxic leak expected to be classified a level 3 incident.
# Golden Label: entailment

incident_level_premise = 3
incident_level_hypothesis = 3

# the hypothesis mentions the incident level, which is also referenced in the premise
# however, the hypothesis states that the Nuclear Regulation Authority said the leak is level 3, while the premise mentions that the International Atomic Energy Agency is aware of reports about this classification
label = "neutral"

print(label)


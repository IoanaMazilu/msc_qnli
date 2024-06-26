distance_traveled_premise = 200
distance_traveled_hypothesis = 300

# the hypothesis refers to the distance traveled on the first day of Louisa's vacation
if distance_traveled_premise <= distance_traveled_hypothesis:
    # check if the estimate of 'distance_traveled_hypothesis' contradicts the distance traveled in the premise
    label = "contradiction"
else:
    # the premise gives an exact value for the distance traveled
    # any distance traveled less than 'distance_traveled_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

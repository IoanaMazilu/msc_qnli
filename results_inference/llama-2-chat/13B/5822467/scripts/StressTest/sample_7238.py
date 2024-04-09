vacation_distance_premise = 240
vacation_distance_hypothesis = 340

# the hypothesis refers to the distance traveled on the first day of the vacation, mentioned in the premise
if vacation_distance_premise <= vacation_distance_hypothesis:
    # check if the estimate of 'vacation_distance_hypothesis' contradicts the distance traveled in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance traveled
    # any distance greater than 'vacation_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

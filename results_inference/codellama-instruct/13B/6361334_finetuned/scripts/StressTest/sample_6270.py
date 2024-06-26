participants_premise = 7
participants_hypothesis = 8

# the hypothesis refers to the number of participants in a cycling race, mentioned in the premise
if participants_premise < participants_hypothesis:
    # check if the estimate of 'participants_hypothesis' contradicts the number of participants in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of participants
    # any number of participants less than 'participants_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

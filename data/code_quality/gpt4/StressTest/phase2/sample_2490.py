boat_speed_premise = 12
boat_speed_hypothesis = 52

# the hypothesis refers to the boat speed which is also mentioned in the premise
if boat_speed_premise >= boat_speed_hypothesis:
    # check if the speed from the premise contradicts the hypothesis estimate of less than 'boat_speed_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)

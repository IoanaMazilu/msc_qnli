distance_walked_premise = 6
distance_walked_hypothesis = 4
time_walked = 1.25 # 1 hour and 15 minutes is 1.25 hours

# the hypothesis refers to the distance walked by Jack mentioned in the premise
if distance_walked_premise <= distance_walked_hypothesis:
    # check if the distance in 'distance_walked_hypothesis' contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis distance does not contradict the distance reported in the premise, we can infer entailment
    label = "entailment"

print(label)

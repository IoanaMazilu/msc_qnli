distance_walked_premise = 4
distance_walked_hypothesis = 3
time_walked = 1.25 # 1 hour and 15 minutes is 1.25 hours

# the hypothesis refers to the distance walked by Jack mentioned in the premise
if distance_walked_premise <= distance_walked_hypothesis:
    # check if the estimate of 'distance_walked_hypothesis' contradicts the distance walked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
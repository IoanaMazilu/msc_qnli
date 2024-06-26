distance_premise = 50
distance_hypothesis = 50

# the hypothesis refers to the distance between their homes mentioned in the premise
if distance_hypothesis < distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance in the premise
    label = "contradiction"
elif maxwell_speed_premise!= maxwell_speed_hypothesis or brad_speed_premise!= brad_speed_hypothesis:
    # check if the values of Maxwell's and Brad's speed in the hypothesis contradict the values in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

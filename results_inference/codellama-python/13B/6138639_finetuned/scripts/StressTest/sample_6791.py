distance_premise = 50
distance_hypothesis = 50
maxwell_speed = 4
brad_speed = 6

# the hypothesis refers to the distance between their homes and the speeds of Maxwell and Brad mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

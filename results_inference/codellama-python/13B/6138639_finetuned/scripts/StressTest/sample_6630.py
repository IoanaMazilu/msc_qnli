distance_premise = 500
distance_hypothesis = 800
speed = 15

# the hypothesis refers to the time Sandy takes to cover a distance, which is also mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

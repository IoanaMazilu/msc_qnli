total_distance_premise = 8/2
total_distance_hypothesis = 1/2

# the hypothesis refers to the distance traveled before Maria stopped, which is also mentioned in the premise
if total_distance_hypothesis >= total_distance_premise:
    # check if the estimate of 'total_distance_hypothesis' contradicts the distance traveled before Maria stopped in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

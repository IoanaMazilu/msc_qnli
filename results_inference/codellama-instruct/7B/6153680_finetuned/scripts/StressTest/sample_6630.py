distance_premise = 500
distance_hypothesis = 800
speed = 15

# the hypothesis refers to the distance covered by Sandy, which is also mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis does not contradict the distance in the premise, we can infer entailment
    label = "entailment"

print(label)

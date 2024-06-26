distance_covered_premise = 500
distance_covered_hypothesis = 500
speed_sandy = 15

# the hypothesis refers to the distance covered by Sandy, mentioned in the premise
if distance_covered_hypothesis <= distance_covered_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

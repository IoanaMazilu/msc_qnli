distance_xy_premise = 17
distance_xy_hypothesis = 77

# The hypothesis refers to the same route from X to Y that is mentioned in the premise
if distance_xy_hypothesis < distance_xy_premise:
    # check if the distance in the hypothesis contradicts the distance from the premise
    label = "contradiction"
elif distance_xy_hypothesis > distance_xy_premise:
    # the hypothesis gives a higher estimate for the distance, which cannot be entailed from the premise
    label = "neutral"
else:
    # if the distance in the hypothesis does not contradict the distance from the premise, we can infer entailment
    label = "entailment"

print(label)

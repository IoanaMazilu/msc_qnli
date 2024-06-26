distance_premise = 45
distance_hypothesis = 35

# the hypothesis refers to the distance between Fred and Sam mentioned in the premise
if distance_hypothesis > distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # check if the distance in the hypothesis is less than the distance reported in the premise
    label = "entailment"
else:
    # if the distance in the hypothesis is exactly the same as the distance reported in the premise, we can infer neutrality
    label = "neutral"

print(label)

distance_premise = 1 * 46 + 3 * 60
distance_hypothesis = 3 * 46 + 3 * 60

# the hypothesis refers to the distance traveled by Andrew between city A and city B
if distance_hypothesis!= distance_premise:
    # check if the distance traveled in the hypothesis contradicts the distance traveled in the premise
    label = "contradiction"
else:
    # if the distance traveled in the hypothesis is consistent with the distance traveled in the premise, we can infer entailment
    label = "entailment"

print(label)

distance_premise = 360
distance_hypothesis = 360

# the hypothesis mentions the same distance from Manila to Negros as in the premise
if distance_hypothesis!= distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"

print(label)

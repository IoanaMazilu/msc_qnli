distance_premise = 10.7
distance_hypothesis = 10.7

# the hypothesis mentions the length of the urban gondola, which is also mentioned in the premise
if distance_hypothesis!= distance_premise:
    # check if the length of the gondola in the hypothesis contradicts the length reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

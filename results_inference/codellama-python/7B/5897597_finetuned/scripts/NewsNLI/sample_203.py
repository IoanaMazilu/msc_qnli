plants_premise = 2
plants_hypothesis = 2

# the hypothesis mentions the number of marijuana plants grown by the grandmother, which is also mentioned in the premise
if plants_hypothesis!= plants_premise:
    # check if the number of plants in the hypothesis contradicts the number of plants reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

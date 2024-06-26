plants_premise = 2
plants_hypothesis = 2

# the hypothesis mentions the number of marijuana plants the grandmother is growing, which is also mentioned in the premise
if plants_hypothesis != plants_premise:
    # check if the number of plants in the hypothesis contradicts the number of plants reported in the premise
    label = "contradiction"
else:
    # if the number of plants from the hypothesis does not contradict the number of plants in the premise, we can infer entailment
    label = "entailment"

print(label)

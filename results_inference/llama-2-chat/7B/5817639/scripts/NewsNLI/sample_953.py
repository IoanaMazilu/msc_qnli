guilty_premise = 1
guilty_hypothesis = 3

# the hypothesis mentions the third person found guilty in the killings, which is also referenced in the premise
if guilty_hypothesis!= guilty_premise:
    # check if the number of guilty parties in the hypothesis contradicts the number of guilty parties in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

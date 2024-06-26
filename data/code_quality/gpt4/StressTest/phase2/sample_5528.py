parents_premise = 38
parents_hypothesis = 88

# the hypothesis refers to the number of parents participating in the Smithville PTA, also mentioned in the premise
if parents_premise != parents_hypothesis:
    # check if the number of parents in the hypothesis contradicts the number of parents reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

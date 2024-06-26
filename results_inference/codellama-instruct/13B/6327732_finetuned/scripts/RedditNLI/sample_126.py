growth_premise = 2.2
growth_hypothesis = 2.2

# the hypothesis and premise mention the same growth rate
if growth_premise!= growth_hypothesis:
    # check if the growth rate in the hypothesis contradicts the growth rate in the premise
    label = "contradiction"
else:
    # if the growth rate in the hypothesis is consistent with the premise, we can infer entailment
    label = "entailment"

print(label)

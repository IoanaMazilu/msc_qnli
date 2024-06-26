growth_rate_premise = 3.7
growth_rate_hypothesis = 3.7

# the hypothesis and premise mention the growth rate of the U.S. economy in the 2nd quarter
if growth_rate_hypothesis != growth_rate_premise:
    # check if the growth rate in the hypothesis contradicts the growth rate in the premise
    label = "contradiction"
else:
    # if the growth rate in the hypothesis does not contradict the growth rate in the premise, we can infer entailment
    label = "entailment"

print(label)

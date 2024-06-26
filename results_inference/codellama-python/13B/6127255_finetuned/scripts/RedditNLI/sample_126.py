growth_rate_premise = 2.2
growth_rate_hypothesis = 2.2

# the hypothesis and premise mention the revised growth rate of the US economy in the first quarter
if growth_rate_hypothesis!= growth_rate_premise:
    # check if the growth rate in the hypothesis contradicts the growth rate in the premise
    label = "contradiction"
else:
    # if the growth rate in the hypothesis does not contradict the growth rate in the premise, we can infer entailment
    label = "entailment"

print(label)

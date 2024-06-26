growth_rate_premise = 2.2
growth_rate_hypothesis = 2.2

# the hypothesis and premise mention the growth rate in the US
if growth_rate_hypothesis!= growth_rate_premise:
    # check if the growth rate in the hypothesis contradicts the growth rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

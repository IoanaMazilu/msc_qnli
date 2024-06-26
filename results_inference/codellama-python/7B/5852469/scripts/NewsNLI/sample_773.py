growth_rate_premise = 0.045
growth_rate_hypothesis = 0.045

# the hypothesis mentions the growth rate of the U.S. economy, which is also mentioned in the premise
if growth_rate_hypothesis!= growth_rate_premise:
    # check if the growth rate in the hypothesis contradicts the growth rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

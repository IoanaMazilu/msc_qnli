growth_premise = 0.025
growth_hypothesis = 0.025

# the hypothesis mentions the growth in the U.S. economy, which is also mentioned in the premise
if growth_hypothesis!= growth_premise:
    # check if the growth in the hypothesis contradicts the growth in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

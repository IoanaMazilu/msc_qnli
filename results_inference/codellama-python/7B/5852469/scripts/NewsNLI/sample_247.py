growth_premise = 0.021
growth_hypothesis = 0.021

# the hypothesis mentions the growth of the U.S. economy in the first quarter, which is also mentioned in the premise
if growth_hypothesis!= growth_premise:
    # check if the growth in the hypothesis contradicts the growth in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

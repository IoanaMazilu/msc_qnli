passengers_premise = 0.44
passengers_hypothesis = 0.44

# the hypothesis mentions the percentage increase in the risk of a teen driver crashing, which is also mentioned in the premise
if passengers_hypothesis!= passengers_premise:
    # check if the percentage increase in the hypothesis contradicts the percentage increase reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

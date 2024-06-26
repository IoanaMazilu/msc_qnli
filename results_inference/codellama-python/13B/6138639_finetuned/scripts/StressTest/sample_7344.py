slump_premise = 28
slump_hypothesis = 68

# the hypothesis refers to the slump of crude oil prices mentioned in the premise
if slump_hypothesis <= slump_premise:
    # check if the estimate of'slump_hypothesis' contradicts the slump in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

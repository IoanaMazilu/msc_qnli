slump_percentage_premise = 68
slump_percentage_hypothesis = 28
increase_percentage = 5

# the hypothesis refers to the slump percentage of crude oil price mentioned in the premise
if slump_percentage_hypothesis > slump_percentage_premise:
    # check if the slump percentage in the hypothesis contradicts the slump percentage reported in the premise
    label = "contradiction"
elif slump_percentage_hypothesis < slump_percentage_premise:
    # the premise gives an estimate for the slump percentage
    # any slump percentage less than'slump_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

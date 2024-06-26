crude_slump_premise = 28
crude_slump_hypothesis = 68

# the hypothesis refers to the percentage slump of crude price mentioned in the premise
if crude_slump_premise >= crude_slump_hypothesis:
    # check if the estimate of 'crude_slump_hypothesis' contradicts the percentage slump in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

# the hypothesis refers to the same conditions as the premise, but with different values
oa_premise = 6
oa_hypothesis = 2
ac_premise = 4
ac_hypothesis = 4
bd_premise = 6
bd_hypothesis = 6

# check if the hypothesis values contradict the premise ones
if oa_hypothesis >= oa_premise:
    label = "contradiction"
elif ac_hypothesis!= ac_premise or bd_hypothesis!= bd_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

oa_premise = 6
ac_premise = 4
bd_premise = 6

oa_hypothesis = 2
ac_hypothesis = 4
bd_hypothesis = 6

# the hypothesis refers to the same conditions as the premise
if oa_hypothesis >= oa_premise:
    # check if the value of 'oa_hypothesis' contradicts the condition of 'oa_premise'
    label = "contradiction"
elif ac_hypothesis!= ac_premise or bd_hypothesis!= bd_premise:
    # check if the values of 'ac_hypothesis' or 'bd_hypothesis' contradict the values reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

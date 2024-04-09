oa_premise = 2
ac_premise = 4
bd_premise = 6

oa_hypothesis = 6
ac_hypothesis = 4
bd_hypothesis = 6

# the hypothesis refers to the same conditions as the premise, but with different estimates for OA
if oa_hypothesis <= oa_premise:
    # check if the estimate of 'oa_hypothesis' contradicts the value of OA in the premise
    label = "contradiction"
elif ac_hypothesis!= ac_premise or bd_hypothesis!= bd_premise:
    # check if the values of AC and BD in the hypothesis contradict the values reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

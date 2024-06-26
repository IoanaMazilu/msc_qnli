oa_premise = 2
ac_premise = 4
bd_premise = 6

oa_hypothesis = 6

# the hypothesis refers to the same conditions as the premise
if oa_premise >= oa_hypothesis:
    # check if the premise value contradicts the estimate of 'oa_hypothesis'
    label = "contradiction"
elif ac_premise!= ac_hypothesis or bd_premise!= bd_hypothesis:
    # check if the values of AC and BD in the hypothesis contradict the values in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

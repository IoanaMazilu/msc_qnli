oa_premise = 2
oa_hypothesis = 2
ac_premise = 4
ac_hypothesis = 4
bd_premise = 6
bd_hypothesis = 6

# the hypothesis refers to the same conditions and variables as the premise
if oa_hypothesis <= oa_premise:
    # check if the hypothesis value contradicts the estimate of 'oa_premise'
    label = "contradiction"
elif ac_hypothesis!= ac_premise:
    # check if the value of 'ac_hypothesis' contradicts the value of 'ac_premise'
    label = "contradiction"
elif bd_hypothesis!= bd_premise:
    # check if the value of 'bd_hypothesis' contradicts the value of 'bd_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

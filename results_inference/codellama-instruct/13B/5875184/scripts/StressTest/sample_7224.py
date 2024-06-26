oa_premise = 2
ac_premise = 4
bd_premise = 6

oa_hypothesis = 6
ac_hypothesis = 4
bd_hypothesis = 6

# the hypothesis refers to the length of OB, which is not mentioned in the premise
if oa_hypothesis <= oa_premise:
    # check if the hypothesis value contradicts the estimate of 'oa_premise'
    label = "contradiction"
elif ac_hypothesis!= ac_premise:
    # check if the hypothesis value contradicts the estimate of 'ac_premise'
    label = "contradiction"
elif bd_hypothesis!= bd_premise:
    # check if the hypothesis value contradicts the estimate of 'bd_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

oa_premise = 6
oa_hypothesis = 2
ac_premise = 4
ac_hypothesis = 4
bd_premise = 6
bd_hypothesis = 6

# the hypothesis refers to the values of OA, AC and BD mentioned in the premise
if oa_hypothesis >= oa_premise:
    # check if the hypothesis value contradicts the estimate of less than 'oa_premise'
    label = "contradiction"
elif ac_hypothesis!= ac_premise:
    # check if the hypothesis value contradicts the value of AC mentioned in the premise
    label = "contradiction"
elif bd_hypothesis!= bd_premise:
    # check if the hypothesis value contradicts the value of BD mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

oa_premise = 2
oa_hypothesis = 2
ac_premise = 4
ac_hypothesis = 4
bd_premise = 6
bd_hypothesis = 6

# the hypothesis refers to the lengths of OA, AC and BD mentioned in the premise
if oa_hypothesis <= oa_premise:
    # check if the hypothesis value contradicts the given value of OA in the premise
    label = "contradiction"
elif ac_hypothesis!= ac_premise or bd_hypothesis!= bd_premise:
    # check if the lengths of AC and BD in the hypothesis contradict the lengths given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

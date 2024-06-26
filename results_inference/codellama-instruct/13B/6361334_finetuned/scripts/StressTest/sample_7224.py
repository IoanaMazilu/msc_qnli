oa_premise = 2
oa_hypothesis = 6
ac_premise = 4
ac_hypothesis = 4
bd_premise = 6
bd_hypothesis = 6

# the hypothesis refers to the length of OA, AC and BD mentioned in the premise
if oa_hypothesis <= oa_premise:
    # check if the estimate of 'oa_hypothesis' contradicts the length of OA in the premise
    label = "contradiction"
elif ac_hypothesis!= ac_premise:
    # check if the length of AC in the hypothesis contradicts the length of AC reported in the premise
    label = "contradiction"
elif bd_hypothesis!= bd_premise:
    # check if the length of BD in the hypothesis contradicts the length of BD reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

boxes_per_case_premise = 5
boxes_per_case_hypothesis = 8

# the hypothesis refers to the number of boxes per case mentioned in the premise
if boxes_per_case_hypothesis <= boxes_per_case_premise:
    # check if the estimate of 'boxes_per_case_hypothesis' contradicts the number of boxes per case in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

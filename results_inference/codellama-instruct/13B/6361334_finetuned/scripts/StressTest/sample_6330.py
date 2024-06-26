boxes_per_case_premise = 5
boxes_per_case_hypothesis = 8

# the hypothesis refers to the number of boxes in a case, which is also mentioned in the premise
if boxes_per_case_hypothesis <= boxes_per_case_premise:
    # check if the hypothesis value contradicts the number of boxes in a case in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boxes in a case
    # any number of boxes greater than 'boxes_per_case_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

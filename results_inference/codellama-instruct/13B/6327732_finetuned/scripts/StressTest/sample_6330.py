boxes_per_case_premise = 5
boxes_per_case_hypothesis = 8

# the hypothesis talks about the number of boxes in a case, referenced also in the premise
if boxes_per_case_hypothesis <= boxes_per_case_premise:
    # check if the hypothesis value contradicts the estimate of more than 'boxes_per_case_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boxes in a case
    # any number of boxes greater than 'boxes_per_case_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

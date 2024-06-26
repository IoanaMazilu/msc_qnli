boxes_case_premise = 5
boxes_case_hypothesis = 8

# the hypothesis refers to the number of boxes of cigarettes in a case, mentioned in the premise
if boxes_case_hypothesis <= boxes_case_premise:
    # check if the estimate of 'boxes_case_hypothesis' contradicts the number of boxes in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boxes
    # any number of boxes less than 'boxes_case_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

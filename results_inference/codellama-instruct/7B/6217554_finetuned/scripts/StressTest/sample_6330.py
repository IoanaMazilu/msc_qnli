boxes_case_premise = 5
boxes_case_hypothesis = 8

# the hypothesis gives an estimate for the number of boxes in one case
# any number of boxes greater than 'boxes_case_hypothesis' contradicts the premise
if boxes_case_hypothesis <= boxes_case_premise:
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boxes
    # any number of boxes greater than 'boxes_case_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

boxes_per_case_premise = 8
boxes_per_case_hypothesis = 5

# the hypothesis refers to the number of boxes of cigarettes in one case, which is also mentioned in the premise
if boxes_per_case_premise <= boxes_per_case_hypothesis:
    # check if the estimate of 'boxes_per_case_hypothesis' contradicts the number of boxes in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boxes in one case
    # any number of boxes greater than 'boxes_per_case_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

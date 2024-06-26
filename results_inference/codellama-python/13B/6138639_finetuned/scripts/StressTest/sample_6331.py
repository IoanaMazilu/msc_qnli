boxes_case_premise = 8
boxes_case_hypothesis = 5

# the hypothesis talks about the number of boxes in a case, referenced also in the premise
if boxes_case_hypothesis >= boxes_case_premise:
    # check if the hypothesis value contradicts the estimate of less than 'boxes_case_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boxes
    # any number of boxes less than 'boxes_case_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

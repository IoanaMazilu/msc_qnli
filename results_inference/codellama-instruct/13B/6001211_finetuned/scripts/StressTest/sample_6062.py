indu_leave_premise = 7
indu_leave_hypothesis = 7

# the hypothesis refers to the number of days Indu leaves before the work is finished, mentioned in the premise
if indu_leave_hypothesis <= indu_leave_premise:
    # check if the hypothesis value contradicts the number of days in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of days
    # any number of days greater than 'indu_leave_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

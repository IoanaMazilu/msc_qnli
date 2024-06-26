days_work_premise = 11
days_work_hypothesis = 11

# the hypothesis and the premise refer to the same number of days
if days_work_hypothesis <= days_work_premise:
    # check if the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the number of days
    # any number of days greater than 'days_work_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

work_days_premise = 8
work_days_hypothesis = 8

# the hypothesis refers to the number of days they worked, mentioned in the premise
if work_days_hypothesis <= work_days_premise:
    # check if the hypothesis value contradicts the exact number of 'work_days_premise'
    label = "contradiction"
else:
    # the premise gives an exact number of days
    # any number of days greater than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

work_days_premise = 20
work_days_hypothesis = 50

# the hypothesis refers to the number of work days mentioned in the premise
if work_days_hypothesis <= work_days_premise:
    # check if the hypothesis value contradicts the number of work days reported in the premise
    label = "contradiction"
else:
    # any number of work days greater than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

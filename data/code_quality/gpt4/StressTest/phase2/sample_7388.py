work_days_premise = 11
work_days_hypothesis = 11

# the hypothesis refers to Mary's working days which is also mentioned in the premise
if work_days_hypothesis < work_days_premise:
    # check if the hypothesis value contradicts the exact number of days in the premise
    label = "contradiction"
elif work_days_hypothesis == work_days_premise:
    # check if the hypothesis value is the same as the one in the premise
    label = "contradiction"
else:
    # any number of days greater than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

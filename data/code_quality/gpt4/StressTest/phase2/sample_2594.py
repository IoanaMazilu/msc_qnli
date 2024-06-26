work_days_premise = 26
work_days_hypothesis = 26

# the hypothesis refers to the time in which Mary can do a piece of work, also mentioned in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the proposition of 'work_days_hypothesis' contradicts the time in the premise
    label = "contradiction"
else:
    # the hypothesis states a shorter time period than the premise, which is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

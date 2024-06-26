work_hours_premise = 20
work_hours_hypothesis = 10

# the hypothesis refers to the number of hours Annie can work alone, also mentioned in the premise
if work_hours_hypothesis >= work_hours_premise:
    # check if the hypothesis value contradicts the estimate of less than 'work_hours_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, it is consistent with the premise but cannot be explicitly entailed from it
    label = "neutral"

print(label)

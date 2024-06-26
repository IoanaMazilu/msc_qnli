dan_work_hours_premise = 8
dan_work_hours_hypothesis = 6

# the hypothesis refers to the number of hours Dan works before stopping, which is also referenced in the premise
if dan_work_hours_hypothesis >= dan_work_hours_premise:
    # check if the estimate of 'dan_work_hours_hypothesis' contradicts the number of hours Dan works before stopping in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours Dan works before stopping
    # any number of hours less than 'dan_work_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

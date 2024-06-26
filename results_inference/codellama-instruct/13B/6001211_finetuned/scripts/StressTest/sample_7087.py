dan_work_hours_premise = 8
dan_work_hours_hypothesis = 6

# the hypothesis refers to the number of hours Dan works, which is also mentioned in the premise
if dan_work_hours_hypothesis >= dan_work_hours_premise:
    # check if the number of hours Dan works in the hypothesis contradicts the estimate of less than 'dan_work_hours_premise'
    label = "contradiction"
elif dan_work_hours_hypothesis < dan_work_hours_premise:
    # the premise gives only an estimate for the number of hours Dan works
    # any number of hours less than 'dan_work_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

dan_work_hours_premise = 2
dan_work_hours_hypothesis = 3

# the hypothesis refers to the number of hours Dan works, mentioned in the premise
if dan_work_hours_hypothesis <= dan_work_hours_premise:
    # check if the number of hours Dan works in the hypothesis contradicts the estimate of more than 'dan_work_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours Dan works
    # any number of hours greater than 'dan_work_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

dan_work_hours_premise = 8
dan_work_hours_hypothesis = 6

# the hypothesis talks about the number of hours Dan works, referenced also in the premise
if dan_work_hours_hypothesis >= dan_work_hours_premise:
    # check if the hypothesis value contradicts the estimate of less than 'dan_work_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours Dan works
    # any number of hours less than 'dan_work_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

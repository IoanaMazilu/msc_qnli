dan_work_hours_premise = 2
dan_work_hours_hypothesis = 3

# the hypothesis talks about the number of hours Dan worked alone, referenced also in the premise
if dan_work_hours_hypothesis <= dan_work_hours_premise:
    # check if the hypothesis value contradicts the estimate of more than 'dan_work_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours Dan worked alone
    # any number of hours greater than 'dan_work_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

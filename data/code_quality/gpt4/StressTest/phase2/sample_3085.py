dan_work_hours_premise = 3
dan_work_hours_hypothesis = 8

# the hypothesis talks about the number of hours Dan worked, referenced also in the premise
if dan_work_hours_hypothesis <= dan_work_hours_premise:
    # if Dan worked less than or equal to the hours mentioned in the premise, it would be a contradiction
    label = "contradiction"
elif dan_work_hours_hypothesis > dan_work_hours_premise:
    # the premise gives only an estimate for the number of hours
    # any number of hours greater than 'dan_work_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

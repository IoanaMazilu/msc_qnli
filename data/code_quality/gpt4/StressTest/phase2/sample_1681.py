suresh_work_hours_premise = 7
suresh_work_hours_hypothesis = 9

# the hypothesis refers to the number of hours Suresh works which is also mentioned in the premise
if suresh_work_hours_hypothesis <= suresh_work_hours_premise:
    # check if the hypothesis value contradicts the estimate of more than 'suresh_work_hours_premise' hours
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours Suresh works
    # any number of hours greater than 'suresh_work_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

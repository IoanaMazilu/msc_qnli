work_hours_suresh_premise = 3
work_hours_suresh_hypothesis = 9

# the hypothesis refers to the work hours of Suresh mentioned in the premise
if work_hours_suresh_hypothesis <= work_hours_suresh_premise:
    # check if the estimate of 'work_hours_suresh_hypothesis' contradicts the number of work hours in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the work hours of Suresh
    # any number of work hours greater than 'work_hours_suresh_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

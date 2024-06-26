hours_paid_x_premise = 10
hours_paid_x_hypothesis = 30

# the hypothesis refers to the number of hours Harry is paid x dollars per hour, mentioned in the premise
if hours_paid_x_hypothesis <= hours_paid_x_premise:
    # check if the number of hours in the hypothesis contradicts the estimate of more than 'hours_paid_x_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours Harry is paid x dollars per hour
    # any number of hours greater than 'hours_paid_x_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

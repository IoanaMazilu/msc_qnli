premise_hours_per_week = 21
hypothesis_hours_per_week = 11
premise_dollars_per_hour = x
hypothesis_dollars_per_hour = x

# the hypothesis refers to the number of hours worked in a week, referenced also in the premise
if hypothesis_hours_per_week <= premise_hours_per_week:
    # check if the hypothesis value contradicts the estimate of more than 'premise_hours_per_week'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked
    # any number of hours greater than 'premise_hours_per_week' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

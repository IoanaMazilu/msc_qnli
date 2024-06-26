premise_hours_per_week = 60
hypothesis_hours_per_week = 40

# the hypothesis refers to the number of hours worked per week mentioned in the premise
if hypothesis_hours_per_week <= premise_hours_per_week:
    # check if the estimate of 'hypothesis_hours_per_week' contradicts the number of hours worked per week in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked per week
    # any number of hours greater than 'premise_hours_per_week' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

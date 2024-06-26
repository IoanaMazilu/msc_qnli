premise_hours_per_week = 24
hypothesis_hours_per_week = 54
premise_dollars_per_hour = x
hypothesis_dollars_per_hour = 1.5 * premise_dollars_per_hour

# the hypothesis mentions a higher number of hours worked per week
if hypothesis_hours_per_week > premise_hours_per_week:
    # check if the estimate of 'hypothesis_dollars_per_hour' contradicts the premise
    if hypothesis_dollars_per_hour <= premise_dollars_per_hour:
        label = "entailment"
    else:
        label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked per week
    # any number of hours greater than 'premise_hours_per_week' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

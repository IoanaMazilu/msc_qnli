premise_hours_per_week = 30
hypothesis_hours_per_week = 80
premise_dollars_per_hour = x
hypothesis_dollars_per_hour = 2 * premise_dollars_per_hour

# the hypothesis talks about the number of hours worked and the hourly wage
if hypothesis_hours_per_week <= premise_hours_per_week:
    # check if the hypothesis value contradicts the estimate of more than 'premise_hours_per_week'
    label = "contradiction"
elif hypothesis_dollars_per_hour!= premise_dollars_per_hour:
    # check if the hourly wage in the hypothesis contradicts the hourly wage mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked and the hourly wage
    # any number of hours greater than 'premise_hours_per_week' and any hourly wage greater than 'premise_dollars_per_hour' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

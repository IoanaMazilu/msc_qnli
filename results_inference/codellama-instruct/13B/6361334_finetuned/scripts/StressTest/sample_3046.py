hours_per_day_premise = 5
hours_per_day_hypothesis = 8

# the hypothesis refers to the number of hours worked per day on specific days, which are also mentioned in the premise
if hours_per_day_hypothesis <= hours_per_day_premise:
    # check if the estimate of 'hours_per_day_hypothesis' contradicts the number of hours worked per day in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked per day on specific days
    # any number of hours greater than 'hours_per_day_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

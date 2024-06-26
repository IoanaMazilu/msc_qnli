hours_per_day_premise = 9
hours_per_day_hypothesis = 5

# the hypothesis refers to the number of hours worked per day, mentioned in the premise
if hours_per_day_hypothesis <= hours_per_day_premise:
    # check if the estimate of 'hours_per_day_hypothesis' contradicts the number of hours worked per day in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked per day
    # any number of hours greater than 'hours_per_day_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

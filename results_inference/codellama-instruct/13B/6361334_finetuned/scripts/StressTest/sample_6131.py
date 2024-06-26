hours_per_week_premise = 21
hours_per_week_hypothesis = 11

# the hypothesis refers to the number of hours worked per week, which is also mentioned in the premise
if hours_per_week_hypothesis <= hours_per_week_premise:
    # check if the estimate of 'hours_per_week_hypothesis' contradicts the number of hours worked in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked
    # any number of hours greater than 'hours_per_week_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

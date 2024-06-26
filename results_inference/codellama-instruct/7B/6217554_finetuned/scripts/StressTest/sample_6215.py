hours_per_day_premise = 10
hours_per_day_hypothesis = 70

# the hypothesis gives a different number of hours per day than the premise
if hours_per_day_hypothesis <= hours_per_day_premise:
    # check if the number of hours per day in the hypothesis contradicts the estimate of more than 'hours_per_day_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours per day
    # any number of hours greater than 'hours_per_day_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

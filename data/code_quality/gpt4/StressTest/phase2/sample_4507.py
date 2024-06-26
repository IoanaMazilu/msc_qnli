hours_week_premise = 20
hours_week_hypothesis = 40

# the hypothesis refers to the number of hours James works per week mentioned in the premise
if hours_week_hypothesis <= hours_week_premise:
    # check if the number of hours in the hypothesis contradicts the estimate of more than 'hours_week_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours James works
    # any number of hours greater than 'hours_week_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
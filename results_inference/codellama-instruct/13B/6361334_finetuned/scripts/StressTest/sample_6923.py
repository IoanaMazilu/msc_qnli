hours_worked_premise = 210
hours_worked_hypothesis = 210

# the hypothesis refers to the amount of money earned by Michael, which is also mentioned in the premise
if hours_worked_hypothesis <= hours_worked_premise:
    # check if the estimate of 'hours_worked_hypothesis' contradicts the amount of money earned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money earned
    # any amount of money greater than 'hours_worked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

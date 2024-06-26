days_together_premise = 5
days_together_hypothesis = 3

# the hypothesis refers to the number of days the two work together, mentioned in the premise
if days_together_hypothesis <= days_together_premise:
    # check if the estimate of 'days_together_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days greater than 'days_together_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

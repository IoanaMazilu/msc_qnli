days_premise = 20
days_hypothesis = 50

# the hypothesis refers to the number of days mentioned in the premise
if days_hypothesis <= days_premise:
    # check if the estimate of 'days_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days greater than 'days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

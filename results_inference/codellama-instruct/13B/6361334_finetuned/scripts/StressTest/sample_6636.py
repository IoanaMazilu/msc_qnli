days_premise = 30
days_hypothesis = 50

# the hypothesis refers to the number of days required to complete a work, mentioned in the premise
if days_hypothesis >= days_premise:
    # check if the estimate of 'days_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the number of days required to complete a work
    # any number of days less than 'days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

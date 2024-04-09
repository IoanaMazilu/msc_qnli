days_premise = 80
days_hypothesis = 30

# the hypothesis refers to the number of days Lexi needed to save to afford a vacation
if days_hypothesis <= days_premise:
    # check if the estimate of 'days_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the number of days Lexi needed to save, but the hypothesis provides a more specific value
    # any number of days less than 'days_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

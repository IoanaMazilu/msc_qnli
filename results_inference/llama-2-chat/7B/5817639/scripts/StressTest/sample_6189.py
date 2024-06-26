days_premise = 30
days_hypothesis = 80

# the hypothesis talks about the number of days Lexi needed to save for a vacation
if days_hypothesis <= days_premise:
    # check if the hypothesis value contradicts the estimate of 'days_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of days Lexi needed to save
    # any number of days less than 'days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

minimum_wage_premise = 190
minimum_wage_hypothesis = 190

# the hypothesis and premise mention the same amount of money in dollars for the increase in labour costs
if minimum_wage_premise!= minimum_wage_hypothesis:
    # check if the amount of money in the hypothesis contradicts the amount of money in the premise
    label = "contradiction"
else:
    # the premise gives an exact amount of money for the increase in labour costs
    # any estimate of the amount in the hypothesis equal to the premise amount is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

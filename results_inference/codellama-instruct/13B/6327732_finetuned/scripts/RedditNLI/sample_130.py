minimum_wage_premise = 15
minimum_wage_hypothesis = 15

# the hypothesis and premise mention the minimum wage increase to $15
if minimum_wage_premise!= minimum_wage_hypothesis:
    # check if the minimum wage in the hypothesis contradicts the minimum wage in the premise
    label = "contradiction"
else:
    # the premise gives an exact value for the minimum wage
    # any estimate of the minimum wage in the hypothesis equal to $15 is consistent with the premise, and can be explicitly entailed from the premise
    label = "entailment"

print(label)

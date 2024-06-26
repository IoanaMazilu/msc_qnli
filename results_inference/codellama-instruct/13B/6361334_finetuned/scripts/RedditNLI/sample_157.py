minimum_wage_premise = 15
minimum_wage_hypothesis = 15

# the hypothesis and premise mention the minimum wage increase to $15
if minimum_wage_hypothesis!= minimum_wage_premise:
    # check if the minimum wage in the hypothesis contradicts the minimum wage in the premise
    label = "contradiction"
else:
    # if the minimum wage in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)

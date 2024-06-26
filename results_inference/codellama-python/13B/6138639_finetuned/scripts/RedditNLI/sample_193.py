minimum_wage_premise = 15
minimum_wage_hypothesis = 15

# the hypothesis and premise mention the minimum wage in both states
if minimum_wage_hypothesis!= minimum_wage_premise:
    # check if the minimum wage in the hypothesis contradicts the minimum wage in the premise
    label = "contradiction"
else:
    # if the minimum wage in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

# Premise: Gov. Brown hails deal to raise minimum wage to $15.
# Hypothesis: California to Raise Minimum Wage to $15/hour.
# Golden Label: entailment

wage_premise = 15
wage_hypothesis = 15

# the hypothesis and premise mention the new minimum wage
if wage_hypothesis != wage_premise:
    # check if the wages in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the wage in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)


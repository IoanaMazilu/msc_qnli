# Premise: California Gov. Jerry Brown approves minimum wage increase to $15.
# Hypothesis: California Is About to Make a $15 Minimum Wage a Reality.
# Golden Label: entailment

wage_premise = 15
wage_hypothesis = 15

# the hypothesis and premise both mention the increase of minimum wage to $15 in California
if wage_hypothesis != wage_premise:
    # check if the wage in the hypothesis contradicts the wage in the premise
    label = "contradiction"
else:
    # if the wage in the hypothesis does not contradict the wage in the premise, we can infer entailment
    label = "entailment"

print(label)


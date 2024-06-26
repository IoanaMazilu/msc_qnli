# For this scenario, we do not have actual numerical values to compare, only the percentage values
rebecca_income_premise = 50
rebecca_income_hypothesis = 80

# the hypothesis and premise both talk about the increase in Rebecca's annual income
# to constitute a certain percentage of the combined income of Rebecca and Jimmy
if rebecca_income_hypothesis != rebecca_income_premise:
    # check if the percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the percentage in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"

print(label)

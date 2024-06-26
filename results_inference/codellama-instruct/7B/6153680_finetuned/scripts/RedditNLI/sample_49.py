debt_premise = 570000000000
debt_hypothesis = 570000000000

# the hypothesis and premise mention the same amount of debt
if debt_hypothesis!= debt_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)

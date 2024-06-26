debt_premise = 57
debt_hypothesis = 57

# the hypothesis and premise mention the same amount of debt
if debt_hypothesis!= debt_premise:
    # check if the debt in the hypothesis contradicts the debt in the premise
    label = "contradiction"
else:
    # if the debt in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)

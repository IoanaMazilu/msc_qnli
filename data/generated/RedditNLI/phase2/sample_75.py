# Premise: Trump Seeks $3.6 Trillion in Spending Cuts to Reshape Government.
# Hypothesis: Trump seeks to slash $3.6 trillion of government spending in budget.
# Golden Label: entailment

cuts_premise = 3.6
cuts_hypothesis = 3.6

# the hypothesis and premise mention the amount of spending cuts Trump seeks
if cuts_hypothesis != cuts_premise:
    # check if the amount of spending cuts in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)


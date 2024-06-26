debt_premise = 57
debt_hypothesis = 57
years_premise = 7
years_hypothesis = 7

# the hypothesis and premise mention the amount of debt and the time period
if debt_hypothesis!= debt_premise:
    # check if the amount of debt in the hypothesis contradicts the amount of debt in the premise
    label = "contradiction"
elif years_hypothesis!= years_premise:
    # check if the time period in the hypothesis contradicts the time period in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

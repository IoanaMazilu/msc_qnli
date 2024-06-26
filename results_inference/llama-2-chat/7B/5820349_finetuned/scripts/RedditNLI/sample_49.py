debt_increase_premise = 57
years_premise = 12
debt_increase_hypothesis = 57
years_hypothesis = 7

# the hypothesis and premise mention the increase in global debt and the time period since the financial crisis
if debt_increase_hypothesis!= debt_increase_premise:
    # check if the increase in debt in the hypothesis contradicts the increase in debt in the premise
    label = "contradiction"
elif years_hypothesis!= years_premise:
    # check if the time period in the hypothesis contradicts the time period in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

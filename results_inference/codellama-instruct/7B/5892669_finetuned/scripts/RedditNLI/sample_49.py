debt_increase_premise = 57
debt_increase_hypothesis = 57

# the hypothesis and premise mention the increase in global debt since the financial crisis
if debt_increase_hypothesis!= debt_increase_premise:
    # check if the increase in debt in the hypothesis contradicts the increase in debt in the premise
    label = "contradiction"
else:
    # if the increase in debt in the hypothesis does not contradict the increase in debt in the premise, we can infer entailment
    label = "entailment"

print(label)
